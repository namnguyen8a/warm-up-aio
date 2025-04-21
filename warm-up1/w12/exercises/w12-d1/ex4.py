'''
Bài 4: Tương tác với Slider để khảo sát đồ thị
Yêu cầu: Dùng st.slider để điều chỉnh giá trị của a, b, c và cập nhật đồ thị theo thời
gian thực.
'''

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Biểu đồ của hàm y = ax^2 + bx + c")

# Input values for a, b, c
a = st.slider("Choose a", min_value=1.0, max_value=10.0, value=1.0)
b = st.slider("Choose b", min_value=1.0, max_value=10.0, value=1.0)
c = st.slider("Choose c", min_value=1.0, max_value=10.0, value=1.0)

# Create x values
x = np.linspace(-5, 5, 100)

# Create y values
y = float(a)*x**2 + float(b)*x + float(c)

# Create plot
fig, ax = plt.subplots()
ax.plot(x, y, label=f'{a}x^2 + {b}x + {c}', color='blue')

# Add grid, legend, and labels
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True)
ax.legend()
ax.set_title(f"Đồ thị của phương trình {a}x^2 + {b}x + {c}")
ax.set_xlabel("x")
ax.set_ylabel(f"{a}x^2 + {b}x + {c}")

# Show plot in Streamlit
st.pyplot(fig)