"""Step class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ratatouille.types.recipe_component import RecipeComponent
    from ratatouille.types.recipe_ingredient import RecipeIngredient


class Step(DeclarativeBase):
    """A recipe step."""

    __tablename__: str = "step"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    text: Mapped[str] = mapped_column(Text())

    component_id: Mapped[str] = mapped_column(ForeignKey("recipe_component.name"))
    component: Mapped[RecipeComponent] = relationship(back_populates="steps")
    ingredients: Mapped[list[RecipeIngredient]] = relationship()
