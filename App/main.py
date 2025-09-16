from fastapi import FastAPI
from App.dependencies import database

from App.routes.admin.dashboard import router as dashboard_router

app = FastAPI()

app.include_router(dashboard_router)