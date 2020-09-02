from tkinter import *
import random
import tkinter.messagebox as box
# import  database_file

window=Tk()
window.geometry("644x344")
window.title("LOGIN")
# images=[]
# i=0
USERNAME = StringVar()
PASSWORD = StringVar()
#for START BUTTON
# database_file.connect_to_database()

def add_user():
    Fname = entry_Firstname.get()
    Lname = entry_Lname.get()
    Email = Email_entry.get()
    Password = password_entry.get()
    gender = var.get()
    if Fname != "" and Lname != "" and Email!= ""  and Password != "":
        database_file.insert_to_user_details(Fname, Lname, Email,gender,Password)

        entry_Firstname.delete(0, 'end')
        entry_Lname.delete(0, 'end')
        Email_entry.delete(0, 'end')

        password_entry.delete(0, 'end')

        sign_up_msgbox = box.showinfo("Sign up", "Sign-up successfully...")
        if sign_up_msgbox == 'ok':
             root.destroy()


    # root.withdraw()



def Login():
    global username,password,st
    USERNAME=username.get()
    PASSWORD=password.get()
    database_file.fetch_user_details(USERNAME, PASSWORD)
    st = database_file.fetch_user_details(USERNAME, PASSWORD)






def sign_up():
    global root
    root=Tk()
    root.title("Home")
    root.geometry("1450x850")

    global  entry_Firstname,entry_Lname,Email_entry,password_entry,var

    label_registration = Label(root, text="signup form", width=20, font=("bold", 20))
    label_registration.place(x=80, y=53)
    label_fname = Label(root, text="FirstName", width=20,fg="black", font=("bold", 10))
    label_fname.place(x=80, y=110)
    entry_Firstname= Entry(root)
    entry_Firstname.place(x=240, y=110)
    label_lname = Label(root, text="LastName", width=20, fg="black", font=("bold", 10))
    label_lname.place(x=80, y=150)
    entry_Lname = Entry(root)
    entry_Lname.place(x=240, y=150)
    label_Email = Label(root, text="Email", width=20, font=("bold", 10))
    label_Email.place(x=68, y=180)
    Email_entry= Entry(root)
    Email_entry.place(x=240, y=180)
    gender_Label = Label(root, text="Gender", width=20, font=("bold", 10))
    gender_Label.place(x=70, y=230)
    var = IntVar()
    Radiobutton(root, text="Male", padx=5, variable=var, value=0).place(x=235, y=230)
    Radiobutton(root, text="Female", padx=20, variable=var, value=1).place(x=290, y=230)
    password_Label = Label(root, text="Password:", width=20, font=("bold", 10))
    password_Label.place(x=70, y=280)
    password_entry = Entry(root)
    password_entry.place(x=240, y=280)
    Button(root, text='Submit', width=20, bg='black', fg='white',command=add_user).place(x=180, y=380)

Top = Frame(window, bd=2, bg="gold")
Top.pack(side=TOP, fill=X)
Form = Frame(window, height=200)
Form.pack(side=TOP, pady=20,expand='true')

lbl_title = Label(Top, text="Online Shopping",bg="black",fg="white", font=('arial', 15),padx=10,pady=10)
lbl_title.pack(fill=X)
lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0)
lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1)


username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

btn_login = Button(Form, text="Login", width=45,bg="black",fg="white",command=Login,relief="solid")
btn_login.grid(pady=25,row=3, columnspan=2)
btn_login = Button(Form, text="Signup", width=45,bg="black",fg="white",command=sign_up,relief="solid")
btn_login.grid(pady=25,row=4, columnspan=2)
Top.mainloop()

