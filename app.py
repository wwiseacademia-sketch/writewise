import streamlit as st

# 1. Page Configuration (Ye sabse upar hona chahiye)
st.set_page_config(
    page_title="WriteWise | Premium Writing Services",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Modern Custom CSS (Premium Look, Hover Effects, Bubble Up)
st.markdown("""
    <style>
    /* Main Background & Text */
    .stApp {
        background-color: #f8f9fc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Main Title Styling */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #1e3c72, #2a5298);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    
    /* Subtitle Styling */
    .sub-title {
        font-size: 1.2rem;
        color: #555555;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 40px;
    }

    /* Modern Button Styling with Bubble Up (Hover Effect) */
    div.stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        font-size: 18px;
        font-weight: 600;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1.5rem;
        width: 100%;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease-in-out;
    }
    
    /* Mouse aane par Button upar uthega (Bubble up) aur glow karega */
    div.stButton > button:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 8px 20px rgba(118, 75, 162, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }

    /* Info Cards Styling */
    .info-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.3s ease;
        border-top: 4px solid #1e3c72;
    }
    
    .info-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)


# 3. Hero Section (Home Page UI)
st.markdown("<h1 class='main-title'>Welcome to WriteWise 🚀</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Your Professional Partner for Premium Content, Copywriting & Academic Needs.</p>", unsafe_allow_html=True)

st.divider()

# 4. Quick Action Buttons (Modern Navigation)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌟 Explore Services"):
        st.switch_page("pages/1_Services.py")

with col2:
    if st.button("📝 Get a Free Quote"):
        st.switch_page("pages/3_Get_a_Quote.py")

with col3:
    if st.button("💼 View Portfolio"):
        st.switch_page("pages/6_Portfolio.py")

st.write("")
st.write("")

# 5. Attractive Features Section (Cards)
st.markdown("### Why Choose WriteWise? ✨")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class='info-card'>
            <h2>🎯</h2>
            <h3>Top Quality</h3>
            <p>100% original, well-researched, and engaging content tailored to your needs.</p>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class='info-card'>
            <h2>⚡</h2>
            <h3>Fast Delivery</h3>
            <p>We value your time. Get your projects delivered strictly before deadlines.</p>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class='info-card'>
            <h2>🔒</h2>
            <h3>Confidential</h3>
            <p>Your data and project details are 100% secure with our strict privacy policies.</p>
        </div>
    """, unsafe_allow_html=True)
