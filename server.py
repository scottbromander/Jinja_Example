from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory="templates")

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Sample datasets for different fruit categories
fruit_data = {
    "default": {"message": "Some default fruit! 🍎 🍌 🍒", "items": ["apple", "banana", "cherry"]},
    "tropical": {"message": "Enjoy these tropical fruits! 🥭 🍍 🥥", "items": ["mango", "pineapple", "coconut"]},
    "berries": {"message": "Fresh berries for you! 🍓 🫐 ", "items": ["strawberry", "blueberry"]}
}

# Render page with default data
@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    data = fruit_data["default"]  # Default dataset
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

# Form submission to update the fruit list
@app.post("/", response_class=HTMLResponse)
async def update_fruit_list(request: Request, category: str = Form("default")):
    data = fruit_data.get(category, fruit_data["default"])
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
