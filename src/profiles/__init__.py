# -*- coding: utf-8 -*-


_NUMERIC = '一 二 三 四 伍 六 七 八 九'.split()
_TYPE = '萬 筒 索'.split()
_SPECIAL = '東 南 西 北 中 發 白'.split()


# Classes
class MahjongProfile:
    """Base class of mahjong profiles."""

    tags = ['wan', 'tong', 'suo', 'fan', 'feng', 'jian']