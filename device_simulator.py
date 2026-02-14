import numpy as np
import random

def simulate_device(trojan_active=False):
    power_usage = []
    network_activity = []

    for i in range(100):
        # Normal behaviour
        power = np.random.normal(500, 20)
        network = np.random.normal(50, 5)

        # If trojan is active, create abnormal spikes
        if trojan_active and random.random() > 0.7:
            power += random.randint(150, 300)
            network += random.randint(30, 80)

        power_usage.append(power)
        network_activity.append(network)

    return power_usage, network_activity
