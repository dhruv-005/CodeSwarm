# tools.py
import os
import yfinance as yf
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from crewai.tools import tool
from datetime import datetime, timedelta

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
WORKSPACE  = os.path.join(BASE_DIR, "workspace")
CSV_PATH   = os.path.join(WORKSPACE, "stock_data.csv")
CHART_PATH = os.path.join(WORKSPACE, "tech_market_analysis.png")

os.makedirs(WORKSPACE, exist_ok=True)


@tool("Stock Data Fetcher")
def fetch_stock_data(ticker_symbols: str) -> str:
    """
    Fetches 6 months of daily closing prices for comma-separated tickers.
    Input must be exactly: 'AAPL,MSFT,NVDA'
    Saves data to workspace/stock_data.csv and returns a short summary.
    """
    try:
        tickers    = [t.strip().upper() for t in ticker_symbols.split(",")]
        end_date   = datetime.today()
        start_date = end_date - timedelta(days=180)

        raw_data = yf.download(
            tickers,
            start       = start_date.strftime("%Y-%m-%d"),
            end         = end_date.strftime("%Y-%m-%d"),
            auto_adjust = True,
            progress    = False,
        )

        if len(tickers) > 1:
            close_data = raw_data["Close"]
        else:
            close_data = raw_data[["Close"]]
            close_data.columns = tickers

        close_data.dropna(how="all", inplace=True)
        close_data.to_csv(CSV_PATH)

        lines = [
            f"✅ CSV saved to: {CSV_PATH}",
            f"📅 Range: {close_data.index[0].date()} to {close_data.index[-1].date()}",
            f"📋 Days : {len(close_data)}",
        ]
        for ticker in tickers:
            if ticker in close_data.columns:
                col = close_data[ticker].dropna()
                lines.append(
                    f"{ticker}: latest=${col.iloc[-1]:.2f} "
                    f"high=${col.max():.2f} "
                    f"low=${col.min():.2f}"
                )
        return "\n".join(lines)

    except Exception as e:
        return f"❌ ERROR: {str(e)}"


@tool("Chart Generator")
def generate_stock_chart(csv_path: str) -> str:
    """
    Generates a professional stock chart PNG from CSV data.
    Always reads from workspace/stock_data.csv automatically.
    Saves chart to workspace/tech_market_analysis.png
    Input: any string — the tool always uses the correct path.
    """
    try:
        # Always use absolute path — ignores whatever agent passes
        if not os.path.exists(CSV_PATH):
            return (
                f"❌ ERROR: {CSV_PATH} not found.\n"
                f"Please run Stock Data Fetcher tool first."
            )

        df = pd.read_csv(CSV_PATH, index_col=0, parse_dates=True)
        df.dropna(how="all", inplace=True)

        colors = {
            "AAPL": "#1f77b4",
            "MSFT": "#2ca02c",
            "NVDA": "#ff7f0e",
        }

        fig, ax = plt.subplots(figsize=(14, 7))

        for col in df.columns:
            ax.plot(
                df.index,
                df[col],
                label      = col,
                linewidth  = 2.5,
                color      = colors.get(col, None),
                marker     = "o",
                markersize = 2,
            )

        ax.set_title(
            "Tech Giants — 6 Month Stock Performance\n(AAPL vs MSFT vs NVDA)",
            fontsize   = 16,
            fontweight = "bold",
            pad        = 20,
        )
        ax.set_xlabel("Date", fontsize=13)
        ax.set_ylabel("Closing Price (USD $)", fontsize=13)
        ax.legend(fontsize=12, loc="upper left", framealpha=0.9)
        ax.grid(True, linestyle="--", alpha=0.5)
        fig.autofmt_xdate(rotation=45)
        plt.tight_layout()
        plt.savefig(CHART_PATH, dpi=150, bbox_inches="tight")
        plt.close()

        return (
            f"✅ Chart saved to: {CHART_PATH}\n"
            f"📐 Stocks: {', '.join(df.columns.tolist())}\n"
            f"📅 Range : {df.index[0].date()} → {df.index[-1].date()}"
        )

    except Exception as e:
        return f"❌ ERROR: {str(e)}"
