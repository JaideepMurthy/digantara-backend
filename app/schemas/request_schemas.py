from pydantic import BaseModel
from typing import List, Dict

class BinarySearchRequest(BaseModel):
    arr: List[int]
    target: int

class QuickSortRequest(BaseModel):
    arr: List[int]

class BFSRequest(BaseModel):
    graph: Dict[str, List[str]]
    start_node: str
