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
PICTURE_CHECK_BUTTON_ROW = 5
PICTURE_CHECK_BUTTON_COL = 1
PHOTOES_CHECK_BUTTON_ROW = 5
PHOTOES_CHECK_BUTTON_COL = 4

PRODUCTS_TYPE_LABEL_ROW = 6
PRODUCTS_TYPE_LABEL_COL = 1
PRODUCTS_TYPE_LIST_BOX_ROW = 6
PRODUCTS_TYPE_LIST_BOX_COL = 2

NUMBER_OF_PARTS_LIST_BOX_ROW = 6
NUMBER_OF_PARTS_LIST_BOX_COL = 5

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
NOTE_LABEL_ROW = 25
NOTE_LABEL_COL = 2
NOTE_ENTRY_ROW = 25
NOTE_ENTRY_COL = 3

OUTPUT_PAD_ROW = 28
OUTPUT_PAD_COL = 2

CANCEL_BUTTON_ROW = 28
CANCEL_BUTTON_COL = 1
SAVE_BUTTON_ROW = 28
SAVE_BUTTON_COL = 6

#SJ0130222 - Ideally the products type list should be stored in a database; the setback of reading from a database
#SJ0130222 - is that there is a need to write a code to allow user to do data entry into the database.
productsType = ['Radiator', 'CAC', 'Condenser', 'Fuel Tank', 'Evaporator', 'Heater Core', 'Radiator Core',
'DPF', 'DPF-DOC Combo', 'EGR', 'Coolant Pipe', 'Oil Cooler', 'AC Hose', 'Cooling Module', 'Other']

numberOfParts = ['Fitting', 'Hoses', 'Sensors', 'Brackets', 'Mounts', 'Rad Cap', 'Shroud', 'FAN', 'Chain', 'Straps']
#TOTAL_NUMBER_OF_PARTS = 10

#numberOfParts = [0] * TOTAL_NUMBER_OF_PARTS

customerName = ''
workOrder = ''
dateReceived = ''
receivedBy = ''
numOfPieces = 0
ofPieces = 0
pictureStatus = 0
photoesStatus = 0
productsTypeListbox = []
numberOfPartsListbox = []
partsInBlueBin = 0
notes = ''
outputPad = ''

