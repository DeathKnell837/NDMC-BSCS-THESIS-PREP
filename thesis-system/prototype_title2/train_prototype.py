import json
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, MaxPooling1D, LSTM, Dense, Dropout

def load_data(directory):
    with open(os.path.join(directory, "url_dataset.json"), "r") as f:
        dataset = json.load(f)
    with open(os.path.join(directory, "char_map.json"), "r") as f:
        char_map = json.load(f)
    return dataset, char_map

def tokenize_url(url, char_map, max_len=150):
    seq = []
    for char in url.lower():
        if char in char_map:
            seq.append(char_map[char])
        else:
            seq.append(char_map.get("<UNK>", 0))
            
    if len(seq) > max_len:
        seq = seq[:max_len]
    else:
        seq = seq + [0] * (max_len - len(seq))
    return seq

def main():
    directory = "C:/Users/ADMIN/OneDrive/Desktop/THESIS/NDMC-BSCS-THESIS-PREP/prototype_title2"
    print("Loading prepared dataset...")
    dataset, char_map = load_data(directory)
    
    max_len = 150
    vocab_size = len(char_map) + 2
    
    X = np.array([tokenize_url(item["url"], char_map, max_len) for item in dataset])
    y = np.array([item["label"] for item in dataset])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
    print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")
    
    print("Compiling hybrid CNN-LSTM neural network...")
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=32, input_length=max_len),
        Conv1D(filters=64, kernel_size=3, padding="same", activation="relu"),
        MaxPooling1D(pool_size=2),
        Dropout(0.2),
        LSTM(64),
        Dropout(0.2),
        Dense(1, activation="sigmoid")
    ])
    
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    model.summary()
    
    print("Starting model training (5 epochs)...")
    history = model.fit(
        X_train, y_train,
        epochs=5,
        batch_size=32,
        validation_split=0.1,
        verbose=1
    )
    
    print("Evaluating model on test dataset...")
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")
    
    y_pred = (model.predict(X_test) > 0.5).astype(int)
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["Benign", "Phishing"]))
    
    model_save_path = os.path.join(directory, "phishing_prototype_model.h5")
    model.save(model_save_path)
    print(f"Trained model saved to: {model_save_path}")

if __name__ == '__main__':
    main()
