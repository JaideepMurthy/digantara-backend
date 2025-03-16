from fastapi import APIRouter, HTTPException
from app.services.bfs import bfs

router = APIRouter()

@router.post("/bfs/", summary="Breadth-First Search API")
async def bfs_api(data: dict):
    try:
        graph = data.get("graph")
        start_node = data.get("start_node")

        if not isinstance(graph, dict) or start_node not in graph:
            raise HTTPException(status_code=400, detail="Invalid input. Graph must be a dictionary and start_node must exist.")

        result = bfs(graph, start_node)
        return {"traversal": result, "message": "BFS traversal successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
