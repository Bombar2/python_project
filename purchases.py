from enum import Enum

from frames.UI.ui import TextLocaleEnum, UIElementEnum

from guess_the_number import GuessTheNumber


class Purchases(Enum):
    AdditionalAttempt = 3
    RestoreHealth = 5
    AdditionalHealth = 7
    SaveTheGame = 10



def restore_health(gtn: GuessTheNumber):
    if gtn.health < gtn.const_health:
        gtn.health = 1
        gtn.coin = -Purchases.RestoreHealth.value

def by_attempt(gtn: GuessTheNumber):
    gtn.attempt = 1
    gtn.const_attempt = 1
    gtn.coin = -Purchases.AdditionalAttempt.value

def by_health(gtn: GuessTheNumber):
    gtn.const_health = 1
    gtn.coin = -Purchases.AdditionalHealth.value

def save_game(gtn: GuessTheNumber):
    pass


PURCHASES_ACTIONS = {
        1: restore_health,
        2: by_attempt,
        3: by_health,
        4: save_game
    }


class PurchaseDict:
    __TEXT_UI = {
        UIElementEnum.PURCHASE_HEALTH.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Дополнительная попытка.",
                TextLocaleEnum.ENGLISH: "Additional attempt."
            },
            "value": "3",
            "action": by_attempt
        },
        UIElementEnum.PURCHASE_ATTEMPT.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Восстановить здоровье на единицу.",
                TextLocaleEnum.ENGLISH: "Restore health by one."
            },
            "value": "5",
            "action": restore_health
        },
        UIElementEnum.PURCHASE_HEALTH_CONST.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Дополнительное здоровье в начале игры.",
                TextLocaleEnum.ENGLISH: "Extra health at the start of the game."
            },
            "value": "7",
            "action": by_health
        },
        UIElementEnum.PURCHASE_SAVE_GAME.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Сохранить игру.",
                TextLocaleEnum.ENGLISH: "Save the game."
            },
            "value": "10",
            "action": save_game
        }
    }

    def __init__(self, locale:TextLocaleEnum = None, default_locale=TextLocaleEnum.RUSSIAN):
        self._default_locale = locale if locale is not None else default_locale

    def get_text_locale(self, ui_element: UIElementEnum, locale:TextLocaleEnum = None) -> str:
        if locale is None:
            locale = self._default_locale

        try:
            element = self.__TEXT_UI[ui_element.value]
            locales = element["locale"]

            return locales.get(locale) or locales.get(self._default_locale)
        except (KeyError, StopIteration):
            return f"[{ui_element.value}]"

    def get_ui_value(self, ui_element_id: UIElementEnum) -> str:
        return self.__TEXT_UI.get(ui_element_id.value, {}).get("value", "")

    def get_locale(self):
        return self._default_locale

    def run_action(self, ui_element: UIElementEnum, gtn: GuessTheNumber):
        self.__TEXT_UI.get(ui_element.value, {}).get("action")(gtn)




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

