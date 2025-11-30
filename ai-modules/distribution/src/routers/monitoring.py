from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    return {"latency_ms": 120, "requests_total": 300, "errors_total": 2}
