from enum import Enum

from guess_the_number import GuessTheNumber
from purchases import Purchase

class LaunchEnum(Enum):
    LAUNCH_IN_CONSOLE = 1
    LAUNCH_IN_ACTIVITY = 2

class AnswerEnum(Enum):
    ANSWER_SUCCESS = "УСПЕХ!"
    ANSWER_FAILURE = "ПРОВАЛ!"


class Game:
    def __init__(self, launch_enum: LaunchEnum = LaunchEnum.LAUNCH_IN_CONSOLE):
        self.gtn = GuessTheNumber()
        self.purchase = Purchase(self.gtn)
        self.launch_enum = launch_enum
        self.end_game = False

    def get_coin(self):
        return self.gtn.coin

    def get_purchases_dict(self):
        return  self.purchase.purchases_list

    def show_welcome_message(self):
        """Вывод приветственного сообщения."""
        messages = [
            "Guess the number. Добро пожаловать в игру 'Угадай число'!",
            "Правила очень просты. Машина загадывает, ты угадываешь!",
            "За каждое угаданное число с трёх попыток начисляются баллы!",
            "За каждый проигрыш снимаются очки жизни. Всего их три!"
        ]
        for message in messages:
            print(message)

    def get_user_input(self, prompt: str) -> int:
        """Безопасное получение числа от пользователя."""
        while True:
            try:
                return int(input(prompt)) if self.launch_enum == LaunchEnum.LAUNCH_IN_CONSOLE else int(prompt)
            except ValueError:
                print("Пожалуйста, введите целое число!")

    def check_user_guess(self, user_guess: int, target_number: int = None) -> bool:
        """Проверяет предположение пользователя и даёт подсказку"""

        if user_guess == (target_number if target_number is not None else self.gtn.random_number):
            return True

        if (self.launch_enum == LaunchEnum.LAUNCH_IN_CONSOLE and
                self.check_user_guess_more(user_guess, target_number)):
            print("Ваше число больше загаданного!")
        else:
            print("Ваше число меньше загазанного!")

        return False

    def check_user_guess_more(self, user_guess: int, target_number: int = None) -> bool:
        if user_guess > (target_number if target_number is not None else self.gtn.random_number):
            return True
        return False

    def handle_correct_guess(self):
        self.gtn.coin = 1
        self.gtn.reload_attempt()
        print(f"Угадал! +1 бал! Баланс: {self.gtn.coin}")

        if (self.launch_enum == LaunchEnum.LAUNCH_IN_CONSOLE and
                self.gtn.coin > 0):
            self.offer_purchases()

    def handle_wrong_guess(self):
        self.gtn.attempt = -1
        if self.gtn.attempt == 0:
            self.handle_out_of_attempts()

    def offer_purchases(self):
        """Предлагает покупки в магазине"""
        answer = input("Хотите зайти в магазин? (Д/Н) ").lower().strip()
        if answer in self.purchase.POSITIVE_ANSWERS:
            self.purchase.making_purchases()

    def handle_out_of_attempts(self):
        """Обработка если количество попыток равна 0"""
        self.gtn.health = -1
        print(f"Попытки закончились. Осталось жизней: {self.gtn.health}")

        self.gtn.reload_attempt()

        if self.gtn.health == 0:
            self.handle_game_over()

    def handle_game_over(self):
        """Обработка конца игры"""

        if self.launch_enum == LaunchEnum.LAUNCH_IN_CONSOLE:
            print("\n" + "="*30)
            print("ИГРА ОКОНЧЕНА! У вас не осталось жизней!")
            print("="*30)

            while True:
                answer = input("Хотите началь игру заново? (Д/Н) ").lower().strip()

                if answer in self.purchase.NEGATIVE_ANSWERS:
                    self.end_game = True
                    break
                elif answer in self.purchase.POSITIVE_ANSWERS:
                    self.gtn.reload()
                    print("\n" + "=" * 40)
                    print("НОВАЯ ИГРА НАЧАТА!")
                    print("=" * 40)
                    break
                else:
                    print("Пожалуйста, ответьте Д (Да) или Н (Нет)")
        else:
            self.gtn.reload()

    def play_round(self):

        random_number = self.gtn.random_number

        if self.launch_enum == LaunchEnum.LAUNCH_IN_CONSOLE:
            print(f"\n{'=' * 30}")
            print(f"НОВОЕ ЧИСЛО ЗАГАДАНО!")
            print(f"У вас: {self.gtn.attempt} попыток, {self.gtn.health} жизней")
            print(f"Баланс: {self.gtn.coin} баллов")
            print('=' * 30)

            while self.gtn.attempt > 0 and not self.end_game:
                try:
                    human_number = self.get_user_input("Введите число: ")

                    if self.check_user_guess(human_number, random_number):
                        self.handle_correct_guess()
                        break
                    else:
                        self.handle_wrong_guess()
                        print(f"Осталось попыток: {self.gtn.attempt}")
                except KeyboardInterrupt:
                    print("\n\n Игра прервана пользователем.")
                    self.end_game = True
                    break

    def run(self):
        """Запуск игры"""
        self.show_welcome_message()

        while not self.end_game:
            self.play_round()
