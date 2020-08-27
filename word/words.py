from random import randint
import os


class WordsFromFile:
    @staticmethod
    def get_path():
        return os.path.abspath(os.path.dirname(__file__))

    def get_random_word(self):
        words_in_file = self.get_words_count()
        word_number = randint(1, words_in_file)
        return self.get_word_from_file(word_number).strip('\n')

    def get_word_from_file(self, word_number):
        with open(f'{self.get_path()}/words.txt', 'r') as file:
            for i in range(1, word_number + 1):
                word = file.readline()
        return word

    def get_words_count(self):
        words_in_file = 0
        with open(f'{self.get_path()}/words.txt', 'r') as file:
            while file.readline():
                words_in_file += 1

        return words_in_file
