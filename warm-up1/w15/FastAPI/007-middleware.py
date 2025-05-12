import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Middleware đo thời gian xử lý
@app.middleware("http")
async def timer_middleware(request: Request, call_next):
    start_time = time.time() # Bắt đầu đo thời gian

    response = await call_next(request) # Gọi trực tiếp sang route handler

    process_time = time.time() - start_time # Đo thời gian sau khi xử lý xong
    response.headers["X-Process-Time"] = str(process_time) # Gắn vào header response

    return response

# route mẫu
@app.get("/hello")
async def hello():
    return {"message": "Hello, FastAPI!"}

"""

User → /hello
|
| (1) Middleware được gọi đầu tiên
|     timer_middleware() ghi lại thời gian bắt đầu
|
| (2) Gọi call_next(request)
|     → chuyển quyền xử lý sang route handler: hello()
|
| (3) Route handler trả lại response {"message": "Hello, FastAPI!"}
|
| (4) Quay lại middleware
|     → đo thời gian xử lý, gắn vào response header "X-Process-Time"
|
| (5) Trả response về cho người dùng

"""