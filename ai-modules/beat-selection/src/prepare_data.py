# prepare_data.py
import pandas as pd
import os
from src.features import extract_features

def load_dataset(data_dir="data/train", annotations_file="data/annotations.csv"):
    """
    Charge les fichiers audio et leurs annotations.
    Retourne X (features) et y (labels).
    """
    annotations = pd.read_csv(annotations_file)
    X, y = [], []

    for _, row in annotations.iterrows():
        file_path = os.path.join(data_dir, row["filename"])
        with open(file_path, "rb") as f:
            audio_bytes = f.read()

        features = extract_features(audio_bytes)
        X.append(features)
        y.append(row["genre"])

    return X, y
