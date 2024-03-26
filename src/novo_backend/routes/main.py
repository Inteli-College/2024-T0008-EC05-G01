from fastapi import APIRouter
from routes import medicamentos, kits, frontend;

router = APIRouter()
router.include_router(medicamentos.router)
router.include_router(kits.router)
router.include_router(frontend.router)