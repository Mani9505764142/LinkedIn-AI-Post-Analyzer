import time
import os

import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# CONFIGURE GEMINI
# =========================================

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# =========================================
# LOAD MODEL
# =========================================

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =========================================
# AI HOOK CLASSIFIER
# =========================================

def classify_hook_ai(hook):

    prompt = f"""
You are an expert LinkedIn growth strategist.

Analyze this LinkedIn hook.

HOOK:
{hook}

Classify it into ONE category only.

Possible Categories:

- Trend Observation
- Psychological Insight
- Framework
- Direct Strategy
- Contrarian
- Insight
- Philosophical
- Common Mistake
- Case Study
- Curiosity
- Value Pricing Concept
- Story

Return EXACTLY:

HOOK_TYPE:
REASON:
CONFIDENCE:
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except ResourceExhausted:

        print("\n⚠️ Gemini rate limit hit.")
        print("⏳ Waiting 25 seconds and retrying...\n")

        time.sleep(25)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"ERROR: {str(e)}"