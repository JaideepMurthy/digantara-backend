from fastapi import APIRouter
from pydantic import BaseModel
from app.services.binary_search import binary_search

router = APIRouter()

# Define request body schema
class BinarySearchRequest(BaseModel):
    arr: list[int]
    target: int

@router.post("/binary-search/")
async def binary_search_api(request: BinarySearchRequest):
    index = binary_search(request.arr, request.target)
    if index != -1:
        return {"index": index, "message": f"Target found at index {index}"}
    return {"index": -1, "message": "Target not found"}
