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
PIECES_ENTRY_COL = 2
OF_LABEL_ROW = 4
OF_LABEL_COL = 4
OF_ENTRY_ROW = 4
OF_ENTRY_COL = 5
PICTURE_CHECK_BUTTON_ROW = 4
PICTURE_CHECK_BUTTON_COL = 6

PRODUCTS_TYPE_LABEL_ROW = 6
PRODUCTS_TYPE_LABEL_COL = 1
PRODUCTS_TYPE_LIST_BOX_ROW = 6
PRODUCTS_TYPE_LIST_BOX_COL = 2

FITTINGS_CHECK_BUTTON_ROW = 6
FITTINGS_CHECK_BUTTON_COL = 5
HOSES_CHECK_BUTTON_ROW = 7
HOSES_CHECK_BUTTON_COL = 5
SENSORS_CHECK_BUTTON_ROW = 8
SENSORS_CHECK_BUTTON_COL = 5
BRACKETS_CHECK_BUTTON_ROW = 9
BRACKETS_CHECK_BUTTON_COL = 5
MOUNTS_CHECK_BUTTON_ROW = 10
MOUNTS_CHECK_BUTTON_COL = 5
RAD_CAP_CHECK_BUTTON_ROW = 11
RAD_CAP_CHECK_BUTTON_COL = 5
SHROUD_CHECK_BUTTON_ROW = 12
SHROUD_CHECK_BUTTON_COL = 5
FAN_CHECK_BUTTON_ROW = 13
FAN_CHECK_BUTTON_COL = 5
CHAIN_CHECK_BUTTON_ROW = 14
CHAIN_CHECK_BUTTON_COL = 5
STRAPS_CHECK_BUTTON_ROW = 15
STRAPS_CHECK_BUTTON_COL = 5

PARTS_IN_BLUE_BIN_ROW = 17
PARTS_IN_BLUE_BIN_COL = 1
NOTE_LABEL_ROW = 19
NOTE_LABEL_COL = 2
NOTE_ENTRY_ROW = 19
NOTE_ENTRY_COL = 3

OUTPUT_PAD_ROW = 21
OUTPUT_PAD_COL = 2

CANCEL_BUTTON_ROW = 21
CANCEL_BUTTON_COL = 2
SAVE_BUTTON_ROW = 21
SAVE_BUTTON_COL = 6

#SJ0130222 - Ideally the products type list should be stored in a database; the setback of reading from a database
#SJ0130222 - is that there is a need to write a code to allow user to do data entry into the database.
productsType = ['Radiator', 'CAC', 'Condenser', 'Fuel Tank', 'Evaporator', 'Heater Core', 'Radiator Core',
'DPF', 'DPF-DOC Combo', 'EGR', 'Coolant Pipe', 'Oil Cooler', 'AC Hose', 'Cooling Module', 'Other']

FITTINGS = 0
HOSES = 1
SENSORS = 2
BRACKETS = 3
MOUNTS = 4
RAD_CAP = 5
SHROUD = 6
FAN = 7
CHAIN = 8
STRAPS = 9
TOTAL_NUMBER_OF_PARTS = 10

numberOfParts = [0] * TOTAL_NUMBER_OF_PARTS

customerName = ''
productsTypelistbox = []
outputPad = ''

