import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Our Services | WriteWise",
    page_icon="✨",
    layout="wide"
)

# 2. Modern Custom CSS for Services Page
st.markdown("""
    <style>
    /* Gradient Title */
    .page-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #ff6a00, #ee0979);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .page-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }

    /* Service Cards Styling */
    .service-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 6px solid #667eea;
        transition: all 0.3s ease-in-out;
        margin-bottom: 20px;
        height: 220px;
    }
    
    /* Hover Effect (Bubble up & Glow) */
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.2);
        border-left: 6px solid #ee0979;
    }

    .service-icon {
        font-size: 35px;
        margin-bottom: 15px;
    }

    .service-title {
        color: #2c3e50;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .service-desc {
        color: #555;
        font-size: 15px;
        line-height: 1.5;
    }

    /* CTA Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        border-radius: 30px;
        border: none;
        padding: 10px 30px;
        display: block;
        margin: 0 auto;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(30, 60, 114, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='page-title'>What We Offer 🎯</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>Premium writing solutions designed to elevate your brand and academic success.</p>", unsafe_allow_html=True)

st.write("---")

# 4. Services Grid (3x2 Layout)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>📝</div>
            <div class='service-title'>Content Writing</div>
            <div class='service-desc'>Engaging blog posts, articles, and website content optimized for SEO and readability.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>��</div>
            <div class='service-title'>Academic Writing</div>
            <div class='service-desc'>Well-researched essays, assignments, and research papers with perfect citations.</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>💡</div>
            <div class='service-title'>Copywriting</div>
            <div class='service-desc'>Persuasive sales copy, ad scripts, and landing pages that convert visitors into customers.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>🔍</div>
            <div class='service-title'>Proofreading</div>
            <div class='service-desc'>Meticulous editing to ensure your documents are grammar-free and flow perfectly.</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>📄</div>
            <div class='service-title'>Resume & Cover Letters</div>
            <div class='service-desc'>Professional resumes and cover letters designed to land you your dream job.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>🎨</div>
            <div class='service-title'>Creative Writing</div>
            <div class='service-desc'>Captivating stories, scripts, and creative pieces that leave a lasting impact.</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("---")

# 5. Call to Action (CTA)
st.markdown("<h3 style='text-align: center; color: #2c3e50;'>Ready to start your project? 🚀</h3>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Get a Free Quote Now"):
        st.switch_page("pages/3_Get_a_Quote.py")
