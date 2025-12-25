from tkinter import *
from tkinter import ttk
from game import Game, LaunchEnum, AnswerEnum
from frames.top_menu_bar import TopMenuButtons


class MainActivity:
    __MAIN_ACTIVITY_TITLE: str = "Gues the number"
    __MAIN_ACTIVITY_ICON_PATH: str = "res/search.png"



    def __init__(self):
        self.game = Game(launch_enum=LaunchEnum.LAUNCH_IN_ACTIVITY)


        __TOP_MENU_BUTTONS_CALLBACKS = {
            "new_game": self.click_button_menu_new_game,
            "save_game": self.click_button_menu_save_game,
            "download_game": self.click_button_menu_download_game,
            "statistic_game": self.click_button_menu_statistic,
            "style_game": self.click_button_menu_style
        }

        self.human_number = ""
        self.number_label = None
        self.attempt_label = None
        self.health_label = None
        self.coin_label = None

        self.shop_frame = None
        self.shop_buttons = []

        root = Tk()
        root.geometry("600x500")
        root.resizable(False, False)

        root.title(self.__MAIN_ACTIVITY_TITLE)

        self.set_main_activity_icon(root, self.__MAIN_ACTIVITY_ICON_PATH) #Выставление иконки.


        #self.create_top_menu(root)
        """Создаю верхнее меню"""
        self.TopMenuButtons = TopMenuButtons(root, __TOP_MENU_BUTTONS_CALLBACKS)

        main_frame = ttk.Frame(root, padding=10)
        main_frame.pack(fill="both", expand=True)

        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)


        self.create_status_frame(main_frame)
        self.create_button_frame(main_frame)
        self.create_purchases_frame(main_frame)

        root.mainloop()

    def click(self, value):
        if (self.number_label.cget("text") == AnswerEnum.ANSWER_SUCCESS or
                self.number_label.cget("text") == AnswerEnum.ANSWER_FAILURE):
            self.clear()

        if value not in "Enter" and len(self.human_number) < 4:
            self.human_number += value
            self.number_label.config(text=f"{self.human_number}")

    def click_button_shop(self, index):
        for idx, purchase in self.game.get_purchases_dict().items():
            if idx == index:
                purchase['action']()

        self.update_status(AnswerEnum.ANSWER_SUCCESS)

    def click_button_menu_new_game(self):
        pass

    def click_button_menu_save_game(self):
        pass

    def click_button_menu_download_game(self):
        pass

    def click_button_menu_statistic(self):
        pass

    def click_button_menu_style(self):
        pass

    def enter(self):
        if len(self.human_number) > 0:
            number = self.game.get_user_input(self.human_number)

            answer_enum = AnswerEnum.ANSWER_FAILURE
            if self.game.check_user_guess(number):
                self.game.handle_correct_guess() #Обработка корректного ответа
                answer_enum = AnswerEnum.ANSWER_SUCCESS
                pass ##Здесь обработка если пользователь угадал.
            elif self.game.check_user_guess_more(number):
                self.game.handle_wrong_guess()
                pass ##Если введённое число больше, выводим информацию, что угадываемое меньше.
            else:
                self.game.handle_wrong_guess()
                pass ##Если введённое число меньше угадываемого.
        self.update_status(answer_enum)

    def clear(self):
        self.human_number = ""
        self.number_label.config(text="")

    def set_main_activity_icon(self, root, file_path):
        """Выставление иконки главного окна, если не будет найдена, ничего не делает"""
        try:
            icon = PhotoImage(file=file_path)
            root.iconphoto(False, icon)
        except FileNotFoundError:
            print("Иконка не найдена!")

    def create_top_menu(self, root):
        top_menu_frame = ttk.Frame(root)
        top_menu_frame.pack(side="top", fill="x")

        ttk.Button(top_menu_frame, text="Новая игра"
                   , command=self.click_button_menu_new_game).pack(side="left", padx=2, pady=2)

        ttk.Button(top_menu_frame, text="Сохранить игру"
                   , command=self.click_button_menu_save_game).pack(side="left", padx=2, pady=2)

        ttk.Button(top_menu_frame, text="Загрузить игру"
                   , command=self.click_button_menu_download_game).pack(side="left", padx=2, pady=2)

        ttk.Button(top_menu_frame, text="Статистика"
                   , command=self.click_button_menu_statistic).pack(side="left", padx=2, pady=2)

        ttk.Button(top_menu_frame, text="Стили"
                   , command=self.click_button_menu_style).pack(side="left", padx=2, pady=2)


    def create_status_frame(self, root_frame):
        status_frame = ttk.LabelFrame(root_frame, text="Статус игры", padding=15)
        status_frame.grid(column=0, row=0, sticky="nsew", padx=(0, 5), pady=(0, 5))

        status_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(status_frame, text="Количество жизней:",
                  font=("Arial", 11)).grid(column=0, row=0, sticky="w", pady=5)
        self.health_label = ttk.Label(status_frame, text=f"{('♥' * self.game.gtn.health)}",
                                      font=("Arial", 14),
                                      foreground="red")
        self.health_label.grid(column=1, row=0, sticky="w", padx=(10, 0), pady=5)

        ttk.Label(status_frame, text="Количество попыток:",
                  font=("Arial", 11)).grid(column=0, row=1, sticky="w", pady=5)
        self.attempt_label = ttk.Label(status_frame, text="3",
                                       font=("Arial", 14),
                                       foreground="blue")
        self.attempt_label.grid(column=1, row=1, sticky="w", padx=(10, 0), pady=5)

        ttk.Separator(status_frame, orient="horizontal").grid(
            column=0, row=2, columnspan=2, sticky="we", pady=15)

        ttk.Label(status_frame, text="Введите число:",
                  font=("Arial", 12, "bold")).grid(
            column=0, row=3, columnspan=2, sticky="w", pady=(0, 10))

        number_display = ttk.Frame(status_frame, relief="solid", borderwidth=1)
        number_display.grid(column=0, row=4, columnspan=2, sticky="we", pady=(0, 5))

        self.number_label = ttk.Label(number_display, text="",
                                      font=("Arial", 20, "bold"),
                                      background="white",
                                      width=10)
        self.number_label.pack(padx=10, pady=10)

        ttk.Label(status_frame, text="Введите 4-значное число",
                  font=("Arial", 9),
                  foreground="gray").grid(
            column=0, row=5, columnspan=2, sticky="w")

    def create_button_frame(self, root_frame):
        button_frm = ttk.LabelFrame(root_frame, text="Цифровая клавиатура", padding=10)
        button_frm.grid(row=1, column=0, sticky="nsew", padx=(0, 5), pady=(5, 0))

        for i in range(3):
            button_frm.grid_columnconfigure(i, weight=1, uniform="btn_col")
        for i in range(4):
            button_frm.grid_rowconfigure(i + 1, weight=1, uniform="btn_row")

        text_num = 1
        for row in range(1, 4):  # Строки 1-3
            for col in range(3):  # Колонки 0-2
                ttk.Button(button_frm, text=str(text_num),
                           command=lambda t=str(text_num): self.click(t)).grid(
                    column=col, row=row, padx=3, pady=3, sticky="nsew")
                text_num += 1

        # Кнопки нижнего ряда
        ttk.Button(button_frm, text="Clear", command=self.clear).grid(
            column=0, row=4, padx=3, pady=3, sticky="nsew")
        ttk.Button(button_frm, text="0", command=lambda t=str("0"): self.click(t)).grid(
            column=1, row=4, padx=3, pady=3, sticky="nsew")
        ttk.Button(button_frm, text="Enter", command=lambda: self.enter()).grid(
            column=2, row=4, padx=3, pady=3, sticky="nsew")

    def create_purchases_frame(self, root_frame):
        purchases_frame = ttk.LabelFrame(root_frame, text="Игровая валюта", padding=10)
        purchases_frame.grid(column=1, row=0, rowspan=2, sticky="nsew")

        ttk.Label(purchases_frame, text="Ваши баллы:",
                  font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 10))

        coins_frm = ttk.Frame(purchases_frame)
        coins_frm.pack(fill="x", pady=5)

        ttk.Label(coins_frm, text="Баллы: ", font=("Arial", 11)).pack(side="left")
        self.coin_label = ttk.Label(coins_frm, text="0",
                                    font=("Arial", 11, "bold"),
                                    foreground="red")
        self.coin_label.pack(side="left", padx=(5, 0))

        ttk.Separator(purchases_frame, orient="horizontal").pack(fill="x", pady=15)

        self.create_shop_frame(purchases_frame)

    def create_shop_frame(self, root_frame):
        self.shop_frame = ttk.Frame(root_frame)
        self.shop_frame.pack(fill="both", expand=True)

        self.shop_frame.grid_columnconfigure(0, weight=1)

        self.update_shop_buttons()

        #ttk.Button(self.shop_frame, text="+1 жизнь\n10 баллов",command=lambda: self.click("10")).grid(row=0, column=0, sticky="we", pady=2)
        #ttk.Button(self.shop_frame, text="+3 попытки\n15 баллов",command=lambda: self.click("15")).grid(row=1, column=0, sticky="we", pady=2)
        #ttk.Button(self.shop_frame, text="Подсказка\n20 баллов",command=lambda: self.click("20")).grid(row=2, column=0, sticky="we", pady=2)

    def update_shop_buttons(self):
        """функция добавления и обновления кнопок в магазине"""

        # Берём словарь со всеми покупками и выводим их все.
        purchases_dict = self.game.get_purchases_dict()

        #Сперва нужно будет удалить все кнопки, если они есть в массиве.
        if len(self.shop_buttons) != 0:
            self.__delete_shop_buttons()

        for i, (idx, purchase) in enumerate(purchases_dict.items()):
            if purchase['cost'] <= self.game.get_coin():
                btn = ttk.Button(self.shop_frame, name=str(idx),
                                 text=f"{idx}. {purchase['name']} - {purchase['cost']} бал(ов).",
                                 command=lambda current_idx=idx: self.click_button_shop(current_idx))
                btn.grid(row=i, column=0, sticky="we", pady=2)
                self.shop_buttons.append(btn)

    def update_status(self, answer_enum: AnswerEnum):
        self.human_number = ""
        self.number_label.config(text=answer_enum.value)
        self.attempt_label.config(text=self.game.gtn.attempt)
        self.health_label.config(text=f"{('♥' * self.game.gtn.health)}")
        self.coin_label.config(text=f"{self.game.gtn.coin}")

        self.update_shop_buttons()

    def __delete_shop_buttons(self):
        for btn in self.shop_buttons:
            btn.destroy()


