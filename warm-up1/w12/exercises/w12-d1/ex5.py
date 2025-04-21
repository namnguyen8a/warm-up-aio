'''
Bài 5: Vẽ Heatmap cho hàm z = x^2 + y^2
Yêu cầu: Dùng sns.heatmap để vẽ biểu đồ nhiệt của hàm z = x^2 + y^2
'''

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.markdown("Biểu đồ nhiệt của hàm z = $x^2$ + $y^2$")

# Define grid range and resolution
x = np.linspace(-10.0, 10.0, 100)
y = np.linspace(-10.0, 10.0, 100)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

# Create heatmap using seaborn
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(Z, cmap='viridis', ax=ax, cbar=True)

ax.set_title("Heatmap of $x^2$ + $y^2$")

st.pyplot(fig)