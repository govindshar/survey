import streamlit as st

st.set_page_config(page_title="Pharmacist Full Scope Survey – Australia", layout="centered")

st.title("🩺 Full Scope Pharmacist Survey (Australia)")
st.markdown("As full scope pharmacy expands in Australia, we're exploring how AI-based phone tools can support pharmacists in remote and high-pressure environments. Your input will help shape future tools built for you.")

# 1️⃣ About You
st.header("1️⃣ About You")
name = st.text_input("Full Name (optional):")
email = st.text_input("Email (optional, for pilot invite):")
state = st.selectbox("State/Territory you practice in:", [
    "New South Wales", "Victoria", "Queensland", "Western Australia",
    "South Australia", "Tasmania", "ACT", "Northern Territory"
])
experience = st.radio("Years of experience as a pharmacist:", [
    "Less than 1 year", "1–3 years", "4–7 years", "8+ years"
])

# 2️⃣ Practice & Challenges
st.header("2️⃣ Current Practice & Challenges")
services = st.multiselect("Which full scope services do you currently deliver?", [
    "UTI management", "Oral contraceptive prescribing", "Minor ailments",
    "Vaccination", "Chronic disease management", "Medication review",
    "Opioid dependence treatment"
])
common_decisions = st.text_area("What are the most common clinical decisions you make daily?")
barriers = st.multiselect("What are your biggest day-to-day challenges?", [
    "Time pressure", "Internet dropout", "Lack of backup", "Uncertainty in guidelines",
    "Language barriers", "Admin load", "Other"
])
delayed_services = st.radio("Have you ever avoided or delayed a service due to lack of tools/support?", ["Yes", "No"])
delayed_reason = st.text_area("If yes, what was the reason?", disabled=(delayed_services != "Yes"))
confidence = st.slider("How confident do you feel delivering full scope services solo?", 1, 5, 3)

# 3️⃣ Communication & Support
st.header("3️⃣ Information & Support Access")
double_check = st.radio("Do you often feel the need to double-check clinical info during consults?", ["Yes", "No"])
current_support = st.multiselect("How do you currently seek support when unsure?", [
    "Ask a colleague", "Search online", "Refer to guidelines", "Call a GP", "I delay the service"
])
support_barriers = st.multiselect("What prevents you from accessing support reliably?", [
    "Poor internet", "No time", "Unclear resources", "Fear of being wrong", "Lack of access"
])
admin_time = st.radio("How much time do you spend daily on documentation/admin?", [
    "<30 min", "30–60 min", "1–2 hrs", ">2 hrs"
])
language_freq = st.radio("How often do you see patients who speak English as a second language?", [
    "Frequently", "Occasionally", "Rarely", "Never"
])

# 4️⃣ AI Assistant Usage
st.header("4️⃣ AI Assistant Use & Relevance")
use_cases = st.multiselect("If you had a phone-based AI assistant, what would you use it for?", [
    "Ask clinical questions", "Triage assistance", "Translate patient info",
    "Dictate and summarize notes", "I wouldn’t use it"
])
top_use_case = st.text_area("Describe your top 2–3 use cases for this tool:")
local_preference = st.radio("Would you prefer a local (offline) AI assistant over cloud-based tools?", [
    "Yes", "No", "Doesn't matter"
])
frequency = st.radio("How often do you think you'd use it?", [
    "Several times per day", "Once daily", "Few times per week", "Rarely", "Never"
])

# 5️⃣ Pilot Participation
st.header("5️⃣ Participation & Final Thoughts")
interested = st.radio("Would you be interested in piloting this tool?", ["Yes", "Maybe", "No"])
modes = st.multiselect("Preferred way to access this system:", [
    "Phone-based access", "Web-based chatbot", "Mobile app", "All of the above"
])
comments = st.text_area("Any other feedback, ideas, or concerns?")

# Submit
if st.button("Submit Survey"):
    st.success("✅ Thank you! Your responses have been recorded.")
    st.write("---")
    st.subheader("📋 Your Summary")
    st.json({
        "Name": name,
        "Email": email,
        "State": state,
        "Experience": experience,
        "Services": services,
        "Common Decisions": common_decisions,
        "Barriers": barriers,
        "Delayed Service": delayed_services,
        "Delay Reason": delayed_reason,
        "Confidence (1-5)": confidence,
        "Double Check Info?": double_check,
        "Current Support": current_support,
        "Support Barriers": support_barriers,
        "Admin Time": admin_time,
        "Language Frequency": language_freq,
        "AI Use Cases": use_cases,
        "Top Use Case Description": top_use_case,
        "Offline Preference": local_preference,
        "Use Frequency": frequency,
        "Pilot Interest": interested,
        "Preferred Modes": modes,
        "Final Comments": comments
    })
