import streamlit as st

# Page configuration
st.set_page_config(page_title="Marlene – AI Landscape Call Agent", layout="centered")

# App Title
st.title("📞 Meet Marlene – Your AI Call Answering Assistant")
st.caption("For Testing Landscape – Serving Manatee & Sarasota County, FL")

# About Marlene
st.subheader("🌿 Who is Marlene?")
st.markdown("""
Marlene is a voice-based AI call handler built to answer every incoming call for **Testing Landscape**, a lawn and landscaping business in **Manatee and Sarasota County, Florida**.

She’s not just a bot — she’s the friendly, efficient front-line voice that schedules estimates, confirms key details, and ensures every lead is properly captured and followed up.
""")

# Role Summary
st.subheader("🎯 Core Responsibilities")
st.markdown("""
- 📞 Answer incoming calls in under 3 seconds  
- 📅 Book in-person estimates into GoHighLevel  
- 📍 Confirm service area eligibility  
- 🔁 Reduce no-shows by double-confirming call details  
- 💬 Log call transcripts and escalate when needed
""")

# Tone and Voice
st.subheader("🗣️ Marlene’s Personality")
st.markdown("""
Marlene is designed to be:

- **Warm**: Friendly and welcoming like a local neighbor  
- **Professional**: Speaks clearly, respectfully, and confidently  
- **Efficient**: Keeps calls moving with smooth transitions  
- **Localized**: Familiar with areas like Bradenton, Lakewood Ranch, Parrish, and Venice
""")

# GHL Integration
st.subheader("🔗 Connected to GoHighLevel")
st.markdown("""
Marlene is fully integrated with the client's **GHL sub-account**, enabling:

- Calendar syncing for real-time estimate scheduling  
- Contact creation and tagging  
- SMS confirmations and reminders  
- Call transcription and missed-call workflows  
""")

# Sample Call Script
st.subheader("📋 Sample Call Flow")

with st.expander("1. Greeting"):
    st.code("“Thank you for calling Testing Landscape, this is Marlene! How can I help you beautify your lawn today?”")

with st.expander("2. Confirm Address & Location"):
    st.code("“May I get the address for the property you’d like serviced?”\n“Is that in Manatee or Sarasota County?”")

with st.expander("3. Book the Estimate"):
    st.code("“We have openings on Wednesday at 10 AM or Thursday at 2 PM. What works best for you?”")

with st.expander("4. Confirm Details"):
    st.code("“To confirm—we’ll meet you at [ADDRESS] on [DATE] at [TIME]. Will you be available?”\n“Is there a gate code or any access instructions?”")

with st.expander("5. Send Confirmation"):
    st.code("“Awesome! You’re all set. We’ll send you a text confirmation shortly. Thanks again for calling Testing Landscape!”")

# QA + Final Note
st.subheader("📈 Improving Marlene")
st.markdown("""
Every call is logged with transcripts and outcomes so that the team can:

- Identify confusion points  
- Improve her training prompts  
- Escalate leads needing human follow-up  
""")

st.success("Marlene is helping Testing Landscape never miss a lead again.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit by [YourName or Company]")
