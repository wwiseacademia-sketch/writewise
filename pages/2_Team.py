import streamlit as st

st.set_page_config(page_title="Team | WriteWise", layout="wide")

st.title("Meet Our Expert Writers")
st.caption("Qualified specialists • Worldwide / Remote Services")

st.subheader("Domain Expertise")
matrix = [
    ("Research Methodology / Technical Writing", "Zaheer Abbas"),
    ("Social Sciences / Business Studies", "Mazhar Abbas"),
    ("Education / Academic Research", "Muhammad Imran"),
    ("Law / Business", "Muhammad Ahmad"),
    ("Accounting / Finance", "Fahad Ali"),
]
st.table({"Domain": [m[0] for m in matrix], "Specialist": [m[1] for m in matrix]})

st.divider()

writers = [
    {
        "name": "Zaheer Abbas",
        "role": "Senior Academic Editor",
        "qualification": "MPhil (Computer Science)",
        "experience": "7+ years",
        "domains": ["Research Methodology", "Technical/Analytical Writing"],
        "strengths": ["Research structure", "Academic clarity", "Referencing accuracy"],
    },
    {
        "name": "Mazhar Abbas",
        "role": "Social Science Specialist",
        "qualification": "MPhil (Social Sciences)",
        "experience": "5+ years",
        "domains": ["Social Sciences", "Business Studies"],
        "strengths": ["Theory-based writing", "Argument flow", "Clear structure"],
    },
    {
        "name": "Muhammad Imran",
        "role": "Education & Research Specialist",
        "qualification": "MPhil (Education)",
        "experience": "5+ years",
        "domains": ["Education", "Academic Research"],
        "strengths": ["Literature review structure", "Academic tone", "Consistency"],
    },
    {
        "name": "Muhammad Ahmad",
        "role": "Law & Research Specialist",
        "qualification": "MS",
        "experience": "5+ years",
        "domains": ["Law", "Business"],
        "strengths": ["Formal tone", "Logic & clarity", "Citation alignment"],
    },
    {
        "name": "Fahad Ali",
        "role": "Accounting & Finance Specialist",
        "qualification": "MS (Accounting & Finance)",
        "experience": "3+ years",
        "domains": ["Accounting", "Finance"],
        "strengths": ["Formatting precision", "Analytical clarity", "Clean presentation"],
    },
]

st.subheader("Writers")
cols = st.columns(2)

for idx, w in enumerate(writers):
    with cols[idx % 2]:
        st.markdown(f"### {w['name']}")
        st.write(f"**Role:** {w['role']}")
        st.write(f"**Qualification:** {w['qualification']}")
        st.write(f"**Experience:** {w['experience']}")
        st.write(f"**Domains:** {', '.join(w['domains'])}")
        st.write(f"**Strengths:** {', '.join(w['strengths'])}")

        # request-writer button (stores selection for Quote page later)
        if st.button(f"Request {w['name']}", key=f"req_{idx}"):
            st.session_state["requested_writer"] = w["name"]
            st.success(f"Saved: You requested **{w['name']}**. Go to **Get a Quote** page next.")

st.divider()
st.info("You can request a specific writer. We respond within 24 hours. Free revisions within 14 days (same scope).")