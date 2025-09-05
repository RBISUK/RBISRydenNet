import streamlit as st

st.set_page_config(
    page_title="RydenNet",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    body {background-color: #0d1117; color: #00ff00;}
    .sidebar .sidebar-content {background-color: #111; color: #00ff00;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("RydenNet – Behavioural & Intelligence AI")
st.sidebar.title("RydenNet Control Panel")

st.sidebar.markdown("Upload PDFs, images, audio to extract intelligence.")

uploaded_files = st.sidebar.file_uploader(
    "Upload your files", accept_multiple_files=True,
    type=['pdf','png','jpg','jpeg','mp3','wav','opus']
)

search_query = st.sidebar.text_input("Search extracted data:")

if uploaded_files:
    for file in uploaded_files:
        st.write(f"Uploaded file: {file.name}")
        # Here you will call your text extraction, OCR, or audio processing functions
        # Example placeholder:
        st.write("Extracted text/intelligence will appear here.")

if search_query:
    st.write(f"Searching for: {search_query}")
    # Example: filter extracted content by search_query
