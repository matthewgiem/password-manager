from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    company = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=company, message=f"These are the details entered:\nEmail: {email}\n"
                                                  f"Password: {password}\n Is it ok to save?")
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

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
