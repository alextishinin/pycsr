from pathlib import Path

import polars as pl
import rtflite as rtf

PROJECT_DIR = Path(__file__).resolve().parents[2]
RTF_PATH = PROJECT_DIR / "rtf" / "exposure_shell.rtf"
COURIER_NEW = 9
FONT_SIZE = 8
SHELL_COLUMNS = ["row", "treatment_a", "treatment_b", "total"]
SHELL_ROWS = [
    ("", "", "", ""),
    ("Duration of Exposure During the Randomized Treatment Period (unit)", "", "", ""),
    ("   continuous descriptive summary", "xx", "xx", "xx"),
    ("", "", "", ""),
    (
        "Duration of Exposure During the Randomized Treatment Period, n (%)",
        "",
        "",
        "",
    ),
    ("   < xx (unit) (or xx to xx (unit))", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   >= xx (unit) (or xx to xx (unit))", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   >= xx (unit) (or xx to xx (unit))", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   >= xx (unit) (or xx to xx (unit))", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Total Amount of Dose Received (unit)", "", "", ""),
    ("   continuous descriptive summary", "xx", "xx", "xx"),
    ("", "", "", ""),
    ("Total Number of Dose/Injection Received, n (%)", "", "", ""),
    ("   xx (or xx to xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   xx (or xx to xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   xx (or xx to xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("   ...", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"),
    ("", "", "", ""),
    ("Exposure Gap Due to Interruption < applicable if defined in SAP >", "", "", ""),
    ("   continuous descriptive summary", "xx", "xx", "xx"),
    ("", "", "", ""),
    ("", "", "", ""),
    ("", "", "", ""),
    ("", "", "", ""),
]


def create_exposure_shell() -> pl.DataFrame:
    return pl.DataFrame(SHELL_ROWS, schema=SHELL_COLUMNS, orient="row")


def write_exposure_shell(output_path: Path = RTF_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    shell = create_exposure_shell()

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
                "Table 14.1.3.X",
                "Extent of Exposure",
                "Safety Analysis Set",
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
                "Duration of Exposure is defined as < insert SAP definition >.",
                "Programming notes:",
                "Categorical duration of exposure should be based on SAP.",
                (
                    "Total number of doses received could either be a single number "
                    "or a range and should be based on SAP."
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
    write_exposure_shell()


if __name__ == "__main__":
    main()
