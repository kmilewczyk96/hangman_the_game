import pygame
from chance import Chance
from difficulty.game_level import GameLevel
from streak import Streak
from word.words import WordsFromFile
from hangman import Hangman
from menus.two_way_menu import TwoWayMenu
from menus.three_way_menu import ThreeWayMenu

pygame.init()

# keep this aspect ratio (16:9 / 16:10), with max resolution of 1920 x 1080
WIDTH, HEIGHT = (1920, 1080)
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
pygame.display.set_caption('H A N _ _ A N')

# time
FPS = 60
clock = pygame.time.Clock()

# colours and fonts:
WHITE = (227, 227, 227)
WHITE_2 = (175, 175, 175)
BACKGROUND = pygame.image.load("chalkboard.jpg").convert()

FONT_SIZE_0 = round(WIDTH / 40)
FONT_SIZE_1 = round(WIDTH / 28)
FONT_SIZE_2 = round(WIDTH / 15)
LETTER_FONT_0 = pygame.font.SysFont('monospace', FONT_SIZE_0, bold=False)
LETTER_FONT_1 = pygame.font.SysFont('monospace', FONT_SIZE_1, bold=False)
LETTER_FONT_2 = pygame.font.SysFont('monospace', FONT_SIZE_2, bold=False)


def quit_prompt():
    menu = TwoWayMenu('< ARE YOU SURE? >', 'YES', 'NO', quit, main_menu)
    menu.prompt(WIDTH, HEIGHT, BACKGROUND, WHITE, WHITE_2, LETTER_FONT_2, FONT_SIZE_2, win)


def main_menu():
    menu = ThreeWayMenu('< H A N G M A N >', 'PLAY', 'HI SCORES', 'QUIT', game_level_menu, game_level_menu, quit_prompt)
    menu.prompt(WIDTH, HEIGHT, BACKGROUND, WHITE, WHITE_2, LETTER_FONT_2, FONT_SIZE_2, win)


def game_level_menu():
    game_level = GameLevel(Chance)
    current_streak = Streak
    level_status = 0
    max_level_status = game_level.game_level_count - 1
    run_game_level = True
    while run_game_level:
        clock.tick(FPS)
        win.blit(BACKGROUND, (0, 0))

        header_shadow = LETTER_FONT_2.render('< CHOOSE DIFFICULTY >', 1, WHITE_2)
        header_text = LETTER_FONT_2.render('< CHOOSE DIFFICULTY >', 1, WHITE)
        win.blit(header_shadow, (int(WIDTH / 2) - int(header_shadow.get_width() / 2),
                                 int(FONT_SIZE_2)))
        win.blit(header_text, (int(WIDTH / 2) - int(header_text.get_width() / 2) + 2,
                               int(FONT_SIZE_2) + 2))

        for i in range(max_level_status + 1):
            lvl_text = LETTER_FONT_2.render(game_level.game_level_list[i].get_name(), 1, WHITE_2)
            win.blit(lvl_text, (int(WIDTH / 2) - int(lvl_text.get_width() / 2),
                                int(FONT_SIZE_2) * (i + 3)))

        lvl2_text = LETTER_FONT_2.render('[ ' + game_level.game_level_list[level_status].get_name() + ' ]', 1, WHITE)
        win.blit(lvl2_text, (int(WIDTH / 2) - int(lvl2_text.get_width() / 2) + 2,
                             int(FONT_SIZE_2) * (level_status + 3) + 2))

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
        win.blit(BACKGROUND, (0, 0))

        pygame.draw.line(win, WHITE,
                         (0, int(HEIGHT) - int(FONT_SIZE_2 * 5/2)), (WIDTH, int(HEIGHT) - int(FONT_SIZE_2 * 5/2)),
                         int(FONT_SIZE_1 / 20))

        chances_left = LETTER_FONT_1.render(f'LIVES | {hangman.chances.get_chances()}', 1, WHITE)
        win.blit(chances_left, (int(FONT_SIZE_1), int(FONT_SIZE_1)))

        current_streak = LETTER_FONT_1.render(f'fail | STREAK', 1, WHITE)
        win.blit(current_streak, (WIDTH - int(current_streak.get_width()) - int(FONT_SIZE_1), int(FONT_SIZE_1)))

        word_to_guess = LETTER_FONT_1.render(f"{' '.join(hangman.word_to_guess)}", 1, WHITE)
        win.blit(word_to_guess, (int(WIDTH / 2) - int(word_to_guess.get_width() / 2),
                                 int(HEIGHT / 2) - int(FONT_SIZE_2)))

        aesthetic_word_to_guess = LETTER_FONT_1.render(f"{' '.join(hangman.aesthetic_word_to_guess)}", 1, WHITE)
        win.blit(aesthetic_word_to_guess, (int(WIDTH / 2) - int(aesthetic_word_to_guess.get_width() / 2),
                                           int(HEIGHT / 2) - int(FONT_SIZE_2)))

        used_letters_text = LETTER_FONT_1.render('USED LETTERS', 1, WHITE)
        win.blit(used_letters_text, (int(WIDTH / 2) - int(used_letters_text.get_width() / 2),
                                     int(HEIGHT) - int(FONT_SIZE_2 * 3) - int(HEIGHT / 100)))

        pygame.draw.rect(win, WHITE,
                         (int(WIDTH / 2) - int((used_letters_text.get_width() + FONT_SIZE_1) / 2),
                          int(HEIGHT) - int(FONT_SIZE_2 * 3 + int(FONT_SIZE_1 / 15)),
                          int(used_letters_text.get_width() + FONT_SIZE_1), int(FONT_SIZE_1)), int(FONT_SIZE_1 / 20))

        used_letters_1 = LETTER_FONT_1.render(f"{' | '.join(hangman.used_letters_row_1)}", 1, WHITE)
        win.blit(used_letters_1, (int(FONT_SIZE_1 * 3/2), int(HEIGHT) - int(FONT_SIZE_2) * 2))

        used_letters_2 = LETTER_FONT_1.render(f"{' | '.join(hangman.used_letters_row_2)}", 1, WHITE)
        win.blit(used_letters_2, (int(FONT_SIZE_1 * 3/2), int(HEIGHT) - int(FONT_SIZE_2 * 5/4)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                    run_game = False

                if event.key in hangman.alphabet:
                    letter = pygame.key.name(event.key).upper()
                    result = hangman.check(letter)
                    if result == 'win':
                        game(chance)
                        run_game = False
                    if result == 'loose':
                        main_menu()
                        run_game = False

        pygame.display.update()


main_menu()
pygame.quit()
