# -*- coding: utf-8 -*-


"""
CardSys - Simple Card Game System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: This module is firstly written for `mahjong-connect` project. A complete
      version can be seen later.
"""


# Metadata
__AUTHOR__ = 'Little_Ye233'
__VERSION__ = '0.0.0-mahjong'

__all__ = ['Card', 'Cardset']


from collections import namedtuple


# Classes
class Card:
    """Simple card class. Frequently for internal uses.
        :param rank: See the source code.

        :param suit: See the source code.

        :param name: Displayed strings.
        :type name: str
    """

    def __init__(self, rank=None, suit=None, name=None):
        self.rank = rank
        self.suit = suit
        self.name = name


class Cardset:
    """Simple card set class. Frequently for internal uses.
        :param cards: Should be a container with `Card`s.
        :type cards: a container
    """

    def __init__(self, cards=None):
        self._cards = cards or []

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, pos):
        return self._cards[pos]