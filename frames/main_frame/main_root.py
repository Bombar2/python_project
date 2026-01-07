from tkinter import Tk, PhotoImage
from frames.UI.ui import TextUI, TextLocaleEnum


class MainActivity:
    __ICON_PATH: str = "res/search.png"

    def __init__(self, locale:TextLocaleEnum = None, height:int = 600, width: int = 500):
        self._textUI = TextUI(locale)

        self.__main_activity_height = height
        self.__main_activity_width = width

        self._root = self._create_main_frame()

    def _create_main_frame(self) -> Tk:
        root = Tk()
        root.geometry(f"{self.__main_activity_height}x{self.__main_activity_width}")
        root.resizable(False, False)

        #self._set_main_activity_icon(root, self.__ICON_PATH)

        return root

    def get_root(self):
        return self._root

    def _set_main_activity_icon(self, root, icon_path):
        try:
            icon = PhotoImage(file=icon_path)
            root.iconphoto(False, icon)
        except FileNotFoundError:
            print("Иконка не найдена!")