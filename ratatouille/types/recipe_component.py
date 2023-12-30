"""Recipe component class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ratatouille.types.recipe import Recipe
    from ratatouille.types.recipe_ingredient import RecipeIngredient
    from ratatouille.types.step import Step


class RecipeComponent(DeclarativeBase):
    """Recipe component."""

    ___tablename__: str = "recipe_component"

    name: Mapped[str] = mapped_column(Text(), primary_key=True)

    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipe.id"))
    recipe: Mapped[Recipe] = relationship(back_populates="components")
    ingredients: Mapped[list[RecipeIngredient]] = relationship()
    steps: Mapped[list[Step]] = relationship()
