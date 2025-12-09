import random as ran


class GuessTheNumber:
    __HEALTH = 3
    __COIN = 0

    def __init__(self, min_number: int = 0, max_number: int = 100):
        self.__random_number = ran.uniform(min_number, max_number)
        self.__coin = 0
        self.__health = 3

    @property
    def random_number(self):
        """getter for random number"""
        return self.__random_number

    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, *, value = None):
        """setter for coin"""
        if value is not None:
            self.__coin += value
        else:
            self.__coin = self.__COIN

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, *, value = None):
        if value is not None:
            self.__health -= value
        else:
            self.__health = self.__HEALTH


    def game(self):
        print("Guess the number. Добро пожаловать в игру 'Угадай число'!")
        print("Правила очень просты. Машина загадывает, ты угадываешь!")
        print("За каждое угажанное число с трех попыток начисляется балы!")
        print("За каждый проигрышь, снимаются очки жизни. Всего их три!")

        human_number = input("Введите число... ")

        print(human_number)
