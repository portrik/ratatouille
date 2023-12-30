from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl

router = APIRouter()


class Recipe(BaseModel):
    url: HttpUrl


@router.post("/recipe", tags=["recipes"])
async def parse_recipe(recipe: Recipe):
    return recipe.url
