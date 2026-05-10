from pathlib import Path

import polars as pl
import rtflite as rtf

PROJECT_DIR = Path(__file__).resolve().parents[2]
RTF_PATH = PROJECT_DIR / "rtf" / "summary_teae_by_soc_shell.rtf"
COURIER_NEW = 9
FONT_SIZE = 8
SHELL_COLUMNS = ["row", "treatment_a", "treatment_b", "total"]
SHELL_ROWS = [
    ("", "", "", ""),
    (
        "Subjects with at Least One Treatment-Emergent Adverse Event",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    ("", "", "", ""),
    ("System Organ Class #1", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   Preferred Term #1.1", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   Preferred Term #1.2", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   Preferred Term #1.3", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   ...", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("", "", "", ""),
    ("System Organ Class #2", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   Preferred Term #2.1", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   Preferred Term #2.2", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   Preferred Term #2.3", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("   ...", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("...", "", "", ""),
]


def create_summary_teae_by_soc_shell() -> pl.DataFrame:
    return pl.DataFrame(SHELL_ROWS, schema=SHELL_COLUMNS, orient="row")


def write_summary_teae_by_soc_shell(output_path: Path = RTF_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    shell = create_summary_teae_by_soc_shell()

    doc = rtf.RTFDocument(
        df=shell,
        rtf_page=rtf.RTFPage(
            orientation="landscape",
            margin=[1, 1, 1, 1, 0.5, 0.5],
            nrow=38,
            page_title="first",
            border_first="single",
            border_last="single",
        ),
        rtf_page_header=rtf.RTFPageHeader(
            text=["Crinetics Pharmaceuticals", "<Protocol Number>"],
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
            text_justification=["r"],
        ),
        rtf_title=rtf.RTFTitle(
            text=[
                "Table 14.3.1.X",
                (
                    "Summary of Treatment-Emergent Adverse Events by System "
                    "Organ Class and Preferred Term"
                ),
                "Safety Analysis Set",
            ],
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
        ),
        rtf_column_header=rtf.RTFColumnHeader(
            text=[
                "System Organ Class\\line    Preferred Term",
                "Treatment A\\line (N=xx)\\line n (%) m",
                "Treatment B\\line (N=xx)\\line n (%) m",
                "Total\\line (N=xx)\\line n (%) m",
            ],
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
                "n is the incidence and m is the number of occurrences.",
                "MedDRA version xx.x",
                "An AE is considered TEAE if < insert SAP definition >.",
                (
                    "Subjects with multiple adverse events within the same system "
                    "organ class or preferred term are only counted once within the "
                    "respective category."
                ),
                "Programming notes:",
                (
                    "Sort by descending frequency of system organ class and "
                    "preferred term, in Total column then from highest dose to "
                    "lowest dose to placebo (follow the order specified in SAP)."
                ),
            ],
        ),
        rtf_page_footer=rtf.RTFPageFooter(
            text=[
                (
                    "<footnote>\\line\\line"
                    "Source: <source SAS code location>\\line"
                    "\\pard\\hyphpar\\sb15\\sa15\\fi0\\li0\\ri0\\ql\\tqr\\tx12960 "
                    "Data Extracted: YYYY-MM-DD, Data Cut: YYYY-MM-DD\\tab "
                    "v9.X DDMMMYYYY:MM:SS"
                ),
            ],
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
            text_justification=["l"],
        ),
    )

    doc.write_rtf(str(output_path))
    return output_path


def main() -> None:
    write_summary_teae_by_soc_shell()


if __name__ == "__main__":
    main()
