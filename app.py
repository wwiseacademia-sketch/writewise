import streamlit as st
import urllib.parse

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="WriteWise Premium", page_icon="🎓", layout="wide", initial_sidebar_state="collapsed")

# ===================== SUPER PRO CSS (MODERN UI) =====================
st.markdown("""
<style>
/* Import Premium Font: Plus Jakarta Sans */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

:root {
    --primary: #064E3B; /* Deep Emerald */
    --accent: #D4AF37; /* Premium Gold */
    --bg-color: #F8FAFC; /* Off white background */
    --card-bg: #FFFFFF;
    --text-main: #0F172A;
    --text-muted: #64748B;
    --shadow-soft: 0 10px 40px -10px rgba(0,0,0,0.08);
    --shadow-hover: 0 20px 40px -10px rgba(6, 78, 59, 0.15);
    --radius: 24px;
}

/* Hide Streamlit default header/footer for a clean website look */
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.stApp {
    background-color: var(--bg-color);
    background-image: radial-gradient(at 0% 0%, rgba(212, 175, 55, 0.05) 0px, transparent 50%),
                      radial-gradient(at 100% 0%, rgba(6, 78, 59, 0.05) 0px, transparent 50%);
    background-attachment: fixed;
}

/* --- HERO SECTION --- */
.hero-container {
    text-align: center;
    padding: 80px 20px 60px 20px;
    max-width: 900px;
    margin: 0 auto;
}
.hero-tag {
    display: inline-block;
    padding: 8px 16px;
    background: rgba(212, 175, 55, 0.1);
    color: #B45309;
    border-radius: 50px;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 20px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.hero-title {
    font-size: 4.5rem;
    font-weight: 800;
    color: var(--primary);
    line-height: 1.1;
    margin-bottom: 24px;
    letter-spacing: -1.5px;
}
.hero-title span {
    background: linear-gradient(135deg, var(--primary), #10B981);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 40px;
}

/* --- MODERN GRID LAYOUTS --- */
.section-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--text-main);
    margin: 60px 0 20px 0;
    letter-spacing: -0.5px;
}
.section-subtitle {
    text-align: center;
    color: var(--text-muted);
    margin-bottom: 50px;
    font-size: 1.1rem;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    padding: 20px 0;
}

/* --- PREMIUM CARDS --- */
.pro-card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 40px 30px;
    box-shadow: var(--shadow-soft);
    border: 1px solid rgba(0,0,0,0.03);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}
.pro-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-hover);
    border-color: rgba(6, 78, 59, 0.1);
}
.card-icon {
    font-size: 2.5rem;
    margin-bottom: 20px;
    display: inline-block;
    padding: 15px;
    background: rgba(6, 78, 59, 0.04);
    border-radius: 16px;
}
.pro-card h3 {
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--text-main);
    margin-bottom: 12px;
}
.pro-card p {
    color: var(--text-muted);
    line-height: 1.6;
    font-size: 1rem;
}

/* --- TEAM SECTION (NEW) --- */
.team-img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 20px;
    border: 4px solid var(--bg-color);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.team-card {
    text-align: center;
    padding: 40px 20px;
}
.team-role {
    color: var(--accent);
    font-weight: 600;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

/* --- PRICING SECTION (NEW) --- */
.pricing-card {
    text-align: center;
    padding: 50px 30px;
    border-radius: 30px;
    background: white;
    box-shadow: var(--shadow-soft);
    position: relative;
    border: 1px solid rgba(0,0,0,0.05);
}
.pricing-card.popular {
    background: var(--primary);
    color: white;
    transform: scale(1.05);
    box-shadow: 0 25px 50px -12px rgba(6, 78, 59, 0.25);
}
.pricing-card.popular p, .pricing-card.popular h3 {
    color: white !important;
}
.price {
    font-size: 3rem;
    font-weight: 800;
    margin: 20px 0;
}
.price span { font-size: 1rem; color: var(--text-muted); font-weight: 400; }
.pricing-card.popular .price span { color: rgba(255,255,255,0.7); }
.pricing-list {
    list-style: none;
    padding: 0;
    margin: 30px 0;
    text-align: left;
}
.pricing-list li {
    margin-bottom: 15px;
    padding-left: 30px;
    position: relative;
    color: var(--text-muted);
}
.pricing-card.popular .pricing-list li { color: rgba(255,255,255,0.9); }
.pricing-list li::before {
    content: "✓";
    position: absolute;
    left: 0;
    color: var(--accent);
    font-weight: bold;
}

/* --- CUSTOM BUTTONS --- */
.btn-primary {
    display: inline-block;
    background: var(--primary);
    color: white !important;
    padding: 16px 36px;
    border-radius: 50px;
    font-weight: 800;
    text-decoration: none;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    box-shadow: 0 10px 20px rgba(6, 78, 59, 0.2);
    border: none;
}
.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 25px rgba(6, 78, 59, 0.3);
    background: #04382A;
}
.btn-outline {
    display: inline-block;
    background: transparent;
    color: var(--primary) !important;
    padding: 14px 34px;
    border-radius: 50px;
    font-weight: 800;
    text-decoration: none;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    border: 2px solid var(--primary);
    margin-left: 15px;
}
.btn-outline:hover {
    background: rgba(6, 78, 59, 0.05);
}

/* Floating WhatsApp */
.wa-float {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #25D366;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    text-align: center;
    font-size: 30px;
    line-height: 60px;
    box-shadow: 0 10px 25px rgba(37, 211, 102, 0.4);
    z-index: 1000;
    transition: all 0.3s ease;
}
.wa-float:hover {
    transform: scale(1.1) rotate(-10deg);
}

/* Stats Ribbon */
.stats-ribbon {
    display: flex;
    justify-content: space-around;
    background: white;
    padding: 40px 20px;
    border-radius: 24px;
    box-shadow: var(--shadow-soft);
    margin: -40px auto 60px auto;
    max-width: 1000px;
    position: relative;
    z-index: 10;
}
.stat-item text-align: center;
.stat-num { font-size: 2.5rem; font-weight: 800; color: var(--primary); }
.stat-label { color: var(--text-muted); font-size: 0.9rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;}
</style>
""", unsafe_allow_html=True)

