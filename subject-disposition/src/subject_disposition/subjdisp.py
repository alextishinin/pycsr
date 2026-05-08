from pathlib import Path

import polars as pl
import rtflite as rtf

PROJECT_DIR = Path(__file__).resolve().parents[2]
RTF_PATH = PROJECT_DIR / "rtf" / "subject_disposition_shell.rtf"
COURIER_NEW = 9
FONT_SIZE = 8

SHELL_COLUMNS = ["row", "treatment_a", "treatment_b", "total"]
SHELL_ROWS = [
    ("", "", "", ""),
    (
        "Screened [1] < applicable only when screen failure is collected in the database >",
        "",
        "",
        "xx",
    ),
    ("   Completed Screening", "", "", "xx (xx.x)"),
    ("   Screen Failures", "", "", "xx (xx.x)"),
    ("      < screen failure reason 1 >", "", "", "xx (xx.x)"),
    ("      < screen failure reason 2 >", "", "", "xx (xx.x)"),
    ("      ...", "", "", "xx (xx.x)"),
    ("", "", "", ""),
    (
        "Entered Run-in [1] < applicable when there is Run-in phase in the study >",
        "",
        "",
        "xx",
    ),
    ("   Completed Run-in", "", "", "xx (xx.x)"),
    ("   Run-in Failure", "", "", "xx (xx.x)"),
    ("      < run-in failure reason 1 >", "", "", "xx (xx.x)"),
    ("      < run-in failure reason 2 >", "", "", "xx (xx.x)"),
    ("      ...", "", "", "xx (xx.x)"),
    ("", "", "", ""),
    ("Randomized Population [1]", "xx", "xx", "xx"),
    ("Intent-To-Treat Set", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("Modified Intent-To-Treat Set", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("Full Analysis Set", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("Safety Analysis Set", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("Per-Protocol Analysis Set", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    (
        "Completed Study Treatment < applicable if collected OR not a single dose study >",
        "xx (xx.x)",
        "xx (xx.x)",
        "xx (xx.x)",
    ),
    ("Ongoing Treatment", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("Early Discontinuation from Study Treatment", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   <reason 1>", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   <reason 2>", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Other", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    (
        "Participated in OLE < applicable to studies with OLE >",
        "xx (xx.x)",
        "xx (xx.x)",
        "xx (xx.x)",
    ),
    ("Refused Participation in OLE", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   <reason 1>", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   <reason 2>", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "", "", ""),
    ("   Other", "", "", ""),
    ("", "", "", ""),
    ("", "", "", ""),
    ("Completed Study", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("Ongoing in the Study", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("Early Discontinuation from Study", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   <reason 1>", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   <reason 2>", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Other", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
]


def create_subject_disposition_shell() -> pl.DataFrame:
    return pl.DataFrame(SHELL_ROWS, schema=SHELL_COLUMNS, orient="row")


def write_subject_disposition_shell(output_path: Path = RTF_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    shell = create_subject_disposition_shell()

    doc = rtf.RTFDocument(
        df=shell,
        rtf_page=rtf.RTFPage(
            orientation="landscape",
            margin=[1, 1, 1, 1, 0.5, 0.5],
            nrow=38,
        ),
        rtf_title=rtf.RTFTitle(
            text=["Table 14.1.1.X", "Subject Disposition", "All Subjects"],
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
        ),
        rtf_column_header=rtf.RTFColumnHeader(
            text=["", "Treatment A\\line n (%)", "Treatment B\\line n (%)", "Total\\line n (%)"],
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
            col_rel_width=[4.8, 1.4, 1.4, 1.4],
            text_justification=["l", "c", "c", "c"],
            border_bottom="single",
        ),
        rtf_body=rtf.RTFBody(
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
            col_rel_width=[4.8, 1.4, 1.4, 1.4],
            text_justification=["l", "c", "c", "c"],
        ),
        rtf_footnote=rtf.RTFFootnote(
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
            text=[
                "OLE = open label extension",
                "[1] Used as denominator for the subcategories.",
                "Programming notes:",
                (
                    "For non-randomized study, the percentages are calculated based on "
                    "the safety population. Update the footnotes, accordingly."
                ),
                "Only keep the subject populations defined in the study and SAP.",
                (
                    "Reason for early discontinuation includes all categories in the "
                    "corresponding CRF, with the same order as CRF entries."
                ),
            ]
        ),
    )

    doc.write_rtf(str(output_path))
    return output_path


def main() -> None:
    write_subject_disposition_shell()


if __name__ == "__main__":
    main()
