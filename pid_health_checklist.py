import streamlit as st

st.set_page_config(page_title="PID Health Checklist", page_icon="⚡")

st.title("⚡ PID Health Checklist")
st.markdown("### Is your solar plant vulnerable to Potential Induced Degradation? Let’s find out!")

st.markdown("---")

score = 0

st.markdown("#### 1. What is your plant type?")
plant_type = st.radio(
    "Select one:",
    ("Rooftop (<20kW)", "Commercial (>20kW, <500kW)", "Utility-scale (>500kW)")
)
if plant_type == "Utility-scale (>500kW)":
    score += 2
elif plant_type == "Commercial (>20kW, <500kW)":
    score += 1

st.markdown("#### 2. What is your location type?")
location = st.radio(
    "Select one:",
    ("Dry (e.g. Rajasthan)", "Humid (e.g. Chennai, Kerala)", "Coastal (e.g. Mumbai, Vizag)")
)
if location == "Coastal (e.g. Mumbai, Vizag)":
    score += 3
elif location == "Humid (e.g. Chennai, Kerala)":
    score += 2

st.markdown("#### 3. Are your strings connected to inverters with transformerless topology?")
transformerless = st.radio("Select one:", ("Yes", "No", "Not sure"))
if transformerless == "Yes":
    score += 2

st.markdown("#### 4. Are your panels PID-resistant certified (as per IEC 62804)?")
pid_resistant = st.radio("Select one:", ("Yes", "No", "Not sure"))
if pid_resistant == "No":
    score += 2
elif pid_resistant == "Not sure":
    score += 1

st.markdown("#### 5. What is your system voltage?")
voltage = st.radio("Select one:", ("Below 600V", "600V – 1000V", "Above 1000V"))
if voltage == "600V – 1000V":
    score += 1
elif voltage == "Above 1000V":
    score += 2

st.markdown("#### 6. Do you clean your panels regularly (once every 15–30 days)?")
cleaning = st.radio("Select one:", ("Yes", "No"))
if cleaning == "No":
    score += 1

st.markdown("#### 7. Is your system grounded properly with periodic insulation resistance checks?")
grounding = st.radio("Select one:", ("Yes", "No", "Not sure"))
if grounding == "No":
    score += 2
elif grounding == "Not sure":
    score += 1

st.markdown("---")

# Result
if st.button("🔍 Check PID Risk Score"):
    st.markdown("## 🔎 Results")

    if score <= 3:
        st.success("✅ Low PID Risk – Your system is fairly safe. Keep up the good practices!")
    elif score <= 6:
        st.warning("⚠️ Medium PID Risk – Take preventive steps like grounding audit or using anti-PID devices.")
    else:
        st.error("❌ High PID Risk – Your plant is vulnerable. Consider immediate PID mitigation strategies!")

    st.markdown(f"**Your PID Risk Score:** `{score}/13`")
    st.markdown("To learn more about PID and its impact, [read this detailed story here](https://medium.com/@yourmediumprofile/pid-the-silent-killer-of-your-solar-dreams-...)")

