from abc import ABC, abstractmethod
from tkinter import ttk

_BASE_MENU_ITEMS = [
    ("new_game", "Новая игра", "child"),
    ("save_game", "Сохранить игру", "child"),
    ("download_game", "Загрузить игру", "child"),
    ("statistic_game", "Статистика игр", "child"),
    ("style_game", "Настройка стилей", "child"),
    ("info_game", "Помощь", "absolut")
]

class BaseTopMenu(ABC):
    def __init__(self, parent_frame, callbacks=None):
        self.parent_frame = parent_frame
        self.callbacks = callbacks or {}

        self.menu_frame = None
        self.buttons = {}

        self._init_frame()
        self.build_menu()

    def _init_frame(self):
        self.menu_frame = ttk.Frame(self.parent_frame, relief="raised", borderwidth=1)
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
        for btn_id, txt, level in _BASE_MENU_ITEMS:
            #if btn_id in self.callbacks:
            btn = ttk.Button(self.menu_frame, text=txt
                             , command=(lambda idx=btn_id: self.callbacks[idx]()) if btn_id in self.callbacks else (lambda : print("handler")))
            btn.pack(side="left", padx=2, pady=2)
            self.buttons[btn_id] = btn