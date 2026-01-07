from enum import Enum
from typing import Optional


class UIElementEnum(Enum):
    STATUS_FRAME_TEXT = "status_game_text"
    STATUS_HEALTH = "status_health"
    STATUS_ATTEMPT = "status_attempt"
    ENTER_NUMBER = "enter_number"
    NUMBER_FIELD = "number_field"
    NUMERIC_FRAME_TEXT = "numeric_frame_text"
    NUMERIC_BUTTON = "numeric_button"
    CLEAR_BUTTON = "clear_button"
    ENTER_BUTTON = "enter_button"
    ZERO_BUTTON = "zero_button"
    GAME_CURRENCY_TEXT = "game_currency_text"
    GAME_CURRENCY = "game_currency"
    COINS_CURRENCY_TEXT = "coins_currency_text"

    PURCHASE_HEALTH = "purchase_health"
    PURCHASE_ATTEMPT = "purchase_attempt"
    PURCHASE_HEALTH_CONST = "purchase_health_const"
    PURCHASE_SAVE_GAME = "purchase_save_game"

    MAIN_ACTIVITY_TITLE = "main_activity_title"

class TextLocaleEnum(Enum):
    RUSSIAN = "ru"
    ENGLISH = "en"
    FRENCH = "fr"

class TextUI:
    __TEXT_UI = {
        UIElementEnum.MAIN_ACTIVITY_TITLE.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN.value: "Угадай число!",
                TextLocaleEnum.ENGLISH.value: "Gues the number!"
            },
            "value": ""
        },
        UIElementEnum.STATUS_FRAME_TEXT.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Статус игры",
                TextLocaleEnum.ENGLISH: "Game status"
            },
            "value": ""
        },
        UIElementEnum.STATUS_HEALTH.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Количество жизней: ",
                TextLocaleEnum.ENGLISH: "Number of lives:"
            },
            "value": "♥"
        },
        UIElementEnum.STATUS_ATTEMPT.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Количество попыток: ",
                TextLocaleEnum.ENGLISH: "Number of attempts: "
            },
            "value": ""
        },
        UIElementEnum.ENTER_NUMBER.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Введите число:",
                TextLocaleEnum.ENGLISH: "Enter the number:"
            },
            "value": ""
        },
        UIElementEnum.NUMBER_FIELD.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Введите число от '0' до '9'",
                TextLocaleEnum.ENGLISH: "Enter a number between '0' and '9'"
            },
            "value": "0"
        },
        UIElementEnum.NUMERIC_FRAME_TEXT.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Цифровая клавиатура",
                TextLocaleEnum.ENGLISH: "Numeric keypad"
            },
            "value": ""
        },
        UIElementEnum.ZERO_BUTTON.value: {
            "locale": {
              TextLocaleEnum.RUSSIAN: "0",
              TextLocaleEnum.ENGLISH: "0"
            },
            "value": "0"
        },
        UIElementEnum.NUMERIC_BUTTON.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "",
                TextLocaleEnum.ENGLISH: ""
            },
            "value": ""
        },
        UIElementEnum.CLEAR_BUTTON.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Очистить",
                TextLocaleEnum.ENGLISH: "Clear"
            },
            "value": ""
        },
        UIElementEnum.ENTER_BUTTON.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Ввод",
                TextLocaleEnum.ENGLISH: "Enter"
            },
            "value": ""
        },
        UIElementEnum.GAME_CURRENCY_TEXT.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Игровая валюта",
                TextLocaleEnum.ENGLISH: "Game currency"
            },
            "value": ""
        },
        UIElementEnum.GAME_CURRENCY.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Ваши баллы: ",
                TextLocaleEnum.ENGLISH: "Your points: "
            },
            "value": ""
        },
        UIElementEnum.COINS_CURRENCY_TEXT.value: {
            "locale": {
                TextLocaleEnum.RUSSIAN: "Баллы: ",
                TextLocaleEnum.ENGLISH: "Points: "
            },
            "value": ""
        }
    }

    def __init__(self, locale:TextLocaleEnum = None, default_locale=TextLocaleEnum.RUSSIAN):
        self._default_locale = locale if locale is not None else default_locale

    def get_text_locale(self, ui_element: UIElementEnum, locale: Optional[TextLocaleEnum] = None) -> str:
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

