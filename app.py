import streamlit as st
import urllib.parse

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="WriteWise | Academic Excellence", page_icon="🏛️", layout="wide", initial_sidebar_state="collapsed")

# ===================== CORPORATE PRO CSS =====================
st.markdown("""
<style>
/* Premium Corporate Font: 'Inter' */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

:root {
    --primary: #0F172A; /* Deep Slate/Navy - Very Corporate */
    --secondary: #2563EB; /* Trust Blue */
    --accent: #F59E0B; /* Subtle Gold/Amber for highlights */
    --bg-color: #F8FAFC; /* Crisp Off-White */
    --surface: #FFFFFF;
    --text-main: #1E293B;
    --text-light: #64748B;
    --border-color: #E2E8F0;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
    --radius: 12px; /* Sharper, more corporate corners */
}

/* Hide Default Streamlit Elements */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Base App Styling */
.stApp {
    background-color: var(--bg-color);
    color: var(--text-main);
}

/* --- INTERACTIVE TABS (Clean Corporate Style) --- */
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
    background-color: transparent;
    border: none;
    transition: all 0.2s ease;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--secondary);
    background-color: #EFF6FF;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: var(--primary);
    background-color: var(--surface);
    border-top: 3px solid var(--secondary);
    border-left: 1px solid var(--border-color);
    border-right: 1px solid var(--border-color);
    border-bottom: none;
    box-shadow: var(--shadow-sm);
}

/* --- HERO SECTION --- */
.hero-wrapper {
    background: linear-gradient(135deg, var(--primary) 0%, #1E293B 100%);
    color: white;
    padding: 80px 20px;
    border-radius: var(--radius);
    text-align: center;
    margin: 20px 0 40px 0;
    box-shadow: var(--shadow-lg);
    position: relative;
    overflow: hidden;
}
/* Subtle background pattern in Hero */
.hero-wrapper::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: radial-gradient(rgba(255,255,255,0.1) 1px, transparent 1px);
    background-size: 20px 20px;
    opacity: 0.5;
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    background: rgba(37, 99, 235, 0.2);
    color: #60A5FA;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 20px;
    border: 1px solid rgba(37, 99, 235, 0.3);
}
.hero-title {
    font-size: 4rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 20px;
    letter-spacing: -1px;
}
.hero-title span { color: var(--secondary); }
.hero-subtitle {
    font-size: 1.2rem;
    color: #CBD5E1;
    max-width: 800px;
    margin: 0 auto 40px auto;
    line-height: 1.6;
}

/* --- BUTTONS --- */
.btn-primary {
    background-color: var(--secondary);
    color: white !important;
    padding: 14px 32px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1.1rem;
    text-decoration: none;
    transition: all 0.2s ease;
    display: inline-block;
    box-shadow: 0 4px 6px rgba(37, 99, 235, 0.25);
    border: 1px solid transparent;
}
.btn-primary:hover {
    background-color: #1D4ED8;
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
}
.btn-outline {
    background-color: transparent;
    color: white !important;
    padding: 14px 32px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1.1rem;
    text-decoration: none;
    transition: all 0.2s ease;
    display: inline-block;
    border: 2px solid rgba(255,255,255,0.3);
    margin-left: 15px;
}
.btn-outline:hover {
    background-color: rgba(255,255,255,0.1);
    border-color: white;
}

/* --- SERVICES CARDS (Clean Grid) --- */
.section-header {
    text-align: center;
    margin: 60px 0 40px 0;
}
.section-header h2 {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--primary);
    letter-spacing: -0.5px;
    margin-bottom: 10px;
}
.section-header p {
    font-size: 1.1rem;
    color: var(--text-light);
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
    box-shadow: var(--shadow-sm);
}
.service-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    border-color: #BFDBFE;
}
.service-icon {
    font-size: 2rem;
    color: var(--secondary);
    background: #EFF6FF;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
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
    line-height: 1.6;
    font-size: 0.95rem;
    margin-bottom: 0;
}

/* --- TEAM TAB STYLING --- */
.team-container {
    max-width: 1000px;
    margin: 0 auto;
}
.team-member {
    display: flex;
    align-items: center;
    background: var(--surface);
    border: 1px solid var(--border-color);
    border-radius: var(--radius);
    padding: 30px;
    margin-bottom: 20px;
    box-shadow: var(--shadow-sm);
    transition: all 0.2s ease;
}
.team-member:hover {
    box-shadow: var(--shadow-md);
    border-left: 4px solid var(--secondary);
}
.team-img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 30px;
    border: 3px solid #EFF6FF;
}
.team-info h3 { font-size: 1.4rem; font-weight: 700; color: var(--primary); margin: 0 0 5px 0;}
.team-role { color: var(--secondary); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;}
.team-desc { color: var(--text-light); line-height: 1.6; margin:0;}

/* --- FLOATING WHATSAPP --- */
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
    box-shadow: 0 4px 10px rgba(37, 211, 102, 0.4);
    z-index: 1000;
    transition: transform 0.2s ease;
    text-decoration: none;
}
.wa-btn:hover { transform: scale(1.1); }

/* --- FOOTER --- */
.footer-clean {
    text-align: center;
    padding: 40px 20px;
    margin-top: 60px;
    border-top: 1px solid var(--border-color);
    color: var(--text-light);
}
.footer-clean h4 { color: var(--primary); font-weight: 700; margin-bottom: 10px;}
</style>
""", unsafe_allow_html=True)

