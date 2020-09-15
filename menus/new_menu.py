import pygame


class NewMenu:
    def __init__(self, name: str, options: dict):
        self.highlight = 0
        self.run_menu = True
        self.name = name
        self.options = options
        self.menu_choice = [i for i in self.options.keys()]
        self.menu_action = [i for i in self.options.values()]
        self.choice_count = len(self.menu_choice)

    def draw_menu(self, WIDTH, HEIGHT, BACKGROUND, WHITE, WHITE_2, LETTER_FONT_2, FONT_SIZE_2, win):
        while self.run_menu:
            win.blit(BACKGROUND, (0, 0))

            header_shadow = LETTER_FONT_2.render(self.name, 1, WHITE_2)
            header = LETTER_FONT_2.render(self.name, 1, WHITE)
            win.blit(header_shadow, (int(WIDTH / 2) - int(header_shadow.get_width() / 2),
                                     int(FONT_SIZE_2)))
            win.blit(header, (int(WIDTH / 2) - int(header.get_width() / 2) + 2,
                              int(FONT_SIZE_2) + 2))

            for i in range(self.choice_count):
                name = LETTER_FONT_2.render(f'{self.menu_choice[i]}', 1, WHITE_2)
                win.blit(name, (int(WIDTH / 2) - int(name.get_width() / 2),
                         int(HEIGHT / 2) - 11/9 * FONT_SIZE_2 * self.choice_count / 3
                         + FONT_SIZE_2 * i * 11/9))

            highlight = LETTER_FONT_2.render(f'[ {self.menu_choice[self.highlight]} ]', 1, WHITE)
            win.blit(highlight, (int(WIDTH / 2) - int(highlight.get_width() / 2) + 2,
                     int(HEIGHT / 2) - 11/9 * FONT_SIZE_2 * self.choice_count / 3
                     + FONT_SIZE_2 * self.highlight * 11/9 + 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.highlight < self.choice_count - 1:
                            self.highlight += 1

                    if event.key == pygame.K_UP:
                        if self.highlight > 0:
                            self.highlight -= 1
                        print(self.highlight)

                    if event.key == pygame.K_RETURN:
                        if self.menu_action[self.highlight]() is not None:
                            return 'go_back'
                        self.run_menu = False

            pygame.display.update()
