from enum import Enum
import logging


class Stock(Enum):
    TCSE = 0
    TSBC = 1
    TCB = 2
    SYS = 3
    SLAG = 4
    IOU = 5
    GRN = 6
    TCHS = 7
    YAZ = 8
    TCT = 9
    CNC = 10
    MSG = 11
    TMI = 12
    TCP = 13
    IIL = 14
    FHG = 15
    SYM = 16
    LSC = 17
    PRN = 18
    EWM = 19
    TCM = 20
    ELBT = 21
    HRG = 22
    TGP = 23
    WSSB = 25
    ISTC = 26
    BAG = 27
    EVL = 28
    MCS = 29
    WLT = 30
    TCC = 31

    def _get_value(self, torn_api, key):
        data = torn_api.stocks(self)
        try:
            return data['stocks'][str(self.value)][key]
        except KeyError as err:
            logging.error(err)

    def available_shares(self, torn_api) -> int:
        return self._get_value(torn_api, 'available_shares')

    def benefit(self, torn_api) -> dict:
        return self._get_value(torn_api, 'benefit')

    def demand(self, torn_api) -> str:
        return self._get_value(torn_api, 'demand')

    def forecast(self, torn_api) -> str:
        return self._get_value(torn_api, 'forecast')

    def history(self, torn_api) -> list:
        return self._get_value(torn_api, 'history')
