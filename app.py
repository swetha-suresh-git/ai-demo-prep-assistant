import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Freshdesk Demo Prep Assistant")

st.title("🚀 Freshdesk Demo Prep Assistant")

meeting_notes = st.text_area(
    "Paste Discovery Notes",
    height=300
)

if st.button("Generate Demo Prep"):

    if meeting_notes:

        with st.spinner("Analyzing discovery notes..."):

            prompt = f"""
You are a Senior Solutions Engineer at Freshworks.

Analyze the following discovery notes and prepare for a Freshdesk demo.

Discovery Notes:
{meeting_notes}

Generate:

1. Executive Summary
2. Customer Challenges
3. Business Goals
4. Stakeholders Mentioned
5. Demo Agenda tailored to this customer
6. Freshdesk Features to Highlight
7. Suggested Demo Flow
8. Discovery Gaps / Follow-up Questions
9. Potential Risks or Objections
10. Follow-up Email

Be specific to Freshdesk.
Avoid generic recommendations.
Format clearly using markdown.
"""

            response = model.generate_content(prompt)

            st.markdown(response.text)

    else:
        st.warning("Please paste discovery notes.")
