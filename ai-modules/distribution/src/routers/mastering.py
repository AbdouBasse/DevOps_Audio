from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def apply_mastering(file: str):
    return {"status": "success", "processed_file": f"{file}_mastered.wav"}
