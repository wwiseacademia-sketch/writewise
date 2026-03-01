import streamlit as st
import urllib.parse

st.set_page_config(page_title="WriteWise Academic Help", layout="wide")

# ===================== MODERN PREMIUM (EMERALD / GOLD • LIGHT) =====================
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
  --border:1px solid rgba(0,0,0,0.06);
}

.stApp{
  background:
    radial-gradient(900px 600px at 12% 0%, rgba(15,118,110,0.12), transparent 60%),
    radial-gradient(900px 600px at 88% 10%, rgba(212,175,55,0.12), transparent 58%),
    linear-gradient(180deg, var(--bg) 0%, #ffffff 60%, var(--bg) 100%);
  color:var(--text);
}

.block-container{ max-width:1150px; padding-top:1.3rem; }
[data-testid="stCaptionContainer"]{ color:var(--muted) !important; }

/* Hero */
.hero{
  background: linear-gradient(135deg, rgba(15,118,110,0.12), rgba(212,175,55,0.10));
  border-radius: 22px;
  padding: 26px;
  box-shadow: var(--shadow);
  border: var(--border);
}
.hero h1{ margin:0; }
.hero p{ margin:10px 0 0 0; color: rgba(11,18,32,0.78); font-size:1.05rem; }

/* Cards */
.card{
  background: var(--surface);
  border-radius: 18px;
  padding: 18px;
  box-shadow: var(--shadow);
  border: var(--border);
}
.card h3, .card h4{ margin:0; }
.card p{ margin:10px 0 0 0; color: rgba(11,18,32,0.78); }

/* Feature card accent */
.accent-left{
  border-left: 5px solid var(--emerald);
  padding-left: 14px;
}

/* Badges */
.badge{
  display:inline-block;
  padding: 8px 12px;
  margin: 6px 8px 0 0;
  border-radius: 999px;
  font-size: 0.92rem;
  font-weight: 800;
  border: 1px solid rgba(0,0,0,0.08);
  background: rgba(255,255,255,0.92);
}
.b-em{ background: rgba(15,118,110,0.10); border-color: rgba(15,118,110,0.25); }
.b-gd{ background: rgba(212,175,55,0.18); border-color: rgba(212,175,55,0.35); }
.b-in{ background: rgba(2,6,23,0.05); border-color: rgba(2,6,23,0.10); }

/* Buttons */
.stLinkButton a{
  background: linear-gradient(135deg, var(--emerald), var(--emerald-dark)) !important;
  color:white !important;
  font-weight: 900 !important;
  border-radius: 14px !important;
  padding: 10px 18px !important;
  border: none !important;
  box-shadow: 0 10px 22px rgba(15,118,110,0.18);
}
.stButton>button{
  border-radius: 14px !important;
  font-weight: 900 !important;
}

/* Turnaround chips */
.chip{
  display:inline-block;
  padding: 10px 14px;
  border-radius: 14px;
  border: 1px solid rgba(0,0,0,0.08);
  background: rgba(255,255,255,0.90);
  margin-right: 10px;
  box-shadow: 0 8px 18px rgba(0,0,0,0.06);
}
.chip strong{ color: var(--emerald-dark); }

/* Sidebar clean */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.92) !important;
  border-right: 1px solid rgba(0,0,0,0.08) !important;
}

/* Footer */
.footer{ margin-top: 34px; opacity:0.86; font-size:0.95rem; }

/* Floating WhatsApp */
.whatsapp-float{
  position:fixed;
  bottom:20px;
  right:20px;
  background: var(--emerald);
  color:white;
  padding:14px 18px;
  border-radius:50px;
  font-weight:900;
  box-shadow:0 8px 25px rgba(0,0,0,0.25);
  text-decoration:none;
  z-index:999;
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
  <p><strong>Professional Academic Support & Research Enhancement Services</strong> • Worldwide / Remote</p>
  <p>Editing, proofreading, formatting, literature review structuring, and research methodology guidance — delivered with confidentiality and clear academic standards.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
c1, c2, c3 = st.columns([1, 1, 1])
with c1:
    st.page_link("pages/3_Get_a_Quote.py", label="Get a Custom Quote", icon="📝")
with c2:
    st.link_button("WhatsApp Now", wa_link)
with c3:
    st.page_link("pages/1_Services.py", label="View Services", icon="📌")

# Floating WhatsApp
st.markdown(f'<a class="whatsapp-float" href="{wa_link}" target="_blank">Chat on WhatsApp</a>', unsafe_allow_html=True)

st.write("")

# ===================== DOMAINS WE SUPPORT (TOP POSITION) =====================
st.subheader("Domains We Support")

st.markdown("""
<span class="badge b-em">Business Studies</span>
<span class="badge b-gd">Social Sciences</span>
<span class="badge b-em">Education</span>
<span class="badge b-in">Law</span>
<span class="badge b-gd">Accounting</span>
<span class="badge b-em">Finance</span>
<span class="badge b-gd">Research Methodology</span>
""", unsafe_allow_html=True)

st.write("")

# ===================== QUICK VALUE CARDS =====================
st.subheader("What You Get")
a, b, c = st.columns(3)

with a:
    st.markdown("""
    <div class="card accent-left">
      <h4>Clarity & Academic Tone</h4>
      <p>We polish language, flow, and academic readability so your work looks professional.</p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="card accent-left">
      <h4>Formatting & Referencing</h4>
      <p>APA, MLA, Harvard, Chicago, Vancouver — clean structure and consistent citations.</p>
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="card accent-left">
      <h4>Research Support</h4>
      <p>Methodology guidance, literature review structuring, and strong research presentation.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ===================== WHY CHOOSE US (8 points) =====================
st.subheader("Why Choose WriteWise")
why_points = [
    ("Qualified Specialists", "Degree-qualified team members with domain expertise."),
    ("24/7 Client Support", "Quick communication and smooth coordination."),
    ("Free Revisions (14 Days)", "Revisions included within 14 days (same scope)."),
    ("On-Time Delivery", "We confirm timeline before starting."),
    ("All Referencing Styles", "Major styles supported + custom formatting."),
    ("Confidential Handling", "Your data and files remain private."),
    ("Research Methodology Expertise", "Strong structure, logic, and presentation."),
    ("Custom Quote Process", "No hidden pricing — scope-based quotation."),
]
cols = st.columns(4)
for i, (title, desc) in enumerate(why_points):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="card">
          <h4>{title}</h4>
          <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# ===================== PROCESS =====================
st.subheader("How It Works")
p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="card">
      <h4>1) Share Requirements</h4>
      <p>Upload files, instructions, referencing style, and deadline.</p>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="card">
      <h4>2) Get a Custom Quote</h4>
      <p>We confirm scope + timeline and share a clear quote.</p>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="card">
      <h4>3) Delivery + Revisions</h4>
      <p>Delivery as per timeline + free revisions within 14 days.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ===================== TURNAROUND (CHIPS) =====================
st.subheader("Turnaround Options")
st.markdown("""
<span class="chip"><strong>Normal:</strong> 7 days</span>
<span class="chip"><strong>Urgent:</strong> 3 days</span>
<span class="chip"><strong>Express:</strong> 24 hours</span>
""", unsafe_allow_html=True)

st.write("")
st.page_link("pages/3_Get_a_Quote.py", label="Start: Get a Quote", icon="✅")

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
  <strong>WriteWise Academic Help</strong> • WhatsApp: <strong>+92 300 7354339</strong><br>
  Worldwide / Remote Services • Free revisions within 14 days • Response within 24 hours
</div>
""", unsafe_allow_html=True)


