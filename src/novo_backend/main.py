import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.main import router as api_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time

from queue import Queue
from threading import Thread

from classes.ApiWrapper import ApiWrapper


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(api_router)

if __name__ == "__main__":
	main()
	# while True: time.sleep(1)