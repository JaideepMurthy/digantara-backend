from pydantic import BaseModel, Field
from typing import List, Dict

class BinarySearchRequest(BaseModel):
    arr: List[int] = Field(..., example=[1, 2, 3, 4, 5, 6, 7])
    target: int = Field(..., example=4)

class BinarySearchResponse(BaseModel):
    index: int = Field(..., example=3)
    message: str = Field(..., example="Object found at position 3")

class QuickSortRequest(BaseModel):
    arr: List[int] = Field(..., example=[5, 3, 8, 6, 2])

class QuickSortResponse(BaseModel):
    sorted_array: List[int] = Field(..., example=[2, 3, 5, 6, 8])

class BFSRequest(BaseModel):
    graph: Dict[str, List[str]] = Field(..., example={"A": ["B", "C"], "B": ["D", "E"], "C": ["F"]})
    start_node: str = Field(..., example="A")

class BFSResponse(BaseModel):
    visited_order: List[str] = Field(..., example=["A", "B", "C", "D", "E", "F"])
    message: str = Field(..., example="Orbital path traversed successfully")
