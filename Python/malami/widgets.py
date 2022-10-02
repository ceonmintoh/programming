from curses import window
from tkinter import *
from tkinter import ttk
window = Tk()

frame = ttk.Frame(window).place(relx=0.5, rely=0.5, anchor='c')
class inputWindows():
    def splashEntry():
        labels = ttk.Label(frame, text='Welcome to Malami Ventures', background='blue',foreground='white').grid(ipadx=10,pady=10)
        #display tabs
        pw = ttk.PanedWindow(frame, orient=HORIZONTAL)
        lgframe = ttk.LabelFrame(pw, text='Login',width=200,height=100, border=5, labelanchor=N, padding=10)
        aboutframe = ttk.LabelFrame(pw, text='About Sofware',width=200,height=100,border=5, labelanchor=N)
        pw.add(lgframe)
        pw.add(aboutframe)
            #Add Login Form
        label1 = ttk.Label(lgframe, text='Username').grid(row=0, column=0)
        label2 = ttk.Label(lgframe, text='Password').grid(row=1, column=0)
        uname = ttk.Entry(lgframe).grid(row=0, column=1, columnspan=2)
        pwords = ttk.Entry(lgframe).grid(row=1, column=1, columnspan=2)
        submit_btn = ttk.Button(lgframe,text='Login Admin', width=20).grid(row=2, column=1)
        submit_btn = ttk.Button(lgframe,text='Login Worker', width=20).grid(row=2, column=2)

            #Software Info
        label4 = ttk.Label(aboutframe, text='Name:',width=10, background='black' ,foreground='white').grid(row=0, column=0)
        label5 = ttk.Label(aboutframe, text='AMV Shop Manager',width=25).grid(row=0, column=1)
        label6 = ttk.Label(aboutframe, text='Creator:',width=10,background='black', foreground='white').grid(row=1, column=0)
        label7 = ttk.Label(aboutframe, text='Nelson ICT Services Gembu',width=25).grid(row=1, column=1)
        label8 = ttk.Label(aboutframe, text='Version:',width=10,background='black', foreground='white').grid(row=2, column=0)
        label9 = ttk.Label(aboutframe, text='1.0',width=25).grid(row=2, column=1)
        label10 = ttk.Label(aboutframe, text='www.nelsonict.org.ng',width=20, justify=CENTER, background='black', foreground='white').grid(row=3, column=0, columnspan=2)

        pw.grid()
        return
    def addUserWidget():
        frame.destroy()
        addWorker = ttk.Frame(window)
        lb1 = ttk.Label(addWorker, text="Username").grid(row=0, column=0, pady=4)
        lb2 = ttk.Label(addWorker, text="First Name").grid(row=1, column=0, pady=4)
        lb3 = ttk.Label(addWorker, text="Last Name").grid(row=2, column=0, pady=4)
        lb4 = ttk.Label(addWorker, text="Address").grid(row=3, column=0, pady=4)
        lb5 = ttk.Label(addWorker, text="Date Of Birth").grid(row=4, column=0, pady=4)
        lb6 = ttk.Label(addWorker, text="Phone Number").grid(row=5, column=0, pady=4)
        lb7 = ttk.Label(addWorker, text="Email").grid(row=0, column=6, pady=4)
        submit_user = ttk.Button(addWorker, text='Add User', command=insertUser).grid(row=7, column=0, pady=4)
        submit_user = ttk.Button(addWorker, text='Add Admin', command=insertAdmin).grid(row=7, column=0, pady=4)

        uname = ttk.Entry(addWorker).grid(row=0, column=1, pady=4)
        fname = ttk.Entry(addWorker).grid(row=1, column=1, pady=4)
        lname = ttk.Entry(addWorker).grid(row=2, column=1, pady=4)
        address = ttk.Entry(addWorker).grid(row=3, column=1, pady=4)
        dob = ttk.Entry(addWorker).grid(row=4, column=1, pady=4)
        phone = ttk.Entry(addWorker).grid(row=5, column=1, pady=4)
        email = ttk.Entry(addWorker).grid(row=6, column=1, pady=4)

        addWorker.place(relx=0.5, rely=0.5, anchor='c')
        return
    def addProductWidget():
        frame.destroy()
        addWorker = ttk.Frame(window)
        lb1 = ttk.Label(addWorker, text="Product Name").grid(row=0, column=0, pady=4)
        lb2 = ttk.Label(addWorker, text="Size (cl)").grid(row=1, column=0, pady=4)
        lb3 = ttk.Label(addWorker, text="Color").grid(row=2, column=0, pady=4)
        lb4 = ttk.Label(addWorker, text="Address").grid(row=3, column=0, pady=4)
        lb5 = ttk.Label(addWorker, text="Date Of Birth").grid(row=4, column=0, pady=4)
        lb6 = ttk.Label(addWorker, text="Phone Number").grid(row=5, column=0, pady=4)
        lb7 = ttk.Label(addWorker, text="Email").grid(row=0, column=6, pady=4)
        submit_user = ttk.Button(addWorker, text='Add Product', command=insertUser).grid(row=7, column=0, pady=4)

        uname = ttk.Entry(addWorker).grid(row=0, column=1, pady=4)
        fname = ttk.Entry(addWorker).grid(row=1, column=1, pady=4)
        lname = ttk.Entry(addWorker).grid(row=2, column=1, pady=4)
        address = ttk.Entry(addWorker).grid(row=3, column=1, pady=4)
        dob = ttk.Entry(addWorker).grid(row=4, column=1, pady=4)
        phone = ttk.Entry(addWorker).grid(row=5, column=1, pady=4)
        email = ttk.Entry(addWorker).grid(row=6, column=1, pady=4)

        addWorker.place(relx=0.5, rely=0.5, anchor='c')
        return
    def addOrderWidget():
        frame.destroy()
        addWorker = ttk.Frame(window)
        lb1 = ttk.Label(addWorker, text="Username").grid(row=0, column=0, pady=4)
        lb2 = ttk.Label(addWorker, text="First Name").grid(row=1, column=0, pady=4)
        lb3 = ttk.Label(addWorker, text="Last Name").grid(row=2, column=0, pady=4)
        lb4 = ttk.Label(addWorker, text="Address").grid(row=3, column=0, pady=4)
        lb5 = ttk.Label(addWorker, text="Date Of Birth").grid(row=4, column=0, pady=4)
        lb6 = ttk.Label(addWorker, text="Phone Number").grid(row=5, column=0, pady=4)
        lb7 = ttk.Label(addWorker, text="Email").grid(row=0, column=6, pady=4)
        submit_user = ttk.Button(addWorker, text='Add User', command=insertUser).grid(row=7, column=0, pady=4)

        uname = ttk.Entry(addWorker).grid(row=0, column=1, pady=4)
        fname = ttk.Entry(addWorker).grid(row=1, column=1, pady=4)
        lname = ttk.Entry(addWorker).grid(row=2, column=1, pady=4)
        address = ttk.Entry(addWorker).grid(row=3, column=1, pady=4)
        dob = ttk.Entry(addWorker).grid(row=4, column=1, pady=4)
        phone = ttk.Entry(addWorker).grid(row=5, column=1, pady=4)
        email = ttk.Entry(addWorker).grid(row=6, column=1, pady=4)

        addWorker.place(relx=0.5, rely=0.5, anchor='c')
        return