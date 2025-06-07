import streamlit as st

st.set_page_config(
    page_title="PID Health Checklist",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("⚡ PID Health Risk Checklist")
st.markdown("""
Use this checklist to evaluate if your solar PV system is at risk of **Potential Induced Degradation (PID)**.  
Answer the following questions honestly to get a quick PID health status for your plant.
""")

st.markdown("#### 1. What is the type of your solar plant?")
plant_type = st.radio("Select one:", (
    "Rooftop (<20kW)", 
    "Commercial (>20kW, <500kW)", 
    "Utility-scale (>500kW)"
), key="plant_type")

st.markdown("#### 2. What is your site's climate condition?")
location = st.radio("Select one:", (
    "Dry (e.g. Rajasthan)", 
    "Humid (e.g. Chennai, Kerala)", 
    "Coastal (e.g. Mumbai, Vizag)"
), key="location")

st.markdown("#### 3. Is your inverter transformerless?")
transformerless = st.radio("Select one:", (
    "Yes", "No", "Not sure"
), key="transformerless")

st.markdown("#### 4. Are your panels PID-resistant certified (as per IEC 62804)?")
pid_resistant = st.radio("Select one:", (
    "Yes", "No", "Not sure"
), key="pid_resistant")

st.markdown("#### 5. What is the maximum string/system voltage?")
voltage = st.radio("Select one:", (
    "Below 600V", 
    "600V – 1000V", 
    "Above 1000V"
), key="voltage")

st.markdown("#### 6. Do you perform regular module cleaning?")
cleaning = st.radio("Select one:", (
    "Yes", "No"
), key="cleaning")

st.markdown("#### 7. Are your modules properly grounded?")
grounding = st.radio("Select one:", (
    "Yes", "No", "Not sure"
), key="grounding")

# --- Scoring logic ---
score = 0

# 1. Plant Type
if plant_type == "Utility-scale (>500kW)":
    score += 2
elif plant_type == "Commercial (>20kW, <500kW)":
    score += 1

# 2. Location
if location == "Coastal (e.g. Mumbai, Vizag)":
    score += 2
elif location == "Humid (e.g. Chennai, Kerala)":
    score += 1

# 3. Transformerless Inverter
if transformerless == "Yes":
    score += 2
elif transformerless == "Not sure":
    score += 1

# 4. PID-resistant Panels
if pid_resistant == "No":
    score += 2
elif pid_resistant == "Not sure":
    score += 1

# 5. Voltage
if voltage == "Above 1000V":
    score += 2
elif voltage == "600V – 1000V":
    score += 1

# 6. Cleaning
if cleaning == "No":
    score += 1

# 7. Grounding
if grounding == "No":
    score += 2
elif grounding == "Not sure":
    score += 1

# --- Risk Level Output ---
st.markdown("---")
st.subheader("📋 PID Risk Assessment")

if score <= 3:
    st.success("✅ Low PID Risk: Your system appears well protected. Keep monitoring periodically.")
elif score <= 6:
    st.warning("⚠️ Medium PID Risk: Consider reviewing inverter type, module specs, and grounding.")
else:
    st.error("❌ High PID Risk: Immediate attention recommended! Review module certification, grounding, and inverter settings.")

st.markdown("""
---
🧠 *Note: This tool provides an indicative assessment. For an in-depth audit, consult a solar performance specialist or your EPC provider.*
""")
