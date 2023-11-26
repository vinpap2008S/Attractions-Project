#pip3 install -r requirements.txt
import customtkinter
import os
from PIL import Image

customtkinter.set_default_color_theme("dark-blue")
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global framgl_name, fram1_name, fram2_name, fram3_name,login_frame,login_label
        framgl_name = "Главная"
        fram1_name = "Добавление обьектов"
        fram2_name = "Профиль"
        fram3_name = ""

        # Загрузка изображений
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")  # Изображение поиск
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=(26, 26))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
        if p.read() == '':
            # Создание окна
            self.title("image_example.py")
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.after(0, lambda: self.state('zoomed'))

            # создаём логин фрейм
            self.login_frame = customtkinter.CTkFrame(self, width=2000, height=2000)
            self.login_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.login_label = customtkinter.CTkLabel(self.login_frame, text="Регистрация/Вход",
                                                      font=customtkinter.CTkFont(size=30, weight="bold"))
            self.login_label.grid(row=0, column=0, padx=600, pady=(150, 15))
            self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="Логин",)
            self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
            self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Пароль")
            self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
            self.login_button = customtkinter.CTkButton(self.login_frame, text="Войти", command=self.main, width=200)
            self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        else:
            self.login_frame = customtkinter.CTkFrame(self, width=2000, height=2000)
            self.login_label = customtkinter.CTkLabel(self.login_frame, text="Регистрация/Вход",
                                                      font=customtkinter.CTkFont(size=30, weight="bold"))
            self.main()
        p.close()
    def select_frame_by_name(self, name):
        # Цвет кнопки от выбора
        self.home_button.configure(fg_color=("gray75", "gray25") if name == framgl_name else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == fram1_name else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == fram2_name else "transparent")

        # Показ выбранного
        if name == framgl_name:
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == fram2_name:
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == fram1_name:
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
    def main(self):
        if self.login_event():
            return
        self.login_label.destroy()
        self.login_frame.destroy()
        self.after(0, lambda: self.state('zoomed'))
        # установиливаю макет сетки 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # Навигация
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        # 1 фрейм
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text=framgl_name,
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        # 2 фрейм
        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text=fram1_name, fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"), image=self.chat_image,
                                                      anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        # 3 фрейм
        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text=fram2_name,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        # выбор темы
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Светлая", "Тёмная", "Системная"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # Главный фрейм
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)


        # создаем фрейм
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Настройка

        self.navigation_frame2_label = customtkinter.CTkLabel(self.second_frame,
                                                              text=login,
                                                              font=customtkinter.CTkFont(size=30, weight="bold"))
        self.navigation_frame2_label.grid(padx=200, pady=100)
        # создаем фрейм
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.navigation_frame_label = customtkinter.CTkLabel(self.third_frame,
                                                             text="В ведите название достопремечательности и через / описание",
                                                             font=customtkinter.CTkFont(size=30, weight="bold"))
        # Настройка
        self.navigation_frame_label.grid(padx=200, pady=100)
        self.home_frame_frame_2_entry = customtkinter.CTkEntry(self.third_frame, width=1000, height=50)
        self.home_frame_frame_2_entry.grid(row=1, column=0, padx=200, pady=10, sticky="nsw")
        self.bitin_2frame = customtkinter.CTkButton(self.third_frame, text='Отправить на проверку', height=50)
        self.bitin_2frame.grid(row=2, column=0, padx=200, pady=10)
        # навигация


        # создаём фрейм


        # Главный фрейм
        self.select_frame_by_name(framgl_name)
    def home_button_event(self):self.select_frame_by_name(framgl_name)# закончено
    def frame_2_button_event(self):self.select_frame_by_name(fram1_name)# закончено
    def frame_3_button_event(self):self.select_frame_by_name(fram2_name)# закончено
    # закончено change_appearance_mode_event
    def change_appearance_mode_event(self, new_appearance_mode):
        if new_appearance_mode == 'Светлая':
            customtkinter.set_appearance_mode("light")
        elif new_appearance_mode == 'Тёмная':
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("system")
    # закончено avtor
    def avtor(self, password, file):
        if password == '':
            return 1
        if login == '':
            return 1
        for file3 in open('file(sgl)/Авторизация', 'r', encoding="UTF-8"):
            if file3[2:file3.find('\t', 2)] == login:
                if file3[file3.find('\t', 2) + 1:file3.find('\t', file3.find('\t', 2) + 1)] == password:
                    self.login_label1 = customtkinter.CTkLabel(self.login_frame, text="Вы вошли",font=customtkinter.CTkFont(size=20, weight="bold"))
                    self.login_label1.grid(row=4, column=0)
                    p = open('file(sgl)/Логин', 'w', encoding="UTF-8")
                    p.write(login)
                    p.close()
                    self.login_frame.grid_forget()  # remove login frame
                    self.login_frame.grid(row=0, column=0, sticky="nsew", padx=100)
                    return 0
                else:
                    self.login_label1.grid_forget()
                    self.login_label1 = customtkinter.CTkLabel(self.login_frame, text="Пароль или логин\nне правильный",
                                                               font=customtkinter.CTkFont(size=20, weight="bold"))
                    self.login_label1.grid(row=4, column=0)
                    return 1
        file.write(str(int(g) + 1) + '\t' + login + '\t' + password + '\t' + 'f' + '\n')
        file.close()
        p = open('file(sgl)/Логин', 'w', encoding="UTF-8")
        p.write(login)
        self.login_label1.grid_forget()
        p.close()
        return 0 #акон №#
    # закончено login_event
    def login_event(self):
        global g,login
        p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
        if p.read() == '':

            self.login_label1 = customtkinter.CTkLabel(self.login_frame, text="",
                                                       font=customtkinter.CTkFont(size=20, weight="bold"))
            self.login_label1.grid(row=4, column=0)

            login = self.username_entry.get()
            password = self.password_entry.get()

            file = open('file(sgl)/Авторизация', 'a', encoding="UTF-8")
            g = 0
            for nine in open('file(sgl)/Авторизация', 'r', encoding="UTF-8"):
                g = nine[0]
            if g == 'Л':
                g = 0
            p.close()
            return self.avtor(password,file)
        else:
            p = open('file(sgl)/Логин', 'r', encoding="UTF-8")
            login = p.read()
            p.close()
            return 0

if __name__ == "__main__":
    app = App()
    app.mainloop()
