import hashlib
import numpy as np
from sklearn.ensemble import IsolationForest

# 1️⃣ Firmware Hash
def calculate_hash(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

# 2️⃣ Train Anomaly Model
def train_model(power_data):
    power_data = np.array(power_data).reshape(-1, 1)
    model = IsolationForest(contamination=0.1)
    model.fit(power_data)
    return model

# 3️⃣ Get Threat Score
def get_threat_score(model, power_data):
    power_data = np.array(power_data).reshape(-1, 1)
    scores = model.decision_function(power_data)

    # Convert to 0–100 scale
    threat_score = int((1 - np.mean(scores)) * 100)
    threat_score = max(0, min(100, threat_score))

    return threat_score
