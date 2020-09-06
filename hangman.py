import pygame
from chance import Chance
from difficulty.game_level import GameLevel
from word.words import WordsFromFile


class Hangman:
    def __init__(self, word, chance):
        self.alphabet = [i for i in range(97, 123)]
        self.random_word = word.get_random_word().upper()
        self.word_to_guess = ['_' for i in self.random_word]
        self.chances = chance

    def check(self, letter):
        if letter in self.random_word:
            print(self.random_word)
            index_start = 0
            for i in range(self.random_word.count(letter)):
                letter_index = self.random_word.index(letter, index_start)
                index_start = letter_index + 1
                self.word_to_guess[letter_index] = letter

        else:
            self.chances.decrease_chances()
            print(self.chances.get_chances())

