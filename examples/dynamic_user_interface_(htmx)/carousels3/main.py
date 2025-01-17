from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from carousel_component import carousel_component  # Import the carousel component

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Assuming templates are in a 'templates' folder

@app.get("/")
async def gallery_page(request: Request):
    carousel_html = carousel_component().render()
    print(f"Carousel HTML: {carousel_html}")  # Added print statement
    return templates.TemplateResponse("gallery.html", {"request": request, "carousel": carousel_html})

@app.get("/carousel")
async def get_carousel():
    carousel_html = carousel_component().render() 
    return HTMLResponse(carousel_html)