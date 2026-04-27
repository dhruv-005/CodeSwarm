# agents.py
import os
from crewai import Agent, LLM
from tools import fetch_stock_data, generate_stock_chart
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env file.")

# ── Best available model from your Groq account ───────────────────────────────
llm = LLM(
    model           = "groq/meta-llama/llama-4-scout-17b-16e-instruct",
    api_key         = api_key,
    temperature     = 0,
    max_tokens      = 512,
    request_timeout = 120,
)


# ── Agent 1: Planner ──────────────────────────────────────────────────────────
planner = Agent(
    role      = "Planner",
    goal      = "Write a short 3-step plan to analyze AAPL MSFT NVDA stocks.",
    backstory = (
        "You are a concise technical planner. "
        "You write short plans under 60 words. "
        "You never delegate work to others."
    ),
    llm              = llm,
    verbose          = True,
    allow_delegation = False,
    max_iter         = 2,
)


# ── Agent 2: Data Engineer ────────────────────────────────────────────────────
data_engineer = Agent(
    role      = "Data Engineer",
    goal      = "Fetch stock data using the Stock Data Fetcher tool.",
    backstory = (
        "You are a data engineer. "
        "Your only job is to call the Stock Data Fetcher tool "
        "with input 'AAPL,MSFT,NVDA' and report the result. "
        "You never delegate work to others."
    ),
    llm              = llm,
    tools            = [fetch_stock_data],
    verbose          = True,
    allow_delegation = False,
    max_iter         = 2,
)


# ── Agent 3: Analyst ──────────────────────────────────────────────────────────
analyst = Agent(
    role      = "Analyst",
    goal      = "Generate a stock chart using the Chart Generator tool.",
    backstory = (
        "You are a chart analyst. "
        "Your only job is to call the Chart Generator tool "
        "with input 'workspace/stock_data.csv' and report the result. "
        "You never delegate work to others."
    ),
    llm              = llm,
    tools            = [generate_stock_chart],
    verbose          = True,
    allow_delegation = False,
    max_iter         = 2,
)


# ── Agent 4: Reviewer ─────────────────────────────────────────────────────────
reviewer = Agent(
    role      = "Reviewer",
    goal      = "Write a short report confirming all files were created.",
    backstory = (
        "You are a QA reviewer. "
        "You write short confirmation reports under 60 words. "
        "You never delegate work to others."
    ),
    llm              = llm,
    verbose          = True,
    allow_delegation = False,
    max_iter         = 2,
)
