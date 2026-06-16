import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ Please set your GEMINI_API_KEY in a .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Study Buddy")
st.write("Explain concepts, summarize notes, and generate quizzes using Google Gemini AI.")

st.sidebar.header("Options")

mode = st.sidebar.radio(
    "Choose Task:",
    ["Explain Concept", "Summarize Notes", "Generate Quiz"]
)

text_input = st.text_area(
    "✏️ Enter your topic, notes, or text:"
)

if st.button("🚀 Generate Result"):

    if text_input.strip():

        if mode == "Explain Concept":
            prompt = f"Explain this concept clearly and simply for a student:\n\n{text_input}"

        elif mode == "Summarize Notes":
            prompt = f"Summarize the following study notes into key points and a short summary:\n\n{text_input}"

        else:
            prompt = f"Generate 5 quiz questions with answers based on this content:\n\n{text_input}"

        try:
            with st.spinner("Generating with Gemini..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.success("✅ Done!")
                st.markdown(response.text)

        except Exception as e:
            st.error(f"❌ Error: {e}")

    else:
        st.warning("Please enter some text first!")

st.caption("Powered by Google Gemini 2.5- Flash ⚡")