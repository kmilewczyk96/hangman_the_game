from difficulty.level import *


class GameLevel:
    __game_level = (
        Easy(),
        Normal(),
        Hard(),
    )

    def __init__(self, chance, multiplier):
        self.chances = chance
        self.multiplier = multiplier
        self.game_level_list = self.__game_level
        self.game_level_count = len(self.__game_level)

    def get_level_chances(self, level_status):
        return self.chances(self.__game_level[level_status].get_chances())

    def get_level_multiplier(self, level_status):
        return self.multiplier(self.__game_level[level_status].get_multiplier())
