import streamlit as st
import urllib.parse
from datetime import datetime, timedelta

# ===================== CONFIGURATION =====================
st.set_page_config(page_title="WriteWise Academic Help", page_icon="🎓", layout="wide")

# ===================== MODERN PREMIUM CSS =====================
st.markdown("""
<style>
:root{
    --bg:#f6f9fc;
    --surface:#ffffff;
    --text:#0b1220;
    --muted:#5b6472;
    --emerald:#0f766e;
    --emerald-dark:#065f46;
    --gold:#d4af37;
    --shadow:0 10px 30px rgba(0,0,0,0.08);
    --border:1px solid rgba(0,0,0,0.06);
}
.stApp{
    background:
        radial-gradient(900px 600px at 12% 0%, rgba(15,118,110,0.12), transparent 60%),
        radial-gradient(900px 600px at 88% 10%, rgba(212,175,55,0.12), transparent 58%),
        linear-gradient(180deg, var(--bg) 0%, #ffffff 60%, var(--bg) 100%);
    color:var(--text);
}
.block-container{ max-width:1150px; padding-top:1.3rem; }

/* Interactive Tabs */
button[data-baseweb="tab"] {
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
    border-radius: 12px 12px 0 0 !important;
    transition: all 0.3s ease !important;
}
button[data-baseweb="tab"]:hover {
    color: var(--emerald) !important;
    background: rgba(15,118,110,0.05) !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--emerald-dark) !important;
    border-bottom: 3px solid var(--emerald) !important;
    background: transparent !important;
}

/* Hero Section */
.hero{
    background: linear-gradient(135deg, rgba(15,118,110,0.12), rgba(212,175,55,0.10));
    border-radius: 22px;
    padding: 30px;
    box-shadow: var(--shadow);
    border: var(--border);
    text-align: center;
    margin-bottom: 20px;
}
.hero h1{ margin:0; color: var(--emerald-dark); font-weight: 900;}
.hero p{ margin:10px 0 0 0; color: rgba(11,18,32,0.78); font-size:1.1rem; }

/* Cards & Testimonials */
.card{
    background: var(--surface);
    border-radius: 18px;
    padding: 20px;
    box-shadow: var(--shadow);
    border: var(--border);
    height: 100%;
    transition: transform 0.3s ease;
}
.card:hover {
    transform: translateY(-5px);
}
.card h3, .card h4{ margin:0; color: var(--emerald-dark); }
.card p{ margin:10px 0 0 0; color: rgba(11,18,32,0.78); }
.accent-left{ border-left: 5px solid var(--emerald); }

/* Badges & Chips */
.badge{
    display:inline-block; padding: 8px 12px; margin: 6px 8px 0 0;
    border-radius: 999px; font-size: 0.92rem; font-weight: 800;
    border: 1px solid rgba(0,0,0,0.08); background: rgba(255,255,255,0.92);
}
.b-em{ background: rgba(15,118,110,0.10); border-color: rgba(15,118,110,0.25); color: var(--emerald-dark); }
.b-gd{ background: rgba(212,175,55,0.18); border-color: rgba(212,175,55,0.35); color: #8a6d1c; }
.chip{
    display:inline-block; padding: 10px 14px; border-radius: 14px;
    border: 1px solid rgba(0,0,0,0.08); background: rgba(255,255,255,0.90);
    margin-right: 10px; box-shadow: 0 8px 18px rgba(0,0,0,0.06);
}
.chip strong{ color: var(--emerald-dark); }

/* Custom Buttons */
.stButton>button {
    background: linear-gradient(135deg, var(--emerald), var(--emerald-dark)) !important;
    color:white !important; font-weight: 900 !important;
    border-radius: 14px !important; padding: 10px 24px !important;
    border: none !important; box-shadow: 0 10px 22px rgba(15,118,110,0.18) !important;
    transition: all 0.3s ease !important;
}
.stButton>button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 15px 25px rgba(15,118,110,0.25) !important;
}

/* Floating WhatsApp */
.whatsapp-float{
    position:fixed; bottom:20px; right:20px;
    background: #25D366; color:white; padding:14px 20px;
    border-radius:50px; font-weight:900; font-size: 16px;
    box-shadow:0 8px 25px rgba(37,211,102,0.4); text-decoration:none;
    z-index:999; transition: transform 0.3s ease;
}
.whatsapp-float:hover { transform: scale(1.1); color: white;}

/* Footer */
.footer{ margin-top: 50px; text-align: center; opacity:0.86; font-size:0.95rem; border-top: 1px solid var(--muted); padding-top: 20px;}
</style>
""", unsafe_allow_html=True)

