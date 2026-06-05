from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
import time
from decimal import Decimal
import datetime
from dotenv import load_dotenv

load_dotenv()

def serialize_value(v):
    if isinstance(v, Decimal):
        return float(v)
    if isinstance(v, (datetime.date, datetime.datetime)):
        return str(v)
    return v

def serialize_rows(rows):
    return [[serialize_value(cell) for cell in row] for row in rows]

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.3,
    max_output_tokens=400
)

def format_with_gemini(question, headers, rows, max_rows=10):
    if not rows:
        return json.dumps({
            "summary": "No data available for this query.",
            "table": {"headers": headers, "rows": []},
            "graph_suggestion": {"type": "none", "labels": [], "values": []}
        }, indent=2)

    # Trim rows to avoid huge input
    trimmed_rows = rows[:max_rows]

    table_csv = "\n".join(
        [", ".join(headers)] + [", ".join(map(str, row)) for row in trimmed_rows]
    )

    prompt = f"""
You are a data assistant. Analyze the CSV table below and return structured insights in valid JSON.

## User Query:
{question}

## Table (CSV):
{table_csv}

## Format (always follow this):
{{
  "summary": "...",
  "table": {{
    "headers": [...],
    "rows": [...]
  }},
  "graph_suggestion": {{
    "type": "bar_chart" | "line_chart" | "pie_chart" | "doughnut_chart" | "none",
    "labels": [...],
    "values": [...]
  }}
}}

- Use only the provided data.
- No markdown, no extra commentary.
    """.strip()

    # Retry up to 3 times with backoff for rate limit errors
    last_error = None
    for attempt in range(3):
        try:
            response = llm.invoke(prompt).content.strip()

            if response.startswith("```json"):
                response = response.replace("```json", "").replace("```", "").strip()

            json.loads(response)  # Validate
            return response

        except Exception as e:
            last_error = e
            err_str = str(e).lower()
            # If rate limited, wait and retry
            if "resource exhausted" in err_str or "quota" in err_str or "429" in err_str:
                wait_time = 20 * (attempt + 1)  # 20s, 40s, 60s
                print(f"⚠️ Rate limit hit. Waiting {wait_time}s before retry {attempt+1}/3...")
                time.sleep(wait_time)
            else:
                break  # Non-rate-limit error, don't retry

    safe_rows = serialize_rows(trimmed_rows)
    return json.dumps({
        "summary": "⚠️ Gemini is temporarily rate-limited. The data table is shown below.",
        "table": {"headers": headers, "rows": safe_rows},
        "graph_suggestion": {"type": "none", "labels": [], "values": []},
        "error": str(last_error)
    }, indent=2)

