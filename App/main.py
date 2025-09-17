from fastapi import FastAPI

from App.routes.admin.user_approvals import router as approval_routers
from App.routes.admin.dashboard import router as dashboard_router

app = FastAPI()

app.include_router(dashboard_router)
app.include_router(approval_routers)