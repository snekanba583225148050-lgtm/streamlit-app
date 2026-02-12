import hashlib
from sklearn.ensemble import IsolationForest
import numpy as np

# Calculate firmware hash
def calculate_hash(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

# Train AI model on normal power
normal_data = np.random.normal(50, 2, 1000).reshape(-1,1)
model = IsolationForest(contamination=0.05)
model.fit(normal_data)

def check_power_anomaly(power_data):
    prediction = model.predict(power_data.reshape(-1,1))
    return -1 in prediction

def check_network(network):
    if network != "Trusted Server":
        return True
    return False
