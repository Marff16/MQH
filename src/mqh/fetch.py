from pathlib import Path
from typing import List
import yfinance as yf
import tqdm



def fetch_data(ticker_list: List[str], start_date: str, end_date: str, output_dir: Path, overwrite: bool = False) -> None:
    """
    Method to fetch all OHLCV data from ticker list yfinance and save it to CSV files
    """
    print(f"\nFETCHING DATA FOR {len(ticker_list)} TICKERS FROM {start_date} TO {end_date}")

    if len(ticker_list) == 0:
        raise ValueError("Ticker list is empty. Please provide a list of tickers to fetch data.")

    downloaded_tickers = []
    for ticker in tqdm.tqdm(ticker_list):
        # Try to fetch data for each ticker
        try:
            data = yf.download(tickers=ticker, start=start_date, end=end_date, progress=False)
        except Exception as e:
            print(f"-> Error fetching data for {ticker}: {e}")
            continue

        # Save the data to a CSV file in the specified output directory
        output_path = output_dir / Path(f"{ticker}.csv")

        # Check if the output directory exists, if not create it
        if not output_path.parent.exists():
            print(f"-> Creating directory: {output_path.parent}")
            output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_path.exists() and not overwrite:
            continue

        data.to_csv(output_path)
        downloaded_tickers.append(ticker)
    return None
    


