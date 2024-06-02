import streamlit as st

st.set_page_config(page_title="Gemini Home", page_icon=":gemini:")

with open("style.css") as f:
    st.set_page_config(layout="wide", content_padding=0)
    st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Navigation")
    # Add navigation options here (e.g., links to different functionalities)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.header("Welcome to Gemini")
    st.subheader("A Large Language Model by Google AI")

with col2:
    # Add an image or logo here (optional)

st.write("---")

# Prompt box
prompt_text = st.text_area("Enter your prompt:", height=100)

if prompt_text:
    # Replace this with your logic to process the prompt using Gemini API (not included)
    st.write("Processing your prompt...")
    # Display the generated response here
