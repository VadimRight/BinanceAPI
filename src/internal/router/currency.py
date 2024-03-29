from types import NoneType

from fastapi import APIRouter
from src.pkg.redis_tools.tools import RedisTools
from fastapi import HTTPException
router = APIRouter(
    prefix='/api/v1/currency'
)


@router.get('/{pair}')
def get_currency_pair(pair: str):
    if pair not in [s.decode('utf-8') for s in RedisTools.get_keys()]:
        return {
            'error': 'This pair doesn\'t exists'
        }

    return {
        'pair': pair,
        'price': RedisTools.get_pair(pair)
    }