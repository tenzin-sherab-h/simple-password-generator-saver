from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Passphrase creator Project
def generate_pword():
    numbers = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    symbls = ['+', '#', '%', '(', ')', '&', '$', '!', '*']
    lttrs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

    pwordsymbols = [choice(symbls) for _ in range(randint(2, 4))]
    pwordnumbers = [choice(numbers) for _ in range(randint(2, 4))]
    pwordletters = [choice(lttrs) for _ in range(randint(8, 10))]

    pword_list = pwordletters + pwordsymbols + pwordnumbers
    shuffle(pword_list)

    passphrase = "".join(pword_list)
    passphrase_entry.insert(0, passphrase)
    pyperclip.copy(passphrase)


# ---------------------------- STORING THE PASSWORD ------------------------------- #
def store():
    website = website_input.get()
    email = em_input.get()
    passphrase = passphrase_entry.get()

    if len(website) == 0 or len(passphrase) == 0:
        messagebox.showinfo(title="Notice", message="Kindly make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The entries are as follows: \nEmail: {email} "
                                                              f"\nPassword: {passphrase} \nProceed to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {passphrase}\n")
                website_input.delete(0, END)
                passphrase_entry.delete(0, END)


# ---------------------------- SETUP OF UI ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

guicanvas = Canvas(height=200, width=200)
logo_picture = PhotoImage(file="C:\python\logo.png")
guicanvas.create_image(101, 101, image=logo_picture)
guicanvas.grid(row=0, column=1)

# Labels
label_web = Label(text="Website:")
label_web.grid(row=1, column=0)
label_em = Label(text="Email/Username:")
label_em.grid(row=2, column=0)
label_pword = Label(text="Password:")
label_pword.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
em_input = Entry(width=35)
em_input.grid(row=2, column=1, columnspan=2)
em_input.insert(0, "tenzin@gmail.com")
passphrase_entry = Entry(width=21)
passphrase_entry.grid(row=3, column=1)

# Buttons
button_to_generate_password = Button(text="Generate Unique Password", command=generate_pword)
button_to_generate_password.grid(row=3, column=2)
button_to_add = Button(text="Save", width=36, command=store)
button_to_add.grid(row=4, column=1, columnspan=2)

screen.mainloop()
