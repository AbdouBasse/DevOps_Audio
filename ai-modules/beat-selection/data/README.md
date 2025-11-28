🎯 Objectif
Ce dossier contient les datasets audio utilisés pour :

L’entraînement du modèle IA (classification des beats)

Les tests et démonstrations (samples annotés)

Les futures extensions (mastering, mixage automatisé)

📦 Contenu
sample.wav : exemple de fichier audio brut pour tester l’API

train/ : fichiers audio annotés pour l’entraînement du modèle

test/ : fichiers audio pour la validation et les tests unitaires

README.md : guide d’utilisation et conventions

📑 Conventions de nommage
Pour garantir la cohérence des datasets :

Format accepté : .wav ou .mp3

Nom des fichiers : <genre>_<id>.wav

Exemple : afro_001.wav, trap_002.wav

Chaque fichier doit être accompagné d’une annotation (genre, tempo, tonalité) dans un fichier CSV ou JSON.

🛠️ Exemple d’annotation
annotations.csv :

csv
filename,genre,tempo,key
afro_001.wav,Afro,110,Cm
trap_002.wav,Trap,140,Am
📚 Bonnes pratiques
Toujours vérifier la qualité audio (échantillonnage ≥ 44.1 kHz).

Normaliser les fichiers (volume homogène).

Documenter les sources (origine des samples).

Ne pas inclure de fichiers protégés par droits d’auteur sans licence.

🚀 Utilisation
Lors de l’entraînement du modèle :

Charger les fichiers depuis data/train/

Utiliser annotations.csv pour associer les labels

Tester le modèle avec data/test/

✨ Résultat : ton dossier data/ devient structuré, clair et pédagogique, prêt pour l’entraînement IA et les démonstrations.
