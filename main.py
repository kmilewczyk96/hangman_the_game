import pygame
from chance import Chance
from difficulty.game_level import GameLevel
from word.words import WordsFromFile
from hangman import Hangman

pygame.init()


# keep this aspect ratio (16:9 / 16:10)
WIDTH, HEIGHT = (1280, 720)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('H A N _ _ A N')

# time
FPS = 60
clock = pygame.time.Clock()

# colours and fonts:
WHITE = (243, 243, 243)
GREEN_TABLE = (51, 67, 42)
BLACK = (5, 5, 5)

FONT_SIZE_1 = round(WIDTH / 32)
FONT_SIZE_2 = round(WIDTH / 15)
LETTER_FONT_1 = pygame.font.SysFont('monospace', FONT_SIZE_1, bold=True)
LETTER_FONT_2 = pygame.font.SysFont('monospace', FONT_SIZE_2, bold=True)


def quit_prompt():
    pass


def main_menu():
    status = 0
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
                        game_level_menu()
                        run_menu = False
                    if status == 1:
                        run_menu = False

        pygame.display.update()


def game_level_menu():
    game_level = GameLevel(Chance)
    level_status = 0
    max_level_status = game_level.game_level_count - 1

    run_game_level = True
    while run_game_level:
        clock.tick(FPS)
        win.fill(WHITE)

        diff_text = LETTER_FONT_2.render('CHOOSE DIFFICULTY:', 1, BLACK)
        win.blit(diff_text, (int(WIDTH / 2) - int(diff_text.get_width() / 2),
                             int(FONT_SIZE_2)))

        for i in range(max_level_status + 1):
            lvl_text = LETTER_FONT_2.render(game_level.game_level_list[i].get_name(), 1, BLACK)
            win.blit(lvl_text, (int(WIDTH / 2) - int(lvl_text.get_width() / 2),
                                int(FONT_SIZE_2) * (i + 3)))

        lvl2_text = LETTER_FONT_2.render(game_level.game_level_list[level_status].get_name(), 1, BLACK)
        pygame.draw.line(win, BLACK,
                         (int(WIDTH / 2) - int(lvl2_text.get_width() / 2),
                          int(FONT_SIZE_2) * (level_status + 4)),
                         (int(WIDTH / 2) + int(lvl2_text.get_width() / 2),
                          int(FONT_SIZE_2) * (level_status + 4)), int(FONT_SIZE_2 / 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                    run_game_level = False

                if event.key == pygame.K_DOWN:
                    if level_status < max_level_status:
                        level_status += 1
                    print(level_status)

                if event.key == pygame.K_UP:
                    if level_status > 0:
                        level_status -= 1
                    print(level_status)

                if event.key == pygame.K_RETURN:
                    chance = game_level.get_level_chances(level_status)
                    game(chance)
                    run_game_level = False

        pygame.display.update()


def game(chance):
    word = WordsFromFile()
    hangman = Hangman(word, chance)

    run_game = True
    while run_game:
        clock.tick(FPS)
        win.fill(WHITE)

        word_to_guess = LETTER_FONT_1.render(f"{' '.join(hangman.word_to_guess)}", 1, BLACK)
        win.blit(word_to_guess, (int(WIDTH / 2) - int(word_to_guess.get_width() / 2),
                                 int(HEIGHT / 2) - int(FONT_SIZE_2)))

        chances_left = LETTER_FONT_1.render(f'Lives:{hangman.chances.get_chances()}', 1, BLACK)
        win.blit(chances_left, (int(FONT_SIZE_1), int(FONT_SIZE_1)))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                    run_game = False

                if event.key in hangman.alphabet:
                    letter = pygame.key.name(event.key).upper()
                    hangman.check(letter)
                    print(letter)


        pygame.display.update()

main_menu()
pygame.quit()

