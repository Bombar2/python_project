from guess_the_number import GuessTheNumber


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





if __name__ == '__main__':
    game()


def pocupci(gtn: GuessTheNumber):
    while True:

        if gtn.coin == 0:
            break

        print("Покупки.")
        if gtn.coin >= 1:
            print("1. Восстановить здоровье на 1 - 1 бал")
        if gtn.coin >= 5:
            print("2. Купить дополнительную попытку для угадывания - 5 балов")
            print("3. Купить дополнительное здоровье - 5 балов")
        if gtn.coin >= 10:
            print("4. Сохранить игру - 10 балов")
        print("Хотите совершить покупку?")
        answer = str(input("Введите для ответа Д/Н "))
        if answer.lower() == "н" or answer.lower() == "не" or answer.lower() == "нет":
            break

        while answer.lower() == "д" or answer.lower() == "да":
            coin = int(input(f"Сейчас у вас {gtn.coin} бал(ов). "
                             f"Введите количество балов, которое хотите потратить... "))
            answer_buy = int(input("Введите номер раздела, который вы хотите оплатить... "))

            if coin > gtn.coin:
                print("У вас нет такого количества балов. Попробуйте ввести количество балов снова.")
            else:
                match answer_buy:
                    case 1:
                        gtn.health = 1
                        gtn.coin = -1
                        break
                    case 2:
                        gtn.attempt = 1
                        gtn.coin = -5
                        break
                    case 3:
                        gtn.health = None
                        gtn.coin = -5
                        break
                    case 4:
                        print("Функция ещё не добавлена! Ожидайте последующих обновлений!")

