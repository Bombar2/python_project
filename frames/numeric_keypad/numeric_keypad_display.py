from tkinter import ttk
from frames.UI.ui import TextUI, TextLocaleEnum, UIElementEnum

class NumericKeypadDisplay:
    """Создание фрейма с кнопками ввода цифр и кнопок ввод и очистка."""
    def __init__(self, parent, locale: TextLocaleEnum = None):
        self._text_ui = TextUI(locale)
        self._buttons_list = {}

        self._frame = self._create_numeric_keypad(parent)

    def _create_numeric_keypad(self, parent) -> ttk.LabelFrame:
        frame = ttk.LabelFrame(parent, text=self._text_ui.get_text_locale(UIElementEnum.NUMERIC_FRAME_TEXT), padding=10)
        frame.grid(row=1, column=0, sticky="nsew", padx=(0, 5), pady=(5, 0))

        for i in range(3):
            frame.grid_columnconfigure(i, weight=1, uniform="btn_col")
        for i in range(4):
            frame.grid_rowconfigure(i + 1, weight=1, uniform="btn_row")

        text_num = 1

        for row in range(1, 4):  # Строки 1-3
            for col in range(3):  # Колонки 0-2
                btn = ttk.Button(frame, text=str(text_num))
                btn.grid(column=col, row=row, padx=3, pady=3, sticky="nsew")
                self._buttons_list[str(text_num)] = btn
                text_num += 1


        # Кнопки нижнего ряда
        btn = ttk.Button(frame, text=self._text_ui.get_ui_value(UIElementEnum.ZERO_BUTTON))
        btn.grid(column=1, row=4, padx=3, pady=3, sticky="nsew")
        self._buttons_list[self._text_ui.get_ui_value(UIElementEnum.ZERO_BUTTON)] = btn

        btn = ttk.Button(frame, text=self._text_ui.get_text_locale(UIElementEnum.CLEAR_BUTTON))
        btn.grid(column=0, row=4, padx=3, pady=3, sticky="nsew")
        self._buttons_list[self._text_ui.get_text_locale(UIElementEnum.CLEAR_BUTTON)] = btn

        btn = ttk.Button(frame, text=self._text_ui.get_text_locale(UIElementEnum.ENTER_BUTTON))
        btn.grid(column=2, row=4, padx=3, pady=3, sticky="nsew")
        self._buttons_list[self._text_ui.get_text_locale(UIElementEnum.ENTER_BUTTON)] = btn

        return frame

    def _callback(self, callbacks, text_button, button_id):
        if button_id in callbacks:
            if button_id == UIElementEnum.CLEAR_BUTTON.value or button_id == UIElementEnum.ENTER_BUTTON.value:
                return lambda : callbacks[button_id](button_id)
            else:
                return lambda : callbacks[button_id](text_button)
        else:
            return lambda: print(f"Для кнопки '{text_button}' (ID: {button_id}) отсутствует обработчик события!")

    def _update_button_state(self, btn: ttk.Button, state="normal") -> None:
        btn.config(state=state)

    def set_buttons_callback(self, callbacks = None):
        for idx, btn in self._buttons_list.items():
            if (idx is not self._text_ui.get_text_locale(UIElementEnum.CLEAR_BUTTON)
                    and idx is not self._text_ui.get_text_locale(UIElementEnum.ENTER_BUTTON)):
                if idx is not self._text_ui.get_text_locale(UIElementEnum.ZERO_BUTTON):
                    btn.config(command=self._callback(callbacks, idx, UIElementEnum.NUMERIC_BUTTON.value))
                else:
                    btn.config(command=self._callback(callbacks, idx, UIElementEnum.ZERO_BUTTON.value))
            elif idx is self._text_ui.get_text_locale(UIElementEnum.ENTER_BUTTON):
                btn.config(command=self._callback(callbacks, idx, UIElementEnum.ENTER_BUTTON.value))
            elif idx is self._text_ui.get_text_locale(UIElementEnum.CLEAR_BUTTON):
                btn.config(command=self._callback(callbacks, idx, UIElementEnum.CLEAR_BUTTON.value))


    def show_hint(self, number, status: bool = True):
        """Функция показа подсказок.
        fl_more = True - введённое число больше угадываемого"""
        for idx, btn in self._buttons_list.items():
            if (idx is not self._text_ui.get_text_locale(UIElementEnum.CLEAR_BUTTON)
                    and idx is not self._text_ui.get_text_locale(UIElementEnum.ENTER_BUTTON)):
                if status and int(idx) >= number:
                    self._update_button_state(btn, state="disabled")
                elif not status and int(idx) <= number:
                    self._update_button_state(btn, state="disabled")

    def reset_hint(self):
        """Функция сброса подсказки"""
        for idx, btn in self._buttons_list.items():
            self._update_button_state(btn)
