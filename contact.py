from tkinter import *
from PIL import Image,ImageTk
window = Tk()

window.minsize(1300, 760)
window.maxsize(1300, 760)
window.title("contact us")

# photo = PhotoImage(file = " ")

contact= Label(window, text=" contact us", bg="black", fg="white", width=150, padx=10, pady=8,
                font=("comicsansms", 10, "bold"), borderwidth=6, relief=SUNKEN)
    # gui.pack(side='top', fill=X)
contact.place(x=50, y=0)



image = Image.open("C:\\Users\\Snehal\\Desktop\\cloth.png")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image = photo)
photo_label.place(x=500,y=50)

contact_us_label = Label(window, text="ADDRESS ", font='Helvetica 20 bold')
contact_us_label.place(x=70, y=250)
var = StringVar()
contact_us_label_content = Message(window, textvariable=var, width=300, font="Helvetica 10 bold")
var.set(
    "#5, 2nd floor, shree plaza,\n \n nampur Rd,\n \n near  Mahatma Nagar,\n \n Hutatma nagar, Malegaon, Maharashtra 423206")
contact_us_label_content.place(x=50, y=300)

contact_us_label_phn_no = Label(window, text="PHONE NUMBER ", font='Helvetica 20 bold')
contact_us_label_phn_no.place(x=520, y=250)
var = StringVar()
contact_us_label_phn_no_content = Message(window, textvariable=var, width=300, font="Helvetica 10 bold")
var.set(
    "Landline No :0253 2352948 \n \nMobile No :+91 7498406427,\n \n                  +91 98811 47497,\n \n                  +91 98238 37327 ")
contact_us_label_phn_no_content.place(x=550, y=300)

contact_us_label_email = Label(window, text="EMAIL ID ", font='Helvetica 20 bold')
contact_us_label_email.place(x=1000, y=250)
var = StringVar()
contact_us_label_email_content = Message(window, textvariable=var, width=300, font="Helvetica 10 bold")
var.set("                xyz@123gmail.com \n \n            malyavarsraees1524k@gmail.com")
contact_us_label_email_content.place(x=950, y=300)




window.mainloop()

