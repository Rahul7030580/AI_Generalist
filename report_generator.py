from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ddr(sections):

    prompt = f"""
Generate a Detailed Diagnostic Report (DDR).

STRICT RULES:
- Do NOT invent information
- Use ONLY given data
- If missing → write "Not Available"
- Keep client-friendly language

STRUCTURE:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

DATA:
{sections}
"""

    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )

    return res.choices[0].message.content