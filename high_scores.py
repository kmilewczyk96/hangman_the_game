import os


class HighScores:
    def __init__(self):
        self.high_scores_count = 5
        self.high_scores_list = []

    @staticmethod
    def get_path():
        return os.path.abspath(os.path.dirname(__file__))

    def get_scores(self):
        with open(f'{self.get_path()}/high_scores.txt', 'r') as file:
            for i in range(1, self.high_scores_count + 1):
                high_score = file.readline().strip('\n')
                self.high_scores_list.append(high_score)
        return self.high_scores_list


# if __name__ == '__main__':
#     score = HighScores()
#     for i in range(score.high_scores_count):
#         print(score.get_scores()[i])
