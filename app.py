import streamlit as st

st.set_page_config(page_title="AI Demo Prep Assistant")

st.title("🚀 AI Demo Prep Assistant")

meeting_notes = st.text_area(
    "Paste customer discovery notes here",
    height=250
)

if st.button("Generate Demo Prep"):
    if meeting_notes:

        st.subheader("Demo Agenda")
        st.write("""
        - Introduction
        - Customer Goals Review
        - Product Demonstration
        - Use Case Discussion
        - Next Steps
        """)

        st.subheader("Discovery Questions")
        st.write("""
        - What is your biggest challenge today?
        - How are you solving this currently?
        - What does success look like?
        """)

        st.subheader("Follow-up Email")
        st.write(f"""
        Thank you for the discussion.

        Based on our conversation, we reviewed:
        {meeting_notes[:150]}...

        Looking forward to our next discussion.

        Best regards,
        Swetha
        """)

    else:
        st.warning("Please enter meeting notes.")