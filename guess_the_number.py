import random as ran

class GuessTheNumber:
    __HEALTH = 3
    __COIN = 0
    __ATTEMPT = 3

    def __init__(self, coin: int = None, attempt: int = None, attempt_const: int = None, health: int = None, health_const: int = None, min_number: int = 0, max_number: int = 9):
        self.__coin = self.__COIN if coin is None else coin
        self.__health = GuessTheNumber.__HEALTH if health is None else health
        GuessTheNumber.__HEALTH = GuessTheNumber.__HEALTH if health_const is None else health_const
        self.__attempt = GuessTheNumber.__ATTEMPT if attempt is None else attempt
        GuessTheNumber.__ATTEMPT = GuessTheNumber.__ATTEMPT if attempt_const is None else attempt_const
        self.min_number = min_number
        self.max_number = max_number
        self.__random_number = int(ran.randint(self.min_number, self.max_number))

    def reload(self):
        """Перезапуск если проиграли"""
        self.__coin = self.__COIN
        self.__health = self.__HEALTH
        self.__attempt = self.__ATTEMPT
        self.set_random_number()

    def set_random_number(self):
        self.__random_number = int(ran.randint(self.min_number, self.max_number))

    @property
    def const_attempt(self):
        return self.__ATTEMPT

    @const_attempt.setter
    def const_attempt(self, value):
        self.__ATTEMPT += value

    @property
    def const_health(self):
        return self.__HEALTH

    @const_health.setter
    def const_health(self, value):
        self.__HEALTH += value

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
        self.set_random_number()

    def to_dict(self):
        return {
            "__HEALTH" : self.__HEALTH,
            "__health" : self.__health,
            "__coin" : self.__coin,
            "__ATTEMPT" : self.__ATTEMPT,
            "__attempt" : self.__attempt
        }

    @staticmethod
    def from_dict(cls, dictionary = None):
        if dictionary is None:
            return cls()

        health = dictionary.get('__health')
        health_const = dictionary.get('__HEALTH')
        coin = dictionary.get('__coin')
        attempt = dictionary.get('__attempt')
        attempt_const = dictionary.get('__ATTEMPT')

        return GuessTheNumber(coin, attempt, attempt_const, health, health_const)