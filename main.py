from guess_the_number import GuessTheNumber


def game():
    gtn = GuessTheNumber()
    random_number = gtn.random_number

    print("Guess the number. Добро пожаловать в игру 'Угадай число'!")
    print("Правила очень просты. Машина загадывает, ты угадываешь!")
    print("За каждое угажанное число с трех попыток начисляется балы!")
    print("За каждый проигрышь, снимаются очки жизни. Всего их три!")

    while True:
        print(f"Угадываемое число {random_number}")
        human_number = int(input("Введите число... "))

        if human_number == random_number:
            gtn.coin = 1
            print(f"Угадал! Плюс бал! Сейчас на балансе {gtn.coin}")

            while True:
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

                while answer == "Д":
                    coin = int(input("Введите количество балов, которое хотите потратить."))
                    answer = int(input("Введите номер раздела, который вы хотите оплатить."))

                    if coin > gtn.coin:
                        print("У вас нет такого количества балов. Попробуйте ввести количество балов снова.")
                    else:
                        match answer:
                            case 1:
                                gtn.health = 1
                            case 2:







if __name__ == '__main__':
    game()


