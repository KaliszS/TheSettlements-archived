from fastapi import APIRouter
from typing import List, Optional

import pandas as pd

router = APIRouter()


@router.get("/{x}x{y}")
async def get_board(x: int, y: int):

    return {"x": x, "y": y}
