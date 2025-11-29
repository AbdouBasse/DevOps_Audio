# Dockerfile
# Étape 1 : Image de base Python
FROM python:3.10-slim

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Copier les dépendances et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 4 : Copier le code source et les données
COPY src/ ./src
COPY data/ ./data

# Étape 5 : Exposer le port de l’API
EXPOSE 8000

# Étape 6 : Commande de lancement
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
