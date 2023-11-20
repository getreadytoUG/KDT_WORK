from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory= "templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    data = {"name": "김사과", "title": "김사과의 홈페이지"}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

