from fastapi import FastAPI
from src.routers import beat, mastering, monitoring

app = FastAPI(title="DevOps Audio Distribution")

# Inclusion des routes spécialisées
app.include_router(beat.router, prefix="/beat", tags=["Beat"])
app.include_router(mastering.router, prefix="/mastering", tags=["Mastering"])
app.include_router(monitoring.router, prefix="/monitoring", tags=["Monitoring"])

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API DevOps Audio Distribution"}
