from enum import Enum
from functools import partial

from guess_the_number import GuessTheNumber


class Purchases(Enum):
    RestoreHealth = 1
    AdditionalAttempt = 3
    AdditionalHealth = 5
    SaveTheGame = 10


def __restore_health(gtn: GuessTheNumber):
    gtn.health = 1
    gtn.coin = -Purchases.RestoreHealth.value

def __by_attempt(gtn: GuessTheNumber):
    gtn.attempt = 1
    gtn.coin = -Purchases.AdditionalAttempt.value

def __by_health(gtn: GuessTheNumber):
    gtn.health = None
    gtn.coin = -Purchases.AdditionalHealth.value

def __save_game(gtn: GuessTheNumber):
    pass


PURCHASES_ACTIONS = {
        1: __restore_health,
        2: __by_attempt,
        3: __by_health,
        4: __save_game
    }


class Purchase:
    POSITIVE_ANSWERS = {"д", "да", "yes", "y"}
    NEGATIVE_ANSWERS = {"н", "нет", "no", "n"}

    CONFIG_LIST = {
        1: {
            "name": "Восстановить здоровье на единицу.",
            "cost": Purchases.RestoreHealth.value,
            "action": 1
        },
        2: {
            "name": "Дополнительная попытка.",
            "cost": Purchases.AdditionalAttempt.value,
            "action": 2
        },
        3: {
            "name": "Дополнительное здоровье на начало игры.",
            "cost": Purchases.AdditionalHealth.value,
            "action": 3
        },
        4: {
            "name": "Сохранить игру.",
            "cost": Purchases.SaveTheGame.value,
            "action": 4
        }
    }


    def __init__(self, gtn: GuessTheNumber):
        self.gtn = gtn
        self.purchases_list = self._create_purchases_list()


    def _create_purchases_list(self):
        purchases = {}
        for idx, config in self.CONFIG_LIST.items():
            purchases[idx] = {
                **config,
                "action": partial(
                    PURCHASES_ACTIONS[config["action"]],
                    self.gtn
                )
            }
        return purchases


    @property
    def purchase_gtn(self):
        return self.gtn


    def making_purchases(self):
        while True:
            print(f"\n{'='*30}")
            print(f"Магазин (Баланс: {self.gtn.coin} бал(ов)")
            print('='*30)


            print("\n0. Выйти из магазина.")

            available_purchases = []
            for idx, purchase in self.purchases_list.items():
                if self.gtn.coin >= purchase["cost"]:
                    print(f"{idx}. {purchase['name']} - {purchase['cost']} бал(ов).")
                    available_purchases.append(idx)

            if not available_purchases:
                print("\nУ вас не достаточно баллов для покупок.")
                break

            choice = input("\nВыберите номер покупки (или 0 для выхода): ").strip()

            if choice == "0":
                break


            try:
                choice_num = int(choice)


                selected = self.purchases_list[choice_num]


                if not selected:
                    print("Такого варианта не существует.")
                    continue


                if self.gtn.coin < selected["cost"]:
                    print(f"Недостаточно балов! Нужно {selected['cost']}, у вас {self.gtn.coin}.")
                    continue


                confirm = input(f"Купить '{selected['name']}' за {selected['cost']} балов? (Д/Н) ").strip().lower()


                if confirm not in self.POSITIVE_ANSWERS:
                    print("Покупка отменена.")
                    continue


                selected['action']()
                print(f"Покупка успешна! Новый баланс: {self.gtn.coin} балов.")

            except ValueError:
                print("Пожалуйста, введите число!")

