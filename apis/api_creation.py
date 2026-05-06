import fastapi
import uvicorn

app = fastapi.FastAPI()

# Basic GET request
@app.get("/")
def fetch():
    return {"message": "This is a GET request from FastAPI"}

# GET request with path parameter
@app.get('/users')
def get_users():
    return [
        {'user_id':1, 'name':'Sheik', 'age':24},
        {'user_id':2, 'name':'Safreen', 'age':22},
        {'user_id':3, 'name':'Valli', 'age':27}
    ]

# GET request with path parameter
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {'user_id':user_id, 'name':'Sheik', 'age':24}


# GET request with query parameter
@app.get("/search")
def search_user(name: str):
    return {'name': name, 'message': 'User found'}

# POST request
@app.post('/login')
def login(name,password):
    return {'name':name,'password':password}

from pydantic import BaseModel
import requests
class LoginRequestModel(BaseModel):
    name:str
    password:str

class LoginResponseModel(BaseModal):
    name:str
    string:str


@app.post('/removePassword',response_model=LoginResponseModel)
def removePass(request:LoginRequestModel):
    if not request.password.strip():
        raise fastapi.HTTPException(status_code=400, detail="Password cannot be empty")
    
    return {
        
    }