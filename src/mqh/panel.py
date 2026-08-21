from pathlib import Path
from typing import List
import pandas as pd


def convert_csv_to_dataframe(csv_files: List[Path]) -> pd.DataFrame:
    dataframes = [pd.read_csv(file, skiprows=[1,2]) for file in csv_files]
    dataframes = [df.rename(columns={"Price": "Date"}).set_index('Date') for df in dataframes]

    same_len = all(len(df) == len(dataframes[0]) for df in dataframes)
    merged_df = pd.DataFrame()
    if same_len:
        merged_df = pd.concat(dataframes, axis=1)
        print(f"-> Merged DataFrame shape: {merged_df.shape}")
    else:
        print(f"-> DataFrames have different lengths. Cannot merge.")
    return merged_df.round(4)

def read_selected_price_data(input_path: Path, ticker_names: List[str]) -> pd.DataFrame:
    """
    Reads CSV files, merges them into a single DataFrame, and performs data cleaning
    """
    print(f"READING {len(ticker_names)} tickers FROM {input_path}")

    # Read all CSV files in the input path
    csv_files = list(input_path.glob("*.csv"))
    csv_files = [file for file in csv_files if file.stem in ticker_names]
    return convert_csv_to_dataframe(csv_files)


def read_all_price_data(input_path: Path) -> pd.DataFrame:
    """
    Reads CSV files, merges them into a single DataFrame, and performs data cleaning
    """
    print(f"READING ALL tickers FROM {input_path}")

    # Read all CSV files in the input path
    csv_files = list(input_path.glob("*.csv"))
    return convert_csv_to_dataframe(csv_files)