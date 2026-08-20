from pathlib import Path
from typing import List
from mqh.fetch import fetch_data
from mqh.parse import parse_tickers
import argparse 

def download_data(ticker_file: Path, start_date: str, end_date: str, output_dir: Path) -> None:
    """
    Method to download data for tickers specified in a text file and save it to CSV files
    """
    tickers = parse_tickers(ticker_file)
    fetch_data(tickers, start_date, end_date, output_dir)

    return None

def main():
    """
    Run this script:
    poetry run python scripts/download_data.py <ticker_file> <start_date> <end_date> [--output_dir <output_dir>]
    
    Example:
    poetry run python scripts/download_data.py data/tickers.txt 2021-01-01 2026-01-01
    """
    parser = argparse.ArgumentParser(description="Download OHLCV data for tickers specified in a text file.")
    parser.add_argument("--ticker_file", type=Path, default=Path("data/tickers.txt"), help="Path to the text file containing tickers.",)
    parser.add_argument("--start_date", type=str, default="2021-01-01", help="Start date for fetching data (YYYY-MM-DD).")
    parser.add_argument("--end_date", type=str, default="2026-01-01", help="End date for fetching data (YYYY-MM-DD).")
    parser.add_argument("--output_dir", type=Path, default=Path("data"), help="Directory to save the CSV files. Default is 'data'.")

    args = parser.parse_args()

    download_data(args.ticker_file, args.start_date, args.end_date, args.output_dir)

if __name__ == "__main__":
    main()