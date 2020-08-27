from difficulty.level import *


class GameLevel:
    __game_level = (
        Normal(),
        Hard(),
    )

    def __init__(self, chance):
        self.chances = chance

    def get_level_chances(self):
        for i in range(len(self.__game_level)):
            print('{lp}. {level}'.format(
                lp=str(i + 1),
                level=self.__game_level[i].get_name())
            )

        level = int(input('Choose difficulty: ')) - 1

        return self.chances(self.__game_level[level].get_chances())
