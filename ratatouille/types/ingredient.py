"""Recipe ingredient class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from ratatouille.types.ingredient_category import (
    ingredient_category_ingredient_association,
)

if TYPE_CHECKING:
    from ratatouille.types.ingredient_category import IngredientCategory


class Ingredient(DeclarativeBase):
    """Ingredient."""

    __tablename__: str = "ingredient"

    name: Mapped[str] = mapped_column(Text(), primary_key=True)

    categories: Mapped[set[IngredientCategory]] = relationship(
        secondary=ingredient_category_ingredient_association,
        back_populates="ingredients",
    )
