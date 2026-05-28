import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
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
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="LinkedIn AI Analyzer",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stTextArea textarea {
    font-size: 16px;
}

h1, h2, h3 {
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.metric-card {
    background-color: #1E1E1E;
    padding: 1rem;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.title("🚀 LinkedIn AI Post Analyzer")

st.markdown("""
Analyze and optimize your LinkedIn posts using AI.

### Features
- Hook analysis
- Engagement optimization
- Virality scoring
- AI-powered rewriting
- CTA improvements
- Smart hashtag generation
""")

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("⚙️ Settings")

tone = st.sidebar.selectbox(
    "Select Post Tone",
    [
        "Professional",
        "Storytelling",
        "Technical",
        "Founder Style",
        "Viral Style"
    ]
)

audience = st.sidebar.selectbox(
    "Target Audience",
    [
        "Developers",
        "Recruiters",
        "Founders",
        "Students",
        "General Tech Audience"
    ]
)

# =========================================
# USER INPUT
# =========================================

post_input = st.text_area(
    "Paste your LinkedIn post here:",
    height=300,
    placeholder="Write or paste your LinkedIn post..."
)

character_count = len(post_input)

st.caption(f"Character Count: {character_count}")

# =========================================
# CHARACTER FEEDBACK
# =========================================

if character_count > 0:

    if character_count < 150:
        st.warning("⚠️ Your post may be too short for strong engagement.")

    elif character_count > 3000:
        st.warning("⚠️ Your post may be too long for LinkedIn readability.")

    else:
        st.success("✅ Good LinkedIn post length.")

# =========================================
# ANALYZE BUTTON
# =========================================

if st.button("🚀 Analyze Post"):

    if post_input.strip() == "":

        st.warning("Please enter a LinkedIn post.")

    else:

        prompt = f"""
You are an expert LinkedIn growth strategist.

Analyze the LinkedIn post below.

POST TONE:
{tone}

TARGET AUDIENCE:
{audience}

Return your response STRICTLY in this exact format.

HOOK_SCORE:
(Return format like 8/10)

READABILITY_SCORE:
(Return format like 7/10)

ENGAGEMENT_SCORE:
(Return format like 9/10)

VIRALITY_SCORE:
(Return format like 8/10)

HOOK_FEEDBACK:
(Explain hook quality)

READABILITY_FEEDBACK:
(Explain readability)

ENGAGEMENT_SUGGESTIONS:
(How to improve engagement)

CTA_SUGGESTIONS:
(How to improve CTA)

BEST_POSTING_TIME:
(Suggest best posting time)

REWRITTEN_POST:
(Write improved LinkedIn version)

HASHTAGS:
(List hashtags separated by commas)

LinkedIn Post:
{post_input}
"""

        try:

            with st.spinner("Analyzing your LinkedIn post..."):

                response = model.generate_content(prompt)

                result = response.text

                # =========================================
                # PARSE RESPONSE
                # =========================================

                sections = {}

                current_key = None

                for line in result.splitlines():

                    line = line.strip()

                    if line.endswith(":"):

                        current_key = line.replace(":", "")

                        sections[current_key] = ""

                    elif current_key:

                        sections[current_key] += line + "\n"

                # =========================================
                # SAFE SCORE EXTRACTION
                # =========================================

                def extract_score(value):

                    try:
                        return int(
                            value.split("/")[0].strip()
                        )
                    except:
                        return 0

                hook_score = extract_score(
                    sections.get("HOOK_SCORE", "0")
                )

                readability_score = extract_score(
                    sections.get("READABILITY_SCORE", "0")
                )

                engagement_score = extract_score(
                    sections.get("ENGAGEMENT_SCORE", "0")
                )

                virality_score = extract_score(
                    sections.get("VIRALITY_SCORE", "0")
                )

                # =========================================
                # RESULTS HEADER
                # =========================================

                st.divider()

                st.header("📊 AI Performance Dashboard")

                # =========================================
                # SCORE DASHBOARD
                # =========================================

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "🎯 Hook Score",
                        f"{hook_score}/10"
                    )

                    st.progress(hook_score / 10)

                    st.metric(
                        "📖 Readability Score",
                        f"{readability_score}/10"
                    )

                    st.progress(readability_score / 10)

                with col2:

                    st.metric(
                        "📈 Engagement Score",
                        f"{engagement_score}/10"
                    )

                    st.progress(engagement_score / 10)

                    st.metric(
                        "🚀 Virality Score",
                        f"{virality_score}/10"
                    )

                    st.progress(virality_score / 10)

                # =========================================
                # BEST SCORE INSIGHT
                # =========================================

                score_map = {
                    "Hook": hook_score,
                    "Readability": readability_score,
                    "Engagement": engagement_score,
                    "Virality": virality_score
                }

                strongest_area = max(
                    score_map,
                    key=score_map.get
                )

                weakest_area = min(
                    score_map,
                    key=score_map.get
                )

                st.info(
                    f"🔥 Strongest Area: {strongest_area} | "
                    f"⚠️ Weakest Area: {weakest_area}"
                )

                # =========================================
                # FEEDBACK SECTIONS
                # =========================================

                st.subheader("🪝 Hook Feedback")

                st.write(
                    sections.get(
                        "HOOK_FEEDBACK",
                        "Not Available"
                    )
                )

                st.subheader("📖 Readability Feedback")

                st.write(
                    sections.get(
                        "READABILITY_FEEDBACK",
                        "Not Available"
                    )
                )

                st.subheader("📈 Engagement Suggestions")

                st.write(
                    sections.get(
                        "ENGAGEMENT_SUGGESTIONS",
                        "Not Available"
                    )
                )

                st.subheader("🔥 CTA Suggestions")

                st.write(
                    sections.get(
                        "CTA_SUGGESTIONS",
                        "Not Available"
                    )
                )

                st.subheader("⏰ Best Posting Time")

                st.success(
                    sections.get(
                        "BEST_POSTING_TIME",
                        "Not Available"
                    )
                )

                # =========================================
                # REWRITTEN POST
                # =========================================

                st.subheader("✍️ Optimized LinkedIn Post")

                rewritten_post = sections.get(
                    "REWRITTEN_POST",
                    "Not Available"
                )

                st.text_area(
                    "AI Rewritten Post",
                    rewritten_post,
                    height=300
                )

                # =========================================
                # HASHTAGS
                # =========================================

                st.subheader("🏷️ Suggested Hashtags")

                st.info(
                    sections.get(
                        "HASHTAGS",
                        "Not Available"
                    )
                )

                # =========================================
                # DOWNLOAD REPORT
                # =========================================

                full_report = f"""
LINKEDIN AI ANALYSIS REPORT

HOOK SCORE:
{sections.get("HOOK_SCORE", "")}

READABILITY SCORE:
{sections.get("READABILITY_SCORE", "")}

ENGAGEMENT SCORE:
{sections.get("ENGAGEMENT_SCORE", "")}

VIRALITY SCORE:
{sections.get("VIRALITY_SCORE", "")}

HOOK FEEDBACK:
{sections.get("HOOK_FEEDBACK", "")}

READABILITY FEEDBACK:
{sections.get("READABILITY_FEEDBACK", "")}

ENGAGEMENT SUGGESTIONS:
{sections.get("ENGAGEMENT_SUGGESTIONS", "")}

CTA SUGGESTIONS:
{sections.get("CTA_SUGGESTIONS", "")}

BEST POSTING TIME:
{sections.get("BEST_POSTING_TIME", "")}

REWRITTEN POST:
{sections.get("REWRITTEN_POST", "")}

HASHTAGS:
{sections.get("HASHTAGS", "")}
"""

                st.download_button(
                    label="📥 Download Full Analysis",
                    data=full_report,
                    file_name="linkedin_ai_analysis.txt",
                    mime="text/plain"
                )

        except ResourceExhausted:

            st.error(
                "⚠️ Gemini API rate limit exceeded. "
                "Please wait 20 seconds and try again."
            )

        except Exception as e:

            st.error(
                f"Unexpected Error: {e}"
            )