🎧 DevOps Audio – Beat Selection (MVP)


🚀 Objectif
Ce module est le premier jalon du projet Audio DevOps SaaS. Il permet de :

Analyser un fichier audio brut

Extraire ses caractéristiques (tempo, énergie, tonalité…)

Recommander automatiquement un beat adapté via IA

👉 Exemple concret de convergence entre IA et DevOps appliquée à l’audio.

🛠️ Stack technique
Python : Librosa (analyse audio), FastAPI (API), PyTorch/TensorFlow (IA)

Docker : containerisation et portabilité

GitHub Actions : CI/CD automatisé (tests + build + push Docker)

AWS Lightsail/EC2 : cible de déploiement futur

docker build -t devops-audio-beatselection .
docker run -p 8000:8000 devops-audio-beatselection

## 🔄 Pipeline DevOps Audio

Le projet suit un pipeline complet, inspiré des pratiques DevOps :

1. **Développement (`src/`)**
   - API FastAPI (`main.py`)
   - Extraction des features audio (`features.py`)
   - Modèle IA (`model.py`)
   - Utilitaires (`utils.py`)

2. **Tests (`tests/`)**
   - Vérification des features (`test_features.py`)
   - Validation du modèle IA (`test_model.py`)
   - Tests des endpoints API (`test_api.py`)

3. **Datasets (`data/`)**
   - Organisation en `train/` et `test/`
   - Annotations (`annotations.csv`)
   - Documentation (`README.md`)

4. **Containerisation (`docker/`)**
   - `Dockerfile` pour construire une image portable
   - Exposition de l’API sur le port 8000

5. **CI/CD (Jenkins)**
   - **Stages** :
     - Checkout du code
     - Installation des dépendances
     - Exécution des tests unitaires
     - Build de l’image Docker
     - Push vers DockerHub
     - Déploiement futur sur AWS EC2/Lightsail
   - **Credentials Jenkins** pour sécuriser l’accès à DockerHub

6. **Déploiement (futur)**
   - AWS EC2/Lightsail comme cible
   - Automatisation possible via Terraform ou Ansible


