from tkinter import *
from tkinter import ttk

window = Tk()
class createMenu():
    def adminMenu():
        # create a menubar
        menubar = Menu(window, foreground='black', bg='red')
        window.config(menu=menubar)

        # create a menu
        file_menu = Menu(menubar, foreground='blue')
        pos_menu = Menu(menubar, foreground='blue')
        customer_menu = Menu(menubar, foreground='blue')
        stock_menu = Menu(menubar, foreground='blue')
        purchasing_menu = Menu(menubar, foreground='blue')
        user_menu = Menu(menubar, foreground='blue')
        report_menu = Menu(menubar, foreground='blue')

        # add a menu item to the menu
        file_menu.add_command(label='Backup',command=window.destroy)
        file_menu.add_command(label='Restore',command=window.destroy)
        file_menu.add_command(label='Exit',command=window.destroy)
        user_menu.add_command(label='Add Employee',command=addUserFrame)


        # add the File menu to the menubar
        menubar.add_cascade(label="Home",menu=file_menu)
        menubar.add_cascade(label="Point Of Sale",menu=pos_menu)
        menubar.add_cascade(label="Customer",menu=customer_menu)
        menubar.add_cascade(label="Inventory",menu=stock_menu)
        menubar.add_cascade(label="Finance",menu=purchasing_menu)
        menubar.add_cascade(label="Employee",menu=user_menu)
        menubar.add_cascade(label="Report",menu=report_menu)
        return
    def workMenu():
        # create a menubar
        menubar = Menu(window, foreground='black', bg='red')
        window.config(menu=menubar)

        # create a menu
        file_menu = Menu(menubar, foreground='blue')
        pos_menu = Menu(menubar, foreground='blue')
        customer_menu = Menu(menubar, foreground='blue')
        stock_menu = Menu(menubar, foreground='blue')
        purchasing_menu = Menu(menubar, foreground='blue')
        user_menu = Menu(menubar, foreground='blue')
        report_menu = Menu(menubar, foreground='blue')

        # add a menu item to the menu
        file_menu.add_command(label='Exit',command=window.destroy)
        user_menu.add_command(label='Add Employee',command=addUserFrame)


        # add the File menu to the menubar
        menubar.add_cascade(label="Home",menu=file_menu)
        menubar.add_cascade(label="Point Of Sale",menu=pos_menu)
        menubar.add_cascade(label="Customer",menu=customer_menu)
        menubar.add_cascade(label="Inventory",menu=stock_menu)
        menubar.add_cascade(label="Finance",menu=purchasing_menu)
        menubar.add_cascade(label="Employee",menu=user_menu)
        menubar.add_cascade(label="Report",menu=report_menu)
        return