from fastapi import APIRouter
from routes import medicamentos, kits;

router = APIRouter()
router.include_router(medicamentos.router)
router.include_router(kits.router)