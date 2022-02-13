#Project: WER checklist
#Date: Feb 11, 2022

from tkinter import *
from tkcalendar import DateEntry


class WER_Main:
    def __init__(self, master):
        master.title('West End Radiators')

        #SJ5110222 - Input field for customer name
        self.customerLabel = Label(master, text='Customer: ').grid(row=0, column=0)
        self.customerEntry = Entry(master)
        self.customerEntry.grid(row=0, column=1)

        #SJ5110222 - Input field for work order
        self.workOrderLabel = Label(master, text='WO: ').grid(row=0, column=3)
        self.workOrderEntry = Entry(master)
        self.workOrderEntry.grid(row=0, column=4)

        #SJ6120222 - Input field for Date received
        self.dateReceivedLabel = Label(text='Date Received: ').grid(row=2, column=0)
        self.dateReceivedEntry = DateEntry(master, values="Text", year=2022, state="readonly", date_pattern="yyyy-mm-dd")
        self.dateReceivedEntry.grid(row=2, column=1, padx=20, pady=5, sticky=W)

        #SJ6120222 - Input field for Received by
        self.receivedByLabel = Label(master, text='Received by: ').grid(row=2, column=3)
        self.receivedByEntry = Entry(master)
        self.receivedByEntry.grid(row=2, column=4)

        #SJ6120222 - Input field for pieces
        self.piecesLabel = Label(master, text='Piece(s): ').grid(row=3, column=0)
        self.piecesEntry = Entry(master)
        self.piecesEntry.grid(row=3, column=1)

        #SJ6120222 - Input field for of
        self.ofLabel = Label(master, text='of: ').grid(row=3, column=3)
        self.ofEntry = Entry(master)
        self.ofEntry.grid(row=3, column=4)

        #self.button = Button(text='Click me', command=self.callback)
        #self.label.grid(row=0, column=0)
        #self.button.grid(row=1, column=0)

    def callback(self):
        self.label.configure(text='Button clicked')


root = Tk()

app = WER_Main(root)

mainloop()
