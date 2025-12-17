from enum import Enum

from guess_the_number import GuessTheNumber

class Purchases(Enum):
    RestoreHealth = 1
    AdditionalAttempt = 3
    AdditionalHealth = 5
    SaveTheGame = 10


def game():
    gtn = GuessTheNumber()


    print("Guess the number. Добро пожаловать в игру 'Угадай число'!")
    print("Правила очень просты. Машина загадывает, ты угадываешь!")
    print("За каждое угажанное число с трех попыток начисляется балы!")
    print("За каждый проигрышь, снимаются очки жизни. Всего их три!")


    end_game = False
    while True:
        random_number = -1
        random_number = gtn.random_number

        while True:
            print(f"Угадываемое число {random_number}")
            human_number = int(input("Введите число... "))

            if human_number == random_number:
                gtn.coin = 1
                gtn.reload_attempt()
                print(f"Угадал! Плюс бал! Сейчас на балансе {gtn.coin}")

                making_purchases(gtn) #Покупки

            elif human_number != random_number:
                if human_number > random_number:
                    print(f"Введённое число больше загаданного!")
                elif human_number < random_number:
                    print(f"Введённое число меньше загаданного!")
                gtn.attempt = -1

                if gtn.attempt == 0:
                    gtn.health = -1
                    print(f"У вас закончились попытки. Осталось {gtn.health} XP!")
                    gtn.reload_attempt()
                    if gtn.health == 0:
                        print(f"У вас не осталось XP!")
                        answer = input("Хотите начть игру заново? Напишите ответ Д/Н... ")
                        if answer.lower() == "н" or answer.lower() == "не" or answer.lower() == "нет":
                            end_game = True
                            break
                        elif answer.lower() == "д" or answer.lower() == "да":
                            gtn.reload()
                            break

        if end_game:
            break


def making_purchases(gtn: GuessTheNumber):
    """Реализация магазина"""
    while True:

        if gtn.coin == 0:
            break

        print("Покупки.")
        if gtn.coin >= Purchases.RestoreHealth.value:
            print("1. Восстановить здоровье на 1 - 1 бал")
        if gtn.coin >= Purchases.AdditionalAttempt.value:
            print("2. Купить дополнительную попытку для угадывания - 3 балов")
        if gtn.coin >= Purchases.AdditionalHealth.value:
            print("3. Купить дополнительное здоровье - 5 балов")
        if gtn.coin >= Purchases.SaveTheGame.value:
            print("4. Сохранить игру - 10 балов")
        print("Хотите совершить покупку?")

        answer = str(input("Введите для ответа Д/Н "))
        if answer.lower() == "н" or answer.lower() == "не" or answer.lower() == "нет":
            break

        while answer.lower() == "д" or answer.lower() == "да":
            print(f"Сейчас у вас {gtn.coin} бал(ов).")
            answer_buy = int(input("Введите номер раздела, который вы хотите оплатить... "))

            match answer_buy:
                case 1:
                    if checking_values(gtn.coin, Purchases.RestoreHealth.value):
                        gtn.health = 1
                        gtn.coin = -Purchases.RestoreHealth.value
                        break
                case 2:
                    if checking_values(gtn.coin, Purchases.AdditionalAttempt.value):
                        gtn.attempt = 1
                        gtn.coin = -Purchases.AdditionalAttempt.value
                        break
                case 3:
                    if checking_values(gtn.coin, Purchases.AdditionalHealth.value):
                        gtn.health = None
                        gtn.coin = -Purchases.AdditionalHealth.value
                        break
                case 4:
                    print("Функция ещё не добавлена! Ожидайте последующих обновлений!")
                case _:
                    print("Выбранный раздел не существует! Попробуйте выбрать другой для покупки!")


def checking_values(all_coin: int, coin: int):
    value = all_coin - coin

    if value < 0:
        print("У вас не достаточно балов, чтобы произвести покупку! Попробуйте выбрать другой раздел!")
    return all_coin - coin >= 0


if __name__ == '__main__':
    game()