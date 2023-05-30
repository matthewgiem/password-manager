from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", '$', "%", "^", "&", "*", "(", ")", "+", "<", ">", "?", "{", "}"]


def random_password():
    password_letters = random.choices(letters, k=9)
    password_numbers = random.choices(numbers, k=3)
    password_symbols = random.choices(symbols, k=3)
    password = "".join(random.sample(password_symbols + password_numbers + password_letters,
                       len(password_symbols + password_numbers + password_letters)))
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    company = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if company or email or password == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=company, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{company} | {email} | {password}\n")
                f.close()
                reset_input()


def reset_input():
    website_entry.delete(0, 'end')
    email_username_entry.delete(0, 'end')
    email_username_entry.insert(0, "matthew.giem.programmer@gmail.com")
    password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "matthew.giem.programmer@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=random_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
