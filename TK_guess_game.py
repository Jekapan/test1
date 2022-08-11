import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from numpy import random



def clear_widgets(frame):
    # select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()


def load_frame1():
    clear_widgets(frame3)
    frame1.tkraise()
    # frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file="images/dice.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg="yellow")
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(
        frame1,
        text="Do you want to play? Press start.",
        bg="yellow",
        fg="black",
        font=40
    ).pack()

    start_btn = tk.Button(
        frame1,
        text="Start",
        width=15,
        font=40,
        bg="gray",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2()
    )
    start_btn.pack(pady=10)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    random_number = random.randint(1, 100)
    tries = 5
    root.counter = 0

    def check_number(n, counter):
        n = int(n)

        def my_click(text):
            tk.Label(
                frame2,
                text=text,
                bg="yellow",
                fg="black",
                font=40
            ).pack()
        if n == random_number:
            messagebox.showinfo(title="Win", message="Congratulations! This is correct number:)")
            load_frame3()
        elif n < random_number:
            root.counter += 1
            my_click(f"Your number is too low than hidden number.\n"
                     f"You have left {tries - counter} tries.")
            if tries - counter == 0:
                load_frame3()
                messagebox.showinfo(title="Loose", message="------You loose!------")

        elif n > random_number:
            root.counter += 1
            my_click(f"Your number is too high the hidden number.\n"
                     f"You have left {tries - counter} tries.")
            if tries - counter == 0:
                load_frame3()
                messagebox.showinfo(title="Loose", message="------You loose!------")

    # create logo widget
    logo_img = ImageTk.PhotoImage(file="images/dice.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg="yellow")
    logo_widget.image = logo_img
    logo_widget.pack()

    # create label widget for instructions
    tk.Label(
        frame2,
        text="You have 5 tries.\nEnter your number:",
        bg="yellow",
        fg="black",
        font=40
    ).pack()

    answer = tk.Entry(frame2, bg='white')
    answer.pack(pady=10)

    confirm_btn = tk.Button(
        frame2,
        text="Confirm",
        font=40,
        bg="gray",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: check_number(answer.get(), root.counter),

    )
    confirm_btn.pack(pady=5)


def load_frame3():
    clear_widgets(frame2)
    frame3.tkraise()

    logo_img = ImageTk.PhotoImage(file="images/dice.png")
    logo_widget = tk.Label(frame3, image=logo_img, bg="yellow")
    logo_widget.image = logo_img
    logo_widget.pack()

    restart_btn = tk.Button(
        frame3,
        text="Play again",
        font=40,
        bg="gray",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    )
    restart_btn.pack()


root = tk.Tk()
root.title("Guess a number")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, bg="yellow",)
frame2 = tk.Frame(root, bg="yellow")
frame3 = tk.Frame(root, bg="yellow")

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="NESW")

load_frame1()

# run app
root.mainloop()
