import streamlit as st
import urllib.parse

st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# Premium CSS
st.markdown("""
<style>
.block-container {padding-top: 1.2rem; max-width: 1100px;}
.ww-badge {
    display:inline-block;
    padding:6px 10px;
    border-radius:999px;
    background:#f1f5f9;
    border:1px solid #e2e8f0;
    margin:4px;
    font-size:0.9rem;
}
.ww-trust {
    background:#f8fafc;
    padding:14px;
    border-radius:12px;
    border:1px solid #e2e8f0;
}
.ww-footer {
    opacity:0.8;
    font-size:0.9rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("WriteWise Academic Help")
st.caption("Professional Academic Support & Research Enhancement Services")
st.divider()

phone = "923007354339"
wa_link = "https://wa.me/" + phone + "?text=" + urllib.parse.quote(
    "Hello WriteWise Academic Help, I need a quote."
)

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("Academic Support You Can Trust")
    st.write("Worldwide / Remote services for editing, formatting, literature review structuring, research methodology guidance, and document improvement.")
    st.page_link("pages/3_Get_a_Quote.py", label="Get a Custom Quote")
    st.link_button("WhatsApp Now: +92 300 7354339", wa_link)

with col2:
    st.markdown("""
    <div class="ww-trust">
    <strong>✔ Response time:</strong> within 24 hours<br>
    <strong>✔ Free revisions:</strong> 14 days<br>
    <strong>✔ Custom quote only</strong><br>
    <strong>✔ Worldwide / Remote Services</strong>
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
<strong>WriteWise Academic Help</strong> • WhatsApp: +92 300 7354339<br>
Professional academic support, editing, formatting & research enhancement services.<br>
Free revisions within 14 days • Response within 24 hours
</div>
""", unsafe_allow_html=True)
