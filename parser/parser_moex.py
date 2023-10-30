# Модуль взаймодействия с сайтом: " https://iss.moex.com"

import apimoex
import requests
import pandas as pd
import uuid
from base_parser import BaseParser


class InteractMOEX(BaseParser):

    def get_dataframe_stock_token(self, token: str) -> pd.DataFrame:
        _df = pd.DataFrame()
        with requests.Session() as session:
            data = apimoex.get_board_candles(session=session, security=token)
            _df = pd.DataFrame(data)
        return _df

    def get_token_stocks(self) -> list:
        return self.stock_tokens

    def get_uuid_request(self) -> uuid.UUID:
        return uuid.uuid4()
