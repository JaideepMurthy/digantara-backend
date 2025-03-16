from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.binary_search import binary_search
from app.services.quick_sort import quick_sort
from app.services.bfs import bfs

router = APIRouter(prefix="/algorithms", tags=["Algorithms"])

# Define request body models
class BinarySearchRequest(BaseModel):
    arr: list[int]
    target: int

class QuickSortRequest(BaseModel):
    arr: list[int]

class BFSRequest(BaseModel):
    graph: dict[str, list[str]]
    start_node: str

@router.post("/star-search")
def search_space_object(request: BinarySearchRequest):
    try:
        result = binary_search(request.arr, request.target)
        return {"algorithm": "Binary Search", "input": request.dict(), "output": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/trajectory-sort")
def sort_trajectories(request: QuickSortRequest):
    try:
        result = quick_sort(request.arr)
        return {"algorithm": "Quick Sort", "input": request.dict(), "output": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/orbital-navigation")
def navigate_orbit(request: BFSRequest):
    try:
        result = bfs(request.graph, request.start_node)
        return {"algorithm": "BFS", "input": request.dict(), "output": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

