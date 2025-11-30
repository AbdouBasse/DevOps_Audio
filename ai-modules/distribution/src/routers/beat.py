from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_beats():
    return {"beats": ["afro", "trap", "jazz"]}
