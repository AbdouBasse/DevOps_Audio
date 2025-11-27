# 🎧 DevOps Audio – Monitoring & Observabilité

## 🚀 Objectif
Ce module est le **troisième jalon** du projet Audio DevOps SaaS.  
Il permet de :
- Collecter des métriques sur les traitements audio (latence, erreurs, temps de mastering)
- Visualiser ces métriques dans **Grafana**
- Détecter les anomalies et améliorer la qualité des services audio

---

## 🛠️ Stack technique
- **FastAPI** (endpoint `/metrics`)
- **Prometheus** (scraping des métriques)
- **Grafana** (visualisation des dashboards)
- **Docker Compose** (orchestration)
- **GitHub Actions** (CI/CD)

---

## 📂 Structure du projet
- `src/` : API instrumentée
- `grafana/` : dashboards
- `prometheus/` : configuration Prometheus
- `docker/` : orchestration Docker Compose
- `.github/workflows/` : pipeline CI/CD

---

## ▶️ Exemple d’utilisation
### 1. Lancer l’environnement
```bash
docker-compose up -d
