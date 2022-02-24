#Project: WER checklist
#Date: Feb 11, 2022
#Remark: This page consist of user interface for user input. It uses tkinter GUI

from tkinter import *
from tkinter.messagebox import *
from tkcalendar import DateEntry
import sqlite3

#SJ0130222 - Global variables declaration

#SJ1210222 - SJ6120222 - Row and Column position of entry fields
CUSTOMER_LABEL_ROW = 1
CUSTOMER_LABEL_COL = 1
CUSTOMER_ENTRY_ROW = CUSTOMER_LABEL_ROW          #row 1
CUSTOMER_ENTRY_COL = CUSTOMER_LABEL_COL + 1      #col 2
WORK_ORDER_LABEL_ROW = CUSTOMER_LABEL_ROW        #row 1
WORK_ORDER_LABEL_COL = CUSTOMER_ENTRY_COL + 2    #col 4
WORK_ORDER_ENTRY_ROW = CUSTOMER_LABEL_ROW        #row 1
WORK_ORDER_ENTRY_COL = WORK_ORDER_LABEL_COL + 1  #col 5
#SJ1210222 - Row 2 not used
DATE_RECEIVED_LABEL_ROW = WORK_ORDER_ENTRY_ROW + 2    #row 3
DATE_RECEIVED_LABEL_COL = 1                           #col 1
DATE_RECEIVED_ENTRY_ROW = DATE_RECEIVED_LABEL_ROW     #row 3
DATE_RECEIVED_ENTRY_COL = DATE_RECEIVED_LABEL_COL + 1 #col 2
RECEIVED_BY_LABEL_ROW = DATE_RECEIVED_LABEL_ROW       #row 3
RECEIVED_BY_LABEL_COL = DATE_RECEIVED_ENTRY_COL + 2   #col 4
RECEIVED_BY_ENTRY_ROW = DATE_RECEIVED_LABEL_ROW       #row 3
RECEIVED_BY_ENTRY_COL = RECEIVED_BY_LABEL_COL + 1     #col 5
#SJ1210222 - row 4 not used
PIECES_LABEL_ROW = RECEIVED_BY_ENTRY_ROW + 2 #row 5
PIECES_LABEL_COL = 1                         #col 1
PIECES_ENTRY_ROW = PIECES_LABEL_ROW          #row 5
PIECES_ENTRY_COL = PIECES_LABEL_COL + 1      #col 2
OF_LABEL_ROW = PIECES_LABEL_ROW              #row 5
OF_LABEL_COL = PIECES_ENTRY_COL + 2          #col 4
OF_ENTRY_ROW = PIECES_LABEL_ROW              #row 5
OF_ENTRY_COL = OF_LABEL_COL + 1              #col 5
#SJ1210222 - row 6 not used
PICTURE_CHECK_BUTTON_ROW = OF_ENTRY_ROW + 2             #row 7
PICTURE_CHECK_BUTTON_COL = 1                            #col 1
PHOTOES_CHECK_BUTTON_ROW = PICTURE_CHECK_BUTTON_ROW     #row 7
PHOTOES_CHECK_BUTTON_COL = PICTURE_CHECK_BUTTON_COL + 3 #col 4
#SJ1210222 - row 8 not used
#SJ1210222 - Products type and num of parts list box occupy row 9 to row 18
PRODUCTS_TYPE_LABEL_ROW = PHOTOES_CHECK_BUTTON_ROW + 2       #row 9
PRODUCTS_TYPE_LABEL_COL = 1                                  #col 1
PRODUCTS_TYPE_LIST_BOX_ROW = PRODUCTS_TYPE_LABEL_ROW         #row 9
PRODUCTS_TYPE_LIST_BOX_COL = PRODUCTS_TYPE_LABEL_COL + 1     #col 2
NUMBER_OF_PARTS_LABEL_ROW = PRODUCTS_TYPE_LABEL_ROW          #row 9
NUMBER_OF_PARTS_LABEL_COL = PRODUCTS_TYPE_LIST_BOX_COL + 2   #col 4
NUMBER_OF_PARTS_LIST_BOX_ROW = PRODUCTS_TYPE_LABEL_ROW       #row 9
NUMBER_OF_PARTS_LIST_BOX_COL = NUMBER_OF_PARTS_LABEL_COL + 1 #col 5
#SJ1210222 - row 19 not used
PARTS_IN_BLUE_BIN_ROW = NUMBER_OF_PARTS_LIST_BOX_ROW + 11 #row 20
PARTS_IN_BLUE_BIN_COL = 1                                 #col 1
QC_CHECKED_BY_LABEL_ROW = PARTS_IN_BLUE_BIN_ROW             #row 20
QC_CHECKED_BY_LABEL_COL = PARTS_IN_BLUE_BIN_COL + 3         #col 4
QC_CHECKED_BY_ENTRY_ROW = PARTS_IN_BLUE_BIN_ROW             #row 20
QC_CHECKED_BY_ENTRY_COL = QC_CHECKED_BY_LABEL_COL + 1         #col 5
#SJ1210222 - row 21 not used
NOTE_LABEL_ROW = QC_CHECKED_BY_ENTRY_ROW + 2 #row 22
NOTE_LABEL_COL = 1                         #col 2
NOTE_ENTRY_ROW = NOTE_LABEL_ROW            #row 22
NOTE_ENTRY_COL = NOTE_LABEL_COL + 1        #col 3
#SJ1210222 - row 23 not used
CANCEL_BUTTON_ROW = NOTE_ENTRY_ROW + 2  #row 24
CANCEL_BUTTON_COL = 1                   #col 1
SAVE_BUTTON_ROW = CANCEL_BUTTON_ROW     #row 24
SAVE_BUTTON_COL = CANCEL_BUTTON_COL + 4 #col 5

