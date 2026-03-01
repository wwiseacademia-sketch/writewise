import streamlit as st
import urllib.parse

PHONE = "923007354339"

def apply_theme(page_title: str = "WriteWise Academic Help"):
    st.set_page_config(page_title=page_title, layout="wide")

    wa_link = "https://wa.me/" + PHONE + "?text=" + urllib.parse.quote(
        "Hello WriteWise Academic Help, I need a quote."
    )

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
    .block-container{ max-width:1150px; padding-top:1.4rem; }

    h1,h2,h3,h4,p,li,div { color: var(--text); }
    [data-testid="stCaptionContainer"] { color: var(--muted) !important; }

    /* Cards */
    .card{
      background:var(--surface);
      border-radius:18px;
      padding:18px;
      box-shadow:var(--shadow);
      border:1px solid rgba(0,0,0,0.05);
    }
    .hero{
      background:linear-gradient(135deg, rgba(15,118,110,0.12), rgba(212,175,55,0.10));
      border-radius:20px;
      padding:25px;
      box-shadow:var(--shadow);
    }
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
    .stButton > button{
      border-radius:12px !important;
      font-weight:800 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
      background:rgba(255,255,255,0.92) !important;
      border-right:1px solid rgba(0,0,0,0.08) !important;
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
      font-weight:800;
      box-shadow:0 8px 25px rgba(0,0,0,0.25);
      text-decoration:none;
      z-index:999;
    }

    .footer{
      margin-top:35px;
      opacity:0.85;
      font-size:0.95rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Floating WhatsApp button on every page
    st.markdown(
        f'<a class="whatsapp-float" href="{wa_link}" target="_blank">Chat on WhatsApp</a>',
        unsafe_allow_html=True
    )

def footer():
    st.markdown("""
    <div class="footer">
      <strong>WriteWise Academic Help</strong><br>
      WhatsApp: <strong>+92 300 7354339</strong><br>
      Worldwide / Remote Services • Free revisions within 14 days • Response within 24 hours
    </div>
    """, unsafe_allow_html=True)
