import json

from frames.UI.ui import TextLocaleEnum, UIElementEnum, TextUI
from frames.factory import Factory
from frames.top_menu_bar import TopMenuButtons
from guess_the_number import GuessTheNumber
from purchases import PurchaseDict


class Game:
    def __init__(self, locale: TextLocaleEnum = TextLocaleEnum.RUSSIAN, height: int = 600, width: int = 500):
        self.__gtn = GuessTheNumber()
        self.__human_number = "0"
        self._text_ui = TextUI(locale=locale)

        self._main_coordinator = Factory.create_main_activity_default(height, width, locale=self._text_ui.get_locale())
        """TopMenuButtons(self._main_coordinator.get_root(),
                       {
                           "new_game" : self.click_button_menu_new_game,
                           "save_game" : self.click_button_menu_save_game,
                           "download_game" : self.click_button_menu_download_game
                       })"""
        self._main_coordinator.create_main_frame()

        self._status_coordinator = Factory.create_status_frame_default(self._main_coordinator.get_main_frame(), locale=self._text_ui.get_locale())
        self._status_coordinator.update_currency_status_health(self.__gtn.health)
        self._status_coordinator.update_currency_status_attempts(self.__gtn.attempt)

        self._numeric_keypad_coordinator = Factory.create_numeric_keypad_default(self._main_coordinator.get_main_frame(), locale=self._text_ui.get_locale())

        self._numeric_keypad_coordinator.set_buttons_callback({
            UIElementEnum.NUMERIC_BUTTON.value: self._numeric_button_click,
            UIElementEnum.ZERO_BUTTON.value: self._numeric_button_click,
            UIElementEnum.ENTER_BUTTON.value: self._numeric_button_click,
            UIElementEnum.CLEAR_BUTTON.value: self._numeric_button_click,
        })
        self._purchases_coordinator = Factory.create_purchases_frame_default(self._main_coordinator.get_main_frame(), locale=self._text_ui.get_locale())
        self._purchases_coordinator.create_shop_buttons({
            UIElementEnum.PURCHASE_HEALTH: self._purchase_button_click,
            UIElementEnum.PURCHASE_ATTEMPT: self._purchase_button_click,
            UIElementEnum.PURCHASE_HEALTH_CONST: self._purchase_button_click,
            UIElementEnum.PURCHASE_SAVE_GAME: self._purchase_button_click
        })
        self._purchases_coordinator.update_button_state(0) # после поставить 0

        self._main_coordinator.run()


    def _purchase_button_click(self, btn_id: UIElementEnum):
        PurchaseDict().run_action(btn_id, self.__gtn)
        self._update_status()

    def _numeric_button_click(self, value):
        if value == UIElementEnum.CLEAR_BUTTON.value:
            self._clear_button_click()
        elif value == UIElementEnum.ENTER_BUTTON.value:
            self._enter_button_click()
        else:
            if len(self.__human_number) < 2:
                if int(self.__human_number) == 0:
                    if value != 0:
                        self.__human_number = str(value)
                        self._status_coordinator.update_currency_number_field(int(self.__human_number))
                else:
                    self.__human_number += str(value)
                    self._status_coordinator.update_currency_number_field(int(self.__human_number))



    def _update_status(self):
        self._status_coordinator.update_currency_status_health(self.__gtn.health)
        self._status_coordinator.update_currency_status_attempts(self.__gtn.attempt)
        self._purchases_coordinator.update_coin(self.__gtn.coin)

    def _enter_button_click(self):
        if len(self.__human_number) > 0:
            if self.__gtn.random_number == int(self.__human_number):
                self._handle_correct_guess()

            elif self.__gtn.random_number > int(self.__human_number):
                self._numeric_keypad_coordinator.show_hint(int(self.__human_number), False)
                self._handle_wrong_guess()

            elif self.__gtn.random_number < int(self.__human_number):
                self._numeric_keypad_coordinator.show_hint(int(self.__human_number), True)
                self._handle_wrong_guess()

        self._update_status()
        self._clear_button_click()

        self._purchases_coordinator.update_button_state(self.__gtn.coin)

    def _clear_button_click(self):
        self._status_coordinator.update_currency_number_field(0)
        self.__human_number = "0"

    def _handle_correct_guess(self):
        self.__gtn.coin = 1
        self.__gtn.reload_attempt()
        self._numeric_keypad_coordinator.reset_hint()

    def _handle_wrong_guess(self):
        self.__gtn.attempt = -1
        if self.__gtn.attempt == 0:
            self.handle_out_of_attempts()

    def handle_out_of_attempts(self):
        self.__gtn.health = -1

        self.__gtn.reload_attempt()

        self._numeric_keypad_coordinator.reset_hint()

        if self.__gtn.health == 0:
            self.handle_game_over()

    def handle_game_over(self):
        self.__gtn.reload()
        self._update_status()

    def click_button_menu_save_game(self):
        dictionary = self.__gtn.to_dict()
        with open("saves/save.json", "w", encoding='utf-8') as file:
            json.dump(dictionary, file, indent=2, ensure_ascii=False)

    def click_button_menu_download_game(self):
        dictionary = {}

        with open("saves/save.json", "r", encoding='utf-8') as file:
            dictionary = json.load(file)

        self.__gtn = GuessTheNumber.from_dict(self.__gtn, dictionary)

        self._update_status()
        self._purchases_coordinator.update_button_state(self.__gtn.coin)

    def click_button_menu_new_game(self):
        self.__gtn.reload()

        self._update_status()
        self._purchases_coordinator.update_button_state(self.__gtn.coin)