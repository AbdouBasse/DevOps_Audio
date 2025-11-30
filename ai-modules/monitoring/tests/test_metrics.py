from src.monitoring import metrics

def test_metrics_structure():
    data = metrics()
    assert "latency_ms" in data
    assert "requests_total" in data
    assert "errors_total" in data
