import streamlit as st
import urllib.parse

st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# ===================== LIGHT PREMIUM THEME =====================
st.markdown("""
<style>
:root{
  --bg:#f6f9fc;
  --surface:#ffffff;
  --text:#0b1220;
  --muted:#5b6472;
  --emerald:#0f766e;
  --emerald-dark:#065f46;
  --gold:#d4af37;
  --shadow:0 10px 30px rgba(0,0,0,0.08);
}

.stApp{
  background:linear-gradient(180deg,var(--bg) 0%, #ffffff 60%, var(--bg) 100%);
  color:var(--text);
}

.block-container{
  max-width:1150px;
  padding-top:1.5rem;
}

/* Hero */
.hero{
  background:linear-gradient(135deg, rgba(15,118,110,0.12), rgba(212,175,55,0.10));
  border-radius:20px;
  padding:25px;
  box-shadow:var(--shadow);
}

/* Cards */
.card{
  background:var(--surface);
  border-radius:18px;
  padding:18px;
  box-shadow:var(--shadow);
  border:1px solid rgba(0,0,0,0.05);
}

/* Why cards */
.why-card{
  background:#ffffff;
  border-radius:16px;
  padding:14px;
  border-left:5px solid var(--emerald);
  box-shadow:var(--shadow);
  font-weight:600;
}

/* Buttons */
.stLinkButton a{
  background:linear-gradient(135deg,var(--emerald),var(--emerald-dark)) !important;
  color:white !important;
  font-weight:800 !important;
  border-radius:12px !important;
  padding:10px 18px !important;
  border:none !important;
}

/* Floating WhatsApp */
.whatsapp-float{
  position:fixed;
  bottom:20px;
  right:20px;
  background:var(--emerald);
  color:white;
  padding:14px 18px;
  border-radius:50px;
  font-weight:700;
  box-shadow:0 8px 25px rgba(0,0,0,0.25);
  text-decoration:none;
  z-index:999;
}

/* Footer */
.footer{
  margin-top:40px;
  opacity:0.8;
  font-size:0.95rem;
}
</style>
""", unsafe_allow_html=True)

phone = "923007354339"
wa_link = "https://wa.me/" + phone + "?text=" + urllib.parse.quote(
    "Hello WriteWise Academic Help, I need a quote."
)

# ===================== HERO =====================

st.markdown("""
<div class="hero">
<h1>WriteWise Academic Help</h1>
<p style="font-size:1.1rem;">
Professional Academic Support & Research Enhancement Services
Worldwide / Remote Services
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns([2,1])

with col1:
    st.page_link("pages/3_Get_a_Quote.py", label="Get a Custom Quote")
    st.link_button("WhatsApp Now", wa_link)

with col2:
    st.markdown("""
<div class="card">
✔ 24/7 Support<br><br>
✔ Free Revisions (14 Days)<br><br>
✔ Response Within 24 Hours<br><br>
✔ Confidential & Secure
</div>
""", unsafe_allow_html=True)

# ===================== WHY CHOOSE US =====================

st.write("")
st.subheader("Why Choose WriteWise")

why_points = [
    "Qualified Academic Specialists",
    "24/7 Client Support",
    "Free Revisions (14 Days)",
    "On-Time Delivery",
    "All Referencing Styles Supported",
    "Confidential Handling",
    "Research Methodology Expertise",
    "Custom Quote – Transparent Process"
]

cols = st.columns(4)

for i, point in enumerate(why_points):
    with cols[i % 4]:
        st.markdown(f'<div class="why-card">✓ {point}</div>', unsafe_allow_html=True)

# ===================== HOW IT WORKS =====================

st.write("")
st.subheader("How It Works")

st.markdown("""
<div class="card">
1️⃣ Submit your requirements via Get a Quote<br><br>
2️⃣ Receive a custom quote & timeline confirmation<br><br>
3️⃣ Delivery + free revision support
</div>
""", unsafe_allow_html=True)

# ===================== TURNAROUND =====================

st.write("")
st.subheader("Turnaround Options")

st.table({
    "Delivery Type":["Normal","Urgent","Express"],
    "Timeline":["7 Days","3 Days","24 Hours"]
})

# ===================== FOOTER =====================

st.markdown(f"""
<div class="footer">
<strong>WriteWise Academic Help</strong><br>
WhatsApp: +92 300 7354339<br><br>
We provide academic support, editing, formatting, and research enhancement services.
</div>

<a class="whatsapp-float" href="{wa_link}" target="_blank">
Chat on WhatsApp
</a>
""", unsafe_allow_html=True)