class WER_Main:
    def __init__(self, master):
        master.title('West End Radiators')

        #SJ5110222 - Input field for customer name
        global customerName
        self.customerLabel = Label(master, text='Customer: ').grid(row=CUSTOMER_LABEL_ROW, column=CUSTOMER_LABEL_COL)
        #self.customerEntry = Entry(master)
        #self.customerEntry.grid(row=CUSTOMER_ENTRY_ROW, column=CUSTOMER_ENTRY_COL)
        customerName = Entry(master)
        customerName.grid(row=CUSTOMER_ENTRY_ROW, column=CUSTOMER_ENTRY_COL)

        #SJ5110222 - Input field for work order
        self.workOrderLabel = Label(master, text='WO: ').grid(row=WORK_ORDER_LABEL_ROW, column=WORK_ORDER_LABEL_COL)
        self.workOrderEntry = Entry(master)
        self.workOrderEntry.grid(row=WORK_ORDER_ENTRY_ROW, column=WORK_ORDER_ENTRY_COL)

        #SJ6120222 - Input field for Date received
        self.dateReceivedLabel = Label(master, text='Date Received: ').grid(row=DATE_RECEIVED_LABEL_ROW, column=DATE_RECEIVED_LABEL_COL)
        self.dateReceivedEntry = DateEntry(master, values="Text", year=2022, state="readonly", date_pattern="yyyy-mm-dd")
        self.dateReceivedEntry.grid(row=DATE_RECEIVED_ENTRY_ROW, column=DATE_RECEIVED_ENTRY_COL, padx=20, pady=5, sticky=W)

        #SJ6120222 - Input field for Received by
        self.receivedByLabel = Label(master, text='Received by: ').grid(row=RECEIVED_BY_LABEL_ROW, column=RECEIVED_BY_LABEL_COL)
        self.receivedByEntry = Entry(master)
        self.receivedByEntry.grid(row=RECEIVED_BY_ENTRY_ROW, column=RECEIVED_BY_ENTRY_COL)

        #SJ6120222 - Input field for pieces
        self.piecesLabel = Label(master, text='Piece(s): ').grid(row=PIECES_LABEL_ROW, column=PIECES_LABEL_COL)
        self.piecesEntry = Entry(master)
        self.piecesEntry.grid(row=PIECES_ENTRY_ROW, column=PIECES_ENTRY_COL)

        #SJ6120222 - Input field for of
        self.ofLabel = Label(master, text='of: ').grid(row=OF_LABEL_ROW, column=OF_LABEL_COL)
        self.ofEntry = Entry(master)
        self.ofEntry.grid(row=OF_ENTRY_ROW, column=OF_ENTRY_COL)

        #SJ6120222 - Input field for pictures
        pictureStatus = IntVar()
        self.pictureCheckButton = Checkbutton(master, text='Pictures', var=pictureStatus)
        self.pictureCheckButton.grid(row=PICTURE_CHECK_BUTTON_ROW, column=PICTURE_CHECK_BUTTON_COL)

        #SJ0130222 - Input field for product types
        self.productsTypeLabel = Label(master, text='Received items: ').grid(row=PRODUCTS_TYPE_LABEL_ROW, column=PRODUCTS_TYPE_LABEL_COL)
        #self.productsTypelistbox = Listbox(master, selectmode=MULTIPLE)
        #for productItem in productsType:
        #    self.productsTypelistbox.insert(END, productItem)
        #self.productsTypelistbox.grid(row=PRODUCTS_TYPE_LIST_BOX_ROW, column=PRODUCTS_TYPE_LIST_BOX_COL)
        global productsTypelistbox
        productsTypelistbox = Listbox(master, selectmode=MULTIPLE)
        for productItem in productsType:
            productsTypelistbox.insert(END, productItem)
        productsTypelistbox.grid(row=PRODUCTS_TYPE_LIST_BOX_ROW, column=PRODUCTS_TYPE_LIST_BOX_COL)

        #SJ1140222 - Check button fields for number of parts
        numberOfPartsFrame = Frame()
        numberOfParts[FITTINGS] = IntVar()
        self.fittingsCheckButton = Checkbutton(numberOfPartsFrame, text='Fittings ', var=numberOfParts[FITTINGS])
        self.fittingsCheckButton.grid(row=FITTINGS_CHECK_BUTTON_ROW, column=FITTINGS_CHECK_BUTTON_COL)

        numberOfParts[HOSES] = IntVar()
        self.hosesCheckButton = Checkbutton(numberOfPartsFrame, text='Hoses ', var=numberOfParts[HOSES])
        self.hosesCheckButton.grid(row=HOSES_CHECK_BUTTON_ROW, column=HOSES_CHECK_BUTTON_COL)

        numberOfParts[SENSORS] = IntVar()
        self.sensorsCheckButton = Checkbutton(numberOfPartsFrame, text='Sensors ', var=numberOfParts[SENSORS])
        self.sensorsCheckButton.grid(row=SENSORS_CHECK_BUTTON_ROW, column=SENSORS_CHECK_BUTTON_COL)

        numberOfParts[BRACKETS] = IntVar()
        self.bracketsCheckButton = Checkbutton(numberOfPartsFrame, text='Brackets ', var=numberOfParts[BRACKETS])
        self.bracketsCheckButton.grid(row=BRACKETS_CHECK_BUTTON_ROW, column=BRACKETS_CHECK_BUTTON_COL)

        numberOfParts[MOUNTS] = IntVar()
        self.mountCheckButton = Checkbutton(numberOfPartsFrame, text='Mount ', var=numberOfParts[MOUNTS])
        self.mountCheckButton.grid(row=MOUNTS_CHECK_BUTTON_ROW, column=MOUNTS_CHECK_BUTTON_COL)

        numberOfParts[RAD_CAP] = IntVar()
        self.radCapCheckButton = Checkbutton(numberOfPartsFrame, text='Rad Cap ', var=numberOfParts[RAD_CAP])
        self.radCapCheckButton.grid(row=RAD_CAP_CHECK_BUTTON_ROW, column=RAD_CAP_CHECK_BUTTON_COL)

        numberOfParts[SHROUD] = IntVar()
        self.shroudCheckButton = Checkbutton(numberOfPartsFrame, text='Shroud ', var=numberOfParts[SHROUD])
        self.shroudCheckButton.grid(row=SHROUD_CHECK_BUTTON_ROW, column=SHROUD_CHECK_BUTTON_COL)

        numberOfParts[FAN] = IntVar()
        self.fanCheckButton = Checkbutton(numberOfPartsFrame, text='Fan ', var=numberOfParts[FAN])
        self.fanCheckButton.grid(row=FAN_CHECK_BUTTON_ROW, column=FAN_CHECK_BUTTON_COL)

        numberOfParts[CHAIN] = IntVar()
        self.chainCheckButton = Checkbutton(numberOfPartsFrame, text='Chain ', var=numberOfParts[CHAIN])
        self.chainCheckButton.grid(row=CHAIN_CHECK_BUTTON_ROW, column=CHAIN_CHECK_BUTTON_COL)

        numberOfParts[STRAPS] = IntVar()
        self.strapsCheckButton = Checkbutton(numberOfPartsFrame, text='Straps ', var=numberOfParts[STRAPS])
        self.strapsCheckButton.grid(row=STRAPS_CHECK_BUTTON_ROW, column=STRAPS_CHECK_BUTTON_COL)
        numberOfPartsFrame.grid(row=FITTINGS_CHECK_BUTTON_ROW, column=FITTINGS_CHECK_BUTTON_COL)

        #SJ3160222 - Check box field for parts in blue bin
        partsInBlueBin = IntVar()
        self.partsInBlueBinCheckButton = Checkbutton(master, text='Are parts in a Blue Bin? ', var=partsInBlueBin)
        self.partsInBlueBinCheckButton.grid(row=PARTS_IN_BLUE_BIN_ROW, column=PARTS_IN_BLUE_BIN_COL)

        #SJ3160222 - Text field for notes
        self.notesLabel = Label(master, text='Notes: ').grid(row=NOTE_LABEL_ROW, column=NOTE_LABEL_COL)
        self.notesTextbox = Text(master, font=('Verdana', 16), height=6, width=20)
        self.notesTextbox.grid(row=NOTE_ENTRY_ROW, column=NOTE_ENTRY_COL)

        global outputPad
        outputPad = Entry(master)
        outputPad.grid(row=OUTPUT_PAD_ROW, column=OUTPUT_PAD_COL)

        self.cancelButton = Button(text='Cancel', command=lambda x=master: self.cancelCallback(x))
        #self.label.grid(row=0, column=0)
        self.cancelButton.grid(row=CANCEL_BUTTON_ROW, column=CANCEL_BUTTON_COL)

        self.saveButton = Button(text='Save', command=lambda x=master: self.saveCallback(x))
        #self.label.grid(row=0, column=0)
        self.saveButton.grid(row=SAVE_BUTTON_ROW, column=SAVE_BUTTON_COL)

    def cancelCallback(self, master):
        #global outputPad
        global customerName
        #self.custo = customerName.get()
        #outputPad.insert(0, self.custo)

    def saveCallback(self, master):
        #global outputPad
        global customerName
        global productsTypelistbox
        self.custo = customerName.get()
        self.productsTypeList = productsTypelistbox.curselection()
        outputPad.insert(0, self.productsTypeList)
        #print('customerEntry is: ', customerEntry.get())
        #self.label.configure(text='Button clicked')


root = Tk()

app = WER_Main(root)

mainloop()

"""
label = Label(text='Not clicked')
button = Button(text='Click me', command=callback)
label.grid(row=0, column=0)
button.grid(row=1, column=0)

Button(text=alphabet[i], command = lambda x=i: callback(x))

"""
