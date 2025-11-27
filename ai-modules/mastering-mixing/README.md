# 🎧 DevOps Audio – Mastering & Mixing (MVP)

## 🚀 Objectif
Ce module est le **deuxième jalon** du projet Audio DevOps SaaS.  
Il permet de :
- Appliquer un **mastering automatique** (normalisation, compression, EQ, limiter)
- Réaliser un **mixage intelligent** (balance des pistes, spatialisation, reverb)
- Produire un fichier audio final prêt à être distribué

---

## 🛠️ Stack technique
- **Python** (pydub, librosa, FastAPI, PyTorch/TensorFlow)
- **Docker** pour containerisation
- **GitHub Actions** pour CI/CD
- **AWS Lightsail/EC2** pour déploiement futur

---

## 📂 Structure du projet
- `src/` : code source (API, mastering, mixage, IA)
- `tests/` : tests unitaires
- `data/` : datasets audio
- `docker/` : configuration Docker
- `.github/workflows/` : pipeline CI/CD

---

## ▶️ Exemple d’utilisation
### 1. Installation
```bash
git clone https://github.com/<username>/DevOps_Audio_MasteringMixing.git
cd DevOps_Audio_MasteringMixing
pip install -r requirements.txt
