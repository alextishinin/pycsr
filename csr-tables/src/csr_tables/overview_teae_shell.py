from pathlib import Path

import polars as pl
import rtflite as rtf

PROJECT_DIR = Path(__file__).resolve().parents[2]
RTF_PATH = PROJECT_DIR / "rtf" / "overview_teae_shell.rtf"
COURIER_NEW = 9
FONT_SIZE = 8
SHELL_COLUMNS = ["row", "treatment_a", "treatment_b", "total"]
SHELL_ROWS = [
    ("", "", "", ""),
    (
        "Any Treatment-Emergent Adverse Events (TEAE)",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    ("Any Related TEAE", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("Any Grade >=3 TEAE", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("Any Grade >=3 Related TEAE", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("Any Severe TEAE", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("Any Serious TEAE", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("      Result in Death", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("      Life-threatening", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("      Hospitalization", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    (
        "      Congenital Anomaly or Birth Defect",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    ("      Significant Disability", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    (
        "      Other Medically Important Event",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    ("Any Serious Related TEAE", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    (
        "Any TEAE Leading to Discontinuation of Study Drug",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    (
        "Any TEAE Leading to Dose Modification of Study Drug",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    ("      Interruption", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("      Dose Reduction", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("      Dose Delay", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("      Other", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    (
        "Any TEAE Leading to Study Discontinuation",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    ("Any TEAE of Special Interest", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    (
        "Any Related TEAE of Special Interest",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
        "xx (xx.x) xx",
    ),
    ("Any Fatal TEAE", "xx (xx.x) xx", "xx (xx.x) xx", "xx (xx.x) xx"),
    ("", "", "", ""),
]


def create_overview_teae_shell() -> pl.DataFrame:
    return pl.DataFrame(SHELL_ROWS, schema=SHELL_COLUMNS, orient="row")


def write_overview_teae_shell(output_path: Path = RTF_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    shell = create_overview_teae_shell()

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
                "Overview of Treatment-Emergent Adverse Events",
                "Safety Analysis Set",
            ],
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
        ),
        rtf_column_header=rtf.RTFColumnHeader(
            text=[
                "",
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
                "An AE is considered TEAE if < insert SAP definition >.",
                (
                    "A related AE is defined as < insert SAP definition including "
                    "missing imputation rule >."
                ),
                "Programming notes:",
                (
                    "Some blue text entries are based on data collection; some "
                    "(e.g., SAE categories and dose modification) are based on the "
                    "disease stage, indication, etc. and should be discussed with "
                    "the study team."
                ),
                (
                    "Typically phase 2 and 3 studies do not need to present the "
                    "occurrences column."
                ),
                (
                    "It is recommended NOT to include the individual SAE criteria "
                    "rows unless specifically needed for a study."
                ),
            ],
        ),
        rtf_page_footer=rtf.RTFPageFooter(
            text=[
                (
                    "<footnote>\\line\\line"
                    "Source: <source python code location>\\line"
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
    write_overview_teae_shell()


if __name__ == "__main__":
    main()
