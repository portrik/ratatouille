"""Recipe ingredient category class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Table, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ratatouille.types.ingredient import Ingredient


class AssociationBase(DeclarativeBase):
    """Base class for association table metadata."""


ingredient_category_ingredient_association = Table(
    "ingredient_category_ingredient",
    AssociationBase.metadata,
    Column("category_id", ForeignKey("ingredient_category.name")),  # pyright: ignore[reportUnknownArgumentType]
    Column("ingredient_id", ForeignKey("ingredient.id")),  # pyright: ignore[reportUnknownArgumentType]
)


class IngredientCategory(DeclarativeBase):
    """Ingredient category."""

    ___tablename__: str = "ingredient_category"

    name: Mapped[str] = mapped_column(Text(), primary_key=True)

    ingredients: Mapped[list[Ingredient]] = relationship(
        secondary=ingredient_category_ingredient_association,
        back_populates="categories",
    )
