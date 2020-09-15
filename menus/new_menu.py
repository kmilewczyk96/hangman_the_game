import pygame

from global_style import GlobalStyle


class NewMenu(GlobalStyle):
    def __init__(self, header, option):
        super().__init__()
        self.run_menu = True
        self.highlight = 0
        self.header = header
        self.option = option
        self.answer = [i for i in self.option.keys()]
        self.action = [i for i in self.option.values()]
        self.option_count = len(self.answer)

    def draw_menu(self):
        while self.run_menu:
            self.win.blit(self.BACKGROUND, (0, 0))
            self.display_header(self.header)
            self.display_answers()
            self.highlight_answers(2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.highlight < self.option_count - 1:
                            self.highlight += 1

                    if event.key == pygame.K_UP:
                        if self.highlight > 0:
                            self.highlight -= 1

                    if event.key == pygame.K_RETURN:
                        self.action[self.highlight]()
                        self.run_menu = False

            pygame.display.update()

    def header_position(self, name, offset):
        position = (self.mid_width() - int(name.get_width() / 2) + offset, self.FONT_SIZE_2 + offset)
        return position

    def display_header(self, header):
        shadow = self.LETTER_FONT_2.render(header, 1, self.GREY)
        name = self.LETTER_FONT_2.render(header, 1, self.WHITE)
        self.win.blit(shadow, self.header_position(shadow, 0))
        self.win.blit(name, self.header_position(name, 2))

    def first_answer(self):
        height = int((self.height - self.FONT_SIZE_2) / 2) - (self.FONT_SIZE_2 * self.option_count / 4)
        return height

    def display_answers(self):
        for i in range(self.option_count):
            name = self.LETTER_FONT_2.render(self.answer[i], 1, self.GREY)
            self.win.blit(name, (self.mid_width() - int(name.get_width() / 2),
                          self.first_answer() + self.FONT_SIZE_2 * i))

    def highlight_answers(self, offset):
        name = self.LETTER_FONT_2.render(self.answer[self.highlight], 1, self.WHITE)
        self.win.blit(name, (self.mid_width() - int(name.get_width() / 2) + offset,
                             self.first_answer() + self.FONT_SIZE_2 * self.highlight + offset))



