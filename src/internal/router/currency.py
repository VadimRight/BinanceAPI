from fastapi import APIRouter
from src.pkg.redis_tools.tools import RedisTools
from fastapi import HTTPException
router = APIRouter(
    prefix='/api/currency'
)


@router.get('/{pair}')
def get_pair(pair: str):
    if pair not in [s.encode("utf-8") for s in RedisTools.get_keys()]:
        raise HTTPException(status_code=404, detail="Pair is not found")
    return {
        "pair": pair,
        "price": RedisTools.get_pair(pair)
    }
