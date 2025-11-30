import time
import random

def metrics():
    """
    Simule des métriques audio :
    - Latence moyenne
    - Nombre de requêtes
    - Erreurs
    """
    return {
        "latency_ms": round(random.uniform(10, 200), 2),
        "requests_total": random.randint(100, 500),
        "errors_total": random.randint(0, 5),
        "timestamp": time.time()
    }
