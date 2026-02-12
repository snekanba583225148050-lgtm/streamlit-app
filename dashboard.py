import streamlit as st
from device_simulator import simulate_device
from detector import calculate_hash, check_power_anomaly, check_network
import matplotlib.pyplot as plt

st.title("⚡ GridGuard AI – Power Device Protection")

trojan = st.checkbox("Activate Hidden Trojan")

power, network = simulate_device(trojan_active=trojan)

# Firmware check
current_hash = calculate_hash(r"C:\Users\welcome\OneDrive\Desktop\GridGuardAI\firmware.bin")
st.write("Firmware Hash:", current_hash)

# Power graph
st.subheader("Power Usage")
fig, ax = plt.subplots()
ax.plot(power)
st.pyplot(fig)

# Detection checks
power_alert = check_power_anomaly(power)
network_alert = check_network(network)

st.subheader("Device Status")

if power_alert or network_alert:
    st.error("🚨 Threat Detected!")
else:
    st.success("✅ Device Operating Normally")

st.write("Network Communication:", network)
import streamlit as st

st.title("My App")


