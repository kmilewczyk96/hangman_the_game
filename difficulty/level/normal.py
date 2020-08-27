from difficulty.abstract_level import AbstractLevel


class Normal(AbstractLevel):
    def get_chances(self):
        return 12

    @staticmethod
    def get_name():
        return 'Normal'
