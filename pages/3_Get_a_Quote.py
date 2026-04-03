import streamlit as st
from utils.theme import apply_pro_theme
import urllib.parse
import streamlit.components.v1 as components

st.set_page_config(page_title="Get a Quote", layout="wide")
apply_pro_theme()

st.markdown('<div class="header-box"><h1>Get Your <span class="gradient-text">Custom Quote</span></h1><p>Fill in the details to get an instant project proposal via WhatsApp.</p></div>', unsafe_allow_html=True)

with st.form("quote_form"):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Name")
        academic_level = st.selectbox("Academic Level", ["Master's", "Ph.D.", "Post-Doc / Researcher"])
    with c2:
        service_type = st.selectbox("Primary Service", ["Structural Editing", "Formatting", "Full Review", "Methodology"])
        words = st.number_input("Word Count", min_value=500, value=2000, step=500)
    
    notes = st.text_area("Tell us about your research challenges...")
    submit = st.form_submit_button("🚀 Submit Request to WhatsApp")

    if submit:
        phone = "923007354339"
        msg = f"Hello WriteWise,\n\n*Name:* {name}\n*Level:* {academic_level}\n*Service:* {service_type}\n*Words:* {words}\n*Notes:* {notes}"
        link = f"https://wa.me/{phone}?text=" + urllib.parse.quote(msg)
        js = f"window.open('{link}', '_blank');"
        components.html(f"<script>{js}</script>", height=0, width=0)
        st.success("✅ Done! WhatsApp is opening in a new tab...")
