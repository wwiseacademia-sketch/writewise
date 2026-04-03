import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="WriteWise | Elite Academic Services", page_icon="✨", layout="wide", initial_sidebar_state="collapsed")

# ===================== VIBRANT TECH PRO CSS =====================
st.markdown("""
<style>
/* 1. Import Bootstrap Icons & Premium Font */
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css');
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* 2. Define Vibrant Color Palette */
:root {
    --primary: #042f2e; /* Deep Teal */
    --secondary: #0d9488; /* Vibrant Teal */
    --accent: #a3e635; /* Lime Green - Pops well! */
    --bg-color: #f0fdfa; /* Very light mint background */
    --surface: #FFFFFF;
    --text-main: #064e3b; /* Dark Greenish Text */
    --text-light: #52525B;
    --border-color: #d1d5db;
    --radius: 12px;
}

/* 3. Hide Default Streamlit Elements */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* --- Base App Styling --- */
.stApp {
    background-color: var(--bg-color);
    color: var(--text-main);
}

/* --- TABS with Vibrant Accent --- */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    padding: 10px 20px 0 20px;
    border-bottom: 2px solid var(--border-color);
    justify-content: center;
}
.stTabs [data-baseweb="tab"] {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-light);
    padding: 12px 24px;
    border-radius: var(--radius) var(--radius) 0 0;
    transition: all 0.2s ease;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--secondary);
    background-color: #ccfbf1;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: var(--primary);
    border-bottom: 3px solid var(--secondary);
}

/* --- HERO SECTION with Gradient Text --- */
.hero-wrapper {
    text-align: center;
    padding: 80px 20px;
    margin: 20px 0;
}
.hero-title {
    font-size: 4.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 20px;
    letter-spacing: -1.5px;
    color: var(--primary);
}
.hero-title .gradient-text {
    background: linear-gradient(135deg, var(--secondary), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-light);
    max-width: 800px;
    margin: 0 auto 40px auto;
}

/* --- BUTTONS with Gradient and Hover Effect --- */
.btn-gradient {
    background: linear-gradient(135deg, var(--secondary), #059669);
    color: white !important;
    padding: 14px 32px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1.1rem;
    text-decoration: none;
    transition: all 0.3s ease;
    display: inline-block;
    border: none;
    box-shadow: 0 4px 15px rgba(13, 148, 136, 0.3);
}
.btn-gradient:hover {
    transform: translateY(-3px);
    box-shadow: 0 7px 20px rgba(13, 148, 136, 0.4);
}

/* --- SERVICE CARDS with Professional Icons --- */
.section-header {
    text-align: center;
    margin: 60px 0 40px 0;
}
.section-header h2 {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--primary);
}
.service-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
}
.service-card {
    background: var(--surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius);
    padding: 32px;
    transition: all 0.3s ease;
}
.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.07);
    border-color: var(--secondary);
}
.service-icon {
    font-size: 2.5rem; /* Icon size */
    color: var(--secondary);
    margin-bottom: 20px;
}
.service-card h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 12px;
}
.service-card p {
    color: var(--text-light);
    font-size: 0.95rem;
}

/* --- TEAM SECTION STYLING --- */
.team-container { max-width: 900px; margin: 0 auto; }
.team-member {
    display: flex;
    align-items: center;
    background: var(--surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius);
    padding: 30px;
    margin-bottom: 20px;
}
.team-img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 30px;
}
.team-info h3 { font-size: 1.4rem; font-weight: 700; color: var(--primary); }
.team-role { color: var(--secondary); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }

/* --- FORM STYLING --- */
div[data-testid="stForm"] {
    max-width: 800px;
    margin: 0 auto;
    background: var(--surface) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: var(--radius) !important;
    padding: 40px !important;
}

/* --- WHATSAPP BUTTON --- */
.wa-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #25D366;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    z-index: 1000;
    transition: transform 0.2s ease;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

phone = "923007354339"
base_wa_link = f"https://wa.me/{phone}?text="

# ===================== FLOATING WHATSAPP =====================
st.markdown(f'<a href="{base_wa_link}Hello WriteWise, I need a consultation." class="wa-btn" target="_blank">💬</a>', unsafe_allow_html=True)

# ===================== TABS =====================
tab1, tab2, tab3 = st.tabs(["🏠 Home & Services", "👥 Our Experts", "📝 Request a Quote"])

# ----------------- TAB 1: HOME & SERVICES -----------------
with tab1:
    st.markdown(f"""
    <div class="hero-wrapper">
        <h1 class="hero-title">Your Research, <br><span class="gradient-text">Perfected.</span></h1>
        <p class="hero-subtitle">We provide elite structural editing, flawless formatting, and strategic methodology guidance for academics and researchers across the globe. Confidential, professional, and precise.</p>
        <a href="{base_wa_link}I'd like to discuss my project." class="btn-gradient" target="_blank">Start Your Project Today</a>
    </div>
    
    <div class="section-header">
        <h2>Core Competencies</h2>
    </div>
    
    <div class="service-grid">
        <div class="service-card">
            <div class="service-icon"><i class="bi bi-pencil-square"></i></div>
            <h3>Structural Editing</h3>
            <p>Enhancing clarity, flow, and academic tone. We go beyond grammar to refine the core architecture of your manuscript.</p>
        </div>
        <div class="service-card">
            <div class="service-icon"><i class="bi bi-file-earmark-ruled"></i></div>
            <h3>Precision Formatting</h3>
            <p>Mastery of APA, MLA, Harvard, and Chicago styles. We ensure every citation and margin is flawlessly aligned.</p>
        </div>
        <div class="service-card">
            <div class="service-icon"><i class="bi bi-lightbulb"></i></div>
            <h3>Methodology Design</h3>
            <p>Expert consultation to help you select, justify, and articulate your research framework with academic authority.</p>
        </div>
        <div class="service-card">
            <div class="service-icon"><i class="bi bi-journal-richtext"></i></div>
            <h3>Literature Synthesis</h3>
            <p>We help you weave disparate sources into a compelling narrative that effectively highlights critical research gaps.</p>
        </div>
        <div class="service-card">
            <div class="service-icon"><i class="bi bi-bar-chart-line"></i></div>
            <h3>Data Presentation</h3>
            <p>Clarity in communication. We refine the presentation of your findings, making complex data easy to understand.</p>
        </div>
        <div class="service-card">
            <div class="service-icon"><i class="bi bi-shield-check"></i></div>
            <h3>Integrity & Originality</h3>
            <p>Rigorous checks to guarantee your work is 100% original and upholds the highest standards of academic integrity.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------- TAB 2: OUR EXPERTS -----------------
with tab2:
    st.markdown("""
    <div class="section-header">
        <h2>Meet The Consulting Team</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # HTML blocks for each team member
    st.markdown("""
    <div class="team-container">
        <div class="team-member">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop" class="team-img" alt="Dr. Sarah Khan">
            <div class="team-info">
                <h3>Dr. Sarah Khan</h3>
                <div class="team-role">Director of Research Methodology</div>
                <p>Ph.D. in Social Sciences. Dr. Khan specializes in structuring complex research frameworks and guiding quantitative methodologies.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="team-container">
        <div class="team-member">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop" class="team-img" alt="Prof. Ali Raza">
            <div class="team-info">
                <h3>Prof. Ali Raza</h3>
                <div class="team-role">Head of Editorial Services</div>
                <p>A veteran in academic publishing with 800+ edited manuscripts. Absolute authority on APA 7th Edition and Harvard systems.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="team-container">
        <div class="team-member">
            <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=200&auto=format&fit=crop" class="team-img" alt="Aisha Malik">
            <div class="team-info">
                <h3>Aisha Malik, M.Phil</h3>
                <div class="team-role">Quality Assurance Lead</div>
                <p>The final checkpoint. Aisha ensures every manuscript meets the stringent linguistic and structural standards of top-tier universities.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------- TAB 3: REQUEST A QUOTE -----------------
with tab3:
    st.markdown("""
    <div class="section-header">
        <h2>Request a Custom Proposal</h2>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("quote_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            level = st.selectbox("Academic Level", ["Undergraduate", "Master's", "Ph.D.", "Post-Doc"])
        with col2:
            service = st.selectbox("Primary Service", ["Structural Editing", "Formatting", "Methodology Guidance", "Full Package"])
            words = st.number_input("Word Count", min_value=0, step=500, value=2000)
        
        urgency = st.radio("Timeline", ["Standard (7+ Days)", "Urgent (3-5 Days)", "Express (24-48 Hours)"], horizontal=True)
        notes = st.text_area("Project details or specific challenges")
        
        st.write("")
        submit = st.form_submit_button("Submit Request via WhatsApp", use_container_width=True)
        
        if submit:
            msg = f"Hello WriteWise,\n\n*Name:* {name}\n*Level:* {level}\n*Service:* {service}\n*Words:* {words}\n*Timeline:* {urgency}\n\n*Notes:* {notes}"
            link = base_wa_link + urllib.parse.quote(msg)
            js = f"window.open('{link}', '_blank');"
            components.html(f"<script>{js}</script>", height=0, width=0)
            st.success("✅ Request processed! [Click Here if WhatsApp didn't open automatically](" + link + ")")

# ===================== FOOTER =====================
st.markdown("""
<div style="text-align: center; padding: 40px; margin-top: 60px; border-top: 1px solid var(--border-color); color: var(--text-light);">
    <h4 style="color: var(--primary); font-weight: 700;">WriteWise</h4>
    <p>© 2026 WriteWise Academic Services. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
