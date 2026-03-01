import streamlit as st

st.set_page_config(page_title="Reviews & FAQ | WriteWise", layout="wide")

st.title("Reviews & FAQ")
st.caption("Trusted by clients worldwide • Response within 24 hours • Free revisions (14 days)")

st.subheader("Client Reviews")

reviews = [
    {"who": "Client (Business Studies)", "text": "Very professional editing and formatting. My document became much clearer and well-structured."},
    {"who": "Client (Education)", "text": "They improved my literature review flow and fixed referencing issues. Delivery was on time."},
    {"who": "Client (Law)", "text": "Good academic tone and strong structure. The final draft looked professional and consistent."},
    {"who": "Client (Finance)", "text": "Formatting and presentation improved a lot. Clear headings, clean referencing, and better readability."},
    {"who": "Client (Social Sciences)", "text": "They helped organize my arguments and improved clarity without changing my meaning."},
    {"who": "Client (Research Methodology)", "text": "Methodology section became more logical and easier to understand. Very helpful support."},
]

cols = st.columns(2)
for i, r in enumerate(reviews):
    with cols[i % 2]:
        st.markdown(f"**{r['who']}**")
        st.write(f"“{r['text']}”")
        st.divider()

st.subheader("FAQ")

faq = [
    ("How do I get a quote?", "Submit details on the Get a Quote page or message us on WhatsApp. We respond within 24 hours."),
    ("Do you support all referencing styles?", "Yes. APA, MLA, Harvard, Chicago, Vancouver, and others upon request."),
    ("Do you offer revisions?", "Yes. Free revisions within 14 days (same scope/instructions)."),
    ("Can I request a specific writer?", "Yes. Go to the Team page and click “Request”. It will be selected in your quote form."),
    ("Is my information confidential?", "Yes. Your files and details are handled privately."),
    ("Do you provide academic integrity support?", "Yes. We focus on editing, formatting, coaching, and research enhancement services."),
]

for q, a in faq:
    with st.expander(q):
        st.write(a)