import streamlit as st
import urllib.parse
# --- Premium CSS (Light + Navy accent) ---
st.markdown("""
<style>
/* Page width + typography */
.block-container {padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1100px;}
h1, h2, h3 {letter-spacing: -0.02em;}
/* Buttons */
.stLinkButton a, .stButton>button {
    border-radius: 12px !important;
    padding: 0.55rem 0.9rem !important;
    font-weight: 600 !important;
}
/* Card style */
.ww-card {
    background: #ffffff;
    border: 1px solid rgba(15, 23, 42, 0.08);
    border-radius: 16px;
    padding: 16px 16px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.04);
}
/* Trust bar */
.ww-trust {
    background: rgba(15, 23, 42, 0.03);
    border: 1px solid rgba(15, 23, 42, 0.08);
    border-radius: 14px;
    padding: 12px 14px;
}
/* Small badge */
.ww-badge {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.06);
    border: 1px solid rgba(15, 23, 42, 0.10);
    margin-right: 8px;
    margin-bottom: 8px;
    font-size: 0.9rem;
}
/* Footer */
.ww-footer {opacity: 0.75; font-size: 0.9rem; margin-top: 1.5rem;}
</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# Top Header
st.title("WriteWise Academic Help")
st.divider()
st.markdown("""
<div class="ww-footer">
<strong>WriteWise Academic Help</strong> • Worldwide / Remote Services<br>
WhatsApp: <strong>+92 300 7354339</strong><br><br>
<span style="opacity:0.85;">
We provide academic support, editing, formatting, and research enhancement services.
Free revisions within 14 days (same scope). Response within 24 hours.
</span>
</div>
""", unsafe_allow_html=True)vices")
st.divider()

# WhatsApp Button
phone = "923007354339"
wa_link = "https://wa.me/" + phone + "?text=" + urllib.parse.quote(
    "Hello WriteWise Academic Help, I need a quote."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Academic Support You Can Trust")
    st.write(
        "Worldwide / Remote services for editing, formatting, literature review structuring, "
        "research methodology guidance, and document improvement."
    )
    st.page_link("pages/3_Get_a_Quote.py", label="Get a Custom Quote")
    st.link_button("WhatsApp Now: +92 300 7354339", wa_link)

with col2:
    st.markdown("""
    <div class="ww-trust">
    <strong>✔ Response time:</strong> within 24 hours<br>
    <strong>✔ Free revisions:</strong> 14 days (same scope)<br>
    <strong>✔ Pricing:</strong> Custom quote only<br>
    <strong>✔ Service mode:</strong> Worldwide / Remote
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader("Domains We Support")

st.markdown("""
<span class="ww-badge">Business Studies</span>
<span class="ww-badge">Social Sciences</span>
<span class="ww-badge">Education</span>
<span class="ww-badge">Law</span>
<span class="ww-badge">Accounting</span>
<span class="ww-badge">Finance</span>
<span class="ww-badge">Research Methodology</span>
""", unsafe_allow_html=True)

st.divider()

st.subheader("Turnaround Options")
st.table({
    "Delivery Type": ["Normal", "Urgent", "Express"],
    "Timeline": ["7 days", "3 days", "24 hours"]
})

st.divider()

st.markdown("""
<div class="ww-footer">
WriteWise Academic Help • WhatsApp: +92 300 7354339<br>
Professional academic support, editing, formatting & research enhancement services.
</div>
""", unsafe_allow_html=True)




