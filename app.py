# Premium CSS (Modern Colorful Theme)
st.markdown("""
<style>
/* ---- Theme Variables ---- */
:root{
  --bg: #0b1220;
  --surface: rgba(255,255,255,0.08);
  --surface2: rgba(255,255,255,0.06);
  --border: rgba(255,255,255,0.14);
  --text: rgba(255,255,255,0.92);
  --muted: rgba(255,255,255,0.72);
  --primary: #22d3ee;   /* cyan */
  --primary2:#60a5fa;   /* blue */
  --chip: rgba(34,211,238,0.14);
}

/* ---- Page background ---- */
.stApp {
  background: radial-gradient(1200px 800px at 10% 10%, rgba(96,165,250,0.20), transparent 55%),
              radial-gradient(900px 700px at 85% 30%, rgba(34,211,238,0.18), transparent 55%),
              linear-gradient(180deg, #0b1220 0%, #070b14 100%);
  color: var(--text);
}

/* content width */
.block-container {padding-top: 1.2rem; max-width: 1120px;}

/* headings */
h1, h2, h3, h4 { letter-spacing: -0.02em; color: var(--text); }
p, li, div { color: var(--text); }

/* Streamlit default text tweaks */
[data-testid="stCaptionContainer"] { color: var(--muted) !important; }

/* ---- Cards ---- */
.ww-card{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 16px 16px;
  box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}
.ww-trust{
  background: linear-gradient(135deg, rgba(34,211,238,0.18), rgba(96,165,250,0.12));
  border: 1px solid rgba(34,211,238,0.28);
  border-radius: 18px;
  padding: 14px 14px;
}

/* ---- Domain badges ---- */
.ww-badge{
  display:inline-block;
  padding:7px 12px;
  border-radius:999px;
  background: var(--chip);
  border: 1px solid rgba(34,211,238,0.22);
  margin: 6px 8px 0 0;
  font-size: 0.92rem;
  color: var(--text);
}

/* ---- Buttons ---- */
.stLinkButton a, .stButton>button{
  border-radius: 14px !important;
  font-weight: 700 !important;
  border: 1px solid rgba(255,255,255,0.18) !important;
}

/* Primary buttons (link_button) */
.stLinkButton a{
  background: linear-gradient(135deg, var(--primary), var(--primary2)) !important;
  color: #07101f !important;
}

/* Page link buttons */
a[data-testid="stPageLink-NavLink"]{
  border-radius: 12px !important;
}

/* ---- Sidebar ---- */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.05) !important;
  border-right: 1px solid rgba(255,255,255,0.10) !important;
}
section[data-testid="stSidebar"] *{ color: rgba(255,255,255,0.88) !important; }

/* Footer */
.ww-footer{ opacity:0.80; font-size:0.95rem; }
</style>
""", unsafe_allow_html=True)