#SJ1210222 - Output pad is used for debug purpose only it is not part of the date entry
OUTPUT_PAD_ROW = 28
OUTPUT_PAD_COL = 2


#SJ0130222 - Ideally the products type list should be stored in a database; the setback of reading from a database
#SJ0130222 - is that there is a need to write a code to allow user to do data entry into the database.
productsType = ['Radiator', 'CAC', 'Condenser', 'Fuel Tank', 'Evaporator', 'Heater Core', 'Radiator Core',
'DPF', 'DPF-DOC Combo', 'EGR', 'Coolant Pipe', 'Oil Cooler', 'AC Hose', 'Cooling Module', 'Other']

numberOfParts = ['Fitting', 'Hoses', 'Sensors', 'Brackets', 'Mounts', 'Rad Cap', 'Shroud', 'FAN', 'Chain', 'Straps']

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
qcCheckedBy = ''
notes = ''
outputPad = ''

#SJ3230222 - database and table global variables
conn = ''
curCursor = ''
tableName = 'werChecklist'

class WER_Main:
    def __init__(self, master):
        master.title('West End Radiators')
        self.setupDataEntryScreen(master)
        self.setupSQLiteDBase('./dbase/werShipping.sqlite')

    def setupDataEntryScreen(self, master):
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
        global qcCheckedBy
        global notes
        global outputPad

        #SJ5110222 - Input field for customer name
        self.customerLabel = Label(master, text='Customer: ').grid(row=CUSTOMER_LABEL_ROW, column=CUSTOMER_LABEL_COL)
        customerName = Entry(master)
        customerName.focus_set()  #SJ1210222 - Put this field into focus
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
        numOfPieces.insert(0, '1')
        numOfPieces.grid(row=PIECES_ENTRY_ROW, column=PIECES_ENTRY_COL)

        #SJ6120222 - Input field for of
        self.ofLabel = Label(master, text='of: ').grid(row=OF_LABEL_ROW, column=OF_LABEL_COL)
        ofPieces = Entry(master)
        ofPieces.insert(0, '1')
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
        self.numOfPartsLabel = Label(master, text='# of parts: ').grid(row=NUMBER_OF_PARTS_LABEL_ROW, column=NUMBER_OF_PARTS_LABEL_COL)
        numberOfPartsListbox = Listbox(master, selectmode=MULTIPLE, exportselection=0)
        for partItem in numberOfParts:
            numberOfPartsListbox.insert(END, partItem)
        numberOfPartsListbox.grid(row=NUMBER_OF_PARTS_LIST_BOX_ROW, column=NUMBER_OF_PARTS_LIST_BOX_COL)

        #SJ3160222 - Check box field for parts in blue bin
        partsInBlueBin = IntVar()
        self.partsInBlueBinCheckButton = Checkbutton(master, text='Are parts in a Blue Bin? ', var=partsInBlueBin)
        self.partsInBlueBinCheckButton.grid(row=PARTS_IN_BLUE_BIN_ROW, column=PARTS_IN_BLUE_BIN_COL)

        #SJ2220222 - Input field for QC Checked by
        self.qcCheckedByLabel = Label(master, text='QC Checked By: ').grid(row=QC_CHECKED_BY_LABEL_ROW, column=QC_CHECKED_BY_LABEL_COL)
        qcCheckedBy = Entry(master, state=DISABLED)  #SJ2220222 - Field will be enabled only in edit mode
        qcCheckedBy.grid(row=QC_CHECKED_BY_ENTRY_ROW, column=QC_CHECKED_BY_ENTRY_COL)
        #qcCheckedBy.focus_set()  #SJ1210222 - Put this field into focus

        #SJ3160222 - Text field for notes
        self.notesLabel = Label(master, text='Notes: ').grid(row=NOTE_LABEL_ROW, column=NOTE_LABEL_COL)
        notes = Text(master, font=('Verdana', 10), height=6, width=20)
        notes.grid(row=NOTE_ENTRY_ROW, column=NOTE_ENTRY_COL)

        outputPad = Entry(master)
        outputPad.grid(row=OUTPUT_PAD_ROW, column=OUTPUT_PAD_COL)

        self.cancelButton = Button(text='Cancel', command=lambda x=master: self.cancelCallback(x))
        #self.label.grid(row=0, column=0)
        self.cancelButton.grid(row=CANCEL_BUTTON_ROW, column=CANCEL_BUTTON_COL)

        self.saveButton = Button(text='Save', command=lambda x=master: self.saveCallback(x))
        #self.label.grid(row=0, column=0)
        self.saveButton.grid(row=SAVE_BUTTON_ROW, column=SAVE_BUTTON_COL)

    def initializeInputFields(self, master):
        self.productsTypeList = ''.join(list(map(str, productsTypeListbox.curselection())))
        self.numberOfPartsList = ''.join(list(map(str, numberOfPartsListbox.curselection())))
        customerName.delete(0, END)
        customerName.focus_set()  #SJ1210222 - Put this field into focus
        workOrder.delete(0, END)
        #dateReceived
        receivedBy.delete(0, END)
        numOfPieces.delete(0, END)
        numOfPieces.insert(0, '1')
        ofPieces.delete(0, END)
        ofPieces.insert(0, '1')
        pictureStatus.set(0)
        photoesStatus.set(0)
        for c in self.productsTypeList: productsTypeListbox.select_clear(int(c))
        for c in self.numberOfPartsList: numberOfPartsListbox.select_clear(int(c))
        #numberOfPartsListbox.select_clear()
        partsInBlueBin.set(0)
        notes.delete(1.0, END)

    def cancelCallback(self, master):
        #global outputPad
        #global customerName
        self.initializeInputFields(master)

    def saveCallback(self, master):
        global tableName
        global conn
        global curCursor
        self.customerName = customerName.get()
        self.workOrder = workOrder.get()
        if len(self.customerName) == 0 or len(self.workOrder) == 0:
            #print("Compulsory input field can't be empty")
            showwarning(title='Missing Fields', message='Check the Customer Name or WOP fields')
        else:
            self.dateReceived = dateReceived.get_date()
            #self.receivedBy = receivedBy.get()
            #self.numOfPieces = eval(numOfPieces.get())
            #self.ofPieces = eval(ofPieces.get())
            #self.pictureStatus = pictureStatus.get()
            #self.photoesStatus = photoesStatus.get()
            #self.productsTypeList = ''.join(list(map(str, productsTypeListbox.curselection())))
            #self.numberOfPartsList = ''.join(list(map(str, numberOfPartsListbox.curselection())))
            #self.partsInBlueBin = partsInBlueBin.get()
            #self.notes = notes.get(1.0, END)

            curCursor.execute('''INSERT INTO werChecklist (customerName, workOrder, dateReceived, receivedBy, numOfPieces,
                           ofPieces, pictureStatus, photoesStatus, productsTypeListbox, numberOfPartsListbox, partsInBlueBin,
                           notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (self.customerName, self.workOrder, self.dateReceived, receivedBy.get(), eval(numOfPieces.get()),
                           eval(ofPieces.get()), pictureStatus.get(), photoesStatus.get(), ''.join(list(map(str, productsTypeListbox.curselection()))),
                           ''.join(list(map(str, numberOfPartsListbox.curselection()))), partsInBlueBin.get(), notes.get(1.0, END)))

            conn.commit()

            self.initializeInputFields(master)

            #print('Customer & WOP: ', self.customerName, self.workOrder)
            #print('Date & Received by: ', self.dateReceived, self.receivedBy)
            #print('Num of pieces & of pieces: ', self.numOfPieces, self.ofPieces)
            #print('Pictures & photoes uploaded: ', self.pictureStatus, self.photoesStatus)
            #print('Products type & Num of parts: ', self.productsTypeList, self.numberOfPartsList)
            #print('Parts in blue bin: ', self.partsInBlueBin)
            #print('Notes: ', self.notes)

    #SJ2220222 - Setup connection to wershipping database
    def setupSQLiteDBase(self, dbName):
        global conn
        global curCursor
        try:
            conn = sqlite3.connect(dbName)
            curCursor = conn.cursor()
        except:
            print('Fail to connect to database')
        #cur.execute('''
        #CREATE TABLE IF NOT EXISTS Twitter
        #(name TEXT, retrieved INTEGER, friends INTEGER)''')

        #outputPad.insert(0, self.productsTypeList+self.numberOfPartsList)
        #print('product type list: ', ''.join(list(map(str, self.productsTypeList))))
        #print('product type list: ', ''.join(list(map(str, self.numberOfPartsList))))


root = Tk()
app = WER_Main(root)
mainloop()
