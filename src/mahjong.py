# -*- coding: utf-8 -*-


from utils.cardsys import Card, Cardset
import profiles


# Constants
_MJ_GAME_PROFILE_KEYS = [
    'japanese',  # Japanese Mahjong, 日本麻将
    'competition'  # Mahjong Competition Rules, 国标麻将
]

_MJ_GAME_PROFILES = {  # TODO: additional rules defined in these files
    'japanese': profiles.japanese,
    'competition': profiles.competition
}


# Classes
class MahjongCard(Card):
    def __init__(self, rank=None, suit=None, name=None, tags=None):
        super().__init__(rank, suit, name)
        self.tags = tags or []