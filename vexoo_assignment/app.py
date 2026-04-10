import streamlit as st
from ingestion import sliding_window, KnowledgeBase
from retrieval import format_output
from router import route_query

st.set_page_config(page_title="AI Knowledge System", layout="centered")

st.title("🧠 AI Knowledge Retrieval System")

# 🔥 Improved Knowledge Base
text = """
Artificial Intelligence is the simulation of human intelligence in machines that are programmed to think and learn.

Operating systems manage computer hardware and software resources and provide services for computer programs.

Machine learning is a subset of AI that enables systems to learn from data without explicit programming.

Data structures organize and store data efficiently for processing.

Errors in systems can occur due to bugs or incorrect logic.
"""

# Build KB
chunks = sliding_window(text)
kb = KnowledgeBase()
kb.add_documents(chunks)

# Input
query = st.text_input("Enter your query:")

if query:
    route = route_query(query)
    result = kb.search(query)
    output = format_output(result)

    st.subheader("🔀 Routing")
    st.write(route)

    st.subheader("🔍 Result")
    st.write("**Summary:**", output["summary"])

    st.subheader("📄 Full Context")
    st.write(result.raw_text)

    st.write("**Category:**", output["category"])
    st.write("**Keywords:**", output["keywords"])