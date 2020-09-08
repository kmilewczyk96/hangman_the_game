class ChancesError(ValueError):
    pass


class Chance:
    def __init__(self, chance):
        self.chances = chance
        self.initial_chances = chance

    def get_chances(self):
        return self.chances

    def decrease_chances(self):
        self.chances -= 1
        if self.chances == 0:
            raise ChancesError

    def reset_chances(self):
        self.chances = self.initial_chances
