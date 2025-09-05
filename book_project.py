from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

BOOKS = [
    {'title': "First Book", 'Author' : "First Author", 'Category' : "Zoology"},
    {'title': "Second Book", 'Author': "Second Author", 'Category': "Chemistry"},
    {'title': "Third Book", 'Author': "Third Author", 'Category': "Physics"},
    {'title': "Fifth Book", 'Author': "Fifth Author", 'Category': "Math"},
    {'title': "Sixth Book", 'Author': "Sixth Author", 'Category': "History"},
]



@app.get("/")
def index():
    return {"Message":"Book Project Initialized"}

@app.get("/books")
def books():
    return JSONResponse(BOOKS)