from typing import List
from pathlib import Path

def parse_tickers(input_file: Path) -> List[str]:
    """
    Method to parse tickers from a text file and return them as a list
    """
    print(f"\nPARSING TICKERS FROM {input_file}")
    if not input_file.exists():
        raise FileNotFoundError(f"Ticker file {input_file} does not exist.")
    tickers = Path(input_file).read_text().splitlines()

    # Remove any empty strings and whitespace
    tickers = [ticker for ticker in tickers if ticker.strip() != ""]

    if len(tickers) == 0:
        raise ValueError(f"-> No tickers found in {input_file}. Please ensure the file is not empty.")
    
    print(f"-> Parsed {len(tickers)} tickers from {input_file}")

    return tickers