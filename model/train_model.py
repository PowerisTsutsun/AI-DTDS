import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from src.feature_extraction import extract_features

def train_model(log_file='data/raw/syslog_example.log'):
    data = []
    with open(log_file, 'r') as f:
        for line in f:
            features = extract_features(line)
            if features:
                data.append(features)
    
    df = pd.DataFrame(data)
    if df.empty:
        print("❌ No data found for training. Please check the log file.")
        return
    
    X = df
    
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/isolation_forest.pkl')
    print("✅ Model trained and saved to model/isolation_forest.pkl")

if __name__ == "__main__":
    train_model()
