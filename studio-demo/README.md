# 🎧 Studio Demo – AudioOps-Cluster

Ce dossier illustre concrètement le projet **AudioOps-Cluster** à travers des exemples audio et des captures de monitoring Grafana.  
Il sert de **preuve de concept** et de **support pédagogique** pour montrer comment DevOps peut transformer les workflows audio.

---

## 📂 Structure du dossier
studio-demo/ 
├── samples/ # Exemples audio
│ ├── raw/ # Audio brut (avant traitement IA)
│ └── mastered/ # Audio masterisé (après pipeline DevOps Audio) 
├── grafana-captures/ # Captures d’écran Grafana 
│ ├── latency.png # Latence du traitement audio 
│ ├── quality.png # Score qualité IA 
│ └── errors.png # Nombre d’erreurs détectées 
└── README.md # Documentation narrative


---

## 🎧 Samples Audio

- **Raw** : fichiers audio bruts, non traités.  
- **Mastered** : fichiers audio après passage dans le pipeline IA (beat selection, mastering, mixage).  
- Objectif : montrer la différence entre un workflow manuel et un workflow automatisé DevOps.

---

## 📊 Monitoring Grafana

Les captures Grafana illustrent le **monitoring en temps réel** du microservice *AI Mastering* :  
- **Latence** : temps de traitement par fichier audio.  
- **Qualité** : score IA (0–100%) évaluant la qualité du mastering.  
- **Erreurs** : nombre d’erreurs rencontrées lors du traitement.  

---

## 🎯 Objectifs pédagogiques

- Montrer comment un pipeline DevOps peut s’appliquer à un domaine créatif (l’audio).  
- Fournir un support visuel et sonore pour les étudiants, studios et artistes.  
- Démontrer l’importance du **monitoring en temps réel** dans un workflow cloud.  

---

## 🌍 Perspectives

- Extension multi-régions (USA, Europe, Asie).  
- Ajout de Prometheus + Loki pour logs et métriques avancées.  
- Démo interactive (audio + dashboard live).  
