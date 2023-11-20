from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional     # None 이어도 관계 없음으로 체크


users = {
    0: {"userid": "apple", "name": "김사과"},
    1: {"userid": "banana", "name": "반하나"},
    2: {"userid": "orange", "name": "오렌지"}
}

app = FastAPI()

# http://127.0.0.1:8000/users/0
@app.get("/users/{id}")
def find_user(id: int):
    user = users[id]
    return user                         # Dict를 자동으로 JSON화 한다

# http://127.0.0.1:8000/users/0/userid
@app.get("/users/{id}/{key}")
def find_user_by_key(id: int, key:str):
    user = users[id][key]
    return user


# http://127.0.0.1:8000/id-by-name?name=김사과
@app.get("/id-by-name")     # 변수를 아무것도 받지 않으면 query string으로 받겠다는 의미
def find_user_by_name(name: str):
    for idx, user in users.items():
        if ( user['name'] == name ):
             return user
    return {"erorr": "데이터를 찾지 못함"}


class User(BaseModel):
    userid: str
    name: str


@app.post("/users/{id}")
def create_user(id: int, user: User):
    if ( id in users ):
        return {"error": "이미 존재하는 id"}
    users[id] = user.__dict__   # JSON을 dict 형태로 변환s
    return {"success": "ok"}


class UserForUpdate(BaseModel):
    userid: Optional[str]       # userid가 str이어도 되고, None이어도 된다.
    name: Optional[str]

@app.put("/users/{id}")
def update_user(id: int, user: UserForUpdate):
    if ( id not in users ):
        return {"error": "수정하고자 하는 id가 존재하지 않음"}
    
    if ( user.userid ):
        users[id]["userid"] = user.userid

    if ( user.name ):
        users[id]["name"] = user.name

    return {"success": "ok"} 

@app.delete("/users/{id}")
def delete_item(id: int):
    users.pop(id)
    return {"success": "ok"}

