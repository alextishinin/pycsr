from pathlib import Path

import polars as pl
import rtflite as rtf

PROJECT_DIR = Path(__file__).resolve().parents[2]
RTF_PATH = PROJECT_DIR / "rtf" / "demographics_shell.rtf"
COURIER_NEW = 9
FONT_SIZE = 8
SHELL_COLUMNS = ["row", "treatment_a", "treatment_b", "total"]
SHELL_ROWS = [
    ("", "", "", ""),
    ("Age (years)", "", "", ""),
    ("   continuous descriptive summary", "xx", "xx", "xx"),
    ("", "", "", ""),
    ("Age Group 1 (years), n (%)", "", "", ""),
    ("   Group #1", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Group #2", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Age Group 2 (years), n (%)", "", "", ""),
    ("   Group #1", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Group #2", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Sex, n (%)", "", "", ""),
    ("   Female", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Male", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Race, n (%)", "", "", ""),
    ("   American Indian or Alaska Native", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Asian", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Black or African American", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Native Hawaiian or Other Pacific Islander", "", "", ""),
    ("   White", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Unknown", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Other", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Race Group, n (%)", "", "", ""),
    ("   Group #1", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Group #2", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Ethnicity, n (%)", "", "", ""),
    ("   Hispanic or Latino", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Not Hispanic or Latino", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   Unknown", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Region, n (%)", "", "", ""),
    ("   < region 1 >", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   < region 2 >", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Country, n (%)", "", "", ""),
    ("   < country 1 >", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   < country 2 >", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Height (cm)", "", "", ""),
    ("   continuous descriptive summary", "xx", "xx", "xx"),
    ("", "", "", ""),
    ("Weight (kg)", "", "", ""),
    ("   continuous descriptive summary", "xx", "xx", "xx"),
    ("", "", "", ""),
    ("Body Mass Index (kg/m2)", "", "", ""),
    ("   continuous descriptive summary", "xx", "xx", "xx"),
    ("", "", "", ""),
    ("< baseline characteristics >", "", "", ""),
    ("< disease characteristics >", "", "", ""),
    ("", "", "", ""),
]


def create_demographics_shell() -> pl.DataFrame:
    return pl.DataFrame(SHELL_ROWS, schema=SHELL_COLUMNS, orient="row")


def write_demographics_shell(output_path: Path = RTF_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    shell = create_demographics_shell()

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
                "Table 14.1.1.X",
                "Demographics and Baseline Characteristics",
                "Randomized Population",
            ],
            text_font=[COURIER_NEW],
            text_font_size=[FONT_SIZE],
        ),
        rtf_column_header=rtf.RTFColumnHeader(
            text=[
                "",
                "Treatment A\\line (N=xx)",
                "Treatment B\\line (N=xx)",
                "Total\\line (N=xx)",
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
                "Programming notes:",
                "Add other study population as needed.",
                (
                    "The categories for 'Race' and 'Ethnicity' should match the "
                    "categories in the corresponding CRF."
                ),
                (
                    "'Not Reported' or 'Unknown' row should be added for each "
                    "categorical summary unless it is all zeros."
                ),
                (
                    "For race and ethnicity, if the team needs to differentiate "
                    "random missing from administrative missing (eg, due to country "
                    "requirement), please add additional rows for each type of "
                    "missing and provide appropriate footnote."
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
    write_demographics_shell()


if __name__ == "__main__":
    main()
