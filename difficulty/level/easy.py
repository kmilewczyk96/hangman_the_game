from difficulty.abstract_level import AbstractLevel


class Easy(AbstractLevel):
    def get_chances(self):
        return 15

    @staticmethod
    def get_name():
        return 'EASY'
