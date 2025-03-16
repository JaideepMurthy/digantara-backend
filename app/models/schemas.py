from pydantic import BaseModel
from typing import List, Dict

class BinarySearchInput(BaseModel):
    array: List[int]
    target: int

class QuickSortInput(BaseModel):
    array: List[int]

class BFSInput(BaseModel):
    graph: Dict[str, List[str]]
    start_node: str
