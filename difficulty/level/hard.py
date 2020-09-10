from difficulty.abstract_level import AbstractLevel


class Hard(AbstractLevel):
    @staticmethod
    def get_name():
        return 'HARD'

    @staticmethod
    def get_chances():
        return 9

    @staticmethod
    def get_multiplier():
        return 150
