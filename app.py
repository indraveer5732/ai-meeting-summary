# app.py
import streamlit as st
import os
from ollama_llm import query_ollama

st.set_page_config(page_title="AI Meeting Summarizer", layout="wide")
st.title("📋 AI Meeting Transcript Summarizer (Offline via Ollama)")

uploaded_file = st.file_uploader("Upload a meeting transcript (.txt)", type=["txt"])

if uploaded_file:
    transcript = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Transcript Preview")
    st.text_area("Transcript", transcript, height=300)

    if st.button("Generate Summary"):
        with st.spinner("Thinking using Ollama model..."):
            result = query_ollama(transcript)
            st.success("Summary Generated!")

        st.subheader("📌 Summary")
        st.markdown(result["summary"])

        st.subheader("🧱 Objections & Resolutions")
        st.markdown(result["objections"])

        st.subheader("✅ Action Items")
        st.markdown(result["action_items"])
