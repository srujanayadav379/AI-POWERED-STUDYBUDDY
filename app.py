import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables (.env for local development)

load_dotenv()

# Get API key from .env or Streamlit Secrets

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
try:
api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
st.error("⚠️ Gemini API key not configured.")
st.stop()

# Initialize Gemini Client

client = genai.Client(api_key=api_key)

# Page Configuration

st.set_page_config(
page_title="AI-Powered Study Buddy",
page_icon="🎓",
layout="wide"
)

# Title

st.title("🎓 AI-Powered Study Buddy")
st.write(
"Explain concepts, summarize notes, and generate quizzes using Google Gemini AI."
)

# Sidebar Options

st.sidebar.header("Options")

mode = st.sidebar.radio(
"Choose Task:",
["Explain Concept", "Summarize Notes", "Generate Quiz"]
)

# User Input

text_input = st.text_area(
"✏️ Enter your topic, notes, or text:",
height=200
)

# Generate Button

if st.button("🚀 Generate Result"):

```
if not text_input.strip():
    st.warning("Please enter some text first!")
    st.stop()

# Prompt Selection
if mode == "Explain Concept":
    prompt = f"""
```

Explain the following concept clearly and simply for a student:

{text_input}
"""

```
elif mode == "Summarize Notes":
    prompt = f"""
```

Summarize the following notes into key points and provide a short summary:

{text_input}
"""

```
else:
    prompt = f"""
```

Generate 5 quiz questions with answers based on the following content:

{text_input}
"""

```
try:
    with st.spinner("Generating response..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.success("✅ Done!")
        st.markdown(response.text)

except Exception as e:

    error_msg = str(e)

    if "429" in error_msg:
        st.error(
            "⚠️ Gemini API quota exceeded. Please try again later or use a new API key."
        )

    elif "503" in error_msg:
        st.error(
            "⚠️ Gemini service is currently busy. Please try again in a few minutes."
        )

    else:
        st.error(f"❌ Error: {e}")
```

# Footer

st.caption("Powered by Google Gemini AI ⚡")
