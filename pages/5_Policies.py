import streamlit as st

st.set_page_config(page_title="Policies | WriteWise", layout="wide")

st.title("Policies")
st.caption("Clear policies build trust • Worldwide / Remote Services")

tab1, tab2, tab3, tab4 = st.tabs(["Privacy Policy", "Terms of Service", "Refund Policy", "Academic Integrity"])

with tab1:
    st.subheader("Privacy Policy")
    st.write("""
We respect your privacy and handle your information confidentially.

**What we collect**
- Contact details you share (name, email, WhatsApp)
- Project information you provide (instructions, domain, urgency, deadline)
- Files you upload (optional)

**How we use it**
- To provide a quote and deliver services
- To communicate updates and clarify requirements

**Data protection**
- We do not sell or share your data with third parties for marketing.
- Uploaded files are used only for your requested service.

**Deletion request**
- You may request deletion of your data by contacting us.
""")

with tab2:
    st.subheader("Terms of Service")
    st.write("""
By using WriteWise Academic Help, you agree to the following:

**Scope of services**
- We provide academic support services such as editing, proofreading, formatting, referencing assistance,
  research methodology guidance, and document improvement.

**Timelines**
- Delivery timelines depend on scope and urgency selected (Normal / Urgent / Express).
- We confirm timelines after reviewing your requirements.

**Revisions**
- Free revisions are available within **14 days**, provided the original scope/instructions do not change.

**Communication**
- Clients must provide complete requirements to avoid delays.
""")

with tab3:
    st.subheader("Refund Policy")
    st.write("""
Refunds depend on the stage of work and the nature of the request.

**Possible refund situations**
- If work has not started and the project is cancelled early, a refund may be considered.
- If there is a major failure to follow confirmed requirements, we will attempt revisions first.

**Not eligible**
- Changes in requirements after confirmation
- Missed deadlines caused by incomplete or late client information

We aim for fairness and will review each request case-by-case.
""")

with tab4:
    st.subheader("Academic Integrity Statement")
    st.write("""
WriteWise Academic Help provides academic support services focused on improving clarity, structure,
formatting, referencing, and research presentation.

We encourage responsible academic practices and do not promote misuse of academic policies.
""")