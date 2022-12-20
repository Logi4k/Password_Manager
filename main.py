from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import os


#Password Generator
def generate_password():
    password_entry.delete(0, END)
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)



#Save the website and password into a file
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="You forgot something...", message="Fill in the empty fields.")
    else:   
        is_ok = messagebox.askokcancel(title=website,
                            message=f"These are the details you entered: \nEmail: {email}\nPassword: {password}"
                            f"\nIs it okay to save")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title="Generated", message="Password has been generated")
                

#Open the saved data file
def open_file():
    file_path = os.path.abspath("data.txt")
    os.startfile(file_path)

#Create a TKinter window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Defining windows parameters
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Text entry fields
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "philips@logi4k.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4,column=1, columnspan=2)

#Open file button
data_file_button = Button(text="Open saved details", command=open_file)
data_file_button.grid(row=5, column=1, columnspan=2)

window.mainloop()