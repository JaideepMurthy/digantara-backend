import json
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.utils.logger import log_api_call, log_error
from app.database.database import SessionLocal
from app.database.models import LogEntry
from app.schemas import (
    BinarySearchRequest, BinarySearchResponse,
    QuickSortRequest, QuickSortResponse,
    BFSRequest, BFSResponse
)
from app.services.binary_search import binary_search
from app.services.quick_sort import quick_sort
from app.services.bfs import bfs
from app.utils.error_handler import raise_bad_request, raise_not_found, raise_internal_error

# ✅ Initialize FastAPI with Digantara Space-Themed Metadata
app = FastAPI(
    title="Digantara Space Monitoring API",
    description="APIs for space object tracking, trajectory sorting, and orbital navigation.",
    version="1.0.0",
    contact={
        "name": "Jaideep Murthy",
        "email": "jaideepmurthy3@gmail.com",
        "url": "https://www.linkedin.com/in/jaideep-murthy/",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# ✅ Include modular routers correctly
from app.routes import binary_search, quick_sort, bfs, algorithms

app.include_router(binary_search.router, prefix="/binary-search", tags=["Binary Search"])
app.include_router(quick_sort.router, prefix="/quick-sort", tags=["Quick Sort"])
app.include_router(bfs.router, prefix="/bfs", tags=["BFS"])
app.include_router(algorithms.router)  # Include this only if needed

@app.get("/", tags=["General"])
def read_root():
    """Root Endpoint"""
    return {"message": "🚀 Welcome to Digantara Space API - Track & Monitor Space Objects!"}

@app.post("/star-search", response_model=BinarySearchResponse, summary="Perform Binary Search", tags=["Algorithms"])
def binary_search_endpoint(request: BinarySearchRequest):
    """Binary Search API to find an element's index in a sorted array."""
    result = binary_search(request.arr, request.target)
    response = BinarySearchResponse(
        index=result,
        message=f"Object found at position {result}" if result != -1 else "Target not found."
    )
    log_api_call("Binary Search", request.dict(), response.dict())
    return response

@app.post("/trajectory-sort", response_model=QuickSortResponse, summary="Sort Array using QuickSort", tags=["Algorithms"])
def quick_sort_endpoint(request: QuickSortRequest):
    """QuickSort API to sort an array."""
    sorted_arr = quick_sort(request.arr)
    response = QuickSortResponse(sorted_array=sorted_arr)
    log_api_call("Quick Sort", request.dict(), response.dict())
    return response

@app.post("/orbital-navigation", response_model=BFSResponse, summary="Perform BFS Traversal", tags=["Algorithms"])
def bfs_endpoint(request: BFSRequest):
    """Breadth-First Search (BFS) API for orbital path traversal."""
    visited_order = bfs(request.graph, request.start_node)
    response = BFSResponse(
        visited_order=visited_order,
        message="Orbital path traversed successfully"
    )
    log_api_call("BFS", request.dict(), response.dict())
    return response

@app.get("/logs", summary="Retrieve API Logs", tags=["Logging"])
def get_logs():
    """Fetch logs from the database."""
    with SessionLocal() as db:
        logs = db.query(LogEntry).order_by(LogEntry.timestamp.desc()).all()
    
    log_list = [
        {
            "algorithm_name": log.algorithm_name,
            "input_data": json.loads(log.input_data),
            "output_data": json.loads(log.output_data),
            "timestamp": log.timestamp.isoformat()
        }
        for log in logs
    ]
    return JSONResponse(content={"logs": log_list})

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global Exception Handler"""
    error_message = f"Exception: {str(exc)} | Path: {request.url.path}"
    log_error(error_message)
    return JSONResponse(status_code=500, content={"detail": "An unexpected error occurred."})

# ✅ Deployment-Ready Configuration
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
