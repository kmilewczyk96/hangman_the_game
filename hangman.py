from chance import ChancesError


class Hangman:
    def __init__(self, word, chance, streak, multiplier):
        self.alphabet = [i for i in range(97, 123)]
        self.random_word = word.get_random_word().upper()
        self.word_to_guess = ['_' if i != '-' else '-' for i in self.random_word]
        self.aesthetic_word_to_guess = ['_' if i != '-' else '-' for i in self.random_word]
        self.used_letters_row_1 = []
        self.used_letters_row_2 = []
        self.capacity = 0
        self.chances = chance
        self.streak = streak
        self.multiplier = multiplier

    def check(self, letter):
        if letter in self.random_word:
            print(self.random_word)
            index_start = 0
            for i in range(self.random_word.count(letter)):
                letter_index = self.random_word.index(letter, index_start)
                index_start = letter_index + 1
                self.word_to_guess[letter_index] = letter

            if '_' not in self.word_to_guess:
                self.streak.increase_streak()
                self.chances.reset_chances()
                return 'win'

        else:
            if letter not in self.used_letters_row_1 and letter not in self.used_letters_row_2:
                if self.capacity < 11:
                    self.used_letters_row_1.append(letter)
                    self.capacity += 1
                else:
                    self.used_letters_row_2.append(letter)
                try:
                    self.chances.decrease_chances()
                except ChancesError:
                    hi_score = self.streak.get_streak() * self.multiplier.get_multiplier()
                    print(hi_score)
                    return 'loose'
