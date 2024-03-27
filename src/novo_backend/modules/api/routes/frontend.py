from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse  
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name="telaInicial.html", context={"request": request})

@router.get("/novoKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="novoKit.html", context={"request": request})

@router.get("/kit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="kit.html", context={"request": request})
