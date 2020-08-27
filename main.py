# pygame inits
import pygame
pygame.init()

WIDTH, HEIGHT = (1280, 720)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('H A N _ _ A N')

FPS = 60
clock = pygame.time.Clock()

# style:
WHITE = (243, 243, 243)
GREEN_TABLE = (51, 67, 42)
BLACK = (5, 5, 5)
LETTER_FONT = pygame.font.SysFont('monospace', 40, bold=True)

alphabet = [i for i in range(97, 123)]

RADIUS = 30
GAP = 15
letters = []
x_pos = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
y_pos = round(3/4 * HEIGHT)
for i in range(26):
    x = x_pos + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = y_pos + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(65 + i)])


def in_game_graphic():
    win.fill(GREEN_TABLE)
    win.blit(LETTER_FONT.render('Used letters:', 1, WHITE), (200, 3/5 * HEIGHT + 10))
    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(win, WHITE, (x, y), RADIUS, 3)
        pygame.draw.line(win, WHITE, (0, 3/5 * HEIGHT), (WIDTH, 3/5 * HEIGHT), 3)
        text = LETTER_FONT.render(ltr, 1, WHITE)
        win.blit(text, (x - text.get_width() / 2, y - text.get_width()))
    pygame.display.update()


run = True
while run:
    clock.tick(FPS)
    in_game_graphic()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key in alphabet:
                guess = pygame.key.name(event.key).upper()
                print(guess)

            if event.key == pygame.K_ESCAPE:
                run = False

pygame.quit()
