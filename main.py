
from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Routes.route import router

app = FastAPI()

app.include_router(router)