import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# 1. Tải file CSV và hiển thị dữ liệu
st.title("Phân tích dữ liệu từ file CSV")

uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dữ liệu ban đầu")
    st.dataframe(df.head())
    st.write("Số dòng", df.shape[0])
    st.write("Số cột", df.shape[1])

# 2. Thống kê mô tả dữ liệu
    st.subheader("Thông tin mô tả dữ liệu")
    st.write("Các thống kê cơ bản")
    st.dataframe(df.describe())
    st.write("Kiểu dữ liệu:")
    st.write(df.dtypes)
    st.write("Số giá trị thiếu:")
    st.write(df.isnull().sum())

# 3. Phân tích EDA bằng PygWalker
    st.subheader("Phân tích dữ liệu tương tác với PygWalker")
    pyg_html = pyg.to_html(df)

    # pyg_html = pyg.walk(df, return_html=True)
    # Wrap with a div that sets width
    # styled_html = f"""
    # <div style="width: 100%; overflow-x: auto;">
    #     <div style="min-width: 1200px;">
    #         {pyg_html}
    #     </div>
    # </div>
    # """

    components.html(pyg_html, height=1000, scrolling=True)

# 4. Gợi ý mở rộng
# • Cho phép người dùng chọn cột để lọc hoặc phân tích cụ thể.
# • Vẽ biểu đồ tương quan giữa các cột số bằng Seaborn.
# • Cho phép người dùng tải dữ liệu đã lọc về dưới dạng CSV.

else: 
    st.info("Vui lòng tải lên file CSV để bắt đầu khám phá dữ liệu.")
