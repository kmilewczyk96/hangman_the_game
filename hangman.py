import pygame
from chance import Chance
from difficulty.game_level import GameLevel
from word.words import WordsFromFile


class Hangman:
    def __init__(self, word, chance):
        self.alphabet = [i for i in range(97, 123)]
        self.random_word = word.get_random_word()
        self.chances = chance
        self.picked_word = ['_' for i in self.random_word]

    def play(self):
        pass


word1 = WordsFromFile()
chance1 = GameLevel(Chance).get_level_chances()
Hangman(word1, chance1).play()
