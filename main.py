from guess_the_number import GuessTheNumber
from purchases import Purchase

gtn = GuessTheNumber()
purchase = Purchase(gtn)

def game():
    print("Guess the number. Добро пожаловать в игру 'Угадай число'!")
    print("Правила очень просты. Машина загадывает, ты угадываешь!")
    print("За каждое угажанное число с трех попыток начисляется балы!")
    print("За каждый проигрышь, снимаются очки жизни. Всего их три!")


    end_game = False
    while True:
        random_number = gtn.random_number

        while True:
            print(f"Угадываемое число {random_number}")
            human_number = int(input("Введите число... "))

            if human_number == random_number:
                gtn.coin = 1
                gtn.reload_attempt()
                print(f"Угадал! Плюс бал! Сейчас на балансе {gtn.coin}")

                purchase.making_purchases() #Покупки

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
                        answer = input("Хотите начть игру заново? (Д/Н) ").lower().strip()
                        if answer in purchase.NEGATIVE_ANSWERS:
                            end_game = True
                            break
                        elif answer in purchase.POSITIVE_ANSWERS:
                            gtn.reload()
                            break
                        else:
                            continue

        if end_game:
            break


if __name__ == '__main__':
    game()