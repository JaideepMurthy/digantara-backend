from fastapi import HTTPException

def raise_bad_request(detail="Invalid request parameters"):
    raise HTTPException(status_code=400, detail=detail)

def raise_not_found(detail="Item not found"):
    raise HTTPException(status_code=404, detail=detail)

def raise_internal_error(detail="Internal server error"):
    raise HTTPException(status_code=500, detail=detail)
