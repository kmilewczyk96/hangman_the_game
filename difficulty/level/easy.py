from difficulty.abstract_level import AbstractLevel


class Easy(AbstractLevel):
    @staticmethod
    def get_name():
        return 'EASY'

    @staticmethod
    def get_chances():
        return 15

    @staticmethod
    def get_multiplier():
        return 50
