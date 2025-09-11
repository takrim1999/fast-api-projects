from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

BOOKS = [
    {'title': "First Book", 'author' : "First Author", 'category' : "Zoology"},
    {'title': "Second Book", 'author': "Second Author", 'category': "Chemistry"},
    {'title': "Third Book", 'author': "Third Author", 'category': "Physics"},
    {'title': "Fifth Book", 'author': "Fifth Author", 'category': "Math"},
    {'title': "Sixth Book", 'author': "Sixth Author", 'category': "History"},
]

@app.get("/")
def index():
    return {"Message":"Book Project Initialized"}

@app.get("/books")
def books():
    return JSONResponse(BOOKS)

@app.get("/books/{parameter}")
def books(parameter):
    data = " ".join(parameter.split())
    for i in BOOKS:
        if i['title'].lower() == data:
            out = i
    return JSONResponse(out)