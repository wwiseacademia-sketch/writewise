import streamlit as st
from style import load_css

st.set_page_config(page_title="Our Services", layout="wide")
load_css()

st.markdown("""
<style>
.service-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
.service-card { background: var(--surface); border: 1px solid var(--border-color); border-radius: 12px; padding: 32px; transition: all 0.3s ease; }
.service-card:hover { transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.07); }
.service-icon { font-size: 2.5rem; color: var(--secondary); margin-bottom: 20px; }
h3 { font-size: 1.25rem; font-weight: 700; color: var(--primary); }
p { color: var(--text-light); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="section-header"><h1>Our Core Services</h1></div>', unsafe_allow_html=True)

st.markdown("""
<div class="service-grid">
    <div class="service-card"><div class="service-icon"><i class="bi bi-pencil-square"></i></div><h3>Structural Editing</h3><p>Beyond grammar. We refine sentence architecture, enhance vocabulary, and establish an authoritative academic voice.</p></div>
    <div class="service-card"><div class="service-icon"><i class="bi bi-file-earmark-ruled"></i></div><h3>Precision Formatting</h3><p>Mastery of APA, MLA, Harvard, etc. We ensure every citation and margin is flawlessly aligned.</p></div>
    <div class="service-card"><div class="service-icon"><i class="bi bi-lightbulb"></i></div><h3>Methodology Design</h3><p>Expert consultation to help you select, justify, and articulate your research framework with academic authority.</p></div>
    <div class="service-card"><div class="service-icon"><i class="bi bi-journal-richtext"></i></div><h3>Literature Synthesis</h3><p>Weave disparate sources into a compelling narrative that effectively highlights critical research gaps.</p></div>
    <div class="service-card"><div class="service-icon"><i class="bi bi-bar-chart-line"></i></div><h3>Data Presentation</h3><p>Clarity in communication. We refine the presentation of your findings, making complex data easy to understand.</p></div>
    <div class="service-card"><div class="service-icon"><i class="bi bi-shield-check"></i></div><h3>Integrity & Originality</h3><p>Rigorous checks to guarantee your work is 100% original and upholds the highest standards of academic integrity.</p></div>
</div>
""", unsafe_allow_html=True)
