import streamlit as st
import urllib.parse

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="WriteWise Pro | Next-Gen", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

# ===================== ULTRA-MODERN DARK CSS =====================
st.markdown("""
<style>
/* Import Premium Font: Inter */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

:root {
    --bg-color: #050505;
    --card-bg: rgba(255, 255, 255, 0.03);
    --card-border: rgba(255, 255, 255, 0.08);
    --text-main: #FFFFFF;
    --text-muted: #A1A1AA;
    --accent-1: #3B82F6; /* Electric Blue */
    --accent-2: #8B5CF6; /* Neon Purple */
    --radius: 24px;
}

/* Hide Streamlit default elements */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Base App Styling */
.stApp {
    background-color: var(--bg-color);
    background-image: 
        radial-gradient(circle at 15% 50%, rgba(59, 130, 246, 0.08), transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.08), transparent 25%);
    color: var(--text-main);
}

/* --- HERO SECTION --- */
.hero-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 100px 20px 80px 20px;
    margin-top: -50px;
}
.hero-badge {
    background: rgba(255,255,255,0.05);
    border: 1px solid var(--card-border);
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 1px;
    color: var(--text-muted);
    margin-bottom: 30px;
    backdrop-filter: blur(10px);
}
.hero-badge span {
    color: var(--accent-1);
}
.hero-title {
    font-size: 5.5rem;
    font-weight: 900;
    line-height: 1.1;
    letter-spacing: -2px;
    margin-bottom: 20px;
    color: var(--text-main);
}
/* The Magic Gradient Text */
.gradient-text {
    background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}
.hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-muted);
    max-width: 700px;
    margin-bottom: 40px;
    line-height: 1.6;
}

/* --- BUTTONS --- */
.btn-glow {
    background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
    color: white !important;
    padding: 16px 40px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.1rem;
    text-decoration: none;
    transition: all 0.3s ease;
    border: none;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.4);
    display: inline-block;
}
.btn-glow:hover {
    transform: translateY(-2px) scale(1.05);
    box-shadow: 0 0 30px rgba(139, 92, 246, 0.6);
}

/* --- GLASSMORPHISM CARDS (BENTO BOX STYLE) --- */
.section-heading {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -1px;
    margin: 80px 0 20px 0;
}
.section-heading span {
    color: var(--text-muted);
    font-weight: 300;
}
.bento-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 24px;
    padding: 20px 0;
}
.glass-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: var(--radius);
    padding: 40px 30px;
    backdrop-filter: blur(12px);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
}
.glass-card:hover {
    border-color: rgba(139, 92, 246, 0.4);
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 0 20px rgba(139, 92, 246, 0.05);
}
.glass-icon {
    font-size: 2.5rem;
    margin-bottom: 20px;
    background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.glass-card h3 {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 15px;
}
.glass-card p {
    color: var(--text-muted);
    line-height: 1.6;
    font-size: 1rem;
}

/* --- TEAM SECTION (CYBER LOOK) --- */
.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
}
.team-card {
    text-align: center;
    padding: 40px 20px;
    border-radius: var(--radius);
    background: linear-gradient(180deg, rgba(255,255,255,0.02) 0%, transparent 100%);
    border: 1px solid var(--card-border);
    transition: all 0.4s ease;
}
.team-card:hover {
    border-color: var(--accent-1);
    background: rgba(59, 130, 246, 0.05);
}
.team-avatar {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    margin-bottom: 20px;
    filter: grayscale(100%) opacity(0.8);
    transition: all 0.4s ease;
    border: 2px solid transparent;
}
.team-card:hover .team-avatar {
    filter: grayscale(0%) opacity(1);
    border-color: var(--accent-1);
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.4);
}
.team-card h3 { font-size: 1.4rem; font-weight: 700; margin-bottom: 5px; }
.team-role { color: var(--accent-2); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 15px;}

/* --- PRICING SECTION --- */
.pricing-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: var(--radius);
    padding: 50px 40px;
    text-align: left;
    transition: all 0.3s;
}
.pricing-pro {
    background: linear-gradient(180deg, rgba(139, 92, 246, 0.1) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(139, 92, 246, 0.5);
    transform: scale(1.05);
    box-shadow: 0 0 40px rgba(139, 92, 246, 0.15);
    position: relative;
}
.pricing-pro::before {
    content: "RECOMMENDED";
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
    color: white;
    padding: 4px 16px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 1px;
}
.price-tag { font-size: 3.5rem; font-weight: 900; margin: 20px 0; color: white;}
.price-tag span { font-size: 1.2rem; color: var(--text-muted); font-weight: 400;}
.pricing-features { list-style: none; padding: 0; margin: 30px 0; }
.pricing-features li { margin-bottom: 16px; color: #D4D4D8; display: flex; align-items: center;}
.pricing-features li::before {
    content: "✦";
    color: var(--accent-2);
    margin-right: 12px;
    font-size: 1.2rem;
}

/* Custom Streamlit Container for Calculator */
div[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 24px !important;
    padding: 30px !important;
}

</style>
""", unsafe_allow_html=True)

