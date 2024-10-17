from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
from space_game import run
import re

conn = sqlite3.connect('DataBase\Diplom.db')
sql=conn.cursor()


welcome_window=Tk()

path = 'img\88.jpg'
image = Image.open(path)
width = 600
height = 300
image = image.resize((width, height))
image = ImageTk.PhotoImage(image)
canvas = tk.Canvas( width=width, height=height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=image)
welcome = canvas.create_text(160, 20, text='Вітаємо в грі SpaceDefenders', font='Verdana 15', fill="#00bfff")
login_entry = Entry(welcome_window, width=30)
canvas.create_window((208, 100), anchor='nw', height=25, window=login_entry)
password_entry = Entry(welcome_window, width=30, show='*')
canvas.create_window((208, 130), anchor='nw', height=25, window=password_entry)
nickname_entry = Entry(welcome_window, width=30)
canvas.create_window((208, 160), anchor='nw', height=25, window=nickname_entry)
email_label = canvas.create_text(175, 110, text='Емейл:', font='Verdana 13', fill="#00bfff")
password_label = canvas.create_text(170, 140, text='Пароль:', font='Verdana 13', fill="#00bfff")
nickname_label = canvas.create_text(168, 168, text='Нікнейм:', font='Verdana 13', fill="#00bfff")
info_label = canvas.create_text(300, 250, text='Для авторизації заповніть поля: "Емайл", "Пароль".\nДля реєстрації заповніть усі поля!', font='Verdana 12', fill="yellow")



