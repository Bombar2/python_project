import random as ran
from enum import Enum

class Mode(Enum):
    ADD = 1
    REMOVE = 2
    RELOAD = 3

class GuessTheNumber:
    __HEALTH = 3
    __COIN = 0

    def __init__(self, min_number: int = 0, max_number: int = 100):
        self.__coin = 0
        self.__health = 3
        self.min_number = min_number
        self.max_number = max_number
        self.__random_number = ran.randint(min_number, max_number)

    @property
    def random_number(self):
        """getter for random number"""
        return self.__random_number

    @random_number.setter
    def random_number(self, value: int = None):
        """setter for random number"""
        self.__random_number = ran.randint(self.min_number, self.max_number)

    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, value: int = None):
        """setter for coin"""
        if value is not None:
            self.__coin += value
        else:
            self.__coin = self.__COIN

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, *, value = None, mode: Mode = Mode.REMOVE):
        if value is not None and mode == Mode.REMOVE:
            self.__health -= value
        elif mode == Mode.RELOAD:
            self.__health = self.__HEALTH
        else:
            self.__HEALTH += 1
