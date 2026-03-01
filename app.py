import streamlit as st
import urllib.parse

st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# Top Header
st.title("WriteWise Academic Help")
st.caption("Professional Academic Support & Research Enhancement Services")
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
    st.success("Response time: within 24 hours")
    st.info("Free revisions: 14 days")
    st.warning("Custom quote only (no fixed pricing)")

st.divider()

st.subheader("Domains We Support")
st.write("Business Studies • Social Sciences • Education • Law • Accounting • Finance • Research Methodology")

st.divider()

st.subheader("Turnaround Options")
st.table({
    "Delivery Type": ["Normal", "Urgent", "Express"],
    "Timeline": ["7 days", "3 days", "24 hours"]
})

st.divider()

st.caption("WhatsApp: +92 300 7354339 • Worldwide / Remote Services")
st.caption("We provide academic support, editing, formatting, and research enhancement services.")