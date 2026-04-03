import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Our Team | WriteWise",
    page_icon="👥",
    layout="wide"
)

# 2. Ultra-Premium Custom CSS for Team Page
st.markdown("""
    <style>
    /* Premium Title styling */
    .page-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #2b5876, #4e4376);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    .page-subtitle {
        text-align: center;
        color: #4a5568;
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 60px;
    }

    /* Team Member Card Styling */
    .team-card {
        background-color: #ffffff;
        padding: 35px 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px -10px rgba(0,0,0,0.08);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-align: center;
        border-top: 5px solid transparent;
        height: 380px;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    /* Hover Effect - Smooth Bubble Up & Top Border Glow */
    .team-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.15);
        border-top: 5px solid #4e4376;
    }

    /* Colorful Avatar Circles */
    .avatar {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 45px;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        color: white;
    }

    /* Gradients for Avatars */
    .av-1 { background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%); }
    .av-2 { background: linear-gradient(135deg, #4776E6 0%, #8E54E9 100%); }
    .av-3 { background: linear-gradient(135deg, #F37335 0%, #FDC830 100%); }
    .av-4 { background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%); }
    .av-5 { background: linear-gradient(135deg, #b20a2c 0%, #fffbd5 100%); }
    .av-6 { background: linear-gradient(135deg, #1D976C 0%, #93F9B9 100%); }

    /* Role Badge Styling */
    .role-badge {
        background-color: #f1f5f9;
        color: #4e4376;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 15px;
    }

    .member-name {
        color: #1a202c;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 10px;
        letter-spacing: -0.5px;
    }

    .member-bio {
        color: #4a5568;
        font-size: 15px;
        line-height: 1.6;
    }

    /* CTA Button */
    div.stButton > button {
        background: linear-gradient(135deg, #2b5876 0%, #4e4376 100%);
        color: white !important;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        padding: 0.8rem 2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 8px 15px rgba(78, 67, 118, 0.3);
    }
    
    div.stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 15px 25px rgba(78, 67, 118, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Premium Header Section
st.markdown("<h1 class='page-title'>Meet The Experts</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>A formidable team of elite wordsmiths, PhD researchers, and conversion strategists dedicated to your success.</p>", unsafe_allow_html=True)

st.write("---")
st.write("")

# 4. Team Members Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='team-card'>
            <div class='avatar av-1'>👩‍💼</div>
            <div class='role-badge'>Chief Strategist</div>
            <div class='member-name'>Sarah Jenkins</div>
            <div class='member-bio'>10+ years scaling Fortune 500 brands through data-driven storytelling and high-converting content frameworks.</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='team-card'>
            <div class='avatar av-4'>👨‍🏫</div>
            <div class='role-badge'>QA Director</div>
            <div class='member-name'>James Sterling</div>
            <div class='member-bio'>Former senior editor at top-tier publications. James meticulously polishes every draft until it achieves absolute perfection.</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='team-card'>
            <div class='avatar av-2'>👨‍🔬</div>
            <div class='role-badge'>Head of Research</div>
            <div class='member-name'>Dr. Robert Chen</div>
            <div class='member-bio'>PhD in Linguistics. Leads our elite academic division, ensuring impeccable research, rigorous citations, and flawless structure.</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='team-card'>
            <div class='avatar av-5'>👩‍🎨</div>
            <div class='role-badge'>Creative Director</div>
            <div class='member-name'>Anita Desai</div>
            <div class='member-bio'>Master storyteller and brand voice architect. Anita breathes life into dry concepts, crafting narratives that deeply resonate.</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='team-card'>
            <div class='avatar av-3'>👩‍💻</div>
            <div class='role-badge'>Lead Copywriter</div>
            <div class='member-name'>Elena Rodriguez</div>
            <div class='member-bio'>Direct-response specialist. Elena engineers copy that triggers psychological buying motives, turning casual browsers into loyal buyers.</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='team-card'>
            <div class='avatar av-6'>👨‍💻</div>
            <div class='role-badge'>SEO Specialist</div>
            <div class='member-name'>David Alaba</div>
            <div class='member-bio'>Growth hacker and SEO savant. David ensures your content doesn't just sound brilliant—it dominates the search engine rankings.</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("---")

# 5. Call to Action (CTA)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1a202c; font-weight: 800;'>Hire World-Class Talent For Your Next Project</h3>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Hire Our Experts Today"):
        st.switch_page("pages/3_Get_a_Quote.py")
