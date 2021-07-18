# -*- coding: utf-8 -*-


from src.utils.cardsys import Card, Cardset
from src.profiles import japanese
from src.profiles import competition


# Constants
_MJ_GAME_PROFILE_KEYS = [
    'japanese',  # Japanese Mahjong, 日本麻将
    'competition'  # Mahjong Competition Rules, 国标麻将
]

_MJ_GAME_PROFILES = {  # TODO: additional rules defined in these files
    'japanese': japanese,
    'competition': competition
}


# Classes
class MahjongCard(Card):
    def __init__(self, rank=None, suit=None, name=None, tags=None):
        super().__init__(rank, suit, name)
        self.tags = tags or []

    def __repr__(self):
        return (f'<MahjongCard rank={self.rank} suit={self.suit} '
                f'name={self.name} tags={self.tags}>')