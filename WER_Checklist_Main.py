#Project: WER checklist
#Date: Feb 11, 2022
#Remark: This page consist of user interface for user input. It uses tkinter GUI

from tkinter import *
from tkcalendar import DateEntry

#SJ0130222 - Global variables declaration

#SJ6120222 - Row and Column position of entry fields
CUSTOMER_LABEL_ROW = 1
CUSTOMER_LABEL_COL = 1
CUSTOMER_ENTRY_ROW = 1
CUSTOMER_ENTRY_COL = 2
WORK_ORDER_LABEL_ROW = 1
WORK_ORDER_LABEL_COL = 4
WORK_ORDER_ENTRY_ROW = 1
WORK_ORDER_ENTRY_COL = 5

DATE_RECEIVED_LABEL_ROW = 3
DATE_RECEIVED_LABEL_COL = 1
DATE_RECEIVED_ENTRY_ROW = 3
DATE_RECEIVED_ENTRY_COL = 2
RECEIVED_BY_LABEL_ROW = 3
RECEIVED_BY_LABEL_COL = 4
RECEIVED_BY_ENTRY_ROW = 3
RECEIVED_BY_ENTRY_COL = 5

PIECES_LABEL_ROW = 4
PIECES_LABEL_COL = 1
PIECES_ENTRY_ROW = 4
PIECES_LABEL_COL = 2
OF_LABEL_ROW = 4
OF_LABEL_COL = 1
OF_ENTRY_ROW = 4
OF_ENTRY_COL = 5
PICTURE_CHECK_BUTTON_ROW = 4
PICTURE_CHECK_BUTTON_COL = 6

PRODUCTS_TYPE_LABEL_ROW = 6
PRODUCTS_TYPE_LABEL_COL = 1
PRODUCTS_TYPE_LIST_BOX_ROW = 6
PRODUCTS_TYPE_LIST_BOX_COL = 2


#SJ0130222 - Ideally the products type list should be stored in a database; the setback of reading from a List
#SJ0130222 - is that there is a need to write a code to allow user to do data entry into the database.
productsType = ['Radiator', 'CAC', 'Condenser', 'Fuel Tank', 'Evaporator', 'Heater Core', 'Radiator Core',
'DPF', 'DPF-DOC Combo', 'EGR', 'Coolant Pipe', 'Oil Cooler', 'AC Hose', 'Cooling Module', 'Other']


class WER_Main:
    def __init__(self, master):
        master.title('West End Radiators')

        #SJ5110222 - Input field for customer name
        self.customerLabel = Label(master, text='Customer: ').grid(row=CUSTOMER_LABEL_ROW, column=CUSTOMER_LABEL_COL)
        self.customerEntry = Entry(master)
        self.customerEntry.grid(row=CUSTOMER_ENTRY_ROW, column=CUSTOMER_ENTRY_COL)

        #SJ5110222 - Input field for work order
        self.workOrderLabel = Label(master, text='WO: ').grid(row=WORK_ORDER_LABEL_ROW, column=WORK_ORDER_LABEL_COL)
        self.workOrderEntry = Entry(master)
        self.workOrderEntry.grid(row=WORK_ORDER_ENTRY_ROW, column=WORK_ORDER_ENTRY_COL)

        #SJ6120222 - Input field for Date received
        self.dateReceivedLabel = Label(text='Date Received: ').grid(row=DATE_RECEIVED_LABEL_ROW, column=DATE_RECEIVED_LABEL_COL)
        self.dateReceivedEntry = DateEntry(master, values="Text", year=2022, state="readonly", date_pattern="yyyy-mm-dd")
        self.dateReceivedEntry.grid(row=DATE_RECEIVED_ENTRY_ROW, column=DATE_RECEIVED_ENTRY_COL, padx=20, pady=5, sticky=W)

        #SJ6120222 - Input field for Received by
        self.receivedByLabel = Label(master, text='Received by: ').grid(row=RECEIVED_BY_LABEL_ROW, column=RECEIVED_BY_LABEL_COL)
        self.receivedByEntry = Entry(master)
        self.receivedByEntry.grid(row=RECEIVED_BY_ENTRY_ROW, column=RECEIVED_BY_ENTRY_COL)

        #SJ6120222 - Input field for pieces
        self.piecesLabel = Label(master, text='Piece(s): ').grid(row=PIECES_LABEL_ROW, column=PIECES_LABEL_COL)
        self.piecesEntry = Entry(master)
        self.piecesEntry.grid(row=PIECES_ENTRY_ROW, column=PIECES_LABEL_COL)

        #SJ6120222 - Input field for of
        self.ofLabel = Label(master, text='of: ').grid(row=OF_LABEL_ROW, column=OF_LABEL_COL)
        self.ofEntry = Entry(master)
        self.ofEntry.grid(row=OF_ENTRY_ROW, column=OF_ENTRY_COL)

        #SJ6120222 - Input field for pictures
        pictureStatus = IntVar()
        self.pictureCheckButton = Checkbutton(text='Pictures', var=pictureStatus)
        self.pictureCheckButton.grid(row=PICTURE_CHECK_BUTTON_ROW, column=PICTURE_CHECK_BUTTON_COL)

        #SJ0130222 - Input field for product types
        self.productsTypeLabel = Label(master, text='Received items: ').grid(row=PRODUCTS_TYPE_LABEL_ROW, column=PRODUCTS_TYPE_LABEL_COL)
        self.productsTypelistbox = Listbox(master, selectmode=MULTIPLE)
        for productItem in productsType:
            self.productsTypelistbox.insert(END, productItem)
        # self.productsTypelistbox.pack()
        self.productsTypelistbox.grid(row=PRODUCTS_TYPE_LIST_BOX_ROW, column=PRODUCTS_TYPE_LIST_BOX_COL)


        #self.button = Button(text='Click me', command=self.callback)
        #self.label.grid(row=0, column=0)
        #self.button.grid(row=1, column=0)

    def callback(self):
        self.label.configure(text='Button clicked')


root = Tk()

app = WER_Main(root)

mainloop()
