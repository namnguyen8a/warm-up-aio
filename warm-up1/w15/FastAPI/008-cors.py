from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "https://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}


"""
Luồng hoạt động CORS:
1. Trình duyệt gửi request kèm Origin header (VD: http://localhost:8080).
2. Middleware kiểm tra Origin có trong danh sách allow_origins không.
3. Nếu hợp lệ, thêm các header CORS vào response (cho phép truy cập).
4. Nếu không hợp lệ, trình duyệt chặn request dù server có phản hồi.
"""