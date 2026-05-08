from pathlib import Path

import polars as pl  # Manipulate data
import rtflite as rtf  # Reporting in RTF format

PROJECT_DIR = Path(__file__).resolve().parents[2]
REPO_DIR = PROJECT_DIR.parent
ADSL_PATH = REPO_DIR / "data" / "adsl.parquet"
RTF_PATH = PROJECT_DIR / "rtf" / "tlf_disposition.rtf"


def create_disposition_table(adsl: pl.DataFrame) -> pl.DataFrame:
    n_rand = (
        adsl.group_by("TRT01PN")
        .agg(n=pl.len())
        .with_columns(
            [
                pl.lit("Participants in population").alias("row"),
                pl.lit(None, dtype=pl.Float64).alias("pct"),
            ]
        )
        .pivot(index="row", on="TRT01PN", values=["n", "pct"], sort_columns=True)
    )

    n_complete = (
        adsl.filter(pl.col("DCREASCD") == "Completed")
        .group_by("TRT01PN")
        .agg(n=pl.len())
        .join(adsl.group_by("TRT01PN").agg(total=pl.len()), on="TRT01PN")
        .with_columns(
            [
                pl.lit("Completed").alias("row"),
                (100.0 * pl.col("n") / pl.col("total")).round(1).alias("pct"),
            ]
        )
        .pivot(index="row", on="TRT01PN", values=["n", "pct"], sort_columns=True)
    )

    n_disc = (
        adsl.filter(pl.col("DISCONFL") == "Y")
        .group_by("TRT01PN")
        .agg(n=pl.len())
        .join(adsl.group_by("TRT01PN").agg(total=pl.len()), on="TRT01PN")
        .with_columns(
            [
                pl.lit("Discontinued").alias("row"),
                (100.0 * pl.col("n") / pl.col("total")).round(1).alias("pct"),
            ]
        )
        .pivot(index="row", on="TRT01PN", values=["n", "pct"], sort_columns=True)
    )

    n_reason = (
        adsl.filter(pl.col("DCREASCD") != "Completed")
        .group_by(["TRT01PN", "DCREASCD"])
        .agg(n=pl.len())
        .join(adsl.group_by("TRT01PN").agg(total=pl.len()), on="TRT01PN")
        .with_columns(
            [
                pl.concat_str([pl.lit("    "), pl.col("DCREASCD")]).alias("row"),
                (100.0 * pl.col("n") / pl.col("total")).round(1).alias("pct"),
            ]
        )
        .pivot(index="row", on="TRT01PN", values=["n", "pct"], sort_columns=True)
        .with_columns(
            [
                pl.col(["n_0", "n_54", "n_81"]).fill_null(0),
                pl.col(["pct_0", "pct_54", "pct_81"]).fill_null(0.0),
            ]
        )
        .sort("row")
    )

    return pl.concat([n_rand, n_complete, n_disc, n_reason])


def create_disposition_rtf(tbl_disp: pl.DataFrame, output_path: Path = RTF_PATH) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc_disp = rtf.RTFDocument(
        df=tbl_disp.select("row", "n_0", "pct_0", "n_54", "pct_54", "n_81", "pct_81"),
        rtf_title=rtf.RTFTitle(text=["Disposition of Participants"]),
        rtf_column_header=[
            rtf.RTFColumnHeader(
                text=["", "Placebo", "Xanomeline Low Dose", "Xanomeline High Dose"],
                col_rel_width=[3] + [2] * 3,
                text_justification=["l"] + ["c"] * 3,
            ),
            rtf.RTFColumnHeader(
                text=["", "n", "(%)", "n", "(%)", "n", "(%)"],
                col_rel_width=[3] + [1] * 6,
                text_justification=["l"] + ["c"] * 6,
                border_top=[""] + ["single"] * 6,
                border_left=["single"] + ["single", ""] * 3,
            ),
        ],
        rtf_body=rtf.RTFBody(
            col_rel_width=[3] + [1] * 6,
            text_justification=["l"] + ["c"] * 6,
            border_left=["single"] + ["single", ""] * 3,
        ),
        rtf_source=rtf.RTFSource(text=["Source: ADSL dataset"]),
    )

    doc_disp.write_rtf(str(output_path))


def main() -> None:
    adsl = pl.read_parquet(ADSL_PATH)
    tbl_disp = create_disposition_table(adsl)
    create_disposition_rtf(tbl_disp)


if __name__ == "__main__":
    main()
