import streamlit as st

def apply_pro_theme():
    st.markdown("""
    <style>
    /* Professional Fonts & Icons */
    @import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

    :root {
        --primary: #042f2e; --secondary: #0d9488; --accent: #a3e635;
        --bg-color: #f0fdfa; --surface: #FFFFFF; --text-main: #064e3b;
        --text-light: #52525B; --border-color: #d1d5db; --radius: 16px;
    }

    .stApp { background-color: var(--bg-color); color: var(--text-main); }

    /* Custom Navbar/Header Style */
    .header-box { text-align: center; padding: 40px 20px; margin-bottom: 30px; }
    .gradient-text {
        background: linear-gradient(135deg, var(--secondary), var(--accent));
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Professional Cards */
    .pro-card {
        background: var(--surface); border: 1px solid var(--border-color);
        border-radius: var(--radius); padding: 30px; transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    .pro-card:hover { transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border-color: var(--secondary); }

    /* Gradient Buttons */
    .stButton>button {
        background: linear-gradient(135deg, var(--secondary), #059669) !important;
        color: white !important; font-weight: 700 !important; border-radius: 10px !important;
        border: none !important; padding: 10px 25px !important; transition: 0.3s !important;
    }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 10px 20px rgba(13, 148, 136, 0.3); }

    /* Icons Styling */
    .icon-box { font-size: 2.5rem; color: var(--secondary); margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)
