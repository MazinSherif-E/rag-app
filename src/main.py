from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env") # one time in main file to make all files see it

from routes import base

app = FastAPI()

app.include_router(base.base_router)