from nsepy import get_history
from datetime import date
from pandas import DataFrame


def get_historical_prices(symbol: str, start_date: date, end_date: date) -> DataFrame:
    return get_history(symbol=symbol, start=start_date, end=end_date)