class WER_Main:
    def __init__(self, master):
        master.title('West End Radiators')

        global customerName
        global workOrder
        global dateReceived
        global receivedBy
        global numOfPieces
        global ofPieces
        global pictureStatus
        global photoesStatus
        global productsTypeListbox
        global numberOfPartsListbox
        global partsInBlueBin
        global notes
        global outputPad

        #SJ5110222 - Input field for customer name
        self.customerLabel = Label(master, text='Customer: ').grid(row=CUSTOMER_LABEL_ROW, column=CUSTOMER_LABEL_COL)
        customerName = Entry(master)
        customerName.grid(row=CUSTOMER_ENTRY_ROW, column=CUSTOMER_ENTRY_COL)

        #SJ5110222 - Input field for work order
        self.workOrderLabel = Label(master, text='WO: ').grid(row=WORK_ORDER_LABEL_ROW, column=WORK_ORDER_LABEL_COL)
        workOrder = Entry(master)
        workOrder.grid(row=WORK_ORDER_ENTRY_ROW, column=WORK_ORDER_ENTRY_COL)

        #SJ6120222 - Input field for Date received
        self.dateReceivedLabel = Label(master, text='Date Received: ').grid(row=DATE_RECEIVED_LABEL_ROW, column=DATE_RECEIVED_LABEL_COL)
        dateReceived = DateEntry(master, values="Text", year=2022, state="readonly", date_pattern="yyyy-mm-dd")
        dateReceived.grid(row=DATE_RECEIVED_ENTRY_ROW, column=DATE_RECEIVED_ENTRY_COL, padx=20, pady=5, sticky=W)

        #SJ6120222 - Input field for Received by
        self.receivedByLabel = Label(master, text='Received by: ').grid(row=RECEIVED_BY_LABEL_ROW, column=RECEIVED_BY_LABEL_COL)
        receivedBy = Entry(master)
        receivedBy.grid(row=RECEIVED_BY_ENTRY_ROW, column=RECEIVED_BY_ENTRY_COL)

        #SJ6120222 - Input field for pieces
        self.piecesLabel = Label(master, text='Piece(s): ').grid(row=PIECES_LABEL_ROW, column=PIECES_LABEL_COL)
        numOfPieces = Entry(master)
        numOfPieces.grid(row=PIECES_ENTRY_ROW, column=PIECES_ENTRY_COL)

        #SJ6120222 - Input field for of
        self.ofLabel = Label(master, text='of: ').grid(row=OF_LABEL_ROW, column=OF_LABEL_COL)
        ofPieces = Entry(master)
        ofPieces.grid(row=OF_ENTRY_ROW, column=OF_ENTRY_COL)

        #SJ6120222 - Input field for pictures
        pictureStatus = IntVar()
        self.pictureCheckButton = Checkbutton(master, text='Pictures', var=pictureStatus)
        self.pictureCheckButton.grid(row=PICTURE_CHECK_BUTTON_ROW, column=PICTURE_CHECK_BUTTON_COL)

        #SJ6190222 - Photoes uploaded
        photoesStatus = IntVar()
        self.photoesCheckButton = Checkbutton(master, text='Photoes Uploaded?', var=photoesStatus)
        self.photoesCheckButton.grid(row=PHOTOES_CHECK_BUTTON_ROW, column=PHOTOES_CHECK_BUTTON_COL)

        #SJ0130222 - Input field for product types
        self.productsTypeLabel = Label(master, text='Received items: ').grid(row=PRODUCTS_TYPE_LABEL_ROW, column=PRODUCTS_TYPE_LABEL_COL)
        productsTypeListbox = Listbox(master, selectmode=MULTIPLE, exportselection=0)
        for productItem in productsType:
            productsTypeListbox.insert(END, productItem)
        productsTypeListbox.grid(row=PRODUCTS_TYPE_LIST_BOX_ROW, column=PRODUCTS_TYPE_LIST_BOX_COL)

        #SJ1140222 - Listbox fields for number of parts
        numberOfPartsListbox = Listbox(master, selectmode=MULTIPLE, exportselection=0)
        for partItem in numberOfParts:
            numberOfPartsListbox.insert(END, partItem)
        numberOfPartsListbox.grid(row=NUMBER_OF_PARTS_LIST_BOX_ROW, column=NUMBER_OF_PARTS_LIST_BOX_COL)

        #SJ3160222 - Check box field for parts in blue bin
        partsInBlueBin = IntVar()
        self.partsInBlueBinCheckButton = Checkbutton(master, text='Are parts in a Blue Bin? ', var=partsInBlueBin)
        self.partsInBlueBinCheckButton.grid(row=PARTS_IN_BLUE_BIN_ROW, column=PARTS_IN_BLUE_BIN_COL)

        #SJ3160222 - Text field for notes
        self.notesLabel = Label(master, text='Notes: ').grid(row=NOTE_LABEL_ROW, column=NOTE_LABEL_COL)
        notes = Text(master, font=('Verdana', 16), height=6, width=20)
        notes.grid(row=NOTE_ENTRY_ROW, column=NOTE_ENTRY_COL)

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
        global outputPad
        global productsTypeListbox
        global numberOfPartsListbox
        self.productsTypeList = productsTypeListbox.curselection()
        self.numberOfPartsList = numberOfPartsListbox.curselection()
        outputPad.insert(0, self.productsTypeList+self.numberOfPartsList)
        print('product type list: ', ''.join(list(map(str, self.productsTypeList))))
        print('product type list: ', ''.join(list(map(str, self.numberOfPartsList))))
        #self.label.configure(text='Button clicked')

        #a = [4, 3, 2, 1, 10, 14, -14]
        #print(list(map(str, a)))



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
