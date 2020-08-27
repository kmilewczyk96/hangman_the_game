from difficulty.abstract_level import AbstractLevel


class Hard(AbstractLevel):
    def get_chances(self):
        return 9

    @staticmethod
    def get_name():
        return 'Hard'
