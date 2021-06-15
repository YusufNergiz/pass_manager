from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



window = Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    input_entry_1 = entry_1.get()
    with open("data.json", "r") as finding_password:
        password_data = json.load(finding_password)
        try:
            found_site = password_data[input_entry_1]
            messagebox.showinfo(title=input_entry_1, message=f"Email: {found_site['email']} "
                                                             f"\nPassword: {found_site['password']}")
        except KeyError:
            messagebox.showerror(message=f"Oops! {input_entry_1} is not found.")


def add_button_pressed():
    input_entry_1 = entry_1.get()
    input_entry_2 = entry_2.get()
    input_entry_3 = entry_3.get()
    new_data = {
        input_entry_1: {

            "email": input_entry_2,
            "password": input_entry_3,
        }
    }

    if len(input_entry_1) == 0 or len(input_entry_3) == 0:
        messagebox.showerror(title="Error!", message="You forgot to fill everything!!")
    elif len(input_entry_1) > 0 or len(input_entry_3) > 0:
        is_ok = messagebox.askokcancel(title=input_entry_1, message=f"Are you sure to save your passwords like this:"
                                                                    f" \nEmail: {input_entry_2}"
                                                                    f" \nPassword: {input_entry_3}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:

                entry_1.delete("0", last="end")
                entry_3.delete("0", last="end")
                entry_2.delete("0", "end")
                entry_2.insert(0, "yusufyn04@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
#  LABELS  #
label_1 = Label(text="Website: ")
label_1.config(height=2, bg="white")
label_1.grid(column=1, row=2)

label_2 = Label(text="Email/Username: ")
label_2.config(height=2, bg="white")
label_2.grid(column=1, row=3)

label_3 = Label(text="Password: ")
label_3.config(height=2, bg="white")
label_3.grid(column=1, row=4)
###############################

#  ENTRIES  #
entry_1 = Entry(width=30)
entry_1.grid(column=2, row=2)
entry_1.focus()


entry_2 = Entry(width=48)
entry_2.grid(column=2, row=3, columnspan=2)
entry_2.insert(0, "yusufyn04@gmail.com")

entry_3 = Entry(width=30)
entry_3.grid(column=2, row=4)
################################

#  BUTTONS  #
button_1 = Button(text="Generate Password")
button_1.config(command=generate_password)
button_1.grid(column=3, row=4)

button_2 = Button(text="Add", width=41)
button_2.config(command=add_button_pressed)
button_2.grid(column=2, row=5, columnspan=3)

button_3 = Button(text="Search", width=14)
button_3.config(command=find_password)
button_3.grid(column=3, row=2)


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file=r"logo.gif")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=2, row=1)

window.mainloop()