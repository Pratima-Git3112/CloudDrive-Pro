from fastapi import FastAPI

app = FastAPI(
    title="CloudDrive Pro API",
    description="Secure Cloud File Storage Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CloudDrive Pro",
        "status": "Running Successfully"
    }