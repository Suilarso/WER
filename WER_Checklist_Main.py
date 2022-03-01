#Project: WER checklist
#Date: Feb 11, 2022
#Remark: This page consist of user interface for user input. It uses tkinter GUI

from tkinter import *
from tkinter.messagebox import *
from tkcalendar import DateEntry
from datetime import datetime
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
#SJ6260222 - Search button
SEARCH_BUTTON_ROW =  CUSTOMER_LABEL_ROW        #row 1
SEARCH_BUTTON_COL = WORK_ORDER_ENTRY_COL + 1   #col 6
#SJ1210222 - Row 2 not used
DATE_RECEIVED_LABEL_ROW = SEARCH_BUTTON_ROW + 2     #row 3
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
QC_CHECKED_BY_LABEL_ROW = PARTS_IN_BLUE_BIN_ROW           #row 20
QC_CHECKED_BY_LABEL_COL = PARTS_IN_BLUE_BIN_COL + 3       #col 4
QC_CHECKED_BY_ENTRY_ROW = PARTS_IN_BLUE_BIN_ROW           #row 20
QC_CHECKED_BY_ENTRY_COL = QC_CHECKED_BY_LABEL_COL + 1     #col 5
#SJ6260222 - QC Check & Update Button
QC_CHECK_BUTTON_ROW =  QC_CHECKED_BY_ENTRY_ROW    #row 20
QC_CHECK_BUTTON_COL = QC_CHECKED_BY_ENTRY_COL + 1 #col 6
#SJ1210222 - row 21 not used
NOTE_LABEL_ROW = QC_CHECK_BUTTON_ROW + 2 #row 22
NOTE_LABEL_COL = 1                       #col 2
NOTE_ENTRY_ROW = NOTE_LABEL_ROW          #row 22
NOTE_ENTRY_COL = NOTE_LABEL_COL + 1      #col 3
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

numberOfParts = ['Fitting', 'Hoses', 'Sensors', 'Brackets', 'Mounts', 'Rad Cap', 'Shroud', 'Fan', 'Chain', 'Straps']

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
#outputPad = ''
qcCheckFlag = False

