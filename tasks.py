# tasks.py
import os
from crewai import Task
from agents import planner, data_engineer, analyst, reviewer

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
CSV_PATH   = os.path.join(BASE_DIR, "workspace", "stock_data.csv")
CHART_PATH = os.path.join(BASE_DIR, "workspace", "tech_market_analysis.png")


# ── Task 1: Plan ──────────────────────────────────────────────────────────────
planning_task = Task(
    description=(
        "Write a 3-step plan under 60 words to:\n"
        "1. Fetch AAPL, MSFT, NVDA stock data\n"
        "2. Generate a line chart\n"
        "3. Review the output files"
    ),
    expected_output="A numbered 3-step plan under 60 words.",
    agent=planner,
)


# ── Task 2: Fetch Data ────────────────────────────────────────────────────────
data_task = Task(
    description=(
        "Use the Stock Data Fetcher tool.\n"
        "Tool input: 'AAPL,MSFT,NVDA'\n"
        f"Confirm CSV was saved to: {CSV_PATH}"
    ),
    expected_output=(
        "One sentence confirming the CSV file was saved "
        "with the file path and latest prices."
    ),
    agent=data_engineer,
    context=[planning_task],
)


# ── Task 3: Generate Chart ────────────────────────────────────────────────────
chart_task = Task(
    description=(
        "Use the Chart Generator tool.\n"
        f"Tool input: '{CSV_PATH}'\n"
        f"Confirm chart was saved to: {CHART_PATH}"
    ),
    expected_output=(
        "One sentence confirming the PNG chart was saved "
        "with the file path."
    ),
    agent=analyst,
    context=[data_task],
)


# ── Task 4: Final Review ──────────────────────────────────────────────────────
review_task = Task(
    description=(
        "Write a final report under 60 words confirming:\n"
        f"- CSV file: {CSV_PATH}\n"
        f"- Chart file: {CHART_PATH}\n"
        "- Stocks covered: AAPL, MSFT, NVDA"
    ),
    expected_output="A confirmation report under 60 words.",
    agent=reviewer,
    context=[data_task, chart_task],
)
