"""Recipe ingredient class."""

from __future__ import annotations

from typing import TYPE_CHECKING, get_args

from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from ratatouille.types.measurement import Measurement

if TYPE_CHECKING:
    from ratatouille.types.ingredient import Ingredient


class RecipeIngredient(DeclarativeBase):
    """Ingredient and it's measurement needed for a recipe."""

    __tablename__: str = "recipe_ingredient"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    amount: Mapped[int] = mapped_column()

    ingredient: Mapped[Ingredient] = relationship()
    measurement: Mapped[Measurement] = mapped_column(
        Enum(
            *get_args(Measurement),
            name="measurement",
            create_constraint=True,
            validate_strings=True,
        ),
    )
