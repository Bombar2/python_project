from tkinter import *
from tkinter import ttk

import json

from frames.numeric_keypad.numeric_keypad_coordinator import NumericKeypadCoordinator
from game import Game, LaunchEnum, AnswerEnum
from frames.top_menu_bar import TopMenuButtons
from frames.purchases_frame import PurchasesFrame
from frames.factory import Factory
from frames.UI.ui import UIElementEnum, TextUI, TextLocaleEnum

class MainActivity:
    __MAIN_ACTIVITY_TITLE: str = "Gues the number"
    __MAIN_ACTIVITY_ICON_PATH: str = "res/search.png"

    def __init__(self):
        self.game = Game(launch_enum=LaunchEnum.LAUNCH_IN_ACTIVITY)
        self._textUI = TextUI(TextLocaleEnum.RUSSIAN)

        __TOP_MENU_BUTTONS_CALLBACKS = {
            "new_game": self.click_button_menu_new_game,
            "save_game": self.click_button_menu_save_game,
            "download_game": self.click_button_menu_download_game,
            "statistic_game": self.click_button_menu_statistic,
            "style_game": self.click_button_menu_style
        }

        self.shop_buttons = []

        root = Tk()
        root.geometry("600x500")
        root.resizable(False, False)

        root.title(self.__MAIN_ACTIVITY_TITLE)

        self.set_main_activity_icon(root, self.__MAIN_ACTIVITY_ICON_PATH) #Выставление иконки.


        #self.create_top_menu(root)
        """Создаю верхнее меню"""
        self.top_menu_buttons = TopMenuButtons(root, __TOP_MENU_BUTTONS_CALLBACKS)

        main_frame = ttk.Frame(root, padding=10)
        main_frame.pack(fill="both", expand=True)

        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        """Новая версия создания интерфейса статусного окна и поля ввода числа"""
        self._status_coordinator = Factory.create_status_frame_default(main_frame)
        self._status_coordinator.update_currency_status_attempts(self.game.gtn.attempt)
        self._status_coordinator.update_currency_status_health(self.game.gtn.health)
        """Новая версия создания интерфейса статусного окна и поля ввода числа"""


        """Новая версия. Создание фрейма с цифровой клавиатурой и кнопок ввод/очистка"""
        self._numeric_keypad_coordinator = NumericKeypadCoordinator(main_frame)
        self._numeric_keypad_coordinator.set_buttons_callback({
            UIElementEnum.NUMERIC_BUTTON.value: self.click,
            UIElementEnum.ZERO_BUTTON.value: self.click,
            UIElementEnum.ENTER_BUTTON.value: self.enter,
            UIElementEnum.CLEAR_BUTTON.value: self.clear,
        })
        """Новая версия. Создание фрейма с цифровой клавиатурой и кнопок ввод/очистка"""


        """Новая версия. Создание фрейма отображения балов и магазина покупок."""
        self._purchases_coordinator = Factory.create_purchases_frame_default(main_frame)
        self._purchases_coordinator.create_shop_buttons({
            UIElementEnum.PURCHASE_HEALTH : self.click_button_shop,
            UIElementEnum.PURCHASE_ATTEMPT : self.click_button_shop,
            UIElementEnum.PURCHASE_HEALTH_CONST : self.click_button_shop,
            UIElementEnum.PURCHASE_SAVE_GAME : self.click_button_shop
        })
        self._purchases_coordinator.update_button_state(self.game.get_coin())
        """Новая версия. Создание фрейма отображения балов и магазина покупок."""


        root.mainloop()


    def click(self, value):
        if (self._status_coordinator.get_currency_number_field_text() == AnswerEnum.ANSWER_SUCCESS or
                self._status_coordinator.get_currency_number_field_text() == AnswerEnum.ANSWER_FAILURE):
            self.clear()

        if (value not in self._textUI.get_text_locale(UIElementEnum.ENTER_BUTTON)
                and value not in self._textUI.get_text_locale(UIElementEnum.CLEAR_BUTTON)):
            if (value == self._textUI.get_ui_value(UIElementEnum.ZERO_BUTTON)
                    and self.game.human_number == self._textUI.get_ui_value(UIElementEnum.ZERO_BUTTON)):
                pass
            else:
                self.game.human_number = value
                self._status_coordinator.update_currency_number_field(int(self.game.human_number))

    def click_button_shop(self, index):

        price = int(self._textUI.get_ui_value(index))

        self.game.gtn.const_attempt = 1
        self.game.gtn.coin = -price

        self._purchases_coordinator.update_button_state(self.game.get_coin())

        pass



    def click_button_menu_new_game(self):
        pass

    def click_button_menu_save_game(self):
        dictionary = self.game.gtn.to_dict()
        with open("saves/save.json", "w", encoding='utf-8') as file:
            json.dump(dictionary, file, indent=2, ensure_ascii=False)


    def click_button_menu_download_game(self):
        pass

    def click_button_menu_statistic(self):
        pass

    def click_button_menu_style(self):
        pass

    def enter(self):
        if len(self.game.human_number) > 0:
            number = self.game.get_user_input(self.game.human_number)

            if self.game.check_user_guess(number):
                self.game.handle_correct_guess() #Обработка корректного ответа
                self._numeric_keypad_coordinator.reset_hint()
                pass ##Здесь обработка если пользователь угадал.
            elif self.game.check_user_guess_more(number):
                self.game.handle_wrong_guess()
                self._numeric_keypad_coordinator.show_hint(number, True)
                pass ##Если введённое число больше, выводим информацию, что угадываемое меньше.
            else:
                self.game.handle_wrong_guess()
                self._numeric_keypad_coordinator.show_hint(number, False)
                pass ##Если введённое число меньше угадываемого.


            if self.game.check_attempt():
                self._numeric_keypad_coordinator.reset_hint()

            self._purchases_coordinator.update_coin(self.game.get_coin())
            self.update_status()
            self._purchases_coordinator.update_button_state(self.game.get_coin())

    def clear(self):
        self.game.human_number_reset()
        self._status_coordinator.update_currency_number_field(int(self._textUI.get_ui_value(UIElementEnum.ZERO_BUTTON)))

    def update_status(self):
        self.game.human_number_reset()
        self._status_coordinator.update_currency_status_health(self.game.gtn.health)
        self._status_coordinator.update_currency_status_attempts(self.game.gtn.attempt)
        self._status_coordinator.update_currency_number_field(int(self._textUI.get_ui_value(UIElementEnum.ZERO_BUTTON)))


    def set_main_activity_icon(self, root, file_path):
        """Выставление иконки главного окна, если не будет найдена, ничего не делает"""
        try:
            icon = PhotoImage(file=file_path)
            root.iconphoto(False, icon)
        except FileNotFoundError:
            print("Иконка не найдена!")



