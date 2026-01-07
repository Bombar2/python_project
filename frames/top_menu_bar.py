from abc import ABC, abstractmethod
from enum import nonmember
from tkinter import ttk

_BASE_MENU_ITEMS = [
    ("new_game", "Новая игра", "child", True),
    ("save_game", "Сохранить игру", "child", True),
    ("download_game", "Загрузить игру", "child", True),
    ("statistic_game", "Статистика игр", "child", False),
    ("style_game", "Настройка стилей", "child", False),
    ("info_game", "Помощь", "absolut", True)
]

class BaseTopMenu(ABC):
    def __init__(self, parent_frame, callbacks=None):
        self.callbacks = callbacks or {}

        self.menu_frame = None
        self.buttons = {}

        self._init_frame(parent_frame)
        self.build_menu()

    def _init_frame(self, parent):
        self.menu_frame = ttk.Frame(parent, borderwidth=1)
        self.menu_frame.pack(side="top", fill="x")

    @abstractmethod
    def build_menu(self):
        pass

class TopMenuBar:
    """Вариант для стандартного меню приложений"""
    pass

class TopMenuButtons(BaseTopMenu):
    """Вариант с кнопками меню вверху окна"""
    def build_menu(self):
        for btn_id, txt, level, show in _BASE_MENU_ITEMS:
            if show:
                if btn_id in self.callbacks:
                    cmd = self.callbacks[btn_id]
                else:
                    cmd = lambda t=txt, idx=btn_id: print(f"У кнопки '{t}' (ID: {idx}) отсутствует обработчик события!")

                btn = ttk.Button(self.menu_frame, text=txt, command=cmd)
                btn.pack(side="left", padx=2, pady=2)
                self.buttons[btn_id] = btn