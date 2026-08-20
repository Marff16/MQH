# MQH — Marff's Quant House

This is more of a personal project to get comfortable with using Pandas, Numpy and PyTorch in the context of QR.

## Setup

Requires [Poetry](https://python-poetry.org/) and Python 3.13+.

```bash
poetry install
```

## Usage

Download daily OHLCV data for a list of tickers:

```bash
poetry run python scripts/download_data.py data/tickers.txt 2020-01-01 <todays-date>
```

- `data/tickers.txt` — one ticker per line
- Positional args: ticker file, start date, end date (`YYYY-MM-DD`)
- `--output_dir` — where to save the CSVs (default: `data`)

## License

Apache-2.0 — see [LICENSE](LICENSE).
