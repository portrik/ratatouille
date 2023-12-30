from fastapi import FastAPI

from .routes import ping, recipes

app = FastAPI()
app.include_router(ping.router)
app.include_router(recipes.router)
