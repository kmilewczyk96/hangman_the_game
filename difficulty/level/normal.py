from difficulty.abstract_level import AbstractLevel


class Normal(AbstractLevel):
    @staticmethod
    def get_name():
        return 'NORMAL'

    @staticmethod
    def get_chances():
        return 12

    @staticmethod
    def get_multiplier():
        return 100


