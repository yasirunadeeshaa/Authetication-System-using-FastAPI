# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to FastAPI!"}

# @app.get("/hello/{name}")
# def say_hello(name: str):
#     return {"message": f"Hello, {name}!"}


from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="User Manager API",
    version="1.0.0"
)

app.include_router(router)
