from fastapi import FastAPI
from src.monitoring import metrics

app = FastAPI(title="DevOps Audio Monitoring")

@app.get("/metrics")
def get_metrics():
    """
    Expose les métriques pour Prometheus.
    """
    return metrics()
