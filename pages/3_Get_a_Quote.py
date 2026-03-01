import streamlit as st
from datetime import date, timedelta
import urllib.parse

st.set_page_config(page_title="Get a Quote | WriteWise", layout="wide")

st.title("Get a Quote")
st.caption("Custom quote only • Worldwide / Remote Services • Response within 24 hours • Free revisions (14 days)")

# Prefill writer if selected on Team page
requested_writer = st.session_state.get("requested_writer", "No preference")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Tell us what you need")

    with st.form("quote_form", clear_on_submit=False):
        full_name = st.text_input("Full name *")
        email = st.text_input("Email *")
        whatsapp = st.text_input("WhatsApp number *")

        domain = st.selectbox(
            "Domain *",
            [
                "Business Studies",
                "Social Sciences",
                "Education",
                "Law",
                "Accounting",
                "Finance",
                "Research Methodology / Technical Writing",
                "Other",
            ],
        )

        services = st.multiselect(
            "Service required *",
            [
                "Assignment Review & Editing",
                "Thesis & Dissertation Editing",
                "Research Proposal Support",
                "Literature Review Structuring",
                "Research Methodology Guidance",
                "Editing & Proofreading",
                "Formatting & Referencing",
                "Similarity Reduction (Ethical)",
                "Turnitin Similarity Check (Add-on)",
            ],
        )

        urgency = st.selectbox("Urgency *", ["Normal (7 days)", "Urgent (3 days)", "Express (24 hours)"])

        # Suggest a deadline based on urgency
        suggested_deadline = date.today() + timedelta(days=7)
        if "Urgent" in urgency:
            suggested_deadline = date.today() + timedelta(days=3)
        if "Express" in urgency:
            suggested_deadline = date.today() + timedelta(days=1)

        deadline = st.date_input("Deadline date *", value=suggested_deadline)
        words_pages = st.text_input("Word count / Pages *", placeholder="e.g., 1500 words or 6 pages")
        referencing = st.selectbox("Referencing style *", ["APA", "MLA", "Harvard", "Chicago", "Vancouver", "Other"])
        instructions = st.text_area("Instructions *", height=180, placeholder="Share topic, rubric, requirements, and any notes.")

        file = st.file_uploader("Upload file (optional) — PDF/DOC/DOCX", type=["pdf", "doc", "docx"])

        writer = st.selectbox("Request a writer (optional)", [requested_writer] + [
            "No preference",
            "Zaheer Abbas",
            "Mazhar Abbas",
            "Muhammad Imran",
            "Muhammad Ahmad",
            "Fahad Ali",
        ])

        submitted = st.form_submit_button("Submit for Quote")

    if submitted:
        # Basic validation
        missing = []
        if not full_name.strip(): missing.append("Full name")
        if not email.strip(): missing.append("Email")
        if not whatsapp.strip(): missing.append("WhatsApp")
        if not services: missing.append("Service required")
        if not words_pages.strip(): missing.append("Word count / Pages")
        if not instructions.strip(): missing.append("Instructions")

        if missing:
            st.error("Please fill required fields: " + ", ".join(missing))
        else:
            st.success("Submitted ✅ (Next step: we will connect within 24 hours.)")

            # Save in session (later we’ll send email + Google Sheets)
            st.session_state["latest_quote"] = {
                "full_name": full_name,
                "email": email,
                "whatsapp": whatsapp,
                "domain": domain,
                "services": services,
                "urgency": urgency,
                "deadline": str(deadline),
                "words_pages": words_pages,
                "referencing": referencing,
                "writer": writer,
                "instructions": instructions,
                "has_file": bool(file),
            }

            st.info("For fastest response, message us on WhatsApp using the button on the right →")

with col2:
    st.subheader("WhatsApp (Fast Response)")
    phone = "923007354339"
    default_msg = "Hello WriteWise Academic Help, I need a quote. Here are my details:"
    wa_link = "https://wa.me/" + phone + "?text=" + urllib.parse.quote(default_msg)

    st.link_button("WhatsApp Now: +92 300 7354339", wa_link)

    st.divider()
    st.subheader("What happens next?")
    st.write("1) We review your requirements")
    st.write("2) We confirm scope + timeline")
    st.write("3) You receive a custom quote")
    st.write("4) Delivery + free revisions (14 days)")

    st.divider()
    st.caption("Note: We provide academic support, editing, formatting, and research enhancement services.")