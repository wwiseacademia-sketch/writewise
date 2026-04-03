import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Get a Quote | WriteWise",
    page_icon="🚀",
    layout="wide"
)

# 2. Ultra-Premium Custom CSS for Quote Form
st.markdown("""
    <style>
    /* Premium Title styling */
    .page-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #FF416C, #FF4B2B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    .page-subtitle {
        color: #4a5568;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 40px;
    }

    /* Styling the Streamlit Form Container */
    [data-testid="stForm"] {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 15px 35px -5px rgba(0,0,0,0.1);
        border: none !important;
        border-top: 6px solid #FF416C !important;
        transition: all 0.3s ease;
    }
    
    [data-testid="stForm"]:hover {
        box-shadow: 0 25px 50px -12px rgba(255, 65, 108, 0.2);
    }

    /* Styling the Submit Button inside the Form */
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
        color: white !important;
        font-size: 20px;
        font-weight: 800;
        border-radius: 12px;
        border: none;
        padding: 0.8rem 2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 10px 20px rgba(255, 65, 108, 0.3);
        margin-top: 15px;
    }
    
    [data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 25px rgba(255, 65, 108, 0.5);
    }

    /* Trust Badge Cards (Right Column) */
    .trust-card {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #2b5876;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    
    .trust-title {
        font-size: 18px;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 5px;
    }
    
    .trust-desc {
        font-size: 14px;
        color: #4a5568;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='page-title'>Transform Your Ideas Into Impact 🚀</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>Fill out the form below to receive a personalized, no-obligation quote from our elite writing team within 24 hours.</p>", unsafe_allow_html=True)

st.write("---")

# 4. Main Layout: Form on Left (Bigger), Trust Badges on Right (Smaller)
col_form, col_trust = st.columns([2.2, 1])

with col_form:
    # THE QUOTE FORM
    with st.form("quote_form", clear_on_submit=True):
        st.markdown("### 📋 Project Details")
        
        # Row 1: Name and Email
        r1_c1, r1_c2 = st.columns(2)
        with r1_c1:
            name = st.text_input("Full Name *", placeholder="John Doe")
        with r1_c2:
            email = st.text_input("Email Address *", placeholder="john@company.com")

        # Row 2: THE GIANT DROPDOWN (All Services Included)
        service_options = [
            "Select a Service...",
            "📝 CONTENT: SEO Blog Posts & Articles",
            "📝 CONTENT: Website Copy & Landing Pages",
            "📝 CONTENT: Product Descriptions",
            "📝 CONTENT: Social Media Management",
            "🎓 ACADEMIC: University Assignments",
            "🎓 ACADEMIC: Master's & PhD Theses",
            "🎓 ACADEMIC: Research Papers & Dissertations",
            "🎓 ACADEMIC: Case Studies & Literature Reviews",
            "💡 COPYWRITING: Sales Pages & Funnels",
            "💡 COPYWRITING: Email Marketing Campaigns",
            "💡 COPYWRITING: Ad & Video Scripts",
            "🔍 EDITING: Proofreading & Grammar Check",
            "🔍 EDITING: Advanced Formatting & Plagiarism Check",
            "📄 CAREER: ATS-Friendly Executive Resumes",
            "📄 CAREER: Cover Letters & LinkedIn Optimization",
            "🎨 CREATIVE: Short Stories & Book Writing",
            "⚡ OTHER: Custom Writing Request"
        ]
        service = st.selectbox("Which specific service do you need? *", service_options)

        # Row 3: Word Count & Deadline
        r3_c1, r3_c2 = st.columns(2)
        with r3_c1:
            word_count = st.selectbox("Estimated Word Count / Length", [
                "Under 500 words", "500 - 1,000 words", "1,000 - 3,000 words", 
                "3,000 - 10,000 words", "10,000+ words", "Not Sure / Project Based"
            ])
        with r3_c2:
            deadline = st.selectbox("Expected Deadline *", [
                "Urgent (24 - 48 Hours)", "Standard (3 - 5 Days)", 
                "Relaxed (1 - 2 Weeks)", "Long Term Project"
            ])

        # Row 4: Project Description
        description = st.text_area("Tell us about your project requirements *", 
                                   placeholder="Describe your goals, target audience, specific formatting styles, or any reference materials...", 
                                   height=120)

        # Submit Button
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Get My Free Quote Now")

        # Form Submission Logic
        if submitted:
            if name == "" or email == "" or service == "Select a Service...":
                st.error("⚠️ Please fill in all the required fields (*).")
            else:
                st.balloons()
                st.success(f"🎉 Thank you, {name}! Your request for '{service}' has been received. Our lead strategist will email you at {email} within 24 hours.")
                # Future logic for sending email can be added here

with col_trust:
    st.markdown("### Why Partner With Us?")
    st.write("")
    
    st.markdown("""
        <div class='trust-card'>
            <div class='trust-title'>🔒 100% Confidential</div>
            <div class='trust-desc'>Your intellectual property and personal details are protected by strict Non-Disclosure Agreements (NDAs).</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='trust-card'>
            <div class='trust-title'>⚡ Lightning Fast Delivery</div>
            <div class='trust-desc'>We respect your time. Deadlines are sacred to us, and we never compromise on quality for speed.</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='trust-card'>
            <div class='trust-title'>💎 Zero Plagiarism</div>
            <div class='trust-desc'>Every single word is crafted from scratch. We provide premium Turnitin/Copyscape reports upon request.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='trust-card' style='border-left: 5px solid #FF416C;'>
            <div class='trust-title'>📞 Need Urgent Help?</div>
            <div class='trust-desc'>Email us directly at:<br><b>hello@writewise.com</b><br>Available 24/7 for premium clients.</div>
        </div>
    """, unsafe_allow_html=True)
