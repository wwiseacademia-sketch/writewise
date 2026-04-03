import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Premium Services | WriteWise",
    page_icon="💎",
    layout="wide"
)

# 2. Ultra-Premium & Colorful Custom CSS
st.markdown("""
    <style>
    .page-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #1A2980, #26D0CE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    .page-subtitle {
        text-align: center;
        color: #4a5568;
        font-size: 1.4rem;
        font-weight: 500;
        margin-bottom: 50px;
    }

    /* Card Styling */
    .service-card {
        background-color: #ffffff;
        padding: 30px 25px;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-align: center;
        min-height: 310px; /* Height barha di taake text ke neechay space bache */
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .service-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 30px -5px rgba(0, 0, 0, 0.15);
    }

    /* Colorful Icon Backgrounds */
    .icon-wrapper {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 35px;
        margin: 0 auto 20px auto;
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        color: white; /* Emoji will remain its color, but any text would be white */
    }

    /* Distinct Gradients for each Service */
    .bg-content { background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%); }
    .bg-academic { background: linear-gradient(135deg, #8e2de2 0%, #4a00e0 100%); }
    .bg-copy { background: linear-gradient(135deg, #f12711 0%, #f5af19 100%); }
    .bg-edit { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); }
    .bg-resume { background: linear-gradient(135deg, #fc4a1a 0%, #f7b733 100%); }
    .bg-creative { background: linear-gradient(135deg, #ff0844 0%, #ffb199 100%); }

    .service-title {
        color: #1a202c;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 15px;
        letter-spacing: -0.5px;
    }

    .service-desc {
        color: #4a5568;
        font-size: 15px;
        line-height: 1.6;
    }

    /* Main Action Button */
    div.stButton > button {
        background: linear-gradient(135deg, #1A2980 0%, #26D0CE 100%);
        color: white !important;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        padding: 0.8rem 2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 8px 15px rgba(38, 208, 206, 0.3);
    }
    
    div.stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 15px 25px rgba(38, 208, 206, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Premium Header Section
st.markdown("<h1 class='page-title'>Unrivaled Writing Solutions</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>Empowering brands, professionals, and academics with words that persuade, engage, and deliver measurable results.</p>", unsafe_allow_html=True)

st.write("---")

# 4. Services Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='service-card'>
            <div class='icon-wrapper bg-content'>📝</div>
            <div class='service-title'>Content Strategy & Writing</div>
            <div class='service-desc'>Dominate search rankings and captivate your audience with SEO-optimized, high-converting content tailored to your brand's unique voice.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Adding space before expander
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    with st.expander("Explore Sub-Services"):
        st.write("🔹 Authority-Building Blog Posts")
        st.write("🔹 SEO-Driven Website Copy")
        st.write("🔹 High-Converting Product Descriptions")
        st.write("🔹 Engaging Social Media Content")

    st.write("") 
    st.write("") 

    st.markdown("""
        <div class='service-card'>
            <div class='icon-wrapper bg-academic'>🎓</div>
            <div class='service-title'>Elite Academic Writing</div>
            <div class='service-desc'>Achieve academic excellence with rigorously researched, flawlessly cited, and intellectually compelling papers crafted by subject-matter experts.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    with st.expander("Explore Sub-Services"):
        st.write("🔹 Masters & PhD Level Theses")
        st.write("🔹 Research Papers & Dissertations")
        st.write("🔹 Complex Case Studies")
        st.write("🔹 Comprehensive Literature Reviews")

with col2:
    st.markdown("""
        <div class='service-card'>
            <div class='icon-wrapper bg-copy'>💡</div>
            <div class='service-title'>Conversion Copywriting</div>
            <div class='service-desc'>Turn clicks into clients. Our conversion-focused copywriters craft persuasive narratives that drive action and maximize your ROI.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    with st.expander("Explore Sub-Services"):
        st.write("🔹 High-Impact Landing Pages")
        st.write("🔹 Direct Response Email Campaigns")
        st.write("🔹 Persuasive Video & Ad Scripts")
        st.write("🔹 Sales Funnel Copy")

    st.write("") 
    st.write("") 

    st.markdown("""
        <div class='service-card'>
            <div class='icon-wrapper bg-edit'>🔍</div>
            <div class='service-title'>Editing & Proofreading</div>
            <div class='service-desc'>Polished to perfection. Our meticulous editors refine your syntax, eliminate errors, and elevate your document's overall impact and clarity.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    with st.expander("Explore Sub-Services"):
        st.write("🔹 Advanced Grammar & Syntax Checking")
        st.write("🔹 Tone, Flow & Style Refinement")
        st.write("🔹 Formatting & Layout Optimization")
        st.write("🔹 Deep Plagiarism Screening")

with col3:
    st.markdown("""
        <div class='service-card'>
            <div class='icon-wrapper bg-resume'>📄</div>
            <div class='service-title'>Executive Resumes</div>
            <div class='service-desc'>Stand out in a highly competitive job market with ATS-optimized, executive-level resumes and compelling cover letters that demand attention.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    with st.expander("Explore Sub-Services"):
        st.write("🔹 ATS-Friendly Resume Engineering")
        st.write("🔹 Custom-Tailored Cover Letters")
        st.write("🔹 LinkedIn Profile Overhauls")
        st.write("🔹 C-Level / Executive Bios")

    st.write("") 
    st.write("") 

    st.markdown("""
        <div class='service-card'>
            <div class='icon-wrapper bg-creative'>🎨</div>
            <div class='service-title'>Creative Storytelling</div>
            <div class='service-desc'>Breathe life into your ideas. We weave imaginative, emotionally resonant stories and scripts that leave a profound, lasting impression on your audience.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    with st.expander("Explore Sub-Services"):
        st.write("🔹 Fiction & Non-Fiction Books")
        st.write("🔹 Compelling Short Stories")
        st.write("🔹 Engaging Podcast Scripts")
        st.write("🔹 Immersive Character Biographies")

st.write("")
st.write("---")

# 5. Call to Action (CTA)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1a202c; font-weight: 800;'>Ready to elevate your brand's voice? Let's talk.</h3>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Request a Custom Quote"):
        st.switch_page("pages/3_Get_a_Quote.py")
