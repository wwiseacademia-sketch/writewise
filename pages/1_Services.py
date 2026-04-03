import streamlit as st
from utils.theme import apply_pro_theme

st.set_page_config(page_title="Our Services", layout="wide")
apply_pro_theme()

st.markdown('<div class="header-box"><h1>Our <span class="gradient-text">Core Services</span></h1></div>', unsafe_allow_html=True)

services = [
    {"icon": "bi-pencil-square", "title": "Structural Editing", "desc": "Refining sentence flow, academic tone, and overall logical progression."},
    {"icon": "bi-file-earmark-ruled", "title": "Precision Formatting", "desc": "Mastery of APA, MLA, Harvard, and Chicago. Flawless citations every time."},
    {"icon": "bi-lightbulb", "title": "Methodology Design", "desc": "Expert guidance on justifying and articulating your research framework."},
    {"icon": "bi-journal-richtext", "title": "Literature Synthesis", "desc": "Transforming scattered sources into a cohesive and compelling narrative."},
    {"icon": "bi-bar-chart-line", "title": "Data Presentation", "desc": "Clarity in communicating complex findings and statistical results."},
    {"icon": "bi-shield-check", "title": "Plagiarism Review", "desc": "Ensuring 100% original work with detailed academic integrity checks."}
]

cols = st.columns(3)
for i, s in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="pro-card">
            <div class="icon-box"><i class="bi {s['icon']}"></i></div>
            <h3>{s['title']}</h3>
            <p>{s['desc']}</p>
        </div><br>
        """, unsafe_allow_html=True)