phone = "923007354339"
base_wa_link = f"https://wa.me/{phone}?text="

# ===================== FLOATING WHATSAPP =====================
st.markdown(f'<a class="whatsapp-float" href="{base_wa_link}{urllib.parse.quote("Hello WriteWise Academic Help, I need your services.")}" target="_blank">💬 Chat on WhatsApp</a>', unsafe_allow_html=True)

# ===================== HEADER =====================
st.markdown("""
<div class="hero">
    <h1>✨ WriteWise Academic Help ✨</h1>
    <p><strong>Professional Academic Support & Research Enhancement Services</strong> • Worldwide / Remote</p>
    <p>Editing, proofreading, formatting, literature review structuring, and research methodology guidance.<br>Delivered with confidentiality and clear academic standards.</p>
</div>
""", unsafe_allow_html=True)

# ===================== MAIN TABS =====================
tab_home, tab_services, tab_quote, tab_faq = st.tabs([
    "🏠 Home", 
    "📌 Our Services", 
    "🧮 Instant Quote", 
    "❓ FAQs"
])

# ----------------- TAB 1: HOME -----------------
with tab_home:
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Specialists", "5+ Professionals")
    with m2: st.metric("Response Time", "≤ 24 hours")
    with m3: st.metric("Free Revisions", "14 days limit")
    with m4: st.metric("Client Satisfaction", "99.9%")

    st.write("---")
    st.subheader("🎓 Domains We Support")
    st.markdown("""
    <span class="badge b-em">Business Studies</span>
    <span class="badge b-gd">Social Sciences</span>
    <span class="badge b-em">Education</span>
    <span class="badge b-in">Law</span>
    <span class="badge b-gd">Accounting</span>
    <span class="badge b-em">Finance</span>
    <span class="badge b-gd">Research Methodology</span>
    """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("🌟 What You Get")
    a, b, c = st.columns(3)
    with a:
        st.markdown("""
        <div class="card accent-left">
            <h4>Clarity & Academic Tone</h4>
            <p>We polish language, flow, and academic readability so your work looks strictly professional.</p>
        </div>
        """, unsafe_allow_html=True)
    with b:
        st.markdown("""
        <div class="card accent-left">
            <h4>Formatting & Referencing</h4>
            <p>APA, MLA, Harvard, Chicago, Vancouver — clean structure and 100% consistent citations.</p>
        </div>
        """, unsafe_allow_html=True)
    with c:
        st.markdown("""
        <div class="card accent-left">
            <h4>Research Support</h4>
            <p>Methodology guidance, literature review structuring, and strong research presentation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("🗣️ Client Success Stories")
    t1, t2 = st.columns(2)
    with t1:
        st.info("**\"My thesis got approved without any major formatting revisions! The referencing was flawless. Highly recommended!\"**\n\n— *Sarah, Master's Student (Social Sciences)*")
    with t2:
        st.info("**\"WriteWise transformed my rough draft into a highly professional research paper. Their turnaround time is impressive.\"**\n\n— *Ali, PhD Candidate (Business Studies)*")

# ----------------- TAB 2: SERVICES -----------------
with tab_services:
    st.subheader("📌 Detailed Breakdown of Our Services")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h4>📝 Proofreading & Editing</h4>
            <p>Fixing grammatical errors, typos, punctuation, and improving sentence flow. We ensure your academic tone remains consistent throughout the document.</p>
        </div>
        <br>
        <div class="card">
            <h4>📚 Literature Review Structuring</h4>
            <p>Organizing your sources logically, identifying gaps in research, and creating a cohesive narrative for your literature review chapter.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <h4>📑 Formatting & Citations</h4>
            <p>Strict adherence to your university's guidelines. We expertly handle in-text citations and bibliographies in APA, Harvard, MLA, and more.</p>
        </div>
        <br>
        <div class="card">
            <h4>📊 Research Methodology</h4>
            <p>Guidance on selecting the right qualitative or quantitative approach, justifying your methods, and structuring the methodology chapter effectively.</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------- TAB 3: INSTANT QUOTE -----------------
with tab_quote:
    st.subheader("🧮 Calculate Your Custom Quote instantly")
    st.write("Fill in your requirements below to get an estimated price and generate a direct WhatsApp request.")
    
    # Simple Pricing Logic (You can change these rates)
    RATES = {
        "Proofreading & Editing": 1.5, # PKR per word
        "Formatting & Citations": 1.0,
        "Full Structural Review": 2.5,
        "Methodology Guidance": 3.0
    }
    URGENCY_MULTIPLIER = {
        "Normal (7 Days)": 1.0,
        "Urgent (3 Days)": 1.5,
        "Express (24 Hours)": 2.0
    }

    q1, q2 = st.columns([2, 1])
    
    with q1:
        with st.container():
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            word_count = st.number_input("Total Word Count:", min_value=100, max_value=100000, step=100, value=1000)
            service_type = st.selectbox("Select Service Type:", list(RATES.keys()))
            urgency = st.select_slider("Select Turnaround Time:", options=list(URGENCY_MULTIPLIER.keys()))
            st.markdown("</div>", unsafe_allow_html=True)

    with q2:
        # Calculate Price
        base_price = word_count * RATES[service_type]
        final_price = base_price * URGENCY_MULTIPLIER[urgency]
        
        st.markdown(f"""
        <div class="card" style="text-align: center; border: 2px solid var(--emerald);">
            <h3 style="color: var(--muted);">Estimated Quote</h3>
            <h1 style="color: var(--emerald); font-size: 2.5rem; margin: 10px 0;">PKR {final_price:,.0f}</h1>
            <p><strong>Service:</strong> {service_type}</p>
            <p><strong>Words:</strong> {word_count}</p>
            <p><strong>Timeline:</strong> {urgency}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        # Auto-generate WhatsApp message with quote details
        quote_msg = f"Hello WriteWise! I need a service.\n\n*Details:*\n- Service: {service_type}\n- Words: {word_count}\n- Urgency: {urgency}\n- Estimated Price: PKR {final_price:,.0f}\n\nPlease let me know how we can proceed."
        wa_quote_link = base_wa_link + urllib.parse.quote(quote_msg)
        
        st.link_button("🚀 Send Request on WhatsApp", wa_quote_link, use_container_width=True)

# ----------------- TAB 4: FAQs -----------------
with tab_faq:
    st.subheader("❓ Frequently Asked Questions")
    
    with st.expander("Is my document kept confidential?"):
        st.write("Absolutely! We strictly adhere to privacy standards. Your files and personal information are never shared with third parties and are deleted from our servers after the project is completed and approved.")
        
    with st.expander("Do you write essays or dissertations from scratch?"):
        st.write("No. WriteWise Academic Help provides ethical academic support. We offer editing, proofreading, structural guidance, and formatting. We do not offer 'ghostwriting' services as it violates university academic integrity policies.")
        
    with st.expander("What happens if I need revisions?"):
        st.write("We offer free revisions within 14 days of delivery, provided the revision request falls within the original instructions and scope of work agreed upon in the quote.")
        
    with st.expander("How do I make the payment?"):
        st.write("Once we finalize your custom quote on WhatsApp, we will provide you with our secure local payment details (Bank Transfer, EasyPaisa, JazzCash, etc.). Work begins once the payment or initial deposit is confirmed.")

# ===================== FOOTER =====================
st.markdown("""
<div class="footer">
    <strong>WriteWise Academic Help</strong> • WhatsApp: <strong>+92 300 7354339</strong><br>
    Worldwide / Remote Services • Ethical Academic Support • Guaranteed Quality
</div>
""", unsafe_allow_html=True)
