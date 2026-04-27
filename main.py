# main.py
import os
import time
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import planner, data_engineer, analyst, reviewer
from tasks  import planning_task, data_task, chart_task, review_task

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError(
        "❌ GROQ_API_KEY not found.\n"
        "Add GROQ_API_KEY=your_key to your .env file\n"
        "Get free key: https://console.groq.com/keys"
    )

os.makedirs("workspace", exist_ok=True)

# ── Assemble Crew ─────────────────────────────────────────────────────────────
codeswarm = Crew(
    agents  = [planner, data_engineer, analyst, reviewer],
    tasks   = [planning_task, data_task, chart_task, review_task],
    process = Process.sequential,
    verbose = True,
)

# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    print("=" * 60)
    print("🐝  CodeSwarm — CrewAI Multi-Agent Pipeline")
    print("=" * 60)
    print("🤖  Agents : Planner → Data Engineer → Analyst → QA")
    print("🧠  Model  : Llama 4 Scout 17B via Groq")
    print("📊  Task   : 6-Month Tech Stock Analysis")
    print("📁  Output : workspace/tech_market_analysis.png")
    print("=" * 60)
    print("⏳  Waiting 20s to clear any rate limits...")
    print("=" * 60)

    time.sleep(20)

    result = codeswarm.kickoff()

    # ── Verify Output Files Exist ─────────────────────────────────────────────
    BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
    CSV_PATH   = os.path.join(BASE_DIR, "workspace", "stock_data.csv")
    CHART_PATH = os.path.join(BASE_DIR, "workspace", "tech_market_analysis.png")

    print("\n" + "=" * 60)
    print("🎉  CodeSwarm Complete!")
    print("=" * 60)
    print(result)
    print()
    print("📁 Output Files:")
    print(f"   CSV   → {CSV_PATH}")
    print(f"   Chart → {CHART_PATH}")
    print()
    print("📂 File Status:")
    print(f"   CSV   : {'✅ EXISTS' if os.path.exists(CSV_PATH)   else '❌ MISSING'}")
    print(f"   Chart : {'✅ EXISTS' if os.path.exists(CHART_PATH) else '❌ MISSING'}")
    print("=" * 60)