phone = "923007354339"
base_wa_link = f"https://wa.me/{phone}?text="
default_msg = urllib.parse.quote("Hello WriteWise, I need a consultation for my academic project.")

# ===================== FLOATING WHATSAPP =====================
st.markdown(f'<a href="{base_wa_link}{default_msg}" class="wa-btn" target="_blank">💬</a>', unsafe_allow_html=True)

# ===================== MAIN APPLICATION TABS =====================
tab1, tab2, tab3 = st.tabs(["🏛️ Home & Services", "👥 Our Experts", "📝 Get a Quote"])

# ----------------- TAB 1: HOME & SERVICES -----------------
with tab1:
    st.markdown(f"""
    <div class="hero-wrapper">
        <div class="hero-badge">Global Academic Consulting</div>
        <h1 class="hero-title">Elevating Academic <span>Standards.</span></h1>
        <p class="hero-subtitle">We provide rigorous structural editing, precise formatting, and expert methodology consultation for researchers and post-graduates worldwide. Strict confidentiality guaranteed.</p>
        <a href="{base_wa_link}I would like to discuss my academic requirements." class="btn-primary" target="_blank">Consult an Expert</a>
        <a href="mailto:info@writewise.com" class="btn-outline">Email Us</a>
    </div>
    
    <div class="section-header">
        <h2>Core Competencies</h2>
        <p>Specialized academic services tailored to meet elite university guidelines.</p>
    </div>
    
    <div class="service-grid">
        <div class="service-card">
            <div class="service-icon">✒️</div>
            <h3>Structural Editing</h3>
            <p>Beyond basic proofreading. We refine sentence flow, correct academic tone, and ensure logical progression throughout your manuscript.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">📑</div>
            <h3>Precision Formatting</h3>
            <p>Flawless implementation of APA, MLA, Harvard, or Chicago styles. We handle complex citations and bibliography structures.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🔬</div>
            <h3>Methodology Consultation</h3>
            <p>Expert guidance on research design. We help justify your qualitative or quantitative approach with academic rigor.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">📚</div>
            <h3>Literature Synthesis</h3>
            <p>We help organize scattered literature into a cohesive narrative, identifying clear research gaps to strengthen your thesis.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">📊</div>
            <h3>Data Presentation</h3>
            <p>Transforming complex datasets into clear, comprehensible narratives. Ensuring your findings are communicated effectively.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🛡️</div>
            <h3>Integrity & Plagiarism</h3>
            <p>Comprehensive reviews to ensure your work is entirely original and adheres to the strictest academic integrity policies.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------- TAB 2: OUR EXPERTS (TEAM) -----------------
with tab2:
    st.markdown("""
    <div class="section-header" style="margin-top: 20px;">
        <h2>The Consulting Team</h2>
        <p>Your work is reviewed by subject-matter experts and seasoned academics.</p>
    </div>
    
    <div class="team-container">
        <div class="team-member">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=200&auto=format&fit=crop" class="team-img" alt="Dr. Sarah Khan">
            <div class="team-info">
                <h3>Dr. Sarah Khan</h3>
                <div class="team-role">Director of Research Methodology</div>
                <p class="team-desc">Ph.D. in Social Sciences. With over 12 years of experience in academia, Dr. Khan specializes in structuring complex research frameworks and guiding quantitative methodologies for doctoral candidates.</p>
            </div>
        </div>
        
        <div class="team-member">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=200&auto=format&fit=crop" class="team-img" alt="Prof. Ali Raza">
            <div class="team-info">
                <h3>Prof. Ali Raza</h3>
                <div class="team-role">Head of Editorial Services</div>
                <p class="team-desc">A veteran in academic publishing, Prof. Raza has meticulously formatted and edited over 800+ manuscripts. He is an absolute authority on APA 7th Edition and Harvard referencing systems.</p>
            </div>
        </div>
        
        <div class="team-member">
            <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=200&auto=format&fit=crop" class="team-img" alt="Aisha Malik">
            <div class="team-info">
                <h3>Aisha Malik, M.Phil</h3>
                <div class="team-role">Quality Assurance Lead</div>
                <p class="team-desc">Holding an M.Phil in Literature, Aisha is the final checkpoint for all documents. She ensures that every manuscript not only meets but exceeds the linguistic and structural standards of elite universities.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------- TAB 3: GET A QUOTE (Direct WhatsApp) -----------------
with tab3:
    st.markdown("""
    <div class="section-header" style="margin-top: 20px;">
        <h2>Request a Custom Proposal</h2>
        <p>Tell us about your project, and we will connect with you directly via WhatsApp to discuss scope, timeline, and pricing.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom Form Layout mimicking a professional contact form
    st.markdown("""
    <style>
    /* Styling the Streamlit Form to look like a Corporate Contact Form */
    div[data-testid="stForm"] {
        max-width: 800px;
        margin: 0 auto;
        background: var(--surface) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: var(--radius) !important;
        padding: 40px !important;
        box-shadow: var(--shadow-md) !important;
    }
    div[data-testid="stFormSubmitButton"] > button {
        background-color: var(--primary) !important;
        color: white !important;
        width: 100%;
        padding: 12px;
        font-size: 1.1rem;
        border-radius: 8px;
        border: none;
        transition: background-color 0.2s;
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #334155 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.form("direct_quote_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your Name / Alias")
            academic_level = st.selectbox("Academic Level", ["Undergraduate", "Master's", "Ph.D.", "Post-Doc / Researcher"])
        with c2:
            service_needed = st.selectbox("Primary Service Needed", ["Structural Editing", "Formatting & Citations", "Methodology Guidance", "Complete Package"])
            word_count = st.number_input("Approximate Word Count", min_value=0, step=500, value=2000)
        
        urgency = st.radio("Required Timeline", ["Standard (7+ Days)", "Urgent (3-5 Days)", "Express (24-48 Hours)"], horizontal=True)
        additional_notes = st.text_area("Briefly describe your requirements or challenges")
        
        st.write("")
        submit_quote = st.form_submit_button("🚀 Submit to WhatsApp")
        
        if submit_quote:
            # Construct WhatsApp Message
            msg = f"Hello WriteWise, I need a quote.\n\n"
            if name: msg += f"*Name:* {name}\n"
            msg += f"*Level:* {academic_level}\n"
            msg += f"*Service:* {service_needed}\n"
            msg += f"*Words:* {word_count}\n"
            msg += f"*Timeline:* {urgency}\n"
            if additional_notes: msg += f"\n*Notes:* {additional_notes}"
            
            final_link = base_wa_link + urllib.parse.quote(msg)
            
            # Using st.components.v1 to automatically open the link in a new tab upon click
            import streamlit.components.v1 as components
            js = f"window.open('{final_link}', '_blank');"
            components.html(f"<script>{js}</script>", height=0, width=0)
            
            st.success("✅ Request generated! If WhatsApp didn't open automatically, [Click Here to send your message.](" + final_link + ")")

# ===================== FOOTER =====================
st.markdown("""
<div class="footer-clean">
    <h4>WriteWise Consulting</h4>
    <p>Ethical Academic Support • 100% Confidential • Professional Excellence</p>
    <p style="font-size: 0.85rem; margin-top: 20px;">© 2026 WriteWise Academic Consulting. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
