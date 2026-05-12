from pathlib import Path

import polars as pl


PROJECT_DIR = Path(__file__).resolve().parents[2]
ADSL_PATH = PROJECT_DIR.parent / "data" / "adsl.parquet"
OUTPUT_PATH = PROJECT_DIR / "output" / "adsl.csv"


def main() -> None:
    adsl = pl.read_parquet(ADSL_PATH)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    adsl.write_csv(OUTPUT_PATH)
    print(f"Wrote {adsl.height} rows and {adsl.width} columns to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
