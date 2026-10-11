from fastapi import APIRouter, HTTPException
from .models import Part
from .database import parts_db

router = APIRouter()

@router.get("/parts")
def get_parts():
    return parts_db

@router.post("/parts")
def add_part(part: Part):
    parts_db.append(part)
    return {"message": "Part added", "part": part}

@router.delete("/parts/{part_id}")
def delete_part(part_id: int):
    for p in parts_db:
        if p.id == part_id:
            parts_db.remove(p)
            return {"message": "Part deleted"}
    raise HTTPException(status_code=404, detail="Part not found")

