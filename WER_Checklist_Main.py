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
BROWSE_BUTTON_ROW = CANCEL_BUTTON_ROW
BROWSE_BUTTON_COL = CANCEL_BUTTON_COL + 2

#SJ1210222 - Output pad is used for debug purpose only it is not part of the data entry
OUTPUT_PAD_ROW = 28
OUTPUT_PAD_COL = 2

#SJ0130222 - Ideally the products type list should be stored in a database; the setback of reading from a database
#SJ0130222 - is that there is a need to write a code to allow user to do data entry into the database.
productsType = ['Radiator', 'CAC', 'Condenser', 'Fuel Tank', 'Evaporator', 'Heater Core', 'Radiator Core',
'DPF', 'DPF-DOC Combo', 'EGR', 'Coolant Pipe', 'Oil Cooler', 'AC Hose', 'Cooling Module', 'Other']

numberOfParts = ['Fitting', 'Hoses', 'Sensors', 'Brackets', 'Mounts', 'Rad Cap', 'Shroud', 'Fan', 'Chain', 'Straps']

usersName = ['Jeffrey, R', 'Jon, C', 'Suzy, K', 'Daniel, N', 'Ian, L', 'Ruslan, L', 'Jason, H', 'Sales', 'WER chauffeur']
qcName = ['Jeffrey, R', 'Jon, C', 'Suzy, K', 'Daniel, N', 'Ian, L', 'Ruslan, L', 'Jason, H', 'Sales', 'WER chauffeur']

customerName = ''
workOrder = ''
dateReceived = ''
receivedBy = ''  #SJ4020622 - May not need it; the value can be retrieved from usersOption
numOfPieces = 0
ofPieces = 0
pictureStatus = 0
photoesStatus = 0
productsTypeListbox = []
numberOfPartsListbox = []
partsInBlueBin = 0
qcCheckedBy = ''  #SJ6040622 - May not need it; same reason as receivedBy
notes = ''
qcCheckFlag = False
usersOption = ''
usersDropdown = ''
qcOption = ''
qcDropdown = ''

