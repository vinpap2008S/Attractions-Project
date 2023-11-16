from customtkinter import *
from PIL import Image
import os
set_appearance_mode("dark")
def login_event():
    print("Login pressed - username:", username_entry.get(), "password:", password_entry.get())

    login_frame.grid_forget()  # remove login frame
    main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

def back_event():
    main_frame.grid_forget()  # remove main frame
    login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
    app = CTk()
    width = 900
    height = 600
    app.title("CustomTkinter example_background_image.py")
    app.geometry(f"{width}x{height}")
    app.resizable(False, False)

    # load and create background image
    current_path = os.path.dirname(os.path.realpath(__file__))
    bg_image = CTkImage(Image.open(current_path + "/test_images/bg_gradient.jpg"),
                                           size=(width, height))
    bg_image_label = CTkLabel(app, image=bg_image)
    bg_image_label.grid(row=0, column=0)

    # create login frame
    login_frame = CTkFrame(app, corner_radius=0)
    login_frame.grid(row=0, column=0, sticky="ns")
    login_label = CTkLabel(login_frame, text="CustomTkinter\nLogin Page",
                                              font=CTkFont(size=20, weight="bold"))
    login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
    username_entry = CTkEntry(login_frame, width=200, placeholder_text="username")
    username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
    password_entry = CTkEntry(login_frame, width=200, show="*", placeholder_text="password")
    password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
    login_button = CTkButton(login_frame, text="Login", command=login_event, width=200)
    login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    # create main frame
    main_frame = CTkFrame(app, corner_radius=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_label = CTkLabel(main_frame, text="Регистрация/Вход", font=CTkFont(size=20, weight="bold"))
    main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
    back_button = CTkButton(main_frame, text="Back", command=back_event, width=200)
    back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    app.mainloop()
