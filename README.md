# MQH — Marff's Quant House

A machine-learning-driven quantitative trading research project. It ranks a
universe of US stocks by expected forward relative return, builds a portfolio
from that ranking, and backtests it — with pandas handling the data and
features, NumPy handling the portfolio maths and backtester, and PyTorch
handling the model, so no library hides a concept along the way.

The goal is to learn how quantitative research is actually structured
(features, honest backtesting, avoiding leakage, evaluating out-of-sample) —
not to produce a guaranteed profitable strategy.

**Status:** v1 in progress. Data layer (fetch + parse) working; features,
baselines, and the model are next.

## Setup

Requires [Poetry](https://python-poetry.org/) and Python 3.13+.

```bash
poetry install
```

This installs dependencies and the local `mqh` package in editable mode.

## Usage

Download daily OHLCV data for a list of tickers:

```bash
poetry run python scripts/download_data.py data/tickers.txt 2010-01-01 2026-08-20
```

- `data/tickers.txt` — one ticker per line
- Positional args: ticker file, start date, end date (`YYYY-MM-DD`)
- `--output_dir` — where to save the CSVs (default: `data`)

## License

Apache-2.0 — see [LICENSE](LICENSE).
