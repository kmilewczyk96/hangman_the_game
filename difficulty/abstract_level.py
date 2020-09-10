from abc import ABC, abstractmethod


class AbstractLevel(ABC):
    @staticmethod
    @abstractmethod
    def get_name():
        pass

    @staticmethod
    @abstractmethod
    def get_chances():
        pass

    @staticmethod
    @abstractmethod
    def get_multiplier():
        pass
