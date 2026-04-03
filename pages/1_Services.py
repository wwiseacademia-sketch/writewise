import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Premium Services | WriteWise",
    page_icon="💎",
    layout="wide"
)

# 2. Ultra-Premium Custom CSS
st.markdown("""
    <style>
    .page-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #0f2027, #203a43, #2c5364);
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

    .service-card {
        background-color: #ffffff;
        padding: 30px 25px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 15px;
        text-align: center;
        height: 250px;
    }
    
    .service-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border-bottom: 4px solid #2563eb; 
    }

    .service-icon {
        font-size: 42px;
        margin-bottom: 15px;
    }

    .service-title {
        color: #1a202c;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }

    .service-desc {
        color: #4a5568;
        font-size: 15px;
        line-height: 1.6;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white !important;
        font-size: 18px;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 0.8rem 2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.3);
    }
    
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px rgba(37, 99, 235, 0.4);
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
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
            <div class='service-icon'>📝</div>
            <div class='service-title'>Content Strategy & Writing</div>
            <div class='service-desc'>Dominate search rankings and captivate your audience with SEO-optimized, high-converting content tailored to your brand's unique voice.</div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Explore Sub-Services"):
        st.write("🔹 Authority-Building Blog Posts")
        st.write("🔹 SEO-Driven Website Copy")
        st.write("🔹 High-Converting Product Descriptions")
        st.write("🔹 Engaging Social Media Content")

    st.write("") 

    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>🎓</div>
            <div class='service-title'>Elite Academic Writing</div>
            <div class='service-desc'>Achieve academic excellence with rigorously researched, flawlessly cited, and intellectually compelling papers crafted by subject-matter experts.</div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Explore Sub-Services"):
        st.write("🔹 Masters & PhD Level Theses")
        st.write("🔹 Research Papers & Dissertations")
        st.write("🔹 Complex Case Studies")
        st.write("🔹 Comprehensive Literature Reviews")

with col2:
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>💡</div>
            <div class='service-title'>Conversion Copywriting</div>
            <div class='service-desc'>Turn clicks into clients. Our conversion-focused copywriters craft persuasive narratives that drive action and maximize your ROI.</div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Explore Sub-Services"):
        st.write("🔹 High-Impact Landing Pages")
        st.write("🔹 Direct Response Email Campaigns")
        st.write("🔹 Persuasive Video & Ad Scripts")
        st.write("🔹 Sales Funnel Copy")

    st.write("") 

    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>🔍</div>
            <div class='service-title'>Editing & Proofreading</div>
            <div class='service-desc'>Polished to perfection. Our meticulous editors refine your syntax, eliminate errors, and elevate your document's overall impact and clarity.</div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Explore Sub-Services"):
        st.write("🔹 Advanced Grammar & Syntax Checking")
        st.write("🔹 Tone, Flow & Style Refinement")
        st.write("🔹 Formatting & Layout Optimization")
        st.write("🔹 Deep Plagiarism Screening")

with col3:
    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>📄</div>
            <div class='service-title'>Executive Resumes</div>
            <div class='service-desc'>Stand out in a highly competitive job market with ATS-optimized, executive-level resumes and compelling cover letters that demand attention.</div>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Explore Sub-Services"):
        st.write("🔹 ATS-Friendly Resume Engineering")
        st.write("🔹 Custom-Tailored Cover Letters")
        st.write("🔹 LinkedIn Profile Overhauls")
        st.write("🔹 C-Level / Executive Bios")

    st.write("") 

    st.markdown("""
        <div class='service-card'>
            <div class='service-icon'>🎨</div>
            <div class='service-title'>Creative Storytelling</div>
            <div class='service-desc'>Breathe life into your ideas. We weave imaginative, emotionally resonant stories and scripts that leave a profound, lasting impression on your audience.</div>
        </div>
    """, unsafe_allow_html=True)
    
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
