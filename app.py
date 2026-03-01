import streamlit as st
import urllib.parse

st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# ------------------- MODERN COLORFUL THEME -------------------
st.markdown("""
<style>

/* ===== Background ===== */
.stApp {
    background: radial-gradient(circle at 20% 20%, #1e3a8a 0%, transparent 40%),
                radial-gradient(circle at 80% 30%, #06b6d4 0%, transparent 40%),
                linear-gradient(135deg, #0f172a 0%, #020617 100%);
    color: white;
}

/* Content Width */
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

/* Headings */
h1, h2, h3 {
    color: white !important;
    letter-spacing: -0.02em;
}

/* Trust Card */
.trust-card {
    background: rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
}

/* Domain badges */
.badge {
    display: inline-block;
    padding: 8px 14px;
    margin: 6px 8px 0 0;
    border-radius: 999px;
    background: linear-gradient(135deg, #06b6d4, #3b82f6);
    color: white;
    font-size: 0.9rem;
    font-weight: 600;
}

/* Buttons */
.stLinkButton a {
    background: linear-gradient(135deg, #06b6d4, #3b82f6) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    padding: 10px 16px !important;
    border: none !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.05) !important;
    border-right: 1px solid rgba(255,255,255,0.15);
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Footer */
.footer {
    margin-top: 2rem;
    opacity: 0.85;
    font-size: 0.95rem;
}

</style>
""", unsafe_allow_html=True)

# ------------------- HEADER -------------------

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
    st.write(
        "Worldwide remote academic support for editing, formatting, literature review structuring, "
        "research methodology guidance, and document enhancement."
    )
    st.page_link("pages/3_Get_a_Quote.py", label="Get a Custom Quote")
    st.link_button("WhatsApp Now", wa_link)

with col2:
    st.markdown("""
    <div class="trust-card">
    ✔ Response within 24 hours<br><br>
    ✔ Free revisions (14 days)<br><br>
    ✔ Custom quote pricing<br><br>
    ✔ Worldwide / Remote Services
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ------------------- DOMAINS -------------------

st.subheader("Domains We Support")

st.markdown("""
<span class="badge">Business Studies</span>
<span class="badge">Social Sciences</span>
<span class="badge">Education</span>
<span class="badge">Law</span>
<span class="badge">Accounting</span>
<span class="badge">Finance</span>
<span class="badge">Research Methodology</span>
""", unsafe_allow_html=True)

st.divider()

# ------------------- TURNAROUND -------------------

st.subheader("Turnaround Options")

st.table({
    "Delivery Type": ["Normal", "Urgent", "Express"],
    "Timeline": ["7 days", "3 days", "24 hours"]
})

st.divider()

# ------------------- FOOTER -------------------

st.markdown("""
<div class="footer">
<strong>WriteWise Academic Help</strong><br>
WhatsApp: +92 300 7354339<br><br>
We provide academic support, editing, formatting, and research enhancement services.
Free revisions within 14 days. Response within 24 hours.
</div>
""", unsafe_allow_html=True)
