import streamlit as st

# App Title
st.set_page_config(page_title="Marlene - AI Landscape Scheduling Agent", layout="centered")
st.title("📞 Meet Marlene – Your Virtual Scheduling Assistant")

# Intro
st.markdown("""
**Marlene** is a warm, professional AI call handler for **Testing Landscape**, a lawn and landscaping company serving **Manatee and Sarasota County, Florida**.

She’s designed to:
- Answer incoming calls quickly
- Schedule in-person estimates
- Confirm critical details to avoid no-shows
- Speak with a friendly, local tone

---  
""")

# Agent Summary
st.subheader("🌿 Agent Overview")
st.markdown("""
- **Name:** Marlene  
- **Role:** AI Call Handler & Scheduling Assistant  
- **Company:** Testing Landscape  
- **Service Area:** Manatee & Sarasota County, FL  
- **Goal:** Book estimates fast. Reduce missed appointments. Deliver amazing first impressions.
""")

# Tone and Personality
st.subheader("🗣️ Tone & Personality")
st.markdown("""
- **Warm:** Like a trusted neighbor with a smile you can hear  
- **Professional:** Courteous, clear, and competent  
- **Efficient:** Gets the job done without wasting time  
- **Localized:** Knows Bradenton, Lakewood Ranch, Venice, and more
""")

# Sample Call Flow
st.subheader("📋 Sample Call Script")

with st.expander("1. Greeting"):
    st.text('"Thank you for calling Testing Landscape, this is Marlene! How can I help you beautify your lawn today?"')

with st.expander("2. Get Info & Confirm Location"):
    st.text('“May I get your name and the address of the property you’re calling about?”')
    st.text('“Is this in Sarasota or Manatee County?”')

with st.expander("3. Schedule Estimate"):
    st.text('“We have availability this week on Wednesday at 10 AM or Thursday at 2 PM. Which works best for you?”')

with st.expander("4. Confirm Details"):
    st.text('“Just to confirm, we’re meeting at [address] on [date] at [time]. Will you be there personally?”')
    st.text('“Is there a good number to reach you just in case?”')

with st.expander("5. Close Call"):
    st.text('“You’re all set. We look forward to helping you make your lawn amazing. Have a great day!”')

# Footer
st.markdown("---")
st.info("Marlene is the first line of contact for Testing Landscape—designed to book more jobs while making customers feel taken care of.")

