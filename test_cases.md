# API Test Cases  

This document provides sample test cases for the API endpoints, including **Binary Search**, **Quick Sort**, and **Breadth-First Search (BFS)**.  

---

## **1. Binary Search**  

```http
POST /binary-search

Sample Input:

{
  "array": [1, 3, 5, 7, 9, 11, 13],
  "target": 7
}

Expected Response:

{
  "index": 3,
  "message": "Target found at index 3"
}
```

---

## **2. Quick Sort**  

```http
POST /quick-sort

Sample Input:

{
  "array": [5, 3, 8, 6, 2, 7, 4, 1]
}

Expected Response:

{
  "sorted_array": [1, 2, 3, 4, 5, 6, 7, 8]
}
```

---

## **3. Breadth-First Search**  

```http
POST /bfs

Sample Input:

{
  "graph": {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
  },
  "start": "A",
  "target": "F"
}

Expected Response:

{
  "path": ["A", "C", "F"],
  "message": "Path found"
}
```

