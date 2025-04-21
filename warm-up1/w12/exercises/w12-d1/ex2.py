'''
Bài 2: So sánh 2 hàm số trên cùng một biểu đồ
Yêu cầu: Chọn hai hàm số bất kỳ trong số: sin, cos, exp, log, và vẽ chúng trên cùng một
biểu đồ.

'''

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Biểu đồ của sin, cos")

# Create x values
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Create y values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create plot
fig, ax = plt.subplots()
ax.plot(x, y_sin, label='sin(x)', color='blue')
ax.plot(x, y_cos, label='cos(x)', color='red')

# Add grid, legend, and labels
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True)
ax.legend()
ax.set_title("Đồ thị của sin(x), cos(x)")
ax.set_xlabel("X")
ax.set_ylabel("Giá trị hàm số")

# Show plot in streamlit
st.pyplot(fig)