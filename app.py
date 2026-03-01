import streamlit as st
import urllib.parse

st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# ------------------- UNICEF-LIKE LIGHT MODERN THEME -------------------
st.markdown(
    """
<style>
:root{
  --bg: #f5f9ff;
  --surface: #ffffff;
  --border: rgba(2, 6, 23, 0.10);
  --text: #0b1220;
  --muted: rgba(11,18,32,0.72);

  /* Primary (UNICEF-ish blue vibe) */
  --primary: #1CABE2;
  --primary_dark: #0B7FB8;

  /* Accent colors */
  --accent_yellow: #FFD24A;
  --accent_coral: #FF5A5F;
  --accent_teal: #14B8A6;
  --accent_purple: #8B5CF6;

  --shadow: 0 10px 30px rgba(2, 6, 23, 0.08);
}

.stApp{
  background: radial-gradient(900px 600px at 10% 0%, rgba(28,171,226,0.12), transparent 60%),
              radial-gradient(800px 500px at 90% 10%, rgba(20,184,166,0.10), transparent 55%),
              linear-gradient(180deg, var(--bg) 0%, #ffffff 55%, var(--bg) 100%);
  color: var(--text);
}

.block-container{
  padding-top: 1.4rem;
  max-width: 1120px;
}

h1, h2, h3, h4, p, li, div { color: var(--text); }
[data-testid="stCaptionContainer"] { color: var(--muted) !important; }

/* Cards */
.ww-card{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 16px 16px;
  box-shadow: var(--shadow);
}

.ww-hero{
  background: linear-gradient(135deg, rgba(28,171,226,0.18), rgba(20,184,166,0.12));
  border: 1px solid rgba(28,171,226,0.25);
  border-radius: 22px;
  padding: 18px 18px;
  box-shadow: var(--shadow);
}

.ww-trust{
  background: linear-gradient(135deg, rgba(255,210,74,0.18), rgba(28,171,226,0.10));
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
  font-weight: 700;
  border: 1px solid rgba(2,6,23,0.10);
  background: rgba(255,255,255,0.90);
}
.b1{ border-color: rgba(28,171,226,0.35); background: rgba(28,171,226,0.10); }
.b2{ border-color: rgba(255,210,74,0.55); background: rgba(255,210,74,0.22); }
.b3{ border-color: rgba(255,90,95,0.40); background: rgba(255,90,95,0.12); }
.b4{ border-color: rgba(20,184,166,0.35); background: rgba(20,184,166,0.12); }
.b5{ border-color: rgba(139,92,246,0.35); background: rgba(139,92,246,0.12); }

/* Buttons */
.stLinkButton a{
  background: linear-gradient(135deg, var(--primary), var(--primary_dark)) !important;
  color: white !important;
  border-radius: 14px !important;
  font-weight: 800 !important;
  padding: 10px 16px !important;
  border: none !important;
  box-shadow: 0 10px 24px rgba(28,171,226,0.20);
}
.stButton > button{
  border-radius: 14px !important;
  font-weight: 800 !important;
  border: 1px solid rgba(2,6,23,0.12) !important;
}

/* Sidebar (keep clean and readable) */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.92) !important;
  border-right: 1px solid rgba(2,6,23,0.10) !important;
}
section[data-testid="stSidebar"] *{
  color: var(--text) !important;
}

/* Footer */
.ww-footer{
  opacity: 0.82;
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
  <h2 style="margin:0;">Academic Support You Can Trust</h2>
  <p style="margin:10px 0 0 0; color: rgba(11,18,32,0.80); font-size: 1.02rem;">
    Clean editing, formatting, research methodology guidance, literature review structuring,
    and academic document enhancement — delivered with confidentiality and clear standards.
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
<span class="badge b1">Business Studies</span>
<span class="badge b4">Social Sciences</span>
<span class="badge b5">Education</span>
<span class="badge b3">Law</span>
<span class="badge b2">Accounting</span>
<span class="badge b1">Finance</span>
<span class="badge b4">Research Methodology</span>
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
