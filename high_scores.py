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

    def update_score(self, name, score, place):
        score = str(score)
        if len(score) < 4:
            score = score.rjust(4)
        score_list = self.get_scores()
        with open(f'{self.get_path()}/high_scores.txt', 'r+') as file:
            for i in range(1, self.high_scores_count + 1):
                if i == place:
                    if i < 5:
                        file.write(f"{name} | {score}\n")
                    else:
                        file.write(f"{name} | {score}")
                if i < 5:
                    file.write(score_list[i - 1] + '\n')
        self.high_scores_list = []

    def check_score(self, score):
        with open(f'{self.get_path()}/high_scores.txt', 'r') as file:
            for i in range(1, self.high_scores_count + 1):
                high_score = int(file.readline().strip('\n')[5:])
                print(high_score)
                if score > high_score:
                    return i


if __name__ == '__main__':
    default = HighScores()
    default.update_score('DEF', 500, 1)
    default.update_score('DEF', 400, 2)
    default.update_score('DEF', 300, 3)
    default.update_score('DEF', 200, 4)
    default.update_score('DEF', 100, 5)
    print(default.get_scores())