phone = "923007354339"
base_wa_link = f"https://wa.me/{phone}?text="
default_msg = urllib.parse.quote("Hello WriteWise Premium, I am looking for academic assistance.")

# ===================== FLOATING WHATSAPP =====================
st.markdown(f'<a href="{base_wa_link}{default_msg}" class="wa-float" target="_blank">💬</a>', unsafe_allow_html=True)

# ===================== HERO SECTION =====================
st.markdown(f"""
<div class="hero-container">
    <div class="hero-tag">🌟 Global Academic Excellence</div>
    <h1 class="hero-title">Elevate Your Research with <span>WriteWise</span></h1>
    <p class="hero-subtitle">Premium editing, flawless formatting, and expert methodology guidance for PhDs, Master's students, and Researchers worldwide. Your success is our signature.</p>
    <a href="{base_wa_link}{default_msg}" class="btn-primary" target="_blank">Get a Custom Quote</a>
    <a href="#services" class="btn-outline">Explore Services</a>
</div>

<div class="stats-ribbon">
    <div class="stat-item">
        <div class="stat-num">500+</div>
        <div class="stat-label">Projects Completed</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">99%</div>
        <div class="stat-label">Approval Rate</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">24/7</div>
        <div class="stat-label">Expert Support</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">14</div>
        <div class="stat-label">Days Free Revision</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ===================== SERVICES SECTION =====================
st.markdown("""
<div id="services">
    <h2 class="section-title">Mastercraft Services</h2>
    <p class="section-subtitle">Comprehensive academic support tailored to global university standards.</p>
    <div class="grid-3">
        <div class="pro-card">
            <div class="card-icon">✒️</div>
            <h3>Elite Proofreading</h3>
            <p>Eradicate grammatical errors, refine sentence structures, and ensure a commanding academic tone throughout your manuscript.</p>
        </div>
        <div class="pro-card">
            <div class="card-icon">📑</div>
            <h3>Precision Formatting</h3>
            <p>Flawless application of APA, MLA, Harvard, or Chicago styles. Perfect citations, bibliographies, and document architecture.</p>
        </div>
        <div class="pro-card">
            <div class="card-icon">🔬</div>
            <h3>Methodology Design</h3>
            <p>Expert consultation on qualitative and quantitative frameworks. We help you justify your research approach with authority.</p>
        </div>
        <div class="pro-card">
            <div class="card-icon">📚</div>
            <h3>Literature Review</h3>
            <p>Transform scattered sources into a compelling, synthesized narrative that highlights gaps and positions your research perfectly.</p>
        </div>
        <div class="pro-card">
            <div class="card-icon">📊</div>
            <h3>Data Presentation</h3>
            <p>Enhance the visual and descriptive presentation of your findings. Making complex data comprehensible and impactful.</p>
        </div>
        <div class="pro-card">
            <div class="card-icon">🛡️</div>
            <h3>Plagiarism Check</h3>
            <p>Comprehensive originality reports ensuring your work is 100% unique and adheres to the strictest academic integrity rules.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ===================== MEET THE TEAM (NEW SECTION) =====================
st.markdown("""
<div>
    <h2 class="section-title">Meet The Experts</h2>
    <p class="section-subtitle">Your work is handled by post-graduates and industry veterans.</p>
    <div class="grid-3">
        <div class="pro-card team-card">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Sarah&backgroundColor=b6e3f4" class="team-img" alt="Team Member">
            <div class="team-role">Head of Research</div>
            <h3>Dr. Sarah Khan</h3>
            <p>Ph.D. in Social Sciences. 10+ years experience in academic structuring and methodology design.</p>
        </div>
        <div class="pro-card team-card">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Ali&backgroundColor=c0aede" class="team-img" alt="Team Member">
            <div class="team-role">Lead Editor</div>
            <h3>Prof. Ali Raza</h3>
            <p>Specialist in Business & Finance literature. Master of APA & Harvard referencing styles.</p>
        </div>
        <div class="pro-card team-card">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Aisha&backgroundColor=ffdfbf" class="team-img" alt="Team Member">
            <div class="team-role">Quality Assurance</div>
            <h3>Aisha Malik, M.Phil</h3>
            <p>Ensures every document meets elite university standards before final delivery.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ===================== PRICING/PACKAGES (NEW SECTION) =====================
st.markdown("""
<div>
    <h2 class="section-title">Transparent Pricing</h2>
    <p class="section-subtitle">No hidden fees. Choose the tier that fits your academic needs.</p>
    <div class="grid-3">
        
        <!-- Basic Tier -->
        <div class="pricing-card">
            <h3>Standard Polish</h3>
            <div class="price">₨ 1.5<span>/word</span></div>
            <p style="color:var(--text-muted); margin-bottom: 20px;">Perfect for final drafts needing a professional touch.</p>
            <ul class="pricing-list">
                <li>Grammar & Spelling Check</li>
                <li>Punctuation Correction</li>
                <li>Basic Sentence Flow</li>
                <li>7-Day Turnaround</li>
            </ul>
        </div>

        <!-- Premium Tier (Highlighted) -->
        <div class="pricing-card popular">
            <div style="position:absolute; top:-15px; left:50%; transform:translateX(-50%); background:#D4AF37; color:#fff; padding:5px 15px; border-radius:20px; font-weight:bold; font-size:0.8rem;">MOST POPULAR</div>
            <h3>Complete Overhaul</h3>
            <div class="price">₨ 2.5<span>/word</span></div>
            <p style="color:rgba(255,255,255,0.8); margin-bottom: 20px;">Comprehensive structural and academic enhancement.</p>
            <ul class="pricing-list">
                <li>Everything in Standard</li>
                <li>Academic Tone Adjustment</li>
                <li>Full Referencing & Citations</li>
                <li>Logical Flow Optimization</li>
                <li>3-Day Turnaround</li>
            </ul>
            <a href="{base_wa_link}I want the Complete Overhaul package" class="btn-primary" style="background:white; color:var(--primary)!important; width:100%;">Select Premium</a>
        </div>

        <!-- Express Tier -->
        <div class="pricing-card">
            <h3>Express Delivery</h3>
            <div class="price">₨ 4.0<span>/word</span></div>
            <p style="color:var(--text-muted); margin-bottom: 20px;">For urgent deadlines without compromising quality.</p>
            <ul class="pricing-list">
                <li>Priority Support queue</li>
                <li>Full Structural Editing</li>
                <li>Advanced Formatting</li>
                <li><strong>24-Hour Turnaround</strong></li>
            </ul>
        </div>

    </div>
</div>
""", unsafe_allow_html=True)


# ===================== STREAMLIT INTERACTIVE QUOTE (Kept & Stylized) =====================
st.markdown("<h2 class='section-title'>Custom Quote Calculator</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-subtitle'>Need something specific? Calculate it instantly.</p>", unsafe_allow_html=True)

with st.container():
    c1, c2 = st.columns([2, 1], gap="large")
    with c1:
        words = st.slider("Select Word Count", min_value=500, max_value=20000, step=500, value=2000)
        service = st.selectbox("Service Type", ["Proofreading", "Formatting", "Full Structural Review", "Methodology"])
        urgency = st.radio("Turnaround Time", ["Standard (7 Days)", "Urgent (3 Days)", "Express (24 Hours)"], horizontal=True)
    
    with c2:
        # Simple Calculation Logic
        base = 1.5 if service == "Proofreading" else 2.0 if service == "Formatting" else 2.5 if service == "Full Structural Review" else 3.0
        mult = 1.0 if "7 Days" in urgency else 1.5 if "3 Days" in urgency else 2.0
        total = words * base * mult
        
        st.markdown(f"""
        <div class="pro-card" style="text-align:center; background: var(--primary); color: white;">
            <h3 style="color:white; margin-bottom:0;">Estimated Cost</h3>
            <div style="font-size:3rem; font-weight:800; margin:10px 0; color: #10B981;">₨ {total:,.0f}</div>
            <p style="color:rgba(255,255,255,0.7); font-size:0.9rem;">{words} words • {urgency}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        custom_msg = f"Hello WriteWise! I need {service} for {words} words. Need it by {urgency}. Estimated price is Rs {total:,.0f}."
        st.markdown(f'<a href="{base_wa_link}{urllib.parse.quote(custom_msg)}" class="btn-primary" style="width:100%; text-align:center;" target="_blank">Book Now via WhatsApp</a>', unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("""
<div style="text-align:center; padding: 60px 20px 30px 20px; border-top: 1px solid rgba(0,0,0,0.05); margin-top: 60px;">
    <h2 style="color: var(--primary); font-weight: 800; margin-bottom: 10px;">WriteWise Premium</h2>
    <p style="color: var(--text-muted); margin-bottom: 20px;">Strictly Confidential • 100% Plagiarism Free • Ethical Academic Support</p>
    <p style="font-size: 0.9rem; color: #94A3B8;">© 2026 WriteWise Academic Help. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