def menu():
    welcome_window.destroy()
    menu_window = Tk()
    path = 'img\menu.jpg'
    image = Image.open(path)
    width = 800
    height = 500
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(menu_window, width=width, height=height)
    canvas.pack(side="top", fill="both")
    canvas.create_image(0, 0, anchor="nw", image=image)

    def start_play():
        menu_window.destroy()
        run()

    def table_of_players():
        def exit():
            table_of_players_window.destroy()
            table_of_players_window.quit()
            menu_window.destroy()
            menu_window.quit()

        table_of_players_window = Toplevel(menu_window)
        table_of_players_window.geometry('900x650+350+80')
        table_of_players_window.resizable(True, True)
        table_of_players_window.overrideredirect(True)
        path = 'img\menu.jpg'
        image = Image.open(path)
        width = 1000
        height = 650
        image = image.resize((width, height))
        image = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(table_of_players_window, width=width, height=height)
        canvas.pack(side="left", fill="both")
        canvas.create_image(0, 0, anchor="nw", image=image)
        exit_btn = Button(canvas, text='Вихід', font='Verdana 10', command=exit, width=10, bg='#00bfff')
        canvas.create_window((1, 621), anchor="nw", window=exit_btn)

        def back_to_menu_window():
            table_of_players_window.withdraw()
            menu_window.deiconify()

        back_btn = Button(canvas, text='Назад', command=back_to_menu_window, font='Verdana 10', width=10, bg='#00bfff')
        canvas.create_window((816, 621), anchor="nw", window=back_btn)
        cursor = conn.execute("SELECT  nickname,marks FROM users ORDER BY marks DESC LIMIT 10;")
        canvas.create_text(200, 70, text="Нікнейм", font='Verdana 20 bold', fill='#EFFF00')
        canvas.create_text(420, 70, text="Бали", font='Verdana 20 bold', fill='#EFFF00')
        i = 50
        for row in cursor:
            canvas.create_text(200, 70 + i, text=row[0], font='Verdana 20 bold', fill='#00bfff')
            canvas.create_text(420, 70 + i, text=row[1], font='Verdantyra 20 bold', fill='#00bfff')
            i += 50
        with open('player.txt', 'r') as p:
            login = p.readline().strip()
            cursor2 = conn.execute(
                f"SELECT COUNT(*)+1 as rank FROM users WHERE marks > (SELECT marks FROM users WHERE login = '{login}');")
        canvas.create_text(700, 70, text="Місце в рейтингу", font='Verdana 20 bold', fill='#EFFF00')
        canvas.create_text(460, 20, text="Топ-10", font='Verdana 23 bold', fill='#EFFF00')
        for row in cursor2:
            canvas.create_rectangle(665, 110, 737, 150, fill='#00bfff', outline='#00bfff')
            canvas.create_text(700, 130, text=row[0], font='Verdana 25 bold', fill='#EFFF00')
        conn.close()
        table_of_players_window.overrideredirect(True)
        table_of_players_window.mainloop()

    def instruction():
        
        def exit():
            instruction_window.destroy()
            instruction_window.quit()
            menu_window.destroy()
            menu_window.quit()

        instruction_window = Toplevel(menu_window)
        instruction_window.geometry('900x600+350+100')
        instruction_window.resizable(True, True)
        instruction_window.overrideredirect(True)
        path = "img\w.jpg"
        image = Image.open(path)
        width = 1000
        height = 600
        image = image.resize((width, height))
        image = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(instruction_window, width=width, height=height)
        canvas.pack(side="left", fill="both")
        canvas.create_image(0, 0, anchor="nw", image=image)
        exit_btn = Button(canvas, text='Вихід', font='Verdana 10', command=exit, width=10, bg='#00bfff')
        canvas.create_window((1, 571), anchor="nw", window=exit_btn)

        def back_to_menu_window():
            instruction_window.withdraw()
            menu_window.deiconify()

        txt = '\t\t\t- ЯК РОЗПОЧАТИ ГРУ?\nПІСЛЯ НАТИСКАННЯ НА КНОПКУ "ПОЧАТИ ГРУ" ВІДБУВАЄТЬСЯ ЇЇ ЗАПУСК. КОЛИ ГРА ' \
              'ЗАПУСТИЛАСЬ ВИ ПОЧИНАЄТЕ ВІДРАЗУ КЕРУВАТИ ЛІТАКОМ І НАВАЛА ПРИБУЛЬЦІВ РУХАЄТЬСЯ НА ВАС.\n' \
              '\t\t\t- ЯК ГРАТИ?\nЗА ДОПОМОГОЮ КНОПКИ "D" ВАШ КОРАБЕЛЬ БУДЕ РУХАТИСЬ ПРАВОРУЧ, А НАТИСНУВАШИ КНОПКУ' \
              '"A" - ЛІВОРУЧ. ДЛЯ ТОГО, ЩОБ СТРІЛЯТИ ПО ПРИБУЛЬЦЯМ, ПОТРІБНО НАТИСНУТИ НА ПРОБІЛ. \n' \
              '\t\t\t- ДОДАТКОВІ КОРАБЛІ\nУ ВАС Є ТРИ ДОДАТКОВИХ КОРАБЛІ, ЯКІ ВИ МОЖЕТЕ ВИКОРИСТАТИ У ТОМУ РАЗІ, ' \
              'ЯКЩО ПРИБУЛЬЦІ ДІЙДУТЬ ДО ВАШОГО КОРАБЛЯ.\n \t\t\t- РАХУНОК\nПРАВОРУЧ ЗВЕРХУ Є ПОТОЧНИЙ ' \
              'РАХУНОК ЗА ЦЮ ГРУ. ПОСЕРЕДИНІ ЗВЕРХУ ВКАЗАНИЙ ВАШ ЗАГАЛЬНИЙ РЕКОРД.\n' \
              '\t\t\t-ЗАВЕРШЕННЯ ГРИ\nГРУ БУДЕ ЗАВЕРШЕНО, ЯКЩО ВИ ЗАКРИЄТЕ ЇЇ АБО У ВАС НЕ ЗАЛИШИТЬСЯ КОРАБЛІВ.'
        back_btn = Button(canvas, text='Назад', command=back_to_menu_window, font='Verdana 10', width=10, bg='#00bfff')
        canvas.create_window((817, 571), anchor="nw", window=back_btn)
        canvas.create_text(450, 250, text=txt, font='Verdana 16', width=800, fill='#00bfff')
        instruction_window.overrideredirect(True)
        instruction_window.mainloop()

    def about_game():
        
        def exit():
            about_game_window.destroy()
            about_game_window.quit()
            menu_window.destroy()
            menu_window.quit()

        about_game_window = Toplevel(menu_window)
        about_game_window.geometry('900x600+350+100')
        about_game_window.resizable(True, True)
        about_game_window.overrideredirect(True)
        path = 'img\qq.jpg'
        image = Image.open(path)
        width = 1000
        height = 600
        image = image.resize((width, height))
        image = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(about_game_window, width=width, height=height)
        canvas.pack(side="left", fill="both")
        canvas.create_image(0, 0, anchor="nw", image=image)
        exit_btn = Button(canvas, text='Вихід', font='Verdana 10', command=exit, width=10, bg='#00bfff')
        canvas.create_window((1, 571), anchor="nw", window=exit_btn)
        text = 'ЦЯ ГРА БУЛА РОЗРОБЛЕНА У 2023 РОЦІ. АВТОР ГРИ КУЛІДА ДЕНИС. ВОНА Є АНАЛОГОМ ' \
              'РІЗНОМАНІТНИХ КОСМІЧНИХ ІГОР.\n' \
              'ГРАВЦІ МОЖУТЬ ПОРИНУТИ У АРКАДНУ ГРУ SPACE DEFENDERS. ЗНИЩУЙТЕ ВОРОГІВ ТА ЗМАГАЙТЕСЬ ' \
              'ОДИН З ОДНИМ ТА СПОСТЕРІГАТИ ЗА РЕЙТИНГОМ У ТІБЛИЦІ. У ГРІ ВАМ НАЛЕЖИТЬ КЕРУВАТИ КОСМІЧНИМ КОРАБЛЕМ' \
              'ТА БОРОТИСЯ ІЗ ЗЛОВІСНИМИ ІНОПЛАНЕТЯНАМИ ТА ЗБЕРЕГТИ ПРОНЕТУ ВІД ЗНИЩЕННЯ.'
        canvas.create_text(450, 250, text=text, font='Verdana 16', width=700, fill='#EFFF00')
        about_game_window.overrideredirect(True)

        def back_to_menu_window():
            about_game_window.withdraw()
            menu_window.deiconify()

        back_btn = Button(canvas, text='Назад', command=back_to_menu_window, font='Verdana 10', width=10, bg='#00bfff')
        canvas.create_window((817, 571), anchor="nw", window=back_btn)
        about_game_window.mainloop()
    
    def exit():
        menu_window.destroy()
        menu_window.quit()
        
    play_game_btn = Button(menu_window, text='ПОЧАТИ ГРУ', command=start_play, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 100), anchor="nw", window=play_game_btn)
    table_of_players_btn = Button(menu_window, text='ТАБЛИЦЯ ЛІДЕРІВ', command=table_of_players, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 170), anchor="nw", window=table_of_players_btn)
    instruction_btn = Button(menu_window, text='ІНСТРУКЦІЯ', command=instruction, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 240), anchor="nw", window=instruction_btn)
    about_game_btn = Button(menu_window, text='ПРО ГРУ', command=about_game, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 310), anchor="nw", window=about_game_btn)
    exit_btn = Button(menu_window, text='ВИХІД', command=exit, width=25, height=2, bg='#00bfff')
    canvas.create_window((320, 380), anchor="nw", window=exit_btn)
    menu_window.geometry('800x500+400+150')
    menu_window.resizable(False, False)
    menu_window.overrideredirect(True)
    menu_window.mainloop()


