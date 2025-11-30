from fastapi import FastAPI
from src.routers import beat, mastering, monitoring

app = FastAPI(title="DevOps Audio Distribution")

app.include_router(beat.router, prefix="/beat")
app.include_router(mastering.router, prefix="/mastering")
app.include_router(monitoring.router, prefix="/monitoring")
