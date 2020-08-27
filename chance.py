class Chance:
    def __init__(self, chance):
        self.chances = chance

    def get_chances(self):
        return self.chances

    def decrease_chances(self):
        self.chances -= 1
        if self.chances == 0:
            pass
