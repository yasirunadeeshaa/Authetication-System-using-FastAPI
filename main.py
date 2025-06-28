from fastapi import FastAPI
from routes import router
from database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Manager API with MySQL")
app.include_router(router)

