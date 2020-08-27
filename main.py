import pygame
pygame.init()

# keep this aspect ratio (16:9/ 16:10)
WIDTH, HEIGHT = (1280, 720)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('H A N _ _ A N')

# time
FPS = 60
clock = pygame.time.Clock()
status = 0

# colours and fonts:
WHITE = (243, 243, 243)
GREEN_TABLE = (51, 67, 42)
BLACK = (5, 5, 5)

FONT_SIZE_1 = round(WIDTH / 32)
FONT_SIZE_2 = round(WIDTH / 15)
LETTER_FONT = pygame.font.SysFont('monospace', FONT_SIZE_1, bold=True)
LETTER_FONT_2 = pygame.font.SysFont('monospace', FONT_SIZE_2, bold=True)


def main_menu():
    global status
    run_menu = True
    while run_menu:
        clock.tick(FPS)
        win.fill(WHITE)
        play_text = LETTER_FONT_2.render('PLAY', 1, BLACK)
        quit_text = LETTER_FONT_2.render('QUIT', 1, BLACK)

        win.blit(play_text, (int(WIDTH/2) - int(play_text.get_width() / 2),
                             int(HEIGHT/2 - FONT_SIZE_2)))
        win.blit(quit_text, (int(WIDTH / 2) - int(quit_text.get_width() / 2),
                             int(HEIGHT / 2 + FONT_SIZE_2 / 2)))

        if status == 0:
            pygame.draw.line(win, BLACK,
                             (int(WIDTH/2) - int(play_text.get_width()/2), int(HEIGHT/2)),
                             (int(WIDTH/2) + int(play_text.get_width()/2), int(HEIGHT/2)),
                             int(FONT_SIZE_2 / 10))

        else:
            pygame.draw.line(win, BLACK,
                             (int(WIDTH/2) - int(quit_text.get_width()/2), int(HEIGHT/2) + int(FONT_SIZE_2 * 5/3)),
                             (int(WIDTH/2) + int(quit_text.get_width()/2), int(HEIGHT/2) + int(FONT_SIZE_2 * 5/3)),
                             int(FONT_SIZE_2 / 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if status == 0:
                        status = 1
                    print(status)

                if event.key == pygame.K_UP:
                    if status == 1:
                        status = 0
                    print(status)

                if event.key == pygame.K_RETURN:
                    if status == 0:
                        play()
                    if status == 1:
                        quit()

        pygame.display.update()


def play():
    run_play = True
    while run_play:
        win.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


run = True
while run:
    main_menu()
    run = False


pygame.quit()
