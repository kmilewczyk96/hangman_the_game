from abc import ABC, abstractmethod


class AbstractLevel(ABC):
    @abstractmethod
    def get_chances(self):
        pass

    @staticmethod
    @abstractmethod
    def get_name():
        pass
