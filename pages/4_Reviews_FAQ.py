import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Reviews & FAQ | WriteWise",
    page_icon="⭐",
    layout="wide"
)

# 2. Ultra-Premium Custom CSS for Reviews & FAQ
st.markdown("""
    <style>
    /* Premium Title styling (Gold & Dark Blue Vibe for Trust) */
    .page-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #1e3c72, #2a5298);
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

    /* Review Card Styling */
    .review-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        border-top: 5px solid #d4af37; /* Premium Gold Border */
        box-shadow: 0 10px 20px -5px rgba(0,0,0,0.05);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 25px;
        height: 260px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .review-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 30px -10px rgba(212, 175, 55, 0.2);
    }

    /* 5-Star Rating Styling */
    .stars {
        color: #FFD700;
        font-size: 20px;
        margin-bottom: 15px;
        letter-spacing: 2px;
    }

    .review-text {
        color: #2d3748;
        font-size: 16px;
        font-style: italic;
        line-height: 1.6;
        flex-grow: 1;
    }

    /* Client Info Styling */
    .client-info {
        display: flex;
        align-items: center;
        margin-top: 15px;
    }
    
    .client-avatar {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 18px;
        margin-right: 15px;
    }

    .client-details {
        display: flex;
        flex-direction: column;
    }

    .client-name {
        font-weight: 800;
        color: #1a202c;
        font-size: 16px;
    }
    
    .client-role {
        color: #718096;
        font-size: 13px;
        font-weight: 600;
    }

    /* FAQ Section Title */
    .faq-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1a202c;
        text-align: center;
        margin-top: 40px;
        margin-bottom: 30px;
    }

    /* Main CTA Button */
    div.stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #aa8c2c 100%); /* Gold Gradient */
        color: white !important;
        font-size: 19px;
        font-weight: 800;
        border-radius: 10px;
        border: none;
        padding: 0.8rem 2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 8px 15px rgba(212, 175, 55, 0.3);
    }
    
    div.stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 15px 25px rgba(212, 175, 55, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='page-title'>Don't Just Take Our Word For It ⭐</h1>", unsafe_allow_html=True)
st.markdown("<p class='page-subtitle'>Trusted by industry leaders, elite academics, and visionary brands worldwide.</p>", unsafe_allow_html=True)

st.write("---")

# 4. Reviews / Testimonials Section (2 Columns for wider, elegant cards)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class='review-card'>
            <div class='stars'>★★★★★</div>
            <div class='review-text'>"WriteWise completely transformed our digital presence. Their SEO-driven content strategy increased our organic traffic by 150% in just three months. Truly unmatched quality."</div>
            <div class='client-info'>
                <div class='client-avatar'>SL</div>
                <div class='client-details'>
                    <span class='client-name'>Sarah Linning</span>
                    <span class='client-role'>CMO @ TechNova Solutions</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='review-card'>
            <div class='stars'>★★★★★</div>
            <div class='review-text'>"The level of rigorous research and flawless citation in my PhD thesis was astounding. They matched my academic tone perfectly and delivered two weeks ahead of the deadline."</div>
            <div class='client-info'>
                <div class='client-avatar'>DK</div>
                <div class='client-details'>
                    <span class='client-name'>Dr. David K.</span>
                    <span class='client-role'>Post-Doc Researcher</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='review-card'>
            <div class='stars'>★★★★★</div>
            <div class='review-text'>"As an e-commerce brand, our landing page copy is everything. Their direct-response copywriters rewrote our funnels and we saw a 40% bump in conversions overnight. Worth every penny."</div>
            <div class='client-info'>
                <div class='client-avatar'>MT</div>
                <div class='client-details'>
                    <span class='client-name'>Marcus Thorne</span>
                    <span class='client-role'>Founder @ Apex Retail</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='review-card'>
            <div class='stars'>★★★★★</div>
            <div class='review-text'>"I was struggling to get interviews for executive roles. The WriteWise team engineered an ATS-friendly resume that landed me interviews at three Fortune 500 companies within a week."</div>
            <div class='client-info'>
                <div class='client-avatar'>ER</div>
                <div class='client-details'>
                    <span class='client-name'>Elena Rodriguez</span>
                    <span class='client-role'>VP of Operations</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("---")

# 5. FAQ Section
st.markdown("<h2 class='faq-title'>Frequently Asked Questions ❓</h2>", unsafe_allow_html=True)

# Using Streamlit Expanders for FAQs (Clean & Interactive)
c1, c2 = st.columns([1, 8]) # To center the FAQ a bit nicely, or just use full width. Let's use full width for better readability on mobile.

with st.expander("🛡️ Is your writing 100% original and plagiarism-free?"):
    st.write("Absolutely. Every single piece of content is crafted from scratch by our expert writers. We strictly do not use spun content. Upon request, we provide premium Turnitin or Copyscape reports to guarantee 100% originality.")

with st.expander("⏱️ How fast can you deliver my project?"):
    st.write("Our standard turnaround time is 3 to 5 business days, depending on project complexity. However, we also offer an **Urgent 24-Hour Delivery** for clients who need premium quality on a tight deadline without compromising excellence.")

with st.expander("🔄 What if I need changes to the delivered document?"):
    st.write("Your satisfaction is our ultimate priority. We offer **Unlimited Revisions** within 14 days of delivery. If the content doesn't align perfectly with your initial brief, our editors will refine it until it exceeds your expectations.")

with st.expander("🔒 Is my personal information and project data confidential?"):
    st.write("Yes, 100%. We operate under strict Non-Disclosure Agreements (NDAs). Your personal details, project requirements, and the final delivered files are securely encrypted and never shared with third parties.")

with st.expander("💰 How does the pricing and payment process work?"):
    st.write("We offer custom, transparent pricing based on your specific requirements (word count, research depth, and deadline). Once you request a quote, we will send you a fixed-price proposal. We accept all major secure payment methods including Stripe, PayPal, and Bank Transfers.")

st.write("")
st.write("")
st.write("---")

# 6. Call to Action (CTA) - Gold Button
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1a202c; font-weight: 800;'>Convinced? Let's write your success story. 🖋️</h3>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Get Your Free Quote Now"):
        st.switch_page("pages/3_Get_a_Quote.py")