def authorization_to_menu():
    get_login = conn.execute(f"SELECT login FROM users where login='{login_entry.get()}'")
    result_login = get_login.fetchall()
    get_password = conn.execute(f"SELECT password FROM users where login='{login_entry.get()}'")
    result_password = get_password.fetchone()
    if result_login != list() and result_password[0] == password_entry.get():
        marks = conn.execute(f"SELECT marks FROM users where login='{login_entry.get()}'")
        result_marks = marks.fetchone()
        with open('highscore.txt', 'w') as f:
            print(result_marks[0], file=f)
        with open('player.txt', 'w') as p:
            print(result_login[0][0], file=p)
        menu()
    else:
        messagebox.showinfo("Помилка", "Введені данні не коректні!")


def registration_to_menu():
    get_login = conn.execute(f"SELECT login FROM users where login='{login_entry.get()}'")
    result_login = get_login.fetchall()
    get_nickname = conn.execute(f"SELECT nickname FROM users where nickname='{nickname_entry.get()}'")
    result_nickname = get_nickname.fetchall()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", login_entry.get()):
            messagebox.showerror("Помилка","Такого емайлу не існує!")
    else:
        if nickname_entry.get() != "":
            if result_login != list() or result_nickname != list():
                messagebox.showerror("Помилка", "Такий емайл або нікнейм вже зареєстрований!")
            else:
                conn.cursor()
                conn.execute(f"INSERT INTO users(login, password, nickname, marks) VALUES('{login_entry.get()}','{password_entry.get()}','{nickname_entry.get()}', 0);")
                with open('highscore.txt', 'w') as f:
                    print(0, file=f)
                with open('player.txt', 'w') as p:
                    print(login_entry.get(), file=p)
                conn.commit()
                messagebox.showinfo("Форма", "Користувач успішно зареєстрований!")
                menu()
        else:
            messagebox.showerror("Помилка","Заповніть усі поля!")


def exit():
    welcome_window.quit()


exit_btn=Button(welcome_window, text='Вихід', command=exit, bg='#00bfff').place(x=2, y=272)
authorization_btn=Button(welcome_window, text='Вхід', command=authorization_to_menu, bd=1, bg='#00bfff', width=5).place(x=200, y=200)
registration_btn=Button(welcome_window, text='Реєстрація', command=registration_to_menu, bd=1, bg='#00bfff').place(x=350, y=200)
welcome_window.geometry('600x300+500+200')
welcome_window.resizable(False, False)
welcome_window.overrideredirect(True)
welcome_window.mainloop()