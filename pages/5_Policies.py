import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Policies & Guarantees | WriteWise",
    page_icon="🛡️",
    layout="wide"
)

# 2. Ultra-Premium Custom CSS for Policies Page
st.markdown("""
    <style>
    /* Premium Title styling (Slate & Deep Blue Vibe for Trust & Security) */
    .page-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #0f172a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    .page-subtitle {
        text-align: center;
        color: #475569;
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 50px;
    }

    /* Policy Box Styling */
    .policy-box {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 16px;
        border-top: 6px solid #3b82f6; /* Trust Blue Border */
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        line-height: 1.8;
    }

    .policy-header {
        color: #0f172a;
        font-size: 26px;
        font-weight: 800;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .policy-text {
        color: #334155;
        font-size: 16px;
    }

    .policy-text ul {
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .policy-text li {
        margin-bottom: 10px;
    }

    /* Streamlit Tabs Customization */
    div[data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
        margin-bottom: 20px;
    }
    
    div[data-baseweb="tab"] {
        font-size: 18px !important;
        font-weight: 600 !important;
        padding: 10px 20px !important;
        background-color: #f8fafc;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }

    /* CTA Button (Trust Blue) */
    div.stButton > button {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        color: white !important;
        font-size: 19px;
        font-weight: 800;
        border-radius: 10px;
        border: none;
        padding: 0.8rem 2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 8px 15px rgba(59, 130, 246, 0.3);
    }
    
    div.stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 15px 25px rgba(59, 130, 246, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='page-title'>Ironclad Guarantees 🛡️</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>Total transparency, zero hidden clauses, and absolute protection for your intellectual property.</p>", unsafe_allow_html=True)

st.write("---")

# 4. Interactive Tabs for Policies
tab1, tab2, tab3, tab4 = st.tabs(["🔒 Privacy & NDA", "🔄 Revisions & Refunds", "💎 Plagiarism Guarantee", "⚖️ Terms of Service"])

with tab1:
    st.markdown("""
        <div class='policy-box'>
            <div class='policy-header'>🔐 Strict Privacy & Non-Disclosure</div>
            <div class='policy-text'>
                Your secrets are safe with us. We treat every project with the highest level of confidentiality. 
                Whether you are a Fortune 500 CEO, a bestselling author, or a PhD candidate, your identity and data are protected.
                <ul>
                    <li><b>Automatic NDA:</b> A legally binding Non-Disclosure Agreement applies the moment you submit your project details.</li>
                    <li><b>Data Encryption:</b> All files and communications are stored on secure, encrypted servers and are permanently deleted 30 days after project approval.</li>
                    <li><b>No Reselling:</b> You retain 100% of the copyright. We never recycle, resell, or publish your custom content anywhere.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
        <div class='policy-box'>
            <div class='policy-header'>🤝 100% Satisfaction & Refunds</div>
            <div class='policy-text'>
                We don't stop until it's perfect. Our goal is to deliver a masterpiece on the first try, but if adjustments are needed, we are fully committed to refining it.
                <ul>
                    <li><b>Unlimited Revisions:</b> You are entitled to unlimited revisions within 14 days of delivery, provided they align with the original project brief.</li>
                    <li><b>Refund Eligibility:</b> If we fail to deliver the project on the agreed deadline, or if the final output completely deviates from your initial instructions even after revisions, you are entitled to a partial or full refund.</li>
                    <li><b>Payment Security:</b> All transactions are processed securely via industry-leading gateways. We never store your credit card details.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
        <div class='policy-box'>
            <div class='policy-header'>🚫 Zero-Tolerance Plagiarism Policy</div>
            <div class='policy-text'>
                In a world of AI-generated fluff and copy-pasted text, we stand for absolute originality.
                Every single word is meticulously crafted by human experts from a blank page.
                <ul>
                    <li><b>Custom Crafted:</b> We do not use templates, spun content, or unauthorized AI generation tools.</li>
                    <li><b>Rigorous Screening:</b> Every document passes through premium plagiarism detection software (such as Turnitin or Copyscape) before delivery.</li>
                    <li><b>Proof of Originality:</b> A detailed originality report can be attached to your final delivery completely free of charge upon request.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
        <div class='policy-box'>
            <div class='policy-header'>⚖️ Fair Terms of Engagement</div>
            <div class='policy-text'>
                Clear, fair, and professional terms to ensure a smooth partnership from start to finish.
                <ul>
                    <li><b>Project Initiation:</b> Work commences immediately after the initial deposit or full payment is cleared and the brief is fully approved.</li>
                    <li><b>Client Responsibilities:</b> To ensure timely delivery, clients are expected to provide clear instructions, necessary reference materials, and prompt feedback during the drafting phase.</li>
                    <li><b>Right to Refuse:</b> We maintain an ethical standard. We reserve the right to decline projects involving hate speech, illegal activities, or academic fraud (we provide model answers and research assistance only).</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("---")

# 5. Call to Action (CTA) - Trust Blue Button
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #0f172a; font-weight: 800;'>Your project is in safe hands. Let's build something great.</h3>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Start Your Secure Project"):
        st.switch_page("pages/3_Get_a_Quote.py")
