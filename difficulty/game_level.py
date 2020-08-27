import pygame
from difficulty.level import *
from global_style import GlobalStyleClass


class GameLevel(GlobalStyleClass):
    __game_level = (
        Easy(),
        Normal(),
        Hard(),
    )

    def __init__(self, chance):
        super().__init__()
        self.chances = chance
        self.game_level_count = len(self.__game_level)

    def get_level_chances(self, win):
        level = 0
        run_level = True
        while run_level:
            win.fill(self.WHITE)

            diff_text = self.letter_font_2.render('CHOOSE DIFFICULTY:', 1, self.BLACK)
            win.blit(diff_text, (int(self.width/2) - int(diff_text.get_width()/2),
                                 int(self.font_size_2)))

            for i in range(self.game_level_count):
                lvl_text = self.letter_font_2.render(self.__game_level[i].get_name(), 1, self.BLACK)
                win.blit(lvl_text, (int(self.width/2) - int(lvl_text.get_width()/2),
                                    int(self.font_size_2)*(i+3)))

            lvl2_text = self.letter_font_2.render(self.__game_level[level].get_name(), 1, self.BLACK)
            pygame.draw.line(win, self.BLACK,
                             (int(self.width/2) - int(lvl2_text.get_width()/2),
                              int(self.font_size_2)*(level + 4)),
                             (int(self.width/2) + int(lvl2_text.get_width()/2),
                              int(self.font_size_2) * (level + 4)), int(self.font_size_2/10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if level < self.game_level_count - 1:
                            level += 1
                        print(level)

                    if event.key == pygame.K_UP:
                        if level > 0:
                            level -= 1
                        print(level)

                    if event.key == pygame.K_RETURN:
                        return self.chances(self.__game_level[level].get_chances())

            pygame.display.update()