#SJ3230222 - database and table global variables
conn = ''
curCursor = ''
tableName = 'werChecklist'
werStructure = {'customerName': 0, 'workOrder': 1, 'dateReceived': 2, 'receivedBy': 3, 'numOfPieces': 4, 'ofPieces': 5,
                'pictureStatus': 6, 'photoesStatus': 7, 'productsTypeListbox': 8, 'numberOfPartsListbox': 9,
                'partsInBlueBin': 10, 'qcCheckedBy': 11,'notes': 12}

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
        #global outputPad

        #SJ5110222 - Input field for customer name
        self.customerLabel = Label(master, text='Customer: ').grid(row=CUSTOMER_LABEL_ROW, column=CUSTOMER_LABEL_COL)
        customerName = Entry(master)
        customerName.focus_set()  #SJ1210222 - Put this field into focus
        customerName.grid(row=CUSTOMER_ENTRY_ROW, column=CUSTOMER_ENTRY_COL)

        #SJ5110222 - Input field for work order
        self.workOrderLabel = Label(master, text='WO: ').grid(row=WORK_ORDER_LABEL_ROW, column=WORK_ORDER_LABEL_COL)
        workOrder = Entry(master)
        workOrder.grid(row=WORK_ORDER_ENTRY_ROW, column=WORK_ORDER_ENTRY_COL)

        #SJ6260222 - QC Check button
        self.searchButton = Button(text='Search', command=lambda x=master: self.searchCallback(x))
        self.searchButton.grid(row=SEARCH_BUTTON_ROW, column=SEARCH_BUTTON_COL)

        #SJ6120222 - Input field for Date received
        self.todayDate = datetime(1,1,1).now()  #SJ5250222 - Getting today system date
        self.dateReceivedLabel = Label(master, text='Date Received: ').grid(row=DATE_RECEIVED_LABEL_ROW, column=DATE_RECEIVED_LABEL_COL)
        dateReceived = DateEntry(master, values="Text", year=self.todayDate.year, state="readonly", date_pattern="yyyy-mm-dd")
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

        #SJ6260222 - QC Check button
        self.qcCheckButton = Button(text='QC Check', state=DISABLED, command=lambda x=master: self.qcCheckCallback(x))
        self.qcCheckButton.grid(row=QC_CHECK_BUTTON_ROW, column=QC_CHECK_BUTTON_COL)

        #SJ3160222 - Text field for notes
        self.notesLabel = Label(master, text='Notes: ').grid(row=NOTE_LABEL_ROW, column=NOTE_LABEL_COL)
        notes = Text(master, font=('Verdana', 10), height=6, width=20)
        notes.grid(row=NOTE_ENTRY_ROW, column=NOTE_ENTRY_COL)

        #outputPad = Entry(master)
        #outputPad.grid(row=OUTPUT_PAD_ROW, column=OUTPUT_PAD_COL)

        self.cancelButton = Button(text='Cancel', command=lambda x=master: self.cancelCallback(x))
        self.cancelButton.grid(row=CANCEL_BUTTON_ROW, column=CANCEL_BUTTON_COL)

        self.saveButton = Button(text='Save', command=lambda x=master: self.saveCallback(x))
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
        partsInBlueBin.set(0)
        notes.delete(1.0, END)

    #SJ0270222 - Search function to handle search button press
    def searchCallback(self, master):
        global qcCheckFlag
        self.workOrder = workOrder.get()
        if len(self.workOrder) == 0:
            showwarning(title='Empty Fields', message='Please key in the WOP to be searched')
        else:
            self.initializeInputFields(master)
            curCursor.execute('SELECT * FROM werChecklist WHERE workOrder = ? LIMIT 1', (self.workOrder, ))
            returnRow = curCursor.fetchone()
            customerName.insert(0, returnRow[werStructure['customerName']])
            workOrder.insert(0, returnRow[werStructure['workOrder']])
            dateReceived.set_date(returnRow[werStructure['dateReceived']])
            receivedBy.insert(0, returnRow[werStructure['receivedBy']])
            numOfPieces.delete(0, END)
            numOfPieces.insert(0, returnRow[werStructure['numOfPieces']])
            ofPieces.delete(0, END)
            ofPieces.insert(0, returnRow[werStructure['ofPieces']])
            pictureStatus.set(returnRow[werStructure['pictureStatus']])
            photoesStatus.set(returnRow[werStructure['photoesStatus']])
            for ndx in returnRow[werStructure['productsTypeListbox']]:
                productsTypeListbox.select_set(int(ndx))
            for ndx in returnRow[werStructure['numberOfPartsListbox']]:
                numberOfPartsListbox.select_set(int(ndx))
            partsInBlueBin.set(returnRow[werStructure['partsInBlueBin']])
            self.qcCheckedBy = returnRow[werStructure['qcCheckedBy']]
            if (self.qcCheckedBy == None):
                #SJ0270222 - If reaches here, record is not qc checked yet. Need to show qc check button, disable save and search button
                self.saveButton.configure(state=DISABLED)
                self.qcCheckButton.configure(state=NORMAL)
                qcCheckFlag = True
            else:
                qcCheckedBy.configure(state=NORMAL)
                qcCheckedBy.insert(0, returnRow[werStructure['qcCheckedBy']])
            notes.insert(END, returnRow[werStructure['notes']])

    #SJ6260222 - Callback function to handle qc button press
    def qcCheckCallback(self, master):
        global qcCheckedBy
        global qcCheckFlag
        if qcCheckFlag:
            qcCheckFlag = False  #SJ1280222 - Here we set the flag to false as the button functionality had been changed to update
            self.qcCheckButton.configure(text='Update')
            qcCheckedBy.configure(state=NORMAL)
            qcCheckedBy.focus_set()  #SJ1210222 - Put this field into focus
        else:
            self.workOrder = workOrder.get()
            curCursor.execute('UPDATE werChecklist SET qcCheckedBy=? WHERE workOrder = ?', (qcCheckedBy.get(), self.workOrder))
            conn.commit()
            self.saveButton.configure(state=NORMAL)
            self.qcCheckButton.configure(text='QC Check', state=DISABLED)
            qcCheckedBy.delete(0, END)
            qcCheckedBy.configure(state=DISABLED)
            self.initializeInputFields(master)

    def cancelCallback(self, master):
        #global customerName
        qcCheckedBy.delete(0, END)
        qcCheckedBy.configure(state=DISABLED)
        self.saveButton.configure(state=NORMAL)
        self.initializeInputFields(master)

    def saveCallback(self, master):
        global tableName
        global conn
        global curCursor
        self.customerName = customerName.get()
        self.workOrder = workOrder.get()
        if len(self.customerName) == 0 or len(self.workOrder) == 0:
            showwarning(title='Missing Fields', message='Check the Customer Name or WOP fields')
        else:
            curCursor.execute('SELECT workOrder FROM werChecklist WHERE workOrder = ? LIMIT 1', (self.workOrder, ))
            try:
                count = curCursor.fetchone()[0]
                print('fetchone: ', count)
                showwarning(title='Duplicate WOP', message='It seems '+self.workOrder+' had been used.')
            except:
                curCursor.execute('''INSERT INTO werChecklist (customerName, workOrder, dateReceived, receivedBy, numOfPieces,
                               ofPieces, pictureStatus, photoesStatus, productsTypeListbox, numberOfPartsListbox, partsInBlueBin,
                               notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (self.customerName, self.workOrder, dateReceived.get_date(),
                               receivedBy.get(), eval(numOfPieces.get()), eval(ofPieces.get()), pictureStatus.get(), photoesStatus.get(),
                               ''.join(list(map(str, productsTypeListbox.curselection()))), ''.join(list(map(str, numberOfPartsListbox.curselection()))),
                               partsInBlueBin.get(), notes.get(1.0, END)))
                conn.commit()

            self.initializeInputFields(master)

    #SJ2220222 - Setup connection to wershipping database
    def setupSQLiteDBase(self, dbName):
        global conn
        global curCursor
        global quitter_function
        try:
            conn = sqlite3.connect(dbName)
            curCursor = conn.cursor()
        except:
            print('Fail to connect to database')
            quitter_function()


def quitter_function():
    conn.close()  #SJ5250222 - Close database connection
    root.destroy()

root = Tk()
root.protocol('WM_DELETE_WINDOW', quitter_function)
app = WER_Main(root)
mainloop()
