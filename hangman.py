import pygame
from chance import Chance, ChancesError
from difficulty.game_level import GameLevel
from word.words import WordsFromFile


class Hangman:
    def __init__(self, word, chance):
        self.alphabet = [i for i in range(97, 123)]
        self.random_word = word.get_random_word().upper()
        self.word_to_guess = ['_' for i in self.random_word]
        self.aesthetic_word_to_guess = ['_' for i in self.random_word]
        self.used_letters_row_1 = []
        self.used_letters_row_2 = []
        self.capacity = 0
        self.chances = chance

    def check(self, letter):
        if letter in self.random_word:
            print(self.random_word)
            index_start = 0
            for i in range(self.random_word.count(letter)):
                letter_index = self.random_word.index(letter, index_start)
                index_start = letter_index + 1
                self.word_to_guess[letter_index] = letter

            if '_' not in self.word_to_guess:
                self.win()

        else:
            try:
                if letter not in self.used_letters_row_1 and letter not in self.used_letters_row_2:
                    self.chances.decrease_chances()
                    if self.capacity < 11:
                        self.used_letters_row_1.append(letter)
                        self.capacity += 1
                    else:
                        self.used_letters_row_2.append(letter)

            except ChancesError:
                self.loose()

    def win(self):
        print('win')

    def loose(self):
        print('lost')
