from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    new_data = {
        company: {
            "email": email,
            "password": password
        }}
    is_ok = messagebox.askokcancel(title=company, message=f"These are the details for {company} entered:\n"
                                                          f"Email: {email}\nPassword: {password}\n Is it ok to save?")
    if is_ok:
        try:
            with open("password.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("password.json", "x") as data_file:
                json.dump(new_data, data_file, indent=4)
                reset_input()
        else:
            with open("password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                reset_input()


def reset_input():
    website_entry.delete(0, 'end')
    email_username_entry.delete(0, 'end')
    email_username_entry.insert(0, "matthew.giem.programmer@gmail.com")
    password_entry.delete(0, 'end')

# ---------------------------- WEBSITE SEARCH ------------------------------- #


def website_search():
    website = website_entry.get()
    try:
        with open("password.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="website", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



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

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

website_search_button = Button(text="Search", command=website_search, bg="blue", width=14)
website_search_button.grid(column=2, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "matthew.giem.programmer@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=random_password, width=14)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
