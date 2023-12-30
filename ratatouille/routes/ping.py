"""Ping-related routes."""

from typing import Literal

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", tags=["diagnostics"])
async def ping() -> Literal["pong"]:
    """Reply to diagnostic ping.

    Returns
    -------
        Literal: A valid "pong" response.
    """
    return "pong"
