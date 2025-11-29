# 📂 Dossier data/

## 🎯 Objectif
Ce dossier contient les datasets audio utilisés pour :
- Tester les fonctions de mastering et mixage
- Entraîner l’IA à ajuster les paramètres selon le style
- Valider les résultats avec des samples de référence

## 📦 Structure
- `samples/` : fichiers audio bruts pour démonstration
- `train/` : fichiers annotés pour l’entraînement IA
- `test/` : fichiers pour validation
- `annotations.csv` : métadonnées (style + paramètres appliqués)
- `README.md` : guide d’utilisation

## 📑 Conventions de nommage
- Format accepté : `.wav` ou `.mp3`
- Nom des fichiers : `<style>_<type>.wav`
  - Exemple : `afro_master.wav`, `trap_mix.wav`

## 🛠️ Exemple d’annotation
```csv
filename,style,eq,compression,reverb
afro_master.wav,Afro,warm,medium,deep
trap_mix.wav,Trap,bright,strong,light
