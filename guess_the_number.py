import random as ran


class GuessTheNumber:
    __HEALTH = 3
    __COIN = 0

    def __init__(self, min_number: int = 0, max_number: int = 100):
        self.__random_number = ran.uniform(min_number, max_number)
        self.__coin = 0
        self.__health = 3

        @property
        def random_number():
            """getter for random number"""
            return self.__random_number

        @property
        def coin():
            return self.__coin

        @coin.setter
        def coin(*, value = None):
            """setter for coin"""
            if value is not None:
                self.__coin += value
            else:
                self.__coin = self.__COIN

        @property
        def health():
            return self.__health

        @health.setter
        def health(*, value = None):
            if value is not None:
                self.__health -= value
            else:
                self.__health = self.__HEALTH


        def game():
            print("Guess the number. Добро пожаловать в игру 'Угадай число'!")
            print("Правила очень просты. Машина загадывает, ты угадываешь!")
            print("За каждое угажанное число с трех попыток начисляется балы!")
            print("За каждый проигрышь, снимаются очки жизни. Всего их три!")
            while True:
