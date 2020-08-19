from tkinter import *
import tkinter.ttk as ttk
import random
# import window as window
from PIL import Image, ImageTk
from tkinter import Menu, Tk, Toplevel,Label
def about_Us():
    global about_us_window1,Label
    about_us_window1 = Tk()
    about_us_window1.geometry("1920x1080")
    about_us_window1.title("About_Us")

    about_us_window1.config(bg="gray")
    phto_label = Label( about_us_window1)
    phto_label.place(x=50,y=500)
    Image1 = Image.open("img2.jpg")
    photo = ImageTk.PhotoImage(Image1)
    phto_label.configure(image=photo)
    phto_label.image = photo
    phto_label.place(x=250, y=30)

    phto_label = Label(about_us_window1)
    phto_label.place(x=50, y=900)
    Image1 = Image.open("img3.jpg")
    photo = ImageTk.PhotoImage(Image1)
    phto_label.configure(image=photo)
    phto_label.image = photo
    phto_label.place(x=750, y=30)

    about_us_label_phn_no = Label(about_us_window1, text="Manyavart Sarees", font='Helvetica 25 bold',bg="gray",fg="Blue")
    about_us_label_phn_no.place(x=600, y=240)
    var = StringVar()
    about_us_content = Message(about_us_window1, textvariable=var, width=600, font="Helvetica 15 bold",bg="gray",fg="black")
    var.set("""Let Manyavart Deliver The Pure Fabrics You Deserve. Stay Safe & Enjoy Your Classy Wear. Don’t Let Your Wardrobe Go Old. Stay Indoors & Shop Online From The Trendy Collections, The wedding you’re invited to is right around the corner, and so is that important presentation at work, or your child’s sports day event. Time has outrun you and now you have nothing to wear? Fear not. We are here to amaze you with our wide collection of beautifully crafted sarees for your day out. At Manyavart, we make the whole experience of designer sarees online shopping as exciting as it ever is.
             Take it from us, there is hardly anything as enchanting as a well draped nine yard and we know you love it just as much; pamper yourself with a wide range of beautifully crafted sarees for a multitude of occasions ranging from elegant cotton sarees to pompous and dressy designer sarees on our online store.
             Buy Women Sarees Online at Manyavart & Get 100% Cashback on Every Order Shop Now. Banarasi Saree, Cotton Saree, Silk Saree, Kanjivaram Saree, Printed Saree, Designer Saree.
            """)
    about_us_content.place(x=500, y=300)


    about_us_window1.mainloop()
about_Us()