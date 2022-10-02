
def adminTab():
    pw.grid_forget()
    tabsNote = ttk.Notebook(frame)
    makeSale = ttk.Frame(tabsNote)
    reStock = ttk.Frame(tabsNote)
    viewStock = ttk.Frame(tabsNote)
    customerMgt = ttk.Frame(tabsNote)
    company = ttk.Frame(tabsNote)
    invoice = ttk.Frame(tabsNote)
    #create simple tabs
    tabsNote.add(makeSale, text='Make Sales')
    tabsNote.add(reStock, text='Stock Items')
    tabsNote.add(viewStock, text='View Stock')
    tabsNote.add(customerMgt, text='Customers')
    tabsNote.add(invoice, text='Print Invoice')
    tabsNote.add(company, text='Company Info')
   
    tabsNote.grid()

def workerTab():
    #this is the function for other workers
    pw.grid_forget()
    tabsNote = ttk.Notebook(frame)
    makeSale = ttk.Frame(tabsNote)
    viewStock = ttk.Frame(tabsNote)
    customerMgt = ttk.Frame(tabsNote)
    invoice = ttk.Frame(tabsNote)
    #create simple tabs
    tabsNote.add(makeSale, text='Make Sales', padding=10)
    tabsNote.add(viewStock, text='View Stock', padding=10)
    tabsNote.add(customerMgt, text='Customers', padding=10)
    tabsNote.add(invoice, text='Print Invoice', padding=10)
    tabsNote.grid()
    return
