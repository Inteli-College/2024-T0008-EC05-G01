from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse  
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="telaInicial.html")

@router.get("/page/{page_name}", response_class=HTMLResponse)
async def read_page(request: Request, page_name: str):
    return templates.TemplateResponse(page_name, {"request": request})
