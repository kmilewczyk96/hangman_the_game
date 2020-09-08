class Streak:
    def __init__(self):
        self.current_streak = 0

    def get_streak(self):
        return self.current_streak

    def increase_streak(self):
        self.current_streak += 1
