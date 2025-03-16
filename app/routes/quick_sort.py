from fastapi import APIRouter, HTTPException
from app.services.quick_sort import quick_sort

router = APIRouter()

@router.post("/quick-sort/", summary="Quick Sort API")
async def quick_sort_api(data: dict):
    try:
        arr = data.get("arr")

        if not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr):
            raise HTTPException(status_code=400, detail="Invalid input. 'arr' must be a list of numbers.")

        sorted_arr = quick_sort(arr)
        return {"sorted_array": sorted_arr, "message": "Quick Sort successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
