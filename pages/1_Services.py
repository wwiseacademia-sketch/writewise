import streamlit as st

st.set_page_config(page_title="Services | WriteWise", layout="wide")

st.title("Services")
st.caption("Custom quote only • Worldwide / Remote Services")

services = [
    ("Assignment Review & Editing", "Improve clarity, structure, academic tone, and citation quality."),
    ("Thesis & Dissertation Editing", "Chapter-level editing, consistency checks, formatting, and readability improvement."),
    ("Research Proposal Support", "Strengthen research question, structure, objectives, and methodology clarity."),
    ("Literature Review Structuring", "Theme-based organization, synthesis improvement, and citation alignment."),
    ("Research Methodology Guidance", "Support for design, framework, variables, tools, and academic logic."),
    ("Editing & Proofreading", "Grammar, flow, academic tone, and clarity polishing."),
    ("Formatting & Referencing", "APA, MLA, Harvard, Chicago, Vancouver—clean structure and referencing."),
    ("Similarity Reduction (Ethical)", "Improve paraphrasing and citations (quality-first approach)."),
    ("Turnitin Similarity Check (Add-on)", "Similarity check support and guidance.")
]

cols = st.columns(2)
for i, (title, desc) in enumerate(services):
    with cols[i % 2]:
        st.subheader(title)
        st.write(desc)

st.divider()
st.info("Free revisions within 14 days (same scope/instructions). Response time: within 24 hours.")