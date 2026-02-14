import streamlit as st
import matplotlib.pyplot as plt
from device_simulator import simulate_device
from detector import calculate_hash, train_model, get_threat_score

st.set_page_config(layout="wide")

st.title("⚡ GridGuard AI – Power Device Protection")

# Sidebar
trojan = st.sidebar.checkbox("Activate Hidden Trojan")

# Simulate Device
power, network = simulate_device(trojan_active=trojan)

# Train model
model = train_model(power)

# Threat Score
threat_score = get_threat_score(model, power)

# Firmware Hash Check
current_hash = calculate_hash("firmware.bin")

st.subheader("🔐 Firmware Hash")
st.code(current_hash)

# Threat Meter
st.subheader("🚨 Threat Score")

st.progress(threat_score)

if threat_score < 30:
    st.success(f"🟢 Safe – {threat_score}% Risk")
elif threat_score < 70:
    st.warning(f"🟡 Suspicious – {threat_score}% Risk")
else:
    st.error(f"🔴 Critical Threat – {threat_score}% Risk")

# Power Graph
st.subheader("📊 Power Usage Pattern")

fig, ax = plt.subplots()
ax.plot(power)
ax.set_title("Power Consumption Over Time")
st.pyplot(fig)

# Attack Timeline
st.subheader("🕒 Attack Timeline")

if trojan:
    st.write("10:02 – Device normal")
    st.write("10:05 – Power spike detected")
    st.write("10:07 – Abnormal behavior detected")
    st.write("10:08 – Threat score increased")
else:
    st.write("Device operating normally")