phone = "923007354339"
base_wa_link = f"https://wa.me/{phone}?text="

# ===================== HERO SECTION =====================
st.markdown(f"""
<div class="hero-wrapper">
    <div class="hero-badge"><span>NEW</span> The Next Generation of Academic Writing</div>
    <h1 class="hero-title">Academic Perfection,<br><span class="gradient-text">Redefined.</span></h1>
    <p class="hero-subtitle">We don't just edit papers; we engineer academic excellence. Experience the most advanced structural formatting and methodology guidance available worldwide.</p>
    <a href="{base_wa_link}Hello, I need premium academic assistance." class="btn-glow" target="_blank">Start Your Project</a>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ===================== SERVICES (BENTO BOX) =====================
st.markdown("""
<h2 class="section-heading">Elite <span>Capabilities</span></h2>
<div class="bento-grid">
    <div class="glass-card">
        <div class="glass-icon">⚡</div>
        <h3>Neural Proofreading</h3>
        <p>Beyond basic grammar. We refine sentence architecture, enhance vocabulary, and establish an authoritative academic voice that commands respect.</p>
    </div>
    <div class="glass-card">
        <div class="glass-icon">📐</div>
        <h3>Architectural Formatting</h3>
        <p>Pixel-perfect adherence to APA 7, MLA, Harvard, or Chicago. Your citations, margins, and bibliography will be mathematically flawless.</p>
    </div>
    <div class="glass-card">
        <div class="glass-icon">🧠</div>
        <h3>Methodology Engineering</h3>
        <p>Struggling with research design? We provide robust justification for your qualitative or quantitative frameworks, ensuring academic rigor.</p>
    </div>
    <div class="glass-card">
        <div class="glass-icon">🔗</div>
        <h3>Literature Synthesis</h3>
        <p>We connect the dots. Transforming disjointed sources into a powerful narrative that highlights critical research gaps seamlessly.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ===================== THE TEAM =====================
st.markdown("""
<h2 class="section-heading">The <span>Minds</span> Behind It</h2>
<div class="team-grid">
    <div class="team-card">
        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=300&auto=format&fit=crop" class="team-avatar" alt="Team">
        <div class="team-role">Lead Architect</div>
        <h3>Dr. Sarah Khan</h3>
        <p style="color:var(--text-muted); font-size:0.9rem;">Ph.D. in Social Sciences. Pioneer in advanced research structuring.</p>
    </div>
    <div class="team-card">
        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=300&auto=format&fit=crop" class="team-avatar" alt="Team">
        <div class="team-role">Chief Editor</div>
        <h3>Prof. Ali Raza</h3>
        <p style="color:var(--text-muted); font-size:0.9rem;">Master of formatting. Has refined over 1,000+ academic dissertations.</p>
    </div>
    <div class="team-card">
        <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=300&auto=format&fit=crop" class="team-avatar" alt="Team">
        <div class="team-role">QA Specialist</div>
        <h3>Aisha Malik</h3>
        <p style="color:var(--text-muted); font-size:0.9rem;">The final checkpoint. Ensures absolute perfection before delivery.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ===================== PRICING =====================
st.markdown("""
<h2 class="section-heading">Transparent <span>Tiers</span></h2>
<div class="bento-grid">
    
    <div class="pricing-card">
        <h3 style="color:var(--text-muted);">Standard Polish</h3>
        <div class="price-tag">₨ 1.5<span>/word</span></div>
        <p style="color:var(--text-muted); margin-bottom:30px;">For pristine, error-free final drafts.</p>
        <ul class="pricing-features">
            <li>Advanced Grammar Correction</li>
            <li>Punctuation & Syntax Check</li>
            <li>Standard Academic Tone</li>
            <li>7-Day Delivery</li>
        </ul>
    </div>

    <div class="pricing-card pricing-pro">
        <h3 style="color:var(--accent-2);">Complete Overhaul</h3>
        <div class="price-tag">₨ 2.5<span>/word</span></div>
        <p style="color:var(--text-muted); margin-bottom:30px;">Full structural and citation enhancement.</p>
        <ul class="pricing-features">
            <li>Everything in Standard</li>
            <li>Full Citation & Bibliography Formatting</li>
            <li>Logical Flow & Structure Editing</li>
            <li>3-Day Priority Delivery</li>
        </ul>
        <a href="https://wa.me/923007354339?text=I%20want%20the%20Complete%20Overhaul%20plan" class="btn-glow" style="width:100%; text-align:center; padding: 12px; margin-top:20px;">Select Pro</a>
    </div>

    <div class="pricing-card">
        <h3 style="color:var(--text-muted);">Express Action</h3>
        <div class="price-tag">₨ 4.0<span>/word</span></div>
        <p style="color:var(--text-muted); margin-bottom:30px;">When deadlines are dangerously close.</p>
        <ul class="pricing-features">
            <li>Highest Priority Queue</li>
            <li>Full Structural Editing</li>
            <li>Direct Expert Communication</li>
            <li style="color:white; font-weight:bold;">24-Hour Turnaround</li>
        </ul>
    </div>

</div>
""", unsafe_allow_html=True)

st.write("---")

# ===================== INTERACTIVE QUOTE ENGINE =====================
st.markdown("<h2 class='section-heading'>Quote <span>Engine</span></h2>", unsafe_allow_html=True)

with st.form("quote_engine"):
    c1, c2 = st.columns(2)
    with c1:
        words = st.number_input("Total Words", min_value=500, value=2000, step=100)
        service = st.selectbox("Select Capability", ["Proofreading", "Formatting", "Structural Review"])
    with c2:
        urgency = st.selectbox("Delivery Speed", ["Standard (7 Days)", "Urgent (3 Days)", "Express (24 Hours)"])
        st.write("")
        st.write("")
        submit = st.form_submit_button("Calculate Project Cost", use_container_width=True)

    if submit:
        base = 1.5 if service == "Proofreading" else 2.0 if service == "Formatting" else 2.5
        mult = 1.0 if "7 Days" in urgency else 1.5 if "3 Days" in urgency else 2.0
        total = words * base * mult
        
        st.markdown(f"""
        <div style="margin-top:20px; text-align:center; padding:30px; border-radius:16px; background:rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.3);">
            <h3 style="color:var(--text-muted); margin:0;">Estimated Investment</h3>
            <h1 style="color:var(--accent-1); font-size:3.5rem; margin:10px 0;">₨ {total:,.0f}</h1>
            <a href="{base_wa_link}Project details: {words} words, {service}, {urgency}. Cost: Rs {total:,.0f}" class="btn-glow" target="_blank">Deploy Request via WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div style="text-align:center; padding: 80px 20px 40px 20px; margin-top: 50px; border-top: 1px solid var(--card-border);">
    <h2 style="font-weight: 900; letter-spacing: -1px;">Write<span style="color:var(--accent-1);">Wise</span></h2>
    <p style="color: var(--text-muted); margin-top: 10px;">The Future of Academic Excellence.</p>
    <p style="font-size: 0.8rem; color: #52525B; margin-top: 30px;">© 2026 WriteWise. Strict Privacy Enforced.</p>
</div>
""", unsafe_allow_html=True)
