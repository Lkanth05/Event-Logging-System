from fastapi import FastAPI
from .routes import router
#from fastapi.staticfiles import StaticFiles
#from app.database import event_logs_collection

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to the Event Logging System!"}

# Include the API routes
app.include_router(router, prefix="/api", tags=["Event Logs"])



