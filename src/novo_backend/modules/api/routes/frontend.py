from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse  
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name="telaInicial.html", context={"request": request})

@router.get("/telaP", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="telaP.html", context={"request": request})

@router.get("/deleteKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="telaExclusao.html", context={"request": request})

@router.get("/visualizacaoKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="visualizacaoKit.html", context={"request": request})

@router.get("/telaKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="telaKit.html", context={"request": request})

@router.get("/kit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="kit.html", context={"request": request})

@router.get("/novoKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="novoKit.html", context={"request": request})

@router.get("/kit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="kit.html", context={"request": request})

@router.get("/config", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="config.html", context={"request": request})

############### ROTAS DO AUXILIAR ####################

@router.get("/auxiliar", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="armazem.html", context={"request": request})

@router.get("/reabastecimento", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="reabastecimento.html", context={"request": request})

