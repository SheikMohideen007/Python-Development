from fastapi import FastAPI,Request,APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from uvicorn import run
from pydantic import BaseModel, ValidationError

class AddItemRequest(BaseModel):
    item: int

class UpdateItemRequest(BaseModel):
    index: int
    value: int

class RemoveItemRequest(BaseModel):
    item: int

def create_app()->FastAPI:
    app = FastAPI(debug=True, title="CRUD API", description="A simple CRUD API using FastAPI",
                  docs_url="/docs",redoc_url="/redocs")
    
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Handle general unhandled exceptions."""
        error_msg = str(exc)
        print(f"[ERROR] Unhandled exception: path={request.url.path}, error={error_msg}")
        
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "An internal server error occurred",
                    "details": {"error": str(exc)}
                },
                "status": "error"
            }
        )
    return app

# Create the app instance at module level for Uvicorn to find
app = create_app()

print(f"CRUD API is ready to run...{app}")

router=APIRouter(tags=["CRUD Operations"])

arr=[1,2,3,4,5]




@router.post("/add")
async def add_item(request: AddItemRequest):
    arr.append(request.item)
    return JSONResponse(
        status_code=200,
        content={"message": "Success", "item": request.item}
    )

@router.delete('/remove')
async def remove_item(request: RemoveItemRequest):
    if len(arr)==0:
        return JSONResponse(
            status_code=400,
            content={"message": "There is no item to remove from the list"}
        )
    if request.item in arr:
        arr.remove(request.item)
        return JSONResponse(
            status_code=200,
            content={"message": "Success", "removed": request.item}
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"message": "Item not found in the list", "item": request.item}
        )

@router.get('/get')
async def getItem():
    return JSONResponse(
        status_code=200,
        content={
            'count':len(arr),
            'items':arr
        }
    )


@router.put('/update')
async  def update_item(request: UpdateItemRequest):
    if request.index >= len(arr) or request.index < 0:
        return JSONResponse(
            status_code=400,
            content={"message": f"Index {request.index} is out of bounds. Valid range: 0-{len(arr)-1}"}
        )
    old_value = arr[request.index]
    arr[request.index]=request.value
    return JSONResponse(
        content={"message": "Success", "old_value": old_value, "new_value": request.value,"items":arr},
        status_code=200
    )

# Register the router with the app (include prefix here)
app.include_router(router, prefix="/api")


if __name__=="__main__":
    run("crud:app", host="0.0.0.0",port=8002, reload=True)