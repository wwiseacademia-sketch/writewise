import streamlit as st
from utils.theme import apply_pro_theme

# Page Configuration
st.set_page_config(page_title="Our Services | WriteWise Academic", page_icon="📜", layout="wide")

# Applying the central professional theme
apply_pro_theme()

# Header Section
st.markdown("""
<div class="header-box">
    <h1>Our <span class="gradient-text">Core Academic Services</span></h1>
    <p style="font-size: 1.1rem; color: var(--text-light); max-width: 800px; margin: 0 auto;">
        We provide high-end academic support tailored to meet the rigorous standards of global universities. 
        Our experts ensure clarity, precision, and excellence in every document.
    </p>
</div>
""", unsafe_allow_html=True)

# Services Data (10 Services Total)
services = [
    {
        "icon": "bi-journal-check", 
        "title": "Assignment Writing", 
        "desc": "Comprehensive support for complex academic assignments, ensuring high-quality content that strictly adheres to specific institutional rubrics and learning outcomes."
    },
    {
        "icon": "bi-mortarboard", 
        "title": "Thesis & Dissertation Writing", 
        "desc": "Expert drafting and structural guidance for Undergraduate, Master’s, and Doctoral theses, focusing on rigorous research, logical flow, and academic integrity."
    },
    {
        "icon": "bi-pen-fill", 
        "title": "Academic Essay Writing", 
        "desc": "Crafting persuasive, well-researched, and articulately composed essays across various disciplines, adhering to strict stylistic and argumentative standards."
    },
    {
        "icon": "bi-clipboard-check", 
        "title": "Research Proposal Writing", 
        "desc": "Developing compelling research proposals that clearly articulate objectives, significance, and methodology to secure institutional approval or project funding."
    },
    {
        "icon": "bi-pencil-square", 
        "title": "Structural Editing", 
        "desc": "Refining sentence architecture, enhancing vocabulary, and establishing an authoritative academic voice that commands respect in scholarly circles."
    },
    {
        "icon": "bi-file-earmark-ruled", 
        "title": "Precision Formatting", 
        "desc": "Mastery of APA, MLA, Harvard, Chicago, and Vancouver styles. We ensure every citation, margin, and reference is mathematically flawless."
    },
    {
        "icon": "bi-lightbulb", 
        "title": "Methodology Consultation", 
        "desc": "Strategic guidance on research design, helping you select, justify, and articulate your qualitative or quantitative framework with academic rigor."
    },
    {
        "icon": "bi-journal-richtext", 
        "title": "Literature Synthesis", 
        "desc": "Transforming fragmented sources into a cohesive and powerful narrative that effectively highlights critical research gaps and justifies your study."
    },
    {
        "icon": "bi-bar-chart-line", 
        "title": "Data Analysis & Presentation", 
        "desc": "Enhancing the visual and descriptive presentation of your findings, making complex statistical data comprehensible, impactful, and clear."
    },
    {
        "icon": "bi-shield-check", 
        "title": "Plagiarism & Integrity Review", 
        "desc": "Comprehensive originality reports and detailed academic integrity checks to guarantee your work is 100% unique and ethically sound."
    }
]

# Displaying Services in a Responsive Grid (2 columns for better readability of descriptions)
cols = st.columns(2)
for i, s in enumerate(services):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="pro-card">
            <div class="icon-box"><i class="bi {s['icon']}"></i></div>
            <h3 style="margin-top: 0; color: var(--primary); font-weight: 700;">{s['title']}</h3>
            <p style="margin-bottom: 0; line-height: 1.6;">{s['desc']}</p>
        </div><br>
        """, unsafe_allow_html=True)

# Call to Action Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h3 style="color: var(--primary);">Ready to excel in your academic journey?</h3>
    <p style="color: var(--text-light); margin-bottom: 30px;">Our consultants are available 24/7 to discuss your project requirements.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,1,1])
with col2:
    if st.button("🚀 Get a Custom Quote", use_container_width=True):
        st.switch_page("pages/6_Get_a_Quote.py")
