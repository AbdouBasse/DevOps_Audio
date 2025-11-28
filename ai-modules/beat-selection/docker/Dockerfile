# Dockerfile
# Étape 1 : Choisir une image de base Python
FROM python:3.10-slim

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY data/ ./data

# Étape 4 : Exposer le port de l’API
EXPOSE 8000

# Étape 5 : Commande de lancement
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
