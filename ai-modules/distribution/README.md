# 🎧 DevOps Audio – Distribution & API publique

## 🚀 Objectif
Ce module est le **quatrième jalon** du projet Audio DevOps SaaS.  
Il permet de :
- Déployer le pipeline audio en **multi-régions cloud**
- Exposer une **API publique** pour studios, artistes et écoles
- Superviser la qualité et la latence via Grafana

---

## 🛠️ Stack technique
- **AWS EC2/Lightsail/EKS** pour déploiement
- **API Gateway** pour endpoints publics
- **FastAPI** pour services audio
- **Docker/Kubernetes** pour orchestration
- **Terraform/Ansible** pour IaC
- **Grafana** pour monitoring

---

## 📂 Structure du projet
- `src/` : API globale
- `infra/` : Infrastructure as Code (Terraform/Ansible)
- `docker/` : Docker/Kubernetes configs
- `docs/` : Documentation API
- `.github/workflows/` : pipeline CI/CD

---

## ▶️ Exemple d’utilisation
### 1. Déploiement multi-régions
```bash
terraform apply
