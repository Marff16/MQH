from pathlib import Path
from typing import List
import yfinance as yf



def fetch_data(ticker_list: List[str], start_date: str, end_date: str, output_dir: Path) -> None:
    """
    Method to fetch all OHLCV data from ticker list yfinance and save it to CSV files
    """
    for ticker in ticker_list:
        # Try to fetch data for each ticker
        try:
            data = yf.download(tickers=ticker, start=start_date, end=end_date)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            continue

        # Save the data to a CSV file in the specified output directory
        output_path = Path(f"data/{ticker}.csv")

        # Check if the output directory exists, if not create it
        if not output_path.parent.exists():
            print(f"Creating directory: {output_path.parent}")
            output_path.parent.mkdir(parents=True, exist_ok=True)
        data.to_csv(output_path)

        print(f"Data for {ticker} saved to {output_path}")
    return None
    


