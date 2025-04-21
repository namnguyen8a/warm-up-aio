'''
Bài 1: Vẽ đồ thị hàm số cơ bản
Yêu cầu: Chọn 1 trong các hàm số sin, cos, exp, log và vẽ biểu đồ trên đoạn [−10, 10].

'''

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Biểu đồ của sin")

# Create x values
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Create y values
y_sin = np.sin(x)

# Create plot
fig, ax = plt.subplots()
ax.plot(x, y_sin, label='sin(x)', color='blue')

# Limit between -10 -> 10
ax.set_xlim(-10, 10)

# Add grid, legend, and labels
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True)
ax.legend()
ax.set_title("Đồ thị của sin(x) trong khoảng [-10, 10]")
ax.set_xlabel("x")
ax.set_ylabel("Giá trị hàm số")

# Show plot in Streamlit
st.pyplot(fig)