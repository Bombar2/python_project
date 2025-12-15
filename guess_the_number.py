import random as ran

class GuessTheNumber:
    __HEALTH = 3
    __COIN = 0
    __ATTEMPT = 3

    def __init__(self, min_number: int = 0, max_number: int = 5):
        self.__coin = self.__COIN
        self.__health = self.__HEALTH
        self.__attempt = self.__ATTEMPT
        self.min_number = min_number
        self.max_number = max_number
        self.__random_number = int(ran.randint(self.min_number, self.max_number))

    def reload(self):
        """Перезапуск если проиграли"""
        self.__coin = self.__COIN
        self.__health = self.__HEALTH
        self.__attempt = self.__ATTEMPT
        self.__random_number = int(ran.randint(self.min_number, self.max_number))

    @property
    def random_number(self):
        """getter for random number"""
        return self.__random_number

    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, value: int):
        """setter for coin"""
        self.__coin += value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        self.__health += value

    @property
    def attempt(self):
        return self.__attempt

    @attempt.setter
    def attempt(self, value: int):
        """setter for attempt"""
        self.__attempt += value

    def reload_attempt(self):
        self.__attempt = self.__ATTEMPT