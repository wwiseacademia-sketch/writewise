import streamlit as st
import urllib.parse

st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# ------------------- EMERALD / GOLD (LIGHT, PREMIUM, READABLE) -------------------
st.markdown(
    """
<style>
:root{
  --bg: #fbf7ef;              /* warm off-white */
  --surface: #ffffff;         /* cards */
  --border: rgba(2, 6, 23, 0.10);
  --text: #0b1220;
  --muted: rgba(11,18,32,0.72);

  --emerald: #0f766e;
  --emerald_dark: #064e3b;

  --gold: #d4af37;
  --gold_soft: rgba(212,175,55,0.18);

  --shadow: 0 12px 30px rgba(2, 6, 23, 0.10);
}

/* Background */
.stApp{
  background:
    radial-gradient(900px 600px at 12% 0%, rgba(15,118,110,0.14), transparent 60%),
    radial-gradient(900px 600px at 88% 8%, rgba(212,175,55,0.12), transparent 58%),
    linear-gradient(180deg, var(--bg) 0%, #ffffff 55%, var(--bg) 100%);
  color: var(--text);
}

/* Layout width */
.block-container{
  padding-top: 1.4rem;
  max-width: 1120px;
}

/* Typography */
h1, h2, h3, h4, p, li, div { color: var(--text); }
[data-testid="stCaptionContainer"] { color: var(--muted) !important; }

/* Hero */
.ww-hero{
  background: linear-gradient(135deg, rgba(15,118,110,0.14), rgba(212,175,55,0.10));
  border: 1px solid rgba(15,118,110,0.22);
  border-radius: 22px;
  padding: 18px 18px;
  box-shadow: var(--shadow);
}

/* Cards */
.ww-card{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 16px 16px;
  box-shadow: var(--shadow);
}

/* Trust box */
.ww-trust{
  background: linear-gradient(135deg, rgba(212,175,55,0.20), rgba(15,118,110,0.10));
  border: 1px solid rgba(2,6,23,0.10);
  border-radius: 18px;
  padding: 14px 14px;
}

/* Badges */
.badge{
  display:inline-block;
  padding: 8px 12px;
  margin: 6px 8px 0 0;
  border-radius: 999px;
  font-size: 0.92rem;
  font-weight: 800;
  border: 1px solid rgba(2,6,23,0.10);
  background: rgba(255,255,255,0.90);
}
.b-emerald{ border-color: rgba(15,118,110,0.35); background: rgba(15,118,110,0.10); }
.b-gold{ border-color: rgba(212,175,55,0.55); background: var(--gold_soft); }
.b-ink{ border-color: rgba(2,6,23,0.16); background: rgba(2,6,23,0.06); }

/* Buttons */
.stLinkButton a{
  background: linear-gradient(135deg, var(--emerald), var(--emerald_dark)) !important;
  color: white !important;
  border-radius: 14px !important;
  font-weight: 900 !important;
  padding: 10px 16px !important;
  border: none !important;
  box-shadow: 0 12px 26px rgba(15,118,110,0.22);
}
.stButton > button{
  border-radius: 14px !important;
  font-weight: 900 !important;
  border: 1px solid rgba(2,6,23,0.12) !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.92) !important;
  border-right: 1px solid rgba(2,6,23,0.10) !important;
}
section[data-testid="stSidebar"] *{
  color: var(--text) !important;
}

/* Footer */
.ww-footer{
  opacity: 0.84;
  font-size: 0.95rem;
}
</style>
""",
    unsafe_allow_html=True,
)

# ------------------- CONTENT -------------------

st.title("WriteWise Academic Help")
st.caption("Professional Academic Support & Research Enhancement Services • Worldwide / Remote")

phone = "923007354339"
wa_link = "https://wa.me/" + phone + "?text=" + urllib.parse.quote(
    "Hello WriteWise Academic Help, I need a quote."
)

st.markdown(
    """
<div class="ww-hero">
  <h2 style="margin:0;">Academic Support With Premium Standards</h2>
  <p style="margin:10px 0 0 0; color: rgba(11,18,32,0.80); font-size: 1.02rem;">
    Editing, proofreading, formatting, literature review structuring, and research methodology guidance —
    delivered with confidentiality, clear academic tone, and strong presentation.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")
col1, col2 = st.columns([2, 1])

with col1:
    st.page_link("pages/3_Get_a_Quote.py", label="Get a Custom Quote", icon="📝")
    st.link_button("WhatsApp Now", wa_link)

with col2:
    st.markdown(
        """
<div class="ww-trust">
  <strong>✔ Response:</strong> within 24 hours<br><br>
  <strong>✔ Revisions:</strong> free within 14 days<br><br>
  <strong>✔ Pricing:</strong> custom quote only<br><br>
  <strong>✔ Service:</strong> worldwide / remote
</div>
""",
        unsafe_allow_html=True,
    )

st.write("")
st.markdown('<div class="ww-card">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Specialists", "5")
c2.metric("Revisions", "14 days")
c3.metric("Response", "≤ 24 hours")
c4.metric("Referencing", "APA/MLA/Harvard/…")
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.subheader("Domains We Support")
st.markdown(
    """
<span class="badge b-emerald">Business Studies</span>
<span class="badge b-gold">Social Sciences</span>
<span class="badge b-emerald">Education</span>
<span class="badge b-ink">Law</span>
<span class="badge b-gold">Accounting</span>
<span class="badge b-emerald">Finance</span>
<span class="badge b-gold">Research Methodology</span>
""",
    unsafe_allow_html=True,
)

st.write("")
st.subheader("Turnaround Options")
st.table({"Delivery Type": ["Normal", "Urgent", "Express"], "Timeline": ["7 days", "3 days", "24 hours"]})

st.write("")
st.markdown(
    """
<div class="ww-footer">
<strong>WriteWise Academic Help</strong> • WhatsApp: <strong>+92 300 7354339</strong><br>
We provide academic support, editing, formatting, and research enhancement services.
</div>
""",
    unsafe_allow_html=True,
)
