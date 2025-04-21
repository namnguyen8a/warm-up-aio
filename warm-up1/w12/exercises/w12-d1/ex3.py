'''
Bài 3: Vẽ đồ thị hàm bậc 2
Yêu cầu: Nhập hệ số a, b, c cho phương trình y = ax2 + bx + c và vẽ đồ thị tương ứng.
'''

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Biểu đồ của hàm y = ax^2 + bx + c")

# Input values for a, b, c
a = st.text_input("Enter a:", value=1.0)  # Default is "1"
b = st.text_input("Enter b:", value=1.0)
c = st.text_input("Enter c:", value=1.0)

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