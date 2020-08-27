import pygame


class GlobalStyleClass:
    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height
        self.WHITE = (243, 243, 243)
        self.BLACK = (5, 5, 5)
        self.clock = pygame.time.Clock()
        self.font_size_1 = round(self.width / 32)
        self.font_size_2 = round(self.width / 15)
        self.letter_font_1 = pygame.font.SysFont('monospace', self.font_size_1, bold=True)
        self.letter_font_2 = pygame.font.SysFont('monospace', self.font_size_2, bold=True)
