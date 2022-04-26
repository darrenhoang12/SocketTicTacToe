def boardSetup(self):
    self.master = tk.Tk()
    self.master.title('Tic Tac Toe')
    self.master.geometry('1000x550')
    self.master.configure(background='purple')

def initTKVariables(self):
    self.player1Name = tk.StringVar()
    self.player2Name = tk.StringVar()
    self.lastPlayer = tk.StringVar()
    self.serverAddress = tk.StringVar()
    self.port = tk.StringVar()

def createServerAddressEntry(self):
    self.saentry = tk.Entry(self.master, textvariable=self.serverAddress)
    self.saentry.grid(row=0, column=4)

def submitServerAddress(self): 
    self.submit = tk.Button(self.master, text='submit', command=lambda: self.setServerAddress(self.saentry.get()))
    self.submit.grid(row=0, column=5)

def setServerAddress(self, sa):
    self.sa = sa
        
def getSA(self):
    return self.sa

def createPortEntry(self):
    self.player2Entry = tk.Entry(self.master, textvariable=self.player2Name)
    self.player2Entry.grid(row=1, column=4)

def createButtons(self):
        self.b1 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b1))
        self.b2 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b2))
        self.b3 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b3))

        self.b4 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b4))
        self.b5 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b5))
        self.b6 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b6))

        self.b7 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b7))
        self.b8 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b8))
        self.b9 = tk.Button(self.master, background='white', font='15', text=' ', height=8, width=16, command=lambda: self.playMoveOnBoard(self.b9))

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

    def createPlayer1Entry(self):
        self.player1Entry = tk.Entry(self.master, textvariable=self.player1Name)
        self.player1Entry.grid(row=4, column=0)

    def createPlayer2Entry(self):
        self.player2Entry = tk.Entry(self.master, textvariable=self.player2Name)
        self.player2Entry.grid(row=4, column=2)

    def createPlayer1Label(self):
        self.player1Label = tk.Label(self.master, text='Player 1')
        self.player1Label.grid(row=3, column=0)

    def createPlayer2Label(self):
        self.player2Label = tk.Label(self.master, text='Player 2')
        self.player2Label.grid(row=3, column=2)

    def createLastPlayerLabel(self):
        self.lastPlayerLabel = tk.Label(self.master, text='Last Player')
        self.lpLabel = tk.Label(self.master, textvariable=self.lastPlayer)
        self.lastPlayerLabel.grid(row=3, column=1)
        self.lpLabel.grid(row=4, column=1)


    def playMoveOnBoard(self, button): 
        if button['text'] == ' ' and self.clicked == True:
            button['text'] = 'X'
            self.clicked = False
            self.moves += 1
            self.lastPlayer.set(self.player2Name.get())
            if button == self.b1:
                self.currentBoard.append('X top left')
            elif button == self.b2:
                self.currentBoard.append('X top middle')
            elif button == self.b3:
                self.currentBoard.append('X top right')
            elif button == self.b4:
                self.currentBoard.append('X middle left')
            elif button == self.b5:
                self.currentBoard.append('X center')
            elif button == self.b6:
                self.currentBoard.append('X middle right')
            elif button == self.b7:
                self.currentBoard.append('X bottom left')
            elif button == self.b8:
                self.currentBoard.append('X bottom middle')
            elif button == self.b9:
                self.currentBoard.append('X bottom right')
        elif button['text'] == ' ' and self.clicked == False:
            button['text'] = 'O'
            self.clicked = True
            self.moves += 1
            self.lastPlayer.set(self.player1Name.get())
            if button == self.b1:
                self.currentBoard.append('O top left')
            elif button == self.b2:
                self.currentBoard.append('O top middle')
            elif button == self.b3:
                self.currentBoard.append('O top right')
            elif button == self.b4:
                self.currentBoard.append('O middle left')
            elif button == self.b5:
                self.currentBoard.append('O center')
            elif button == self.b6:
                self.currentBoard.append('O middle right')
            elif button == self.b7:
                self.currentBoard.append('O bottom left')
            elif button == self.b8:
                self.currentBoard.append('O bottom middle')
            elif button == self.b9:
                self.currentBoard.append('O bottom right')

    def runUI(self):
        self.master.mainloop()
