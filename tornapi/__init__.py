import datetime
from .items import Item
import requests
from .stocks import Stock
from typing import Iterable, Union

from .errors import *


def get_apikey() -> str:
    with open('apikey.txt', 'r') as f:
        key = f.read()
    return key


class TornAPI:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get(self, section: str, id_='', selections: Union[Iterable, str] = '') -> dict:
        """{'error': {'code': 2, 'error': 'Incorrect key'}}"""
        url = f'https://api.torn.com/{section}/{id_}?selections={selections if isinstance(selections, str) else ",".join(selections)}&key={self.api_key}'
        print(f'{datetime.datetime.now()} - Checking API: {url}')
        r = requests.get(url)
        data = r.json()
        if 'error' in data:
            error_dict = {
                0: UnknownError,
                1: EmptyKey,
                2: IncorrectKey,
                3: WrongType,
                4: WrongFields,
                5: TooManyRequests,
                6: IncorrectID,
                7: IncorrectIDEntityRelated,
                8: IPBlock,
                9: APIDisabled,
                10: KeyOwnerFederalJail,
                11: KeyChangeError,
                12: KeyReadError
            }
            code = data["error"]["code"]
            msg = data["error"]["error"]
            raise error_dict[code](msg)
        return data

    def faction(self, faction_id=None, selections=None):
        """
        :param faction_id:
        :param selections:
        Available fields:
        applications, armor, armorynews, armorynewsfull, attacknews,
        attacknewsfull, attacks, attacksfull, basic, boosters, cesium, chain, chains, contributors, crimenews,
        crimenewsfull, crimes, currency, donations, drugs, fundsnews, fundsnewsfull, mainnews, mainnewsfull, medical,
        membershipnews, membershipnewsfull, revives, revivesfull, stats, temporary, territory, timestamp, upgrades,
        weapons
        :return:
        """
        return NotImplemented
        # if faction_id is None:
        #     user = self.user(selections='profile')
        #     faction_id = user['faction']['faction_id']
        # r = requests.get(f'')

    def itemmarket(self, item_id: Union[Item, int], selections: Union[Iterable, str] = 'itemmarket,timestamp'):
        r = requests.get(f'https://api.torn.com/market/{item_id.value if hasattr(item_id, "value") else item_id}?selections={selections if isinstance(selections, str) else ",".join(selections)}&key={self.api_key}')
        return r.json()

    def stocks(self, stock_id: Union[Stock, int] = '', timestamp: bool = True):
        return self._get('torn', stock_id.value if isinstance(stock_id, Stock) else stock_id, f'stocks{",timestamp" if timestamp else ""}')

    def torn(self, id_='', selections: Union[Iterable, str] = ''):
        return self._get('torn', id_, selections)

    def user(self, user_id: Union[int, str] = '', selections: Union[Iterable, str] = ''):
        """
        Available fields: ammo, attacks, attacksfull, bars, basic, battlestats, bazaar, cooldowns, crimes, discord,
                          display, education, events, gym, hof, honors, icons, inventory, jobpoints, medals, merits,
                          messages, money, networth, notifications, perks, personalstats, profile, properties,
                          receivedevents, refills, revives, revivesfull, stocks, timestamp, travel, weaponexp, workstats
        Available fields (for any user): basic, bazaar, crimes, discord, display, icons, personalstats, profile,
                                         properties, timestamp

        :param user_id:
        :param selections: enter a field from above or multiple
        :return:
        """
        return self._get('user', user_id, selections)
