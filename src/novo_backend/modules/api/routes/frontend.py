from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse  
from fastapi.templating import Jinja2Templates
from database.wrapper import DB
from tinydb import Query

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name="telaInicial.html", context={"request": request})

@router.get("/telaP", response_class=HTMLResponse)
async def read_page(request: Request):
    kits = []

    try:
        with DB('database/archives/kits.json') as kits_db:
            kits = kits_db.all()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return templates.TemplateResponse("telaP.html", {"request": request, "kits": kits})

@router.get("/deleteKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="telaExclusao.html", context={"request": request})

@router.get("/visualizacaoKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="visualizacaoKit.html", context={"request": request})

@router.get("/kit", response_class=HTMLResponse)
async def read_kit(request: Request):
    nome_do_kit = request.query_params.get('kit', 'Nome do Kit Não Encontrado')
    medicamentos = []  
    
    try:
        with DB('database/archives/kits.json') as kits_db:
            kits = kits_db.all()

            for kit in kits:
                if kit['nome'] == nome_do_kit:
                    medicamentos = kit['medicamentos']
                    break
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    return templates.TemplateResponse('kit.html', {"request": request, "nome_do_kit": nome_do_kit, "medicamentos": medicamentos})

@router.get("/telaKit", response_class=HTMLResponse)
async def read_medicamentos(request: Request):
    nome_do_kit = request.query_params.get('kit', 'Nome do Kit Não Encontrado')
    medicamentos = []  
    
    try:
        with DB('database/archives/kits.json') as kits_db:
            kits = kits_db.all()

            for kit in kits:
                if kit['nome'] == nome_do_kit:
                    medicamentos = kit['medicamentos']
                    break
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    print(nome_do_kit, medicamentos)
    return templates.TemplateResponse('telaKit.html', {"request": request, "nome_do_kit": nome_do_kit, "medicamentos": medicamentos})   

@router.get("/novoKit", response_class=HTMLResponse)
async def read_page(request: Request):
    return templates.TemplateResponse(name="novoKit.html", context={"request": request})

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

