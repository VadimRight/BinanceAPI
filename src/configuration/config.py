import os
from dotenv import load_dotenv

load_dotenv()
ALL_PAIRS_KEY = os.environ.get('ALL_PAIRS_KEY')
CURRENCY_PAIR_KEY = os.environ.get('CURRENCY_PAIR_KEY')