#SJ6070522 - Global var for table movement
totalRecords = 0
rowsPerPage = 5
numOfRow = 0
numOfCol = 0
currentRecord = 0
currentPage = 0
pageFirstRecord = []
totalRecordsBrowsed = 0

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
        #global receivedBy
        global numOfPieces
        global ofPieces
        global pictureStatus
        global photoesStatus
        global productsTypeListbox
        global numberOfPartsListbox
        global partsInBlueBin
        #global qcCheckedBy
        global notes
        global usersOption
        global usersDropdown
        global qcOption
        global qcDropdown

        #SJ5110222 - Input field for customer name
        self.customerLabel = Label(master, text='Customer: ').grid(row=CUSTOMER_LABEL_ROW, column=CUSTOMER_LABEL_COL)
        customerName = Entry(master)
        customerName.focus_set()  #SJ1210222 - Put this field into focus
        customerName.grid(row=CUSTOMER_ENTRY_ROW, column=CUSTOMER_ENTRY_COL)

        #SJ5110222 - Input field for work order
        self.workOrderLabel = Label(master, text='WO: ').grid(row=WORK_ORDER_LABEL_ROW, column=WORK_ORDER_LABEL_COL)
        workOrder = Entry(master)
        workOrder.grid(row=WORK_ORDER_ENTRY_ROW, column=WORK_ORDER_ENTRY_COL)

        #SJ6260222 - Search button
        self.searchButton = Button(text='Search', command=lambda x=master: self.searchCallback(x))
        self.searchButton.grid(row=SEARCH_BUTTON_ROW, column=SEARCH_BUTTON_COL)

        #SJ6120222 - Input field for Date received
        self.todayDate = datetime(1,1,1).now()  #SJ5250222 - Getting today system date
        self.dateReceivedLabel = Label(master, text='Date Received: ').grid(row=DATE_RECEIVED_LABEL_ROW, column=DATE_RECEIVED_LABEL_COL)
        dateReceived = DateEntry(master, values="Text", year=self.todayDate.year, state="readonly", date_pattern="yyyy-mm-dd")
        dateReceived.grid(row=DATE_RECEIVED_ENTRY_ROW, column=DATE_RECEIVED_ENTRY_COL, padx=20, pady=5, sticky=W)

        #SJ6120222 - Input field for Received by
        self.receivedByLabel = Label(master, text='Received by: ').grid(row=RECEIVED_BY_LABEL_ROW, column=RECEIVED_BY_LABEL_COL)
        #receivedBy = Entry(master)
        #receivedBy.grid(row=RECEIVED_BY_ENTRY_ROW, column=RECEIVED_BY_ENTRY_COL)
        usersOption = StringVar(master)
        usersOption.set(usersName[0])
        usersDropdown = OptionMenu(master, usersOption, *usersName)
        #usersDropdown.config(width=16, height=1)
        usersDropdown.configure(width=16, height=1)
        usersDropdown.grid(row=RECEIVED_BY_ENTRY_ROW, column=RECEIVED_BY_ENTRY_COL)

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
        productsTypeListboxFrame = Frame(master)
        productsTypeScrollbar = Scrollbar(productsTypeListboxFrame, orient=VERTICAL)
        self.productsTypeLabel = Label(master, text='Received items: ').grid(row=PRODUCTS_TYPE_LABEL_ROW, column=PRODUCTS_TYPE_LABEL_COL)
        productsTypeListbox = Listbox(productsTypeListboxFrame, selectmode=MULTIPLE, exportselection=0, yscrollcommand=productsTypeScrollbar.set)
        for productItem in productsType:
            productsTypeListbox.insert(END, productItem)
        productsTypeScrollbar.config(command=productsTypeListbox.yview)
        productsTypeScrollbar.pack(side=RIGHT, fill=Y)
        productsTypeListbox.pack(side=LEFT, fill=BOTH, expand=1)
        productsTypeListboxFrame.grid(row=PRODUCTS_TYPE_LIST_BOX_ROW, column=PRODUCTS_TYPE_LIST_BOX_COL)

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
        #qcCheckedBy = Entry(master, state=DISABLED)  #SJ2220222 - Field will be enabled only in edit mode
        #qcCheckedBy.grid(row=QC_CHECKED_BY_ENTRY_ROW, column=QC_CHECKED_BY_ENTRY_COL)
        qcOption = StringVar(master)
        self.qcNameNdx = len(qcName)
        qcOption.set(qcName[self.qcNameNdx-1])
        qcDropdown = OptionMenu(master, qcOption, *qcName)  #SJ0050622 - separate name list
        #qcDropdown = OptionMenu(master, qcOption, *usersName)  #SJ0050622 - Sharing namelist with usersDropdown
        #qcDropdown.config(width=16, height=1)
        qcDropdown.configure(width=16, height=1, state=DISABLED)
        qcDropdown.grid(row=QC_CHECKED_BY_ENTRY_ROW, column=QC_CHECKED_BY_ENTRY_COL)

        #SJ6260222 - QC Check button
        self.qcCheckButton = Button(text='QC Check', state=DISABLED, command=lambda x=master: self.qcCheckCallback(x))
        self.qcCheckButton.grid(row=QC_CHECK_BUTTON_ROW, column=QC_CHECK_BUTTON_COL)

        #SJ3160222 - Text field for notes
        self.notesLabel = Label(master, text='Notes: ').grid(row=NOTE_LABEL_ROW, column=NOTE_LABEL_COL)
        notes = Text(master, font=('Verdana', 10), height=6, width=20)
        notes.grid(row=NOTE_ENTRY_ROW, column=NOTE_ENTRY_COL)

        self.cancelButton = Button(text='Cancel', command=lambda x=master: self.cancelCallback(x))
        self.cancelButton.grid(row=CANCEL_BUTTON_ROW, column=CANCEL_BUTTON_COL)

        self.saveButton = Button(text='Save', command=lambda x=master: self.saveCallback(x))
        self.saveButton.grid(row=SAVE_BUTTON_ROW, column=SAVE_BUTTON_COL)

        #SJ4210422 - Browse Button
        self.browseButton = Button(text='Browse', command=lambda x=master: self.browseCallback(x))
        self.browseButton.grid(row=BROWSE_BUTTON_ROW, column=BROWSE_BUTTON_COL)

    def initializeInputFields(self, master):
        productsTypeListbox.configure(selectmode=MULTIPLE)
        self.productsTypeList = self.removeAlphaChar(str(productsTypeListbox.curselection()), "Initialize")
        numberOfPartsListbox.configure(selectmode=MULTIPLE)
        self.numberOfPartsList = self.removeAlphaChar(str(numberOfPartsListbox.curselection()), "Initialize")
        customerName.configure(state=NORMAL)
        customerName.delete(0, END)
        customerName.focus_set()  #SJ1210222 - Put this field into focus
        workOrder.delete(0, END)
        self.todayDate = datetime(1,1,1).now()  #SJ5250222 - Getting today system date
        dateReceived.configure(state=NORMAL)
        dateReceived.set_date(str(self.todayDate.strftime("%Y-%m-%d")))
        #receivedBy.configure(state=NORMAL)
        #receivedBy.delete(0, END)
        usersDropdown.configure(state=NORMAL)
        usersOption.set(usersName[0])
        numOfPieces.configure(state=NORMAL)
        numOfPieces.delete(0, END)
        numOfPieces.insert(0, '1')
        ofPieces.configure(state=NORMAL)
        ofPieces.delete(0, END)
        ofPieces.insert(0, '1')
        self.pictureCheckButton.configure(state=NORMAL)
        pictureStatus.set(0)
        self.photoesCheckButton.configure(state=NORMAL)
        photoesStatus.set(0)
        for c in self.productsTypeList: productsTypeListbox.select_clear(int(c))
        for c in self.numberOfPartsList: numberOfPartsListbox.select_clear(int(c))
        self.partsInBlueBinCheckButton.configure(state=NORMAL)
        partsInBlueBin.set(0)
        #qcCheckedBy.configure(state=NORMAL)
        #qcCheckedBy.delete(0, END)
        #qcCheckedBy.configure(state=DISABLED)
        qcDropdown.configure(state=NORMAL)
        #self.qcNameNdx = len(qcName)
        #qcOption.set(qcName[self.qcNameNdx-1])  #SJ0050622 - Separate name list
        qcOption.set(usersName[0])  #SJ0050622 - Sharing name list with usersDropdown
        qcDropdown.configure(state=DISABLED)
        notes.configure(state=NORMAL)
        notes.delete(1.0, END)

        #SJ6050322 - Put back all button functionality accordingly
        self.saveButton.configure(state=NORMAL)
        self.browseButton.configure(state=NORMAL)
        self.qcCheckButton.configure(text='QC Check', state=DISABLED)

    #SJ0270222 - Search function to handle search button press
    def searchCallback(self, master, optionalWorkOrder=0):
        global qcCheckFlag

        if (optionalWorkOrder != 0):
            self.workOrder = optionalWorkOrder.strip()
        else:
            self.workOrder = workOrder.get().strip()

        if len(self.workOrder) == 0:
            showwarning(title='Empty Fields', message='Please key in the WO to be searched')
        else:
            self.initializeInputFields(master)
            curCursor.execute('SELECT * FROM werChecklist WHERE workOrder = ? LIMIT 1', (self.workOrder, ))
            returnRow = curCursor.fetchone()
            if returnRow != None:
                customerName.insert(0, returnRow[werStructure['customerName']])
                customerName.configure(state=DISABLED)
                workOrder.insert(0, returnRow[werStructure['workOrder']])
                dateReceived.set_date(returnRow[werStructure['dateReceived']])
                dateReceived.configure(state=DISABLED)
                #receivedBy.insert(0, returnRow[werStructure['receivedBy']])
                #receivedBy.configure(state=DISABLED)
                self.usersOptionIndex = self.setUsersOption(returnRow[werStructure['receivedBy']])
                usersOption.set(usersName[self.usersOptionIndex])
                usersDropdown.configure(state=DISABLED)
                numOfPieces.delete(0, END)
                numOfPieces.insert(0, returnRow[werStructure['numOfPieces']])
                numOfPieces.configure(state=DISABLED)
                ofPieces.delete(0, END)
                ofPieces.insert(0, returnRow[werStructure['ofPieces']])
                ofPieces.configure(state=DISABLED)
                pictureStatus.set(returnRow[werStructure['pictureStatus']])
                self.pictureCheckButton.configure(state=DISABLED)
                photoesStatus.set(returnRow[werStructure['photoesStatus']])
                self.photoesCheckButton.configure(state=DISABLED)
                self.tempProductType = self.removeAlphaChar(returnRow[werStructure['productsTypeListbox']], "Search")
                for ndx in self.tempProductType:
                    productsTypeListbox.select_set(int(ndx))
                productsTypeListbox.configure(selectmode=BROWSE)
                self.tempPartsList = self.removeAlphaChar(returnRow[werStructure['numberOfPartsListbox']], "Search")
                for ndx in self.tempPartsList:
                    numberOfPartsListbox.select_set(int(ndx))
                numberOfPartsListbox.configure(selectmode=BROWSE)
                partsInBlueBin.set(returnRow[werStructure['partsInBlueBin']])
                self.partsInBlueBinCheckButton.configure(state=DISABLED)
                self.qcCheckedBy = returnRow[werStructure['qcCheckedBy']]
                if (self.qcCheckedBy == None):
                    #SJ0270222 - If reaches here, record is not qc checked yet. Need to show qc check button, disable save and search button
                    self.qcCheckButton.configure(state=NORMAL)
                    qcCheckFlag = True
                    #qcDropdown.configure(state=NORMAL)
                    #qcOption.set(qcName[0])
                    #qcDropdown.configure(state=DISABLED)
                else:
                    #qcCheckedBy.configure(state=NORMAL)
                    #qcCheckedBy.insert(0, returnRow[werStructure['qcCheckedBy']])
                    #qcCheckedBy.configure(state=DISABLED)
                    qcDropdown.configure(state=NORMAL)
                    self.qcOptionIndex = self.setQcOption(returnRow[werStructure['qcCheckedBy']])
                    qcOption.set(qcName[self.qcOptionIndex])
                    #self.qcOptionIndex = self.setUsersOption(returnRow[werStructure['qcCheckedBy']])
                    #qcOption.set(usersName[self.qcOptionIndex])
                    qcDropdown.configure(state=DISABLED)
                notes.insert(END, returnRow[werStructure['notes']])
                notes.configure(state=DISABLED)
                self.saveButton.configure(state=DISABLED)
                self.browseButton.configure(state=DISABLED)
            else:
                showwarning(title='Record Not Found', message='Work order '+self.workOrder+' not found.')

    #SJ4020622 - This method set usersOption drop down list to the appropriate index
    def setUsersOption(self, receivedBy):
        try:
            usersIndex = usersName.index(receivedBy)
        except:
            usersIndex = 0
        return (usersIndex)

    #SJ6040622 - This method set qcOption drop down list to the appropriate index
    def setQcOption(self, qcCheckedBy):
        try:
            qcIndex = qcName.index(qcCheckedBy)
        except:
            qcIndex = 0
        return (qcIndex)

    #SJ3020322 - This method is used to strip of comma and bracket from incoming string
    def removeAlphaChar(self, inString, callingFn):
        #SJ3020322 - First we remove the , to be followed by left bracket and finally right brachket
        self.tempString = inString.replace(",", '').replace("(", '').replace(")", '')
        self.tempString = self.tempString.split()
        return (self.tempString)

    #SJ6260222 - Callback function to handle qc button press
    def qcCheckCallback(self, master):
        #global qcCheckedBy
        global qcCheckFlag
        global workOrder
        global qcDropdown
        global qcOption
        if qcCheckFlag:
            qcCheckFlag = False  #SJ1280222 - Here we set the flag to false as the button functionality had been changed to update
            workOrder.configure(state=DISABLED)  #SJ0170422 - Disabled workOrder field to prevent it from being updated
            self.qcCheckButton.configure(text='Update')
            #qcCheckedBy.configure(state=NORMAL)
            #qcCheckedBy.focus_set()  #SJ1210222 - Put this field into focus
            #SJ3080622 - Using dropdown list to select qc name
            qcDropdown.configure(state=NORMAL)
            qcOption.set(qcName[0])  #SJ5100622 - Default is set to first element of the list
            #qcDropdown.configure(state=DISABLED)
            #self.qcOptionIndex = self.setQcOption(returnRow[werStructure['qcCheckedBy']])
            #self.qcNameNdx = len(qcName)
            #qcName.append('None')
        else:
            #if qcCheckedBy.get().strip() == '':
            #    showwarning(title='Empty Field', message='Please key in your name or initials.')
            #else:
            self.workOrder = workOrder.get().strip()
            #self.qcCheckedBy = qcCheckedBy.get().strip()
            #curCursor.execute('UPDATE werChecklist SET qcCheckedBy=? WHERE workOrder = ?', (self.qcCheckedBy, self.workOrder))
            curCursor.execute('UPDATE werChecklist SET qcCheckedBy=? WHERE workOrder = ?', (qcOption.get(), self.workOrder))
            conn.commit()
            workOrder.configure(state=NORMAL)  #SJ0170422 - Reinstate workOrder field to normal
            self.initializeInputFields(master)

    def cancelCallback(self, master):
        global qcCheckFlag
        global workOrder
        if qcCheckFlag == False:
            workOrder.configure(state=NORMAL)  #SJ0170422 - Reinstate workOrder field which was disabled in qcCheckCallback
        self.initializeInputFields(master)

    def saveCallback(self, master):
        if (self.verifyInputData(master) == True):
            #self.prodType = productsTypeListbox.curselection()
            #self.prodString = list(self.prodType)
            try:
                curCursor.execute('''INSERT INTO werChecklist (customerName, workOrder, dateReceived, receivedBy, numOfPieces,
                               ofPieces, pictureStatus, photoesStatus, productsTypeListbox, numberOfPartsListbox, partsInBlueBin,
                               notes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (self.customerName, self.workOrder, dateReceived.get_date(),
                               usersOption.get(), eval(numOfPieces.get()), eval(ofPieces.get()), pictureStatus.get(), photoesStatus.get(),
                               str(productsTypeListbox.curselection()), str(numberOfPartsListbox.curselection()),
                               partsInBlueBin.get(), notes.get(1.0, END)))  #SJ4020622 - Change receivedBy to usersOption
                conn.commit()

                self.initializeInputFields(master)
            except:
                showwarning(title='Critical Error', message='Data entry error. Please check all input data.')

    #SJ3130422 - This method verify input data validity
    def verifyInputData(self, master):
        global conn
        global curCursor

        self.returnValue = False
        self.customerName = customerName.get().strip()
        self.workOrder = workOrder.get().strip()
        #self.receivedBy = receivedBy.get().strip()  #SJ2310522 - Original sttmt. DO NOT REMOVE
        #self.usersOption = usersOption.get()
        self.numOfPieces = numOfPieces.get().strip()
        self.ofPieces = ofPieces.get().strip()
        self.pictureStatus = pictureStatus.get()
        self.photoesStatus = photoesStatus.get()
        self.prodType = self.removeAlphaChar(str(productsTypeListbox.curselection()), "Initialize")
        self.partsList = self.removeAlphaChar(str(numberOfPartsListbox.curselection()), "Initialize")

        print('pictureStatus and photoesStatus', self.pictureStatus, self.photoesStatus)
        print('productsTypeListbox and numberOfPartsListbox', len(self.prodType), len(self.partsList))
        #SJ3130422 - First we check to see if customerName or workOrder is empty
        if len(self.customerName) == 0 or len(self.workOrder) == 0:
            showwarning(title='Missing Fields', message='Check the Customer Name or WOP fields')
            customerName.focus_set()
        else:
            #SJ3130422 - Here we check for duplicate workOrder
            curCursor.execute('SELECT workOrder FROM werChecklist WHERE workOrder = ? LIMIT 1', (self.workOrder, ))
            count = curCursor.fetchone()
            if count != None:
                #count = curCursor.fetchone()[0]
                showwarning(title='Duplicate WOP', message='It seems '+self.workOrder+' had been used.')
                workOrder.delete(0, END)  #SJ3130422 - Empty workOrder field
                workOrder.focus_set()  #SJ3130422 - Put workOrder field to focus
            #SJ3130422 - receivedBy field is empty
            #elif (self.receivedBy == ''):
                #showwarning(title='Empty Field', message='Received by input field is empty.')
                #receivedBy.focus_set()
            #SJ3130422 - Check if numOfPieces contains invalid characters
            elif (not (self.numOfPieces.isdigit())):
                showwarning(title='Invalid Data', message='Pieces must be a number.')
                numOfPieces.focus_set()
            #SJ3130422 - Check if ofPieces contains invalid characters
            elif (not (self.ofPieces.isdigit())):
                showwarning(title='Invalid Data', message='Of Pieces must be a number.')
                ofPieces.focus_set()
            #SJ3130422 - Check if numOfPieces or ofPieces is greater than 0
            elif (eval(self.numOfPieces) <= 0):
                showwarning(title='Invalid Data', message='Pieces must be greater than 0.')
                numOfPieces.focus_set()
            elif (eval(self.ofPieces)  <= 0):
                showwarning(title='Invalid Data', message='Of Pieces must be greater than 0.')
                ofPieces.focus_set()
            elif (eval(self.numOfPieces) != eval(self.ofPieces)):
                showwarning(title='Invalid Data', message='Pieces and Of Pieces do not match.')
                numOfPieces.focus_set()
            #SJ4180822 - Verify if picture check button is checked
            elif (self.pictureStatus == 0):
                showwarning(title='Invalid Data', message='Pictures field is not checked.')
                self.pictureCheckButton.focus_set()
            #SJ4180822 - Verify if photoes check button is checked
            elif (self.photoesStatus == 0):
                showwarning(title='Invalid Data', message='Photoes Uploaded field is not checked.')
                self.photoesCheckButton.focus_set()
            #print('pictureStatus and photoesStatus', self.pictureStatus, self.photoesStatus)
            #print('productsTypeListbox and numberOfPartsListbox', len(self.prodType), len(self.partsList))
            else:
                self.returnValue = True

        return (self.returnValue)

    #SJ4210422 - Callback for browse Button
    def browseCallback(self, master):
        global conn
        global curCursor
        global totalRecords
        global rowsPerPage
        global numOfRow
        global numOfCol
        global currentRecord
        global currentPage
        global pageFirstRecord
        global totalRecordsBrowsed

        #numOfRow = 5  #SJ2100522 - Don't initialise here as it will be computed based on availabel records to display
        numOfCol = 3
        fromDate = datetime(1,1,1).now()  #SJ2260422 - Default to today date
        toDate = ''

        self.curRowNumber = self.startRow = 2

        inputDate = selectDateDialog(master)
        master.wait_window(inputDate.dateDialog)
        fromDate = str(inputDate.getFromDate())
        #toDate = fromDate[:5]+str(int(fromDate[5:7])+1).zfill(2)+'-01'  #SJ1020522 - This computes to first day of the next month
        toDate = self.computeToDate(fromDate)

        #curCursor.execute('SELECT customerName, workOrder FROM werChecklist WHERE dateReceived >= ? AND dateReceived < ?', [fromDate])
        curCursor.execute('SELECT workOrder, customerName, dateReceived FROM werChecklist WHERE dateReceived >= ? AND dateReceived < ?', (fromDate, toDate))
        recData = curCursor.fetchall()  #SJ0010522 - if use fetchall check using len
        #recData = curCursor.fetchone()  #SJ0010522 - if use fetchone can use None to check
        totalRecords = len(recData)
        if totalRecords == 0:
            showwarning(title='No Records Found', message='No records that match your input date.')
        else:
            print('recData ', totalRecords, recData)
            self.browseButton.configure(state=DISABLED)
            self.browseWindow = Toplevel()
            self.browseTable = SJTable(self.browseWindow, rowsPerPage, numOfCol)

            #SJ6230422 - Use str(chr(923)) for up indicator and capital letter V for down indicator
            self.upButton = Button(self.browseWindow, text=str(chr(923)), command=lambda x=self.browseTable: self.upButtonCallback(x))
            self.upButton.grid(row=self.curRowNumber, column=0)
            self.cancelButton = Button(self.browseWindow, text='Cancel', command=lambda x=self.browseWindow, y=self.browseTable:
                                       self.cancelButtonCallback(x, y))
            self.cancelButton.grid(row=self.curRowNumber, column=numOfCol+1)
            self.curRowNumber += 1

            self.downButton = Button(self.browseWindow, text='V', command=lambda x=self.browseTable: self.downButtonCallback(x))
            self.downButton.grid(row=self.curRowNumber, column=0)
            self.selectButton = Button(self.browseWindow, text='Select', command=lambda x=master, y=self.browseWindow, z=self.browseTable:
                                       self.selectButtonCallback(x, y, z))
            self.selectButton.grid(row=self.curRowNumber, column=numOfCol+1)
            self.curRowNumber += 1

            self.prevPageButton = Button(self.browseWindow, text=str(chr(171)), command=lambda x=self.browseTable, y=recData: self.prevPageButtonCallback(x, y))
            self.prevPageButton.grid(row=self.curRowNumber, column=0)
            self.curRowNumber += 1
            self.nextPageButton = Button(self.browseWindow, text=str(chr(187)), command=lambda x=self.browseTable, y=recData: self.nextPageButtonCallback(x, y))
            self.nextPageButton.grid(row=self.curRowNumber, column=0)

            #SJ5130522 - re-intialize global var
            if (len(pageFirstRecord) != 0):
                del pageFirstRecord[:]
            totalRecordsBrowsed = 0

            numOfRow = rowsPerPage if totalRecords >= rowsPerPage else totalRecords
            currentRecord = 0  #SJ1090522 - valid value = 0 to numOfRow - 1
            currentPage = 0  #SJ5130522 - First page of records
            pageFirstRecord.append(0)  #SJ2100522 - 0 being the first record of the total searched records
            totalRecordsBrowsed += numOfRow
            print('numOfRow, pageFirstRecord, totalRecordsBrowsed: ', numOfRow, pageFirstRecord, totalRecordsBrowsed)

            for i in range(numOfRow):
                self.browseTable.addRowOfData(i, recData[i])

            self.browseTable.highlightRow(currentRecord, numOfCol)

    def computeToDate(self, fromDate):
        try:
            self.year = int(fromDate[:4])
            self.month = int(fromDate[5:7])
            self.day = int(fromDate[8:])
            self.newDay = self.day + 14

            #SJ6140522 - If comes to any of this if else, the next 14 days extend to the next month
            if (self.newDay > 31 and self.month in [1, 3, 5, 7, 8, 10, 12]):
                self.newDay -= 31
                if (self.month == 12):
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
            elif (self.newDay > 30 and self.month in [4, 6, 9, 11]):
                self.newDay -= 30
                self.month += 1
            elif (self.newDay > 28 and self.month == 2):  #SJ6140522 - Here we ignore leap year
                self.newDay -= 28
                self.month += 1
            self.toDate = str(self.year)+'-'+str(self.month).zfill(2)+'-'+str(self.newDay).zfill(2)
        except:
            fromDate = str(datetime(1,1,1).now())
            self.toDate = fromDate[:5]+str(int(fromDate[5:7])).zfill(2)+'-28'

        return(self.toDate)

    def upButtonCallback(self, browseTable):
        global numOfCol
        global currentRecord
        #SJ1090522 - Can only move up if currentRecord is not pointing to first record of the table
        if currentRecord > 0:
            browseTable.deHighlightRow(currentRecord, numOfCol)
            currentRecord -= 1
            browseTable.highlightRow(currentRecord, numOfCol)
        else:
            pass

    def downButtonCallback(self, browseTable):
        global numOfRow
        global numOfCol
        global currentRecord
        #SJ1090522 - Can only move down if currentRecord is not pointing to the last record of the table
        if currentRecord < (numOfRow - 1):
            browseTable.deHighlightRow(currentRecord, numOfCol)
            currentRecord += 1
            browseTable.highlightRow(currentRecord, numOfCol)
        else:
            pass

    def prevPageButtonCallback(self, browseTable, recData):
        #global totalRecords
        global rowsPerPage
        global numOfRow
        global numOfCol
        global currentRecord
        global currentPage
        global pageFirstRecord
        global totalRecordsBrowsed

        #SJ5130522 - Can go back to previous page if only current page is beyond first page
        if currentPage != 0:
            del pageFirstRecord[currentPage]  #S5130522 - remove the first record of current page before going back to previous page
            currentPage -= 1
            totalRecordsBrowsed -= numOfRow
            currentRecord = 0

            #SJ412-522 - Clear table before populating the table with new page of data
            browseTable.clearTable(numOfRow, numOfCol)
            numOfRow = rowsPerPage
            for i in range(numOfRow):
                browseTable.addRowOfData(i, recData[pageFirstRecord[currentPage] + i])
            browseTable.highlightRow(currentRecord, numOfCol)

        print('currentPage, numOfRow, pageFirstRecord, totalRecordsBrowsed: ',
               currentPage, numOfRow, pageFirstRecord, totalRecordsBrowsed)

    def nextPageButtonCallback(self, browseTable, recData):
        global totalRecords
        global rowsPerPage
        global numOfRow
        global numOfCol
        global currentRecord
        global currentPage
        global pageFirstRecord
        global totalRecordsBrowsed

        #SJ2100522 - Computer how many records left available for display
        self.availRecord = totalRecords - totalRecordsBrowsed
        if self.availRecord == 0:
            #SJ4120522 - If comes here, means no more records available for browsing
            pass
            #return
        else:
            #SJ4120522 - If comes here, means there are still records to be displayed
            currentRecord = 0
            numOfRow = rowsPerPage if self.availRecord >= rowsPerPage else self.availRecord
            pageFirstRecord.append(pageFirstRecord[currentPage] + rowsPerPage)
            currentPage += 1
            totalRecordsBrowsed += numOfRow

            #SJ4120522 - Clear table before populating the table with new page of data
            browseTable.clearTable(rowsPerPage, numOfCol)
            for i in range(numOfRow):
                browseTable.addRowOfData(i, recData[pageFirstRecord[currentPage] + i])
            browseTable.highlightRow(currentRecord, numOfCol)

            print('currentPage, numOfRow, pageFirstRecord, totalRecordsBrowsed: ',
                   currentPage, numOfRow, pageFirstRecord, totalRecordsBrowsed)

    def cancelButtonCallback(self, browseWindow, browseTable):
        self.browseButton.configure(state=NORMAL)
        del(browseTable)
        browseWindow.destroy()


    def selectButtonCallback(self, masterWindow, browseWindow, browseTable):
        global currentRecord
        self.selectedWorkOrder = browseTable.getWorkOrder(currentRecord)
        self.browseButton.configure(state=NORMAL)
        del(browseTable)
        browseWindow.destroy()
        #print('selectButtonCallback ', self.selectedWorkOrder)
        self.searchCallback(masterWindow, self.selectedWorkOrder)

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

#SJ1250422 - This class prompts user for a date and return the date to the calling function
class selectDateDialog:
    def __init__(self, master):
        self.dateDialog = Toplevel(master)
        #self.fromDate = '0'
        self.fromDate = str(datetime(1,1,1).now())[:10]  #SJ6110622 - Only need the date portion
        #SJ1250422 - Input field for Date received
        self.todayDate = datetime(1,1,1).now()  #SJ1250422 - Getting today system date
        self.dateReceivedLabel = Label(self.dateDialog, text='Please select the date you wish to browse the record from').grid(row=2, column=1)
        self.dateReceived = DateEntry(self.dateDialog, values="Text", year=self.todayDate.year, state="readonly", date_pattern="yyyy-mm-dd")
        self.dateReceived.grid(row=4, column=1, padx=20, pady=5, sticky=W)

        self.okButton = Button(self.dateDialog, text="Ok", command = self.okCallback)
        self.okButton.grid(row=4, column=2)

    def okCallback(self):
        self.fromDate = self.dateReceived.get_date()
        self.dateDialog.destroy()

    def getFromDate(self):
        return (self.fromDate)
        #return (self.fromDate[:10])

    def __del__(self):
        print('Destructor for selectDateDialog')

#SJ6230422 - Class to create table
class SJTable:
    def __init__(self, master, numOfRow, numOfCol):
        self.browseTable = master #Toplevel(master)
        self.entryFields = [[0 for x in range(numOfCol)] for y in range(numOfRow)]
        self.rowNumber = 2
        #self.label = Label(master, text='Records Browser')
        #self.label.grid(row=0, column=0)
        # code for creating table
        for i in range(numOfRow):
            for j in range(numOfCol):
                #self.e = Entry(self.browseTable, width=20, fg='blue', font=('Arial',16,'bold'))
                self.e = Entry(self.browseTable, width=20, fg='black', font=('Arial',12))
                self.e.grid(row=self.rowNumber+i, column=1+j)
                self.entryFields[i][j] = self.e

    def addRowOfData(self, rowNumber, recData):
        #SJ2030522 - seq of input data: workOrder, customerName, dateReceived
        self.entryFields[rowNumber][0].insert(0, recData[0])
        self.entryFields[rowNumber][0].configure(state=DISABLED)
        self.entryFields[rowNumber][1].insert(0, recData[1])
        self.entryFields[rowNumber][1].configure(state=DISABLED)
        #self.entryFields[rowNumber][2].set_date(recData[2])
        self.entryFields[rowNumber][2].insert(0, recData[2])
        self.entryFields[rowNumber][2].configure(state=DISABLED)

    def highlightRow(self, rowNumber, numOfCol):
        for i in range(numOfCol):
            self.entryFields[rowNumber][i].configure(state=NORMAL, bg='green')  #'#A202FF'

    def deHighlightRow(self, rowNumber, numOfCol):
        for i in range(numOfCol):
            self.entryFields[rowNumber][i].configure(state=DISABLED)

    def clearTable(self, numOfRow, numOfCol):
        for i in range(numOfRow):
            for j in range(numOfCol):
                self.entryFields[i][j].configure(state=NORMAL, bg='white')
                self.entryFields[i][j].delete(0, END)

    def getWorkOrder(self, currentRecord):
        return (self.entryFields[currentRecord][0].get())

    def __del__(self):
        #SJ4050522 - Need to add code to call destroy() method
        print('Destructor for SJTable')

def quitter_function():
    print('quitter_function: Closing sql connection and destroy root object...')
    conn.close()  #SJ5250222 - Close database connection
    root.destroy()

#SJ1230522 - This function creates main menu
def mainMenu(root):
    menu = Menu()
    root.config(menu=menu)
    tools_menu = Menu(menu, tearoff=0)
    tools_menu.add_command(label='Backup', command=toolsCallback)
    tools_menu.add_separator()
    tools_menu.add_command(label='Exit', command=quitter_function)
    menu.add_cascade(label='Tools', menu=tools_menu)


def toolsCallback():
    print('Inside toolsCallback...')
    pass

root = Tk()
root.protocol('WM_DELETE_WINDOW', quitter_function)
app = WER_Main(root)
mainMenu(root)
mainloop()

#str(list(productsTypeListbox.curselection())), str(list(numberOfPartsListbox.curselection())),
