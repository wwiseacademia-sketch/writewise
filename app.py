import streamlit as st

# 1. Page Configuration (Ye hamesha line 1 par hona chahiye)
st.set_page_config(
    page_title="WriteWise | Premium Writing & Copywriting Agency",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Ultra-Premium Custom CSS for the Landing Page
st.markdown("""
    <style>
    /* Hero Section Title (Deep Purple to Vibrant Pink Gradient for High-End Tech/Agency Vibe) */
    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #3a1c71, #d76d77, #ffaf7b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 10px;
        letter-spacing: -2px;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #4b5563;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 30px;
        font-weight: 500;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Trust Bar (Small pill badges below the subtitle) */
    .trust-bar {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 50px;
        flex-wrap: wrap;
    }
    
    .trust-pill {
        background-color: #f3f4f6;
        color: #374151;
        padding: 8px 18px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.5px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
    }

    /* Highlight Cards (Home Page Specific) */
    .feature-card {
        background: white;
        padding: 35px 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border-top: 5px solid transparent;
        height: 280px;
        margin-bottom: 20px;
    }
    
    /* Individual Top Borders on Hover */
    .fc-1:hover { transform: translateY(-15px); border-top: 5px solid #d76d77; box-shadow: 0 20px 40px -10px rgba(215, 109, 119, 0.2); }
    .fc-2:hover { transform: translateY(-15px); border-top: 5px solid #3a1c71; box-shadow: 0 20px 40px -10px rgba(58, 28, 113, 0.2); }
    .fc-3:hover { transform: translateY(-15px); border-top: 5px solid #ffaf7b; box-shadow: 0 20px 40px -10px rgba(255, 175, 123, 0.2); }

    .feature-icon {
        font-size: 45px;
        margin-bottom: 15px;
    }

    .feature-title {
        color: #111827;
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .feature-desc {
        color: #4b5563;
        font-size: 15px;
        line-height: 1.6;
    }

    /* Quick Stats Section */
    .stat-container {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        border-radius: 20px;
        padding: 40px 20px;
        color: white;
        text-align: center;
        margin-top: 40px;
        margin-bottom: 40px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #ffaf7b, #d76d77);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        font-size: 16px;
        font-weight: 600;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Modern Gradient Global Button styling */
    div.stButton > button {
        background: linear-gradient(135deg, #3a1c71 0%, #d76d77 100%);
        color: white !important;
        font-size: 19px;
        font-weight: 800;
        border-radius: 12px;
        border: none;
        padding: 0.8rem 1.5rem;
        width: 100%;
        box-shadow: 0 10px 20px rgba(215, 109, 119, 0.3);
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(215, 109, 119, 0.5);
        background: linear-gradient(135deg, #d76d77 0%, #3a1c71 100%);
    }
    </style>
""", unsafe_allow_html=True)


# 3. Massive Hero Section
st.markdown("<h1 class='hero-title'>Words That Command Authority.</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Stop losing clients to bad copy and grades to poor structure. We engineer premium, high-converting content and elite academic papers tailored for absolute success.</p>", unsafe_allow_html=True)

# Trust Pills
st.markdown("""
    <div class='trust-bar'>
        <span class='trust-pill'>⭐ 4.9/5 Average Rating</span>
        <span class='trust-pill'>🔒 100% NDA Protected</span>
        <span class='trust-pill'>⚡ Plagiarism-Free Guarantee</span>
        <span class='trust-pill'>🏆 Top 1% Writers</span>
    </div>
""", unsafe_allow_html=True)

# 4. Hero Action Buttons (Side by Side)
col_empty1, col_btn1, col_btn2, col_empty2 = st.columns([1, 1.5, 1.5, 1])

with col_btn1:
    if st.button("🚀 Start Your Project Now"):
        st.switch_page("pages/3_Get_a_Quote.py")

with col_btn2:
    if st.button("📊 View Our Case Studies"):
        st.switch_page("pages/6_Portfolio.py")

st.write("")
st.write("")
st.write("---")
st.write("")

# 5. Core Pillars (Value Proposition Cards)
st.markdown("<h2 style='text-align: center; color: #111827; font-weight: 900; margin-bottom: 30px;'>Our Three Pillars of Excellence</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class='feature-card fc-1'>
            <div class='feature-icon'>🎯</div>
            <div class='feature-title'>Conversion Copywriting</div>
            <div class='feature-desc'>We don't just write words; we build 24/7 sales machines. Landing pages, emails, and ads engineered to trigger psychological buying motives.</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class='feature-card fc-2'>
            <div class='feature-icon'>🎓</div>
            <div class='feature-title'>Elite Academic Writing</div>
            <div class='feature-desc'>Flawless research, rigorous citations, and impeccable structure. From Ivy League admissions to PhD-level dissertations, we deliver perfection.</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class='feature-card fc-3'>
            <div class='feature-icon'>🔍</div>
            <div class='feature-title'>SEO Content Strategy</div>
            <div class='feature-desc'>Dominate Google search results. We craft highly authoritative, long-form content that drives organic traffic and builds massive brand trust.</div>
        </div>
    """, unsafe_allow_html=True)

# 6. Trust Stats Banner (Dark Mode)
st.markdown("""
    <div class='stat-container'>
        <div style='display: flex; justify-content: space-around; flex-wrap: wrap;'>
            <div>
                <div class='stat-number'>500+</div>
                <div class='stat-label'>Projects Delivered</div>
            </div>
            <div>
                <div class='stat-number'>99%</div>
                <div class='stat-label'>Client Satisfaction</div>
            </div>
            <div>
                <div class='stat-number'>24/7</div>
                <div class='stat-label'>Premium Support</div>
            </div>
            <div>
                <div class='stat-number'>0%</div>
                <div class='stat-label'>AI/Plagiarism</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 7. Final Footer CTA
st.markdown("<h3 style='text-align: center; color: #111827; font-weight: 800; margin-top: 30px;'>Ready to experience the WriteWise difference?</h3>", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns([1, 1, 1])
with col_f2:
    if st.button("Get Your Free Custom Quote"):
        st.switch_page("pages/3_Get_a_Quote.py")
