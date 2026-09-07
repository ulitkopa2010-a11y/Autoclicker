# pip install mouse
# pip install keyboard

# import tkinter as tk
# from tkinter import messagebox
# import mouse
# import keyboard
# import time


# running = False
# delay = 0

# def start_clicker():
#     global running, delay

#     try:
#         clicks_per_seconde = int(entry.get())

#         if clicks_per_seconde <= 0:
#             messagebox.showerror("Помилка","Швидкшсть має бути білше 0")
#             return

#         delay = int(1000 / clicks_per_seconde)
#         messagebox.showinfo("Auto Clicker", "Auto Clicker розпочато! Натисніть 'ESC' щоб зупинити.")
#         running = True
#         # click root.after
#         schedule_click()

#     except ValueError:
#        messagebox.showerror("Помилка вводу", "Будь ласка, введіть коректне число кліків на секунду")

# def exit_app():
#     global running

#     if running:
#         running = False

#     messagebox.showinfo("Auto Clicker", "Auto Clicker stopped")
#     root.destroy()

# def show_info(event):
#     messagebox.showinfo("Інформація","Це автоклікер, він буде клікати з такю щвидкістю, яку ти вкажеш")


# #==================================================================
# # Створення графічного інтрфейсу (GUI)
# #==================================================================

# root = tk.TK()
# root.title("Auto Clicker")
# root.geometry("300x220")
# root.resizable(False,False)
# root.configure(bg="#e0f7fa")

# root.binf('i', show_info)

# title_label = tk.Label(
#     root,
#     text = "Auto Clicker"
#     font = ("Trebuchet MS", 16, "bold")
#     bg="#e0f7fa"
#     fg="#00796b"
# )
# label.pack(pady=10)


# lable = tk.Label(
#     root,
#     text="clicks per second"
#     font=("Trebuchet MS", 12)
#     bg="#e0f7fa"
#     fg="#00796b"
# )
# lable.pack(pady=10)

# entry = tk.Entry(
#     root,
#     font=("Arial", 12),
#     width=10,
#     justify='center'
# )
# entry.pack(pady=5)
# entry.insert(0,"10")


# pip install mouse
# pip install keyboard

# import tkinter as tk
# from tkinter import messagebox
# import mouse
# import keyboard
# import time


# running = False
# delay = 0


# def schedule_click():
#     global running

#     if running:
#         mouse.click()
#         root.after(int(delay), schedule_click)


# def start_clicker():
#     global running, delay

#     try:
#         clicks_per_seconde = int(entry.get())

#         if clicks_per_seconde <= 0:
#             messagebox.showerror("Помилка", "Швидкість має бути більше 0")
#             return

#         delay = 1000 / clicks_per_seconde
#         messagebox.showinfo(
#             "Auto Clicker",
#             "Auto Clicker розпочато! Натисніть 'ESC' щоб зупинити."
#         )

#         running = True
#         schedule_click()

#     except ValueError:
#         messagebox.showerror(
#             "Помилка вводу",
#             "Будь ласка, введіть коректне число кліків на секунду"
#         )


# def exit_app():
#     global running

#     running = False

#     messagebox.showinfo("Auto Clicker", "Auto Clicker stopped")
#     root.destroy()


# def show_info(event):
#     messagebox.showinfo(
#         "Інформація",
#         "Це автоклікер, він буде клікати з такою швидкістю, яку ти вкажеш"
#     )


# def stop_clicker():
#     global running
#     running = False


# # ================================================================
# # Створення графічного інтерфейсу (GUI)
# # ================================================================

# root = tk.Tk()
# root.title("Auto Clicker")
# root.geometry("300x220")
# root.resizable(False, False)
# root.configure(bg="#e0f7fa")

# root.bind("<i>", show_info)
# root.bind("<Escape>", lambda event: stop_clicker())

# title_label = tk.Label(
#     root,
#     text="Auto Clicker",
#     font=("Trebuchet MS", 16, "bold"),
#     bg="#e0f7fa",
#     fg="#00796b"
# )
# title_label.pack(pady=10)


# label = tk.Label(
#     root,
#     text="Clicks per second",
#     font=("Trebuchet MS", 12),
#     bg="#e0f7fa",
#     fg="#00796b"
# )
# label.pack(pady=10)


# entry = tk.Entry(
#     root,
#     font=("Arial", 12),
#     width=10,
#     justify="center"
# )
# entry.pack(pady=5)
# entry.insert(0, "10")


# start_button = tk.Button(
#     root,
#     text="Start",
#     command=start_clicker
# )
# start_button.pack(pady=5)


# exit_button = tk.Button(
#     root,
#     text="Exit",
#     command=exit_app
# )
# exit_button.pack(pady=5)


# root.mainloop()
import customtkinter as ctk
from tkinter import messagebox
import mouse
import keyboard


running = False
delay = 100


def schedule_click():
    if running:
        mouse.click()
        root.after(delay, schedule_click)


def start_clicker():
    global running, delay

    try:
        clicks_per_second = int(entry.get())

        if clicks_per_second <= 0:
            raise ValueError

        delay = max(1, int(1000 / clicks_per_second))
        running = True

        start_button.configure(state="disabled")
        status_label.configure(text="Клікер працює", text_color="#22c55e")

        schedule_click()

    except ValueError:
        messagebox.showerror(
            "Помилка вводу",
            "Введіть додатне ціле число."
        )


def stop_clicker(event=None):
    global running

    running = False
    start_button.configure(state="normal")
    status_label.configure(text="Клікер зупинено", text_color="#ef4444")


def exit_app():
    keyboard.remove_hotkey(esc_hotkey)
    stop_clicker()
    root.destroy()


def show_info(event=None):
    messagebox.showinfo(
        "Інформація",
        "Автоклікер натискає ліву кнопку миші із заданою швидкістю."
    )


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Auto Clicker")
root.geometry("360x300")
root.resizable(False, False)

root.bind("<Escape>", stop_clicker)
root.bind("<F1>", show_info)
esc_hotkey = keyboard.add_hotkey(
    "esc",
    lambda: root.after(0, stop_clicker)
)

title_label = ctk.CTkLabel(
    root,
    text="AUTO CLICKER",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=(25, 15))

label = ctk.CTkLabel(
    root,
    text="Кліків за секунду"
)
label.pack(pady=5)

entry = ctk.CTkEntry(
    root,
    width=150,
    justify="center",
    font=("Arial", 16)
)
entry.pack(pady=5)
entry.insert(0, "10")

start_button = ctk.CTkButton(
    root,
    text="▶  Запустити",
    fg_color="#16a34a",
    hover_color="#15803d",
    command=start_clicker
)
start_button.pack(pady=(20, 8))

exit_button = ctk.CTkButton(
    root,
    text="✖  Вийти",
    fg_color="#dc2626",
    hover_color="#b91c1c",
    command=exit_app
)
exit_button.pack(pady=8)

status_label = ctk.CTkLabel(
    root,
    text="Клікер зупинено",
    text_color="#ef4444"
)
status_label.pack(pady=10)

root.mainloop()
# ...existing code...

root = ctk.CTk()
root.title("Auto Clicker")
root.geometry("360x300")
root.resizable(False, False)
root.iconbitmap("autoclicker.ico")

# ...existing code...

root = ctk.CTk()
root.title("Auto Clicker")
root.geometry("360x300")
root.resizable(False, False)
root.iconbitmap("autoclicker.ico")

# ...existing code...