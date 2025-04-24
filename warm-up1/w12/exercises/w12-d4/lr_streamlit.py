import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Đọc dữ liệu từ CSV
df = pd.read_csv("data/advertising.csv")
X = df[["TV", "Radio", "Newspaper"]].values
y = df["Sales"].values.reshape(-1, 1)

# Chuẩn hóa dữ liệu
X = (X - X.mean(axis=0)) / X.std(axis=0)

# Hàm huấn luyện Linear Regression
def train_linear_regression(X, y, lr=0.01, epochs=100):
    n_samples, n_features = X.shape
    w = np.zeros((n_features, 1))
    b = 0
    losses = []

    for _ in range(epochs):
        y_pred = np.dot(X, w) + b
        
        loss = (1/n_samples) * np.sum((y_pred-y)**2)
        losses.append(loss)


        dw = (2/n_samples)*np.dot(X.T, (y_pred-y))
        db = (2/n_samples)*np.sum(y_pred-y)

        w -= lr*dw
        b -= lr*db

    return w, b, losses

st.title("Huấn luyện Linear Regression với Numpy")

lr = st.slider("Learning rate", 0.001, 0.1, 0.01)
epochs = st.slider("Số epoch", 10, 1000, 200)

if st.button("Train model"):
    w, b, loss_history = train_linear_regression(X, y, lr, epochs)

    st.subheader("Loss theo epoch")
    fig, ax = plt.subplots()
    ax.plot(loss_history)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("MSE Loss")
    st.pyplot(fig)

    st.write("Trọng số cuối cùng (w)", w.flatten())
    st.write("Bias (b):", b)
    st.write("Loss: ", loss_history[-1])