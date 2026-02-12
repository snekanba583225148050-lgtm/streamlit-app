import numpy as np
import time
import random

def generate_power_data(normal=True):
    if normal:
        return np.random.normal(50, 2, 100)
    else:
        return np.random.normal(70, 8, 100)

def generate_network_activity(normal=True):
    if normal:
        return "Trusted Server"
    else:
        return "Unknown External IP"

def simulate_device(trojan_active=False):
    power = generate_power_data(normal=not trojan_active)
    network = generate_network_activity(normal=not trojan_active)
    return power, network
