import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.main import router as api_router

app = FastAPI()

# origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    print("Running on port 3000")
    uvicorn.run("main:app", host='0.0.0.0', port=3000, log_level="info", reload=True)