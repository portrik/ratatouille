"""Recipe class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ratatouille.types.recipe_component import RecipeComponent


class Recipe(DeclarativeBase):
    """Recipe."""

    ___tablename__: str = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    name: Mapped[str] = mapped_column(Text())
    source: Mapped[str] = mapped_column(Text())

    components: Mapped[list[RecipeComponent]] = relationship(back_populates="recipe")
