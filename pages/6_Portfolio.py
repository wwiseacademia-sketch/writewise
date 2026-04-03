import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Our Portfolio | WriteWise",
    page_icon="🏆",
    layout="wide"
)

# 2. Ultra-Premium Custom CSS for Portfolio Page
st.markdown("""
    <style>
    /* Premium Title styling (Emerald & Dark Slate for Success/Growth Vibe) */
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
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 50px;
    }

    /* Portfolio Case Study Cards */
    .portfolio-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        border-top: 5px solid #10b981; /* Success Green / Emerald */
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.08);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 25px;
        position: relative;
        overflow: hidden;
    }
    
    .portfolio-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 35px -10px rgba(16, 185, 129, 0.2);
    }

    /* Industry / Category Badge */
    .category-badge {
        background: linear-gradient(135deg, #10b981 0%, #047857 100%);
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 15px;
    }

    .project-title {
        color: #1a202c;
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 15px;
        line-height: 1.3;
    }

    /* Challenge & Solution Section */
    .cs-section {
        margin-bottom: 15px;
    }
    
    .cs-label {
        font-weight: 800;
        color: #374151;
        font-size: 14px;
        text-transform: uppercase;
    }
    
    .cs-text {
        color: #4b5563;
        font-size: 15px;
        line-height: 1.6;
        margin-top: 5px;
    }

    /* The 'Result' Highlight Box */
    .result-box {
        background-color: #ecfdf5;
        border-left: 4px solid #10b981;
        padding: 15px;
        border-radius: 0 8px 8px 0;
        margin-top: 20px;
    }
    
    .result-text {
        color: #065f46;
        font-size: 16px;
        font-weight: 800;
    }

    /* Streamlit Tabs Customization */
    div[data-baseweb="tab-list"] {
        gap: 15px;
        justify-content: center;
        margin-bottom: 30px;
    }

    /* CTA Button (Emerald/Teal) */
    div.stButton > button {
        background: linear-gradient(135deg, #047857 0%, #10b981 100%);
        color: white !important;
        font-size: 19px;
        font-weight: 800;
        border-radius: 10px;
        border: none;
        padding: 0.8rem 2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 8px 15px rgba(16, 185, 129, 0.3);
    }
    
    div.stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 15px 25px rgba(16, 185, 129, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='page-title'>Proven Track Record 🏆</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>Explore our featured case studies. We don't just write words; we deliver measurable success.</p>", unsafe_allow_html=True)

st.write("---")

# 4. Interactive Tabs for Different Categories
tab1, tab2, tab3 = st.tabs(["💡 Conversion Copywriting", "📝 SEO & Content Strategy", "🎓 Academic & Executive"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class='portfolio-card'>
                <div class='category-badge'>E-Commerce Funnel</div>
                <div class='project-title'>Revamping a Supplement Brand's Landing Page</div>
                <div class='cs-section'>
                    <span class='cs-label'>The Challenge:</span>
                    <div class='cs-text'>A premium health brand was driving massive ad traffic to their landing page, but the conversion rate was a dismal 1.2%. The copy was too technical and lacked emotional appeal.</div>
                </div>
                <div class='cs-section'>
                    <span class='cs-label'>Our Solution:</span>
                    <div class='cs-text'>We rewrote the entire sales page using a direct-response psychological framework, focusing on the customer's pain points and the ultimate dream outcome.</div>
                </div>
                <div class='result-box'>
                    <span class='result-text'>📈 Result: Conversion rate skyrocketed to 4.8%, generating an additional $120,000 in revenue in just 30 days.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <div class='portfolio-card'>
                <div class='category-badge'>SaaS Email Marketing</div>
                <div class='project-title'>B2B Onboarding Email Sequence</div>
                <div class='cs-section'>
                    <span class='cs-label'>The Challenge:</span>
                    <div class='cs-text'>A software company was losing 60% of their free-trial users before they ever upgraded to the paid premium plan.</div>
                </div>
                <div class='cs-section'>
                    <span class='cs-label'>Our Solution:</span>
                    <div class='cs-text'>We engineered a 7-day automated email sequence. Instead of hard-selling, we shared value-driven stories, case studies, and subtle urgency triggers.</div>
                </div>
                <div class='result-box'>
                    <span class='result-text'>🚀 Result: Free-to-Paid upgrade rate increased by 55%, significantly lowering their Cost Per Acquisition (CPA).</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class='portfolio-card'>
                <div class='category-badge'>Tech & Fintech Blog</div>
                <div class='project-title'>Scaling Organic Traffic for a FinTech Startup</div>
                <div class='cs-section'>
                    <span class='cs-label'>The Challenge:</span>
                    <div class='cs-text'>A new finance app had zero organic footprint and was relying entirely on expensive Facebook ads to acquire users.</div>
                </div>
                <div class='cs-section'>
                    <span class='cs-label'>Our Solution:</span>
                    <div class='cs-text'>We produced a series of 15 long-form, highly authoritative SEO articles (2,500+ words each) targeting low-competition, high-intent financial keywords.</div>
                </div>
                <div class='result-box'>
                    <span class='result-text'>🥇 Result: 3 articles ranked #1 on Google within 4 months, driving 40,000+ free organic visitors monthly.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <div class='portfolio-card'>
                <div class='category-badge'>Brand Storytelling</div>
                <div class='project-title'>Complete Website Overhaul for a Luxury Hotel</div>
                <div class='cs-section'>
                    <span class='cs-label'>The Challenge:</span>
                    <div class='cs-text'>A 5-star boutique hotel's website copy sounded generic and boring, failing to capture the luxury experience they offered.</div>
                </div>
                <div class='cs-section'>
                    <span class='cs-label'>Our Solution:</span>
                    <div class='cs-text'>We crafted highly immersive, sensory-rich website copy that painted a vivid picture of the guest experience, making the reader "feel" the luxury.</div>
                </div>
                <div class='result-box'>
                    <span class='result-text'>💎 Result: Direct bookings increased by 30%, saving the hotel thousands in third-party commission fees.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class='portfolio-card'>
                <div class='category-badge'>Academic Excellence</div>
                <div class='project-title'>Ivy League Admission & Statement of Purpose</div>
                <div class='cs-section'>
                    <span class='cs-label'>The Challenge:</span>
                    <div class='cs-text'>A brilliant student had the grades but struggled to articulate their personal story and passion in their University admissions essay.</div>
                </div>
                <div class='cs-section'>
                    <span class='cs-label'>Our Solution:</span>
                    <div class='cs-text'>Our academic experts worked closely with the student to craft a compelling, deeply personal narrative that highlighted their unique worldview without sounding boastful.</div>
                </div>
                <div class='result-box'>
                    <span class='result-text'>🎓 Result: Student received acceptance letters from 3 Ivy League institutions, including a partial scholarship.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <div class='portfolio-card'>
                <div class='category-badge'>Executive Career</div>
                <div class='project-title'>C-Suite Resume & LinkedIn Optimization</div>
                <div class='cs-section'>
                    <span class='cs-label'>The Challenge:</span>
                    <div class='cs-text'>A senior marketing director was applying for VP roles but wasn't passing the initial ATS (Applicant Tracking System) screening phase.</div>
                </div>
                <div class='cs-section'>
                    <span class='cs-label'>Our Solution:</span>
                    <div class='cs-text'>We engineered an ATS-compliant, achievement-based executive resume and completely overhauled their LinkedIn profile to position them as a thought leader.</div>
                </div>
                <div class='result-box'>
                    <span class='result-text'>💼 Result: Landed 4 final-round interviews and successfully secured a VP position at a Fortune 500 company.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("---")

# 5. Call to Action (CTA) - Emerald Green Button
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1a202c; font-weight: 800;'>Want results like these for your business? 🚀</h3>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Claim Your Custom Strategy Now"):
        st.switch_page("pages/3_Get_a_Quote.py")
