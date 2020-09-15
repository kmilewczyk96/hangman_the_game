import pygame


class GlobalStyle:
    def __init__(self):
        # keep this aspect ratio (16:9 / 16:10), with max resolution of 1920 x 1080:
        self.width = 1920
        self.height = 1080
        self.win = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        # colours:
        self.WHITE = (227, 227, 227)
        self.GREY = (175, 175, 175)
        self.BACKGROUND = pygame.image.load("chalkboard.jpg").convert()
        # fonts:
        self.FONT_SIZE_0 = int(self.width / 40)
        self.FONT_SIZE_1 = int(self.width / 28)
        self.FONT_SIZE_2 = int(self.width / 15)
        self.LETTER_FONT_0 = pygame.font.SysFont('monospace', self.FONT_SIZE_0, bold=False)
        self.LETTER_FONT_1 = pygame.font.SysFont('monospace', self.FONT_SIZE_1, bold=False)
        self.LETTER_FONT_2 = pygame.font.SysFont('monospace', self.FONT_SIZE_2, bold=False)

    def mid_width(self):
        return int(self.width / 2)

    def mid_height(self):
        return int(self.height / 2)
