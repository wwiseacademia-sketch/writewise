import streamlit as st
from utils.theme import apply_pro_theme

st.set_page_config(page_title="WriteWise | Academic Perfection", page_icon="✨", layout="wide")
apply_pro_theme()

st.markdown("""
<div class="header-box">
    <h1 style="font-size: 4rem; font-weight: 800;">Academic Success, <br><span class="gradient-text">Redefined.</span></h1>
    <p style="font-size: 1.2rem; color: var(--text-light); max-width: 750px; margin: 20px auto;">Elite structural editing, precision formatting, and strategic research methodology guidance for global scholars. We turn drafts into masterpieces.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🚀 Start Your Project Now", use_container_width=True):
        st.switch_page("pages/6_Get_a_Quote.py") # Direct quote page par le jayein

st.markdown("---")
# Quick Stats
c1, c2, c3, c4 = st.columns(4)
c1.metric("Projects", "500+", "Global")
c2.metric("Approval", "99.8%", "Guaranteed")
c3.metric("Experts", "15+", "PhDs")
c4.metric("Support", "24/7", "WhatsApp")
