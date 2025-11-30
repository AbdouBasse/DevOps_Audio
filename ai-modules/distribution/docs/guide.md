# 🎧 Guide API pour studios

## Objectif
Cette API permet aux studios de :
- Récupérer des beats (`/beat`)
- Appliquer un mastering automatique (`/mastering`)
- Surveiller la qualité et la performance (`/monitoring/metrics`)

## Exemple d’utilisation
```bash
curl http://localhost:8000/beat
curl -X POST http://localhost:8000/mastering -d '{"file":"sample.wav"}'
curl http://localhost:8000/monitoring/metrics
