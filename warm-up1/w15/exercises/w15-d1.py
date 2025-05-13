from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#  Bài 1. Hello API: Tạo một route GET trả về chuỗi "Xin chào từ FastAPI!" tại /hello.

@app.get("/hello/")
async def get_hello():
    return {"message": "Xin chào từ FastAPI"}

# API Máy tính: Tạo 4 route GET như sau:
# • /add?a=5&b=3 → trả về 8
# • /subtract?a=10&b=7 → trả về 3
# • /multiply?a=4&b=2 → trả về 8
# • /divide?a=8&b=2 → trả về 4 (xử lý chia cho 0)

@app.get("/math-operations/add")
async def add(a: float, b: float):
    res = a + b
    return {"result": res}

@app.get("/math-operations/subtract")
async def subtract(a: float, b: float):
    res = a - b
    return {"result": res}

@app.get("/math-operations/multiply")
async def multiply(a: float, b: float):
    res = a * b
    return {"result": res}

@app.get("/math-operations/divide")
async def divide(a: float, b: float):
    if b != 0:
        res = a / b
        return {"result": res}
    else:
        return {"message": "b must be different from 0"}

# Bài 3. API Thông tin người dùng: Tạo một API POST /user nhận dữ liệu JSON gồm:
# • name (str)
# • age (int)
# • email (str)
# Và trả về: is_adult = True nếu tuổi ≥ 18.

class User(BaseModel):
    name: str
    age: int
    email: str | None = None

@app.post("/user-management/add_user")
async def add_user(user: User):
    is_adult = False
    if user.age >= 18:
        is_adult = True
        return {"message": is_adult}
    else:
        return {"message": is_adult}
    
# Bài 4. Quản lý danh sách sản phẩm:
# • GET /products trả về danh sách sản phẩm
# • POST /products thêm sản phẩm vào danh sách (lưu tạm bằng list)

fake_db = [
    {"product_id": 0, "product_name": "Banh dau xanh", "expired_date": "20/5/24"},
    {"product_id": 1, "product_name": "Banh hat de", "expired_date": "21/5/25"},
]

@app.get("/products")
async def get_products():
    return fake_db

class Product(BaseModel):
    product_id: int
    product_name: str
    expired_date: str

@app.post("/products")
async def add_products(product: Product):
    product.product_id = len(fake_db)
    fake_db.append(product)
    return {"message": "Adding product successful!"}