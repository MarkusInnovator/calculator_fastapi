from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate/", response_class=HTMLResponse)
async def calculate(x: float = Form(...), y: float = Form(...), operator: str = Form(...)):
    result = None
    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "/":
        if y != 0:
            result = x / y

    return templates.TemplateResponse("result.html", {"result": result})
