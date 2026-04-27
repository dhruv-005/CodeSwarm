<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6C63FF,50:F55036,100:0668E1&height=200&section=header&text=CodeSwarm&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Autonomous%20Multi-Agent%20AI%20Workflow&descAlignY=60&descSize=22&animation=fadeIn" width="100%"/>

# ⚡ Where AI Agents Think, Collaborate & Deliver ⚡

### *Four Minds. One Mission. Zero Human Intervention.*

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-1.13.0-FF6B35?style=for-the-badge&logo=robotframework&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-F55036?style=for-the-badge&logo=thunderstore&logoColor=white)
![Meta](https://img.shields.io/badge/Meta-Llama%204%20Scout-0668E1?style=for-the-badge&logo=meta&logoColor=white)
![LiteLLM](https://img.shields.io/badge/LiteLLM-Model%20Router-8A2BE2?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

<br/>

> 🚀 A **production-grade Multi-Agent AI Pipeline** built with **CrewAI**, powered by **Meta's Llama 4 Scout**
> via **Groq's ultra-fast LPU inference**. Four specialized autonomous AI agents collaborate in sequence —
> fetching real-time financial data, performing deep analysis, generating professional visualizations,
> and delivering a quality-assured report. **All without a single human intervention.**

<br/>

[![⭐ Star this repo](https://img.shields.io/github/stars/dhruv-005/CodeSwarm?style=for-the-badge&logo=github&color=FFD700&logoColor=black&label=⭐%20Star%20This%20Repo)](https://github.com/dhruv-005/CodeSwarm)
[![🍴 Fork](https://img.shields.io/github/forks/dhruv-005/CodeSwarm?style=for-the-badge&logo=github&color=6C63FF&logoColor=white&label=🍴%20Fork)](https://github.com/dhruv-005/CodeSwarm/fork)

</div>

---

<div align="center">

## 🌊 The Pipeline at a Glance

```
╔══════════════╗    ╔══════════════════╗    ╔══════════════╗    ╔══════════════╗
║  🧠 Planner  ║ ──▶║ 🔧 Data Engineer  ║ ──▶║ 📊 Analyst   ║ ──▶║  ✅ QA Lead  ║
║              ║    ║                  ║    ║              ║    ║              ║
║  3-Step Plan ║    ║   stock_data.csv ║    ║  chart.png   ║    ║ Final Report ║
╚══════════════╝    ╚══════════════════╝    ╚══════════════╝    ╚══════════════╝
      │                      │                     │                    │
   yfinance              matplotlib            CrewAI              Groq LPU
```

</div>

---

## 📖 Table of Contents

| # | Section | Description |
|---|---------|-------------|
| 1 | [🚀 Project Overview](#-project-overview) | What CodeSwarm is and why it matters |
| 2 | [✨ Key Features](#-key-features) | All major capabilities at a glance |
| 3 | [🛠️ Architecture & Tech Stack](#️-architecture--tech-stack) | Technologies powering the system |
| 4 | [📂 Project Structure](#-project-structure) | File and folder layout |
| 5 | [🤖 Agent Roles & Responsibilities](#-agent-roles--responsibilities) | What each agent does |
| 6 | [🔬 How It Works Under the Hood](#-how-it-works-under-the-hood) | Deep-dive into internals |
| 7 | [⚙️ Installation & Setup](#️-installation--setup) | Step-by-step setup guide |
| 8 | [🧭 Usage Guide](#-usage-guide) | How to run CodeSwarm |
| 9 | [🖼️ Screenshots & Output](#️-screenshots--output) | Visual results and sample outputs |
| 10 | [📊 Output & Results](#-output--results) | Output file specifications |
| 11 | [🚀 Future Enhancements](#-future-enhancements) | Planned features and roadmap |
| 12 | [📜 License](#-license) | Licensing information |
| 13 | [👤 Author](#-author) | About the creator |

---

## 🚀 Project Overview

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║           WHAT MAKES CODESWARM DIFFERENT?                        ║
║                                                                  ║
║   Traditional AI  →  One model, one call, one answer             ║
║   CodeSwarm       →  4 agents, sequential pipeline, real tools   ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

**CodeSwarm** demonstrates the full power of **Agentic AI** — a paradigm where multiple specialized AI agents autonomously collaborate to complete complex, multi-step real-world tasks.

Rather than relying on a single monolithic AI call, CodeSwarm orchestrates a **team of four purpose-built agents**, each with a defined role, goal, backstory, and set of callable tools. The result is a robust, production-style pipeline that mirrors how real engineering teams work.

<br/>

### 🎯 What It Does

```
📡 Real-Time Stock Data  ──▶  📈 Professional Chart  ──▶  🔍 QA Review  ──▶  📄 Final Report
      (yfinance)                   (matplotlib)              (AI Agent)        (workspace/)
```

<br/>

### 💡 What You Will Learn From This Project

| Concept | How CodeSwarm Demonstrates It |
|---------|-------------------------------|
| 🤖 **Multi-Agent Orchestration** | 4 agents with distinct roles coordinated by CrewAI |
| 🧠 **LLM-Powered Reasoning** | Llama 4 Scout drives every agent decision via Groq |
| 🔧 **Tool-Augmented Agents** | Agents call Python functions as real executable tools |
| 🔗 **Sequential Context Passing** | Each agent builds on the previous agent's output |
| 📡 **Real-World Data Integration** | Live Yahoo Finance stock data via yfinance |
| 🛡️ **Production Safety Patterns** | Absolute path resolution, output verification, QA gate |

---

## ✨ Key Features

<div align="center">

```
┌──────────────────────────────────────────────────────────────────────┐
│                    CODESWARM FEATURE SET                             │
├──────────────────────────────────────────────────────────────────────┤
│  🤖  4 Specialized AI Agents    🔥  Groq LPU Ultra-Fast Inference     │
│  📡  Real-Time Market Data      📊  Publication-Quality Charts        │
│  🔗  Sequential Pipeline        🛠️  Tool-Augmented Agents             │
│  🛡️  Absolute Path Safety       ✅  Automated QA Verification         │
└──────────────────────────────────────────────────────────────────────┘
```

</div>

| # | 🏷️ Feature | 📝 Description |
|---|------------|----------------|
| 1 | 🤖 **4 Specialized AI Agents** | Planner, Data Engineer, Analyst, and QA Reviewer each have distinct roles, goals, and backstories |
| 2 | ⚡ **Llama 4 Scout via Groq** | Powered by Meta's latest model on Groq's blazing-fast LPU inference — sub-second responses |
| 3 | 📡 **Real-Time Market Data** | Live 6-month stock data fetched from Yahoo Finance for AAPL, MSFT, and NVDA |
| 4 | 📊 **Professional Charts** | Matplotlib generates 14×7 inch, 150 DPI publication-quality multi-line stock charts |
| 5 | 🔗 **Sequential Pipeline** | Agents execute in strict order with full context passed between each step |
| 6 | 🛠️ **Tool-Augmented Agents** | Agents call Python tools directly to fetch data and generate visualizations |
| 7 | 🛡️ **Absolute Path Safety** | Chart tool always resolves to the correct file path regardless of agent input |
| 8 | ✅ **Output Verification** | Final QA agent verifies all deliverables exist before reporting completion |

---

## 🛠️ Architecture & Tech Stack

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║                  TECHNOLOGY LAYERS                       ║
╠══════════════════════════════════════════════════════════╣
║  🎭  CrewAI 1.13.0        →  Multi-Agent Orchestration   ║
║  🔀  LiteLLM              →  Model Provider Abstraction  ║
║  ⚡  Groq LPU API         →  Ultra-Fast Inference        ║
║  🧠  Llama 4 Scout 17B    →  Agent Reasoning & Planning  ║
║  📡  yFinance             →  Real-Time Market Data       ║
║  📊  Matplotlib + Pandas  →  Charts & Data Processing    ║
║  🔐  python-dotenv        →  Secure Key Management       ║
║  🐍  Python 3.11          →  Core Runtime                ║
╚══════════════════════════════════════════════════════════╝
```

</div>

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | **Python** | `3.11` | Core runtime |
| ![CrewAI](https://img.shields.io/badge/-CrewAI-FF6B35?logo=robotframework&logoColor=white) | **CrewAI** | `1.13.0` | Multi-agent orchestration framework |
| ![Groq](https://img.shields.io/badge/-Groq-F55036?logo=thunderstore&logoColor=white) | **Groq API** | Latest | Ultra-fast LPU inference engine |
| ![Meta](https://img.shields.io/badge/-Meta%20Llama-0668E1?logo=meta&logoColor=white) | **Llama 4 Scout 17B** | 16E Instruct | Agent reasoning and decision making |
| ![LiteLLM](https://img.shields.io/badge/-LiteLLM-8A2BE2?logo=openai&logoColor=white) | **LiteLLM** | Latest | Model provider abstraction layer |
| ![Yahoo](https://img.shields.io/badge/-yFinance-6001D2?logo=yahoo&logoColor=white) | **yFinance** | Latest | Real-time Yahoo Finance stock data |
| ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?logo=python&logoColor=white) | **Matplotlib** | Latest | Professional chart generation |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) | **Pandas** | Latest | CSV handling and data manipulation |
| ![dotenv](https://img.shields.io/badge/-python--dotenv-ECD53F?logo=dotenv&logoColor=black) | **python-dotenv** | Latest | Secure API key management |

---

## 📂 Project Structure

```
📦 CodeSwarm/
│
├── 📄 main.py                    ← Pipeline orchestrator — assembles & runs the crew
├── 📄 agents.py                  ← All 4 agent definitions with roles, goals & LLM config
├── 📄 tasks.py                   ← Task definitions with descriptions & expected outputs
├── 📄 tools.py                   ← Custom Python tools agents use to fetch data & chart
├── 📄 requirements.txt           ← Pinned Python dependencies
├── 📄 .env                       ← 🔐 API keys — NEVER committed to Git
├── 📄 .gitignore                 ← Git exclusion rules
├── 📄 README.md                  ← 📖 You are reading this file
│
└── 📁 workspace/                 ← Auto-generated output directory
    ├── 📊 stock_data.csv         ← Raw fetched stock closing prices
    ├── 🖼️  tech_market_analysis.png ← Final rendered stock chart
    └── 📌 .gitkeep               ← Keeps folder tracked in Git when empty
```

> 💡 **Note:** The `workspace/` directory is **created automatically at runtime**.
> All generated files (`*.csv`, `*.png`) are **excluded from Git** via `.gitignore`.

---

## 🤖 Agent Roles & Responsibilities

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                      CODESWARM AGENT PIPELINE                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌──────────────┐    ┌──────────────────┐    ┌──────────────┐    ┌────────┐  ║
║  │  🧠 Planner  │───▶│ 🔧 Data Engineer  │───▶│ 📊 Analyst   │───▶│ ✅ QA  │  ║
║  └──────────────┘    └──────────────────┘    └──────────────┘    └────────┘  ║
║         │                     │                      │                │      ║
║         ▼                     ▼                      ▼                ▼      ║
║    3-Step Plan           stock_data.csv         chart.png       Final Report ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

| 🤖 Agent | 🎭 Role | 🛠️ Tools | 📋 Responsibility |
|----------|---------|----------|------------------|
| 🧠 **Planner** | Lead Technical Planner | None | Creates a concise 3-step execution plan for the crew |
| 🔧 **Data Engineer** | Senior Data Engineer | `Stock Data Fetcher` | Fetches 6-month closing prices for AAPL, MSFT, NVDA and saves to CSV |
| 📊 **Analyst** | Financial Data Analyst | `Chart Generator` | Reads the CSV and generates a professional multi-line PNG chart |
| ✅ **QA Reviewer** | Quality Assurance Lead | None | Verifies all deliverables exist and writes the final completion report |

<br/>

### 🧠 Agent 1 — The Planner

> *"I lay the blueprint before the first line of code runs."*

- **Goal:** Produce a clear, actionable 3-step plan
- **Backstory:** Senior AI systems architect with experience orchestrating complex pipelines
- **Output:** A structured plan consumed by all downstream agents as context

### 🔧 Agent 2 — The Data Engineer

> *"I speak to APIs so the rest of the team doesn't have to."*

- **Goal:** Reliably fetch and persist real-time stock data
- **Tool Used:** `fetch_stock_data()` — calls yfinance, saves CSV to `workspace/`
- **Output:** `workspace/stock_data.csv` with AAPL, MSFT, NVDA closing prices

### 📊 Agent 3 — The Analyst

> *"Raw numbers mean nothing — I turn them into stories."*

- **Goal:** Transform CSV data into a professional visual analysis
- **Tool Used:** `generate_chart()` — reads CSV, renders matplotlib chart, saves PNG
- **Output:** `workspace/tech_market_analysis.png`

### ✅ Agent 4 — The QA Reviewer

> *"Nothing ships without my sign-off."*

- **Goal:** Verify all deliverables are present and report completion
- **Check:** Confirms both `stock_data.csv` and `tech_market_analysis.png` exist
- **Output:** Final human-readable completion report

---

## 🔬 How It Works Under the Hood

### 1️⃣ Agent Reasoning Loop — ReAct Pattern

Each agent follows the **ReAct** (Reasoning + Acting) loop internally:

```
 ╔════════════════════════════════════════════════════╗
 ║              🔄 REACT AGENT LOOP                   ║
 ╠════════════════════════════════════════════════════╣
 ║                                                    ║
 ║  1. 💭 THINK   →  Analyze the task description.    ║
 ║  2. ⚡ ACT     →  Call a tool or form a response.  ║
 ║  3. 👁️ OBSERVE →  Read and process tool output.    ║
 ║  4. 🔁 REPEAT  →  Loop until task is complete.     ║
 ║  5. 📤 OUTPUT  →  Return final answer to crew.     ║
 ║                                                    ║
 ╚════════════════════════════════════════════════════╝
```

### 2️⃣ Sequential Context Passing

Agents share information through CrewAI's `context` parameter — each agent's output becomes the next agent's input:

```python
# Context flows forward through the pipeline
planning_task  →  no context needed       (first agent)
data_task      →  context=[planning_task]
chart_task     →  context=[data_task]
review_task    →  context=[data_task, chart_task]
```

### 3️⃣ Tool Execution Flow

```
🤖 Agent decides to use a tool
            │
            ▼
    CrewAI invokes Python function
            │
            ▼
  Tool executes (yfinance / matplotlib)
            │
            ▼
    Tool returns string result
            │
            ▼
  🤖 Agent reads result and continues
```

### 4️⃣ LLM Call Architecture

```
🤖 CrewAI Agent
        │
        ▼
🔀 LiteLLM  (model provider abstraction)
        │
        ▼
⚡ Groq API  (LPU hardware inference)
        │
        ▼
🧠 Meta Llama 4 Scout 17B 16E Instruct
        │
        ▼
📤 Response returned to Agent
```

### 📊 Stock Data Schema

| Column | Description | Source |
|--------|-------------|--------|
| `Date` | Trading day timestamp | Yahoo Finance |
| `AAPL` | Apple Inc. closing price (USD) | Yahoo Finance |
| `MSFT` | Microsoft Corp. closing price (USD) | Yahoo Finance |
| `NVDA` | NVIDIA Corp. closing price (USD) | Yahoo Finance |

---

## ⚙️ Installation & Setup

### ✅ Prerequisites

Before you begin, ensure you have the following:

| Requirement | Details |
|-------------|---------|
| 🐍 **Python** | Version `3.11` exactly (CrewAI 1.13.0 requires `< 3.13`) |
| 📦 **pip** | Latest version recommended |
| 🔑 **Groq API Key** | Free key from [console.groq.com/keys](https://console.groq.com/keys) |
| 🐙 **Git** | For cloning the repository |

---

### 📋 Step 1 — Clone the Repository

```bash
git clone https://github.com/dhruv-005/CodeSwarm.git
cd CodeSwarm
```

---

### 📋 Step 2 — Install pyenv & Python 3.11

```bash
# ── Install build dependencies ──────────────────────────────────────
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev sqlite3 curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev

# ── Install pyenv ────────────────────────────────────────────────────
curl https://pyenv.run | bash

# ── Add pyenv to your shell ──────────────────────────────────────────
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

# ── Install Python 3.11 ──────────────────────────────────────────────
pyenv install 3.11.9
pyenv local 3.11.9

# ── Verify ───────────────────────────────────────────────────────────
python --version
# Expected → Python 3.11.9
```

---

### 📋 Step 3 — Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
# Your prompt should now show (venv)
```

---

### 📋 Step 4 — Install Dependencies

```bash
pip install --upgrade pip
pip install "crewai[litellm]==1.13.0"
pip install crewai-tools==1.13.0
pip install groq python-dotenv yfinance matplotlib pandas
```

---

### 📋 Step 5 — Configure API Key

```bash
cat > .env << EOF
GROQ_API_KEY=your_groq_api_key_here
EOF
```

> 🔑 **Get your FREE Groq API key here:**
> **[https://console.groq.com/keys](https://console.groq.com/keys)**

---

### 📋 Step 6 — Verify Available Models

```bash
python -c "
import groq, os
from dotenv import load_dotenv
load_dotenv()
client = groq.Groq(api_key=os.getenv('GROQ_API_KEY'))
models = client.models.list()
print('✅ Available Models:')
for m in sorted(models.data, key=lambda x: x.id):
    print(f'   → {m.id}')
"
```

---

## 🧭 Usage Guide

### 🔄 Activate Environment (Every Session)

```bash
cd ~/CodeSwarm
source venv/bin/activate
```

### ▶️ Run CodeSwarm

```bash
python main.py
```

### 🖥️ Expected Console Output

```
🚀 CodeSwarm Pipeline Starting...
──────────────────────────────────────────
🧠 [Planner]        → Generating execution plan...
🔧 [Data Engineer]  → Fetching AAPL, MSFT, NVDA data...
📊 [Analyst]        → Generating market chart...
✅ [QA Reviewer]    → Verifying all deliverables...
──────────────────────────────────────────
✅ Pipeline Complete! Check workspace/ for outputs.
```

### 🖼️ View Output Chart

```bash
# Open chart on Linux
xdg-open workspace/tech_market_analysis.png

# Copy to Desktop
cp workspace/tech_market_analysis.png ~/Desktop/
```

---

## 🖼️ Screenshots & Output

> 📸 **Visual results generated by CodeSwarm after a successful pipeline run.**

---

### 📊 Generated Stock Performance Chart

<div align="center">

> *The chart below is auto-generated by the 📊 Analyst Agent using Matplotlib.*
> *It shows 6 months of closing prices for AAPL, MSFT, and NVDA.*

Tech Market Analysis Chart<img width="2084" height="1039" alt="tech_market_analysis" src="https://github.com/user-attachments/assets/a619c9ac-7ac4-48cd-9db1-898990395091" />

`workspace/tech_market_analysis.png` 

</div>

---

### 🖥️ Terminal Pipeline Execution

<div align="center">

> *CodeSwarm's sequential agent pipeline running in the terminal —
> each agent logs its progress in real-time.*

Terminal Output <img width="826" height="734" alt="Screenshot_2026-04-27_16_40_05" src="https://github.com/user-attachments/assets/956418da-d280-4be8-a619-4f3b1127cb42" /><img width="833" height="704" alt="Screenshot_2026-04-27_16_40_14" src="https://github.com/user-attachments/assets/cddbcaf5-fee1-44e5-9488-3a180e6b3d9d" /><img width="904" height="684" alt="Screenshot_2026-04-27_16_40_21" src="https://github.com/user-attachments/assets/3cd79be0-c226-46fc-92f7-ae636d6f6a80" /><img width="996" height="673" alt="Screenshot_2026-04-27_16_40_28" src="https://github.com/user-attachments/assets/d9348b8e-6090-4b2d-a82d-6e8551c6b3a4" /> <img width="956" height="652" alt="Screenshot_2026-04-27_16_40_36" src="https://github.com/user-attachments/assets/64de89ab-dc44-4126-8c31-a06e88637a10" /> <img width="1054" height="706" alt="Screenshot_2026-04-27_16_40_44" src="https://github.com/user-attachments/assets/e4169367-7ca4-43b8-9791-a9b1e7798b4a" /><img width="1054" height="706" alt="Screenshot_2026-04-27_16_40_44" src="https://github.com/user-attachments/assets/cf604a88-9db5-4856-8d46-f1187443e122" /> <img width="1024" height="658" alt="Screenshot_2026-04-27_16_40_49" src="https://github.com/user-attachments/assets/42838c73-e468-4f1e-bf05-dcdb44c5247b" /> <img width="928" height="617" alt="Screenshot_2026-04-27_16_40_55" src="https://github.com/user-attachments/assets/cc3a9186-c0b1-4817-9ef1-40710b7b1818" /> <img width="1098" height="682" alt="Screenshot_2026-04-27_16_41_00" src="https://github.com/user-attachments/assets/d3d9ef78-11a7-422c-a48c-d298a87ea8cc" /> <img width="1075" height="647" alt="Screenshot_2026-04-27_16_41_07" src="https://github.com/user-attachments/assets/70ea46ce-816c-432c-8b76-251fcc415099" /> <img width="1046" height="638" alt="Screenshot_2026-04-27_16_41_14" src="https://github.com/user-attachments/assets/c26dbcaa-8fcf-43a4-b30e-ce49b1bcb8fc" /> <img width="1081" height="641" alt="Screenshot_2026-04-27_16_41_23" src="https://github.com/user-attachments/assets/fa41356a-d024-4ead-9347-fc4d31459d9e" />


*Four agents execute in sequence — Planner → Data Engineer → Analyst → QA Reviewer*

</div>

---

### 📁 Workspace Output Files

<div align="center">

> *Auto-generated workspace directory after a successful run.*

Workspace Files <img width="1200" height="608" alt="Screenshot_2026-04-27_17_48_43" src="https://github.com/user-attachments/assets/b9debb76-0a73-4436-b085-b59ebc8b2a16" />
<img width="2084" height="1039" alt="tech_market_analysis" src="https://github.com/user-attachments/assets/a619c9ac-7ac4-48cd-9db1-898990395091" />

*`workspace/stock_data.csv` and `workspace/tech_market_analysis.png` — both verified by the QA Agent*

</div>

---

## 📊 Output & Results

After a successful run, the `workspace/` directory contains:

| 📁 File | 📝 Description |
|---------|----------------|
| 📄 `stock_data.csv` | 6 months of daily closing prices for AAPL, MSFT, NVDA |
| 🖼️ `tech_market_analysis.png` | Professional multi-line stock performance chart |

<br/>

### 🖼️ Chart Specifications

| ⚙️ Property | 📐 Value |
|-------------|----------|
| 📏 **Size** | 14 × 7 inches |
| 🔍 **Resolution** | 150 DPI (high quality) |
| 📈 **AAPL** | Blue line |
| 📈 **MSFT** | Green line |
| 📈 **NVDA** | Orange line |
| 📅 **X Axis** | Date range (6 months) |
| 💵 **Y Axis** | Closing Price in USD |
| 💾 **Format** | PNG with tight bounding box |

<br/>

### 📄 CSV Sample Structure

```
Date,AAPL,MSFT,NVDA
2024-07-01,210.62,446.34,123.54
2024-07-02,220.27,451.10,131.38
2024-07-03,221.55,462.37,135.58
...
```

---

## 🚀 Future Enhancements

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║              🗺️  CODESWARM ROADMAP                       ║
╚══════════════════════════════════════════════════════════╝
```

</div>

| Status | Feature | Description |
|--------|---------|-------------|
| 🔲 | **📈 More Stocks** | Extend to any user-defined ticker list |
| 🔲 | **🗞️ Sentiment Analysis Agent** | 5th agent scraping headlines for sentiment scoring |
| 🔲 | **📄 PDF Report Generator** | Full PDF combining chart + written analysis |
| 🔲 | **📧 Email Delivery Agent** | Auto-email final report to stakeholders |
| 🔲 | **🌐 Streamlit Dashboard** | Real-time web UI to trigger pipeline and view results |
| 🔲 | **🐳 Docker Deployment** | Containerized stack for one-command deployment |
| 🔲 | **⏰ Scheduled Runs** | Cron job support for daily automated market reports |
| 🔲 | **🪙 Multi-Market Support** | Extend to crypto (BTC, ETH) and forex markets |
| 🔲 | **🧪 Unit Tests** | Full test suite for agents, tools, and tasks |
| 🔲 | **📡 Live WebSocket Data** | Real-time streaming prices instead of batch fetching |

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
Copyright (c) 2024 Dhruv Sonani
```

---

## 👤 Author

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0668E1,50:8A2BE2,100:F55036&height=120&section=footer&fontSize=16&fontColor=ffffff&text=Built%20with%20%E2%9D%A4%EF%B8%8F%20by%20Dhruv%20Sonani&fontAlignY=65&animation=fadeIn" width="100%"/>

### ⚡ Dhruv Sonani

*"Building intelligent systems that think, collaborate, and deliver."*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-dhruv--005-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dhruv-005)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit%20Now-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://dhruv-005.github.io/Dhruv-s_Portfolio/)
[![Email](https://img.shields.io/badge/Email-dhruvsonani3312%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dhruvsonani3312@gmail.com)

<br/>

---

**⭐ If CodeSwarm helped you, inspired you, or saved you time — a star means the world! ⭐**

<br/>

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/-CrewAI-FF6B35?style=flat-square&logo=robotframework&logoColor=white)
![Groq](https://img.shields.io/badge/-Groq-F55036?style=flat-square&logo=thunderstore&logoColor=white)
![Meta](https://img.shields.io/badge/-Llama%204-0668E1?style=flat-square&logo=meta&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)
![LiteLLM](https://img.shields.io/badge/-LiteLLM-8A2BE2?style=flat-square&logo=openai&logoColor=white)
![yFinance](https://img.shields.io/badge/-yFinance-6001D2?style=flat-square&logo=yahoo&logoColor=white)

</div>
