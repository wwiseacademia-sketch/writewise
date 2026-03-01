import streamlit as st

st.set_page_config(page_title="Portfolio | WriteWise", layout="wide")

st.title("Portfolio")
st.caption("Redacted samples + case studies • Client privacy respected")

st.subheader("Filter by Domain")
domains = ["All", "Business Studies", "Social Sciences", "Education", "Law", "Accounting & Finance", "Research Methodology"]
selected = st.selectbox("Select domain", domains)

portfolio = [
    {
        "title": "Business Report Improvement (Redacted Sample)",
        "domain": "Business Studies",
        "type": "Redacted Sample",
        "work": ["Editing", "Referencing"],
        "summary": "Improved clarity, structure, and referencing consistency while keeping client details private."
    },
    {
        "title": "Social Sciences Essay Strengthening (Case Study)",
        "domain": "Social Sciences",
        "type": "Case Study",
        "work": ["Structure", "Argument flow"],
        "summary": "Organized arguments, improved academic flow, and aligned citations to the required style."
    },
    {
        "title": "Education Literature Review Structuring (Case Study)",
        "domain": "Education",
        "type": "Case Study",
        "work": ["Synthesis", "Citations"],
        "summary": "Re-structured themes and strengthened synthesis with cleaner academic tone."
    },
    {
        "title": "Finance Assignment Formatting Fix (Redacted Sample)",
        "domain": "Accounting & Finance",
        "type": "Redacted Sample",
        "work": ["Formatting", "Referencing"],
        "summary": "Clean formatting, consistent headings, and improved presentation quality."
    }
]

def show_item(item):
    st.markdown(f"### {item['title']}")
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        st.write(f"**Domain:** {item['domain']}")
        st.write(f"**Type:** {item['type']}")
    with c2:
        st.write("**Work included:**")
        for w in item["work"]:
            st.write(f"- {w}")
    with c3:
        st.write("**Summary:**")
        st.write(item["summary"])
    st.page_link("pages/3_Get_a_Quote.py", label="Request similar help →", icon="📝")
    st.divider()

filtered = []
for p in portfolio:
    if selected == "All" or p["domain"] == selected:
        filtered.append(p)

st.subheader("Samples & Case Studies")
if not filtered:
    st.info("No items in this filter yet. More samples can be added anytime.")
else:
    for item in filtered:
        show_item(item)

st.caption("Note: Samples are redacted to protect client privacy.")