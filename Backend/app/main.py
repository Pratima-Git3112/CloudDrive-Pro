from fastapi import FastAPI

from app.config.settings import APP_NAME, APP_VERSION
from app.database.database import Base, engine
from app.models.user import User
from app.routes.users import router as user_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Secure Cloud File Storage Platform"
)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {APP_NAME}",
        "status": "Running Successfully"
    }


# Register Routes
app.include_router(user_router)