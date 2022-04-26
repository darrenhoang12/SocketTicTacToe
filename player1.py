import tkinter as tk
import socket
import threading
from gameboard import gameBoard

gb = gameBoard()
serverAddress = 0
portNumber = 0
clientSocket, clientAddress = None, None


master = tk.Tk()
master.title('Tic Tac Toe')
master.geometry('1000x600')
master.configure(background='purple')
master.resizable(width=False, height=False)

address = tk.StringVar()
port = tk.StringVar()
player1 = tk.StringVar()

def submitHostInfo():
    global serverAddress
    global portNumber
    global serverSocket
    try:
        serverAddress = address.get()
        portNumber = int(port.get())
        print(serverAddress)
        print(portNumber)
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((serverAddress, portNumber))
        serverSocket.listen(1)
        createThread(waitingForConnection)
        submitHostInfoButton.destroy()
        message.config(text='Waiting for player 2...')
    except Exception:
        message.config(text='Invalid host information. Please try again.')
        clearHostInfo()
        

def clearHostInfo():
    address.set('')
    port.set('')

def sendUserName():
    userName = player1.get()
    gb.setPlayer1Name(userName)
    sendUserName = userName.encode()
    clientSocket.send(sendUserName)
    player1Submit.destroy()

turn = False
def clicked1():
    global turn
    if turn == True and b1['text'] == ' ':
        b1['text'] = 'O'
        move = gb.playMoveOnBoard(1)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked2():
    global turn
    if turn == True and b2['text'] == ' ':
        b2['text'] = 'O'
        move = gb.playMoveOnBoard(2)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked3():
    global turn
    if turn == True and b3['text'] == ' ':
        b3['text'] = 'O'
        move = gb.playMoveOnBoard(3)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked4():
    global turn
    if turn == True and b4['text'] == ' ':
        b4['text'] = 'O'
        move = gb.playMoveOnBoard(4)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked5():
    global turn
    if turn == True and b5['text'] == ' ':
        b5['text'] = 'O'
        move = gb.playMoveOnBoard(5)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked6():
    global turn
    if turn == True and b6['text'] == ' ':
        b6['text'] = 'O'
        move = gb.playMoveOnBoard(6)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked6():
    global turn
    if turn == True and b6['text'] == ' ':
        b6['text'] = 'O'
        move = gb.playMoveOnBoard(6)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked7():
    global turn
    if turn == True and b7['text'] == ' ':
        b7['text'] = 'O'
        move = gb.playMoveOnBoard(7)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked8():
    global turn
    if turn == True and b8['text'] == ' ':
        b8['text'] = 'O'
        move = gb.playMoveOnBoard(8)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)

def clicked9():
    global turn
    if turn == True and b9['text'] == ' ':
        b9['text'] = 'O'
        move = gb.playMoveOnBoard(9)
        checkForGameFinish()
        turn = False
        gb.setLastPlayer(gb.getPlayer1Name())
        print('Last Player:', gb.lastPlayer)
        currentPlayerName.config(text=gb.getPlayer2Name())
        dataToSend = move.encode()
        clientSocket.send(dataToSend)


def createThread(targett):
    thread = threading.Thread(target=targett)
    thread.daemon = True
    thread.start()

def receiveData():
    global turn
    global decoded
    while True:
        clientData = clientSocket.recv(1024)
        decoded = clientData.decode()
        print(decoded)
        if decoded == '1':
            b1['text'] = 'X'
            gb.playMoveOnBoard(1)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '2':
            b2['text'] = 'X'
            gb.playMoveOnBoard(2)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '3':
            b3['text'] = 'X'
            gb.playMoveOnBoard(3)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '4':
            b4['text'] = 'X'
            gb.playMoveOnBoard(4)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '5':
            b5['text'] = 'X'
            gb.playMoveOnBoard(5)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '6':
            b6['text'] = 'X'
            gb.playMoveOnBoard(6)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '7':
            b7['text'] = 'X'
            gb.playMoveOnBoard(7)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '8':
            b8['text'] = 'X'
            gb.playMoveOnBoard(8)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == '9':
            b9['text'] = 'X'
            gb.playMoveOnBoard(9)
            turn = True
            gb.setLastPlayer(gb.getPlayer2Name())
            print('Last Player:', gb.lastPlayer)
            currentPlayerName.config(text=gb.getPlayer1Name())
            checkForGameFinish()
        elif decoded == 'Play Again':
            playAgainLabel.destroy()
            currentPlayerName.config(text=gb.getPlayer2Name())
            clearBoard()
            gb.resetTurn()
            gb.recordGamePlayed()
        elif decoded == 'Fun Times':
            playAgainLabel.destroy()
            funTimesMsg = 'Fun Times'
            encodedMsg = funTimesMsg.encode()
            clientSocket.send(encodedMsg)
            createScoreBoard()
            serverSocket.close()
            return
        elif decoded == 'Connected':
            message.config(text='Connected')
        else:
            gb.setPlayer2Name(decoded)
            player2Name.config(text=gb.getPlayer2Name())
            currentPlayerName.config(text=gb.getPlayer2Name())
            gb.recordGamePlayed()
        

def checkForGameFinish():
    global turn
    global playAgainLabel
    isBoardFull = gb.isBoardFull()
    isGameFinished = gb.isGameFinished()
    if isGameFinished == ('X wins!'):
        gb.incrementTotalLosses()
        playAgainLabel = tk.Label(container, text='X wins! Waiting for player 2...')
        playAgainLabel.grid(row=3, column=0)
        turn = False
    elif isGameFinished == ('O wins!'):
        gb.incrementTotalWins()
        playAgainLabel = tk.Label(container, text='O wins! Waiting for player 2...')
        playAgainLabel.grid(row=3, column=0)
        turn = False
    elif isBoardFull == True and isGameFinished == None:
        gb.incrementTotalTies()
        playAgainLabel = tk.Label(container, text='Draw! Waiting for player 2...')
        playAgainLabel.grid(row=3, column=0)
        turn = False

def clearBoard():
    gb.resetGameBoard()
    listButtons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    for button in listButtons:
        button['text'] = ' '
        
def createScoreBoard():
    scoreBoard = tk.Frame(master)
    scoreBoard.grid(row=1, column=5)
    scoreBoardTitle = tk.Label(scoreBoard, font=(None, 12), text='Scoreboard')
    scoreBoardTitle.grid(row=0, column=0)
    scoreBoardTitle
    player1SBLabel = tk.Label(scoreBoard, text='Player 1:')
    player1SBLabel.grid(row=1, column=0)
    player1SBName = tk.Label(scoreBoard, text=gb.getPlayer1Name())
    player1SBName.grid(row=1, column=1)
    player2SBLabel = tk.Label(scoreBoard, text='Player 2:')
    player2SBLabel.grid(row=2, column=0)
    player2SBName = tk.Label(scoreBoard, text=gb.getPlayer2Name())
    player2SBName.grid(row=2, column=1)
    lastPlayerSBLabel = tk.Label(scoreBoard, text='Last Player:')
    lastPlayerSBLabel.grid(row=3, column=0)
    lastPlayerSBName = tk.Label(scoreBoard, text=gb.lastPlayer)
    lastPlayerSBName.grid(row=3, column=1)
    totalGamesLabel = tk.Label(scoreBoard, text='Total Games:')
    totalGamesLabel.grid(row=4, column=0)
    totalGamesPlayed = tk.Label(scoreBoard, text=gb.games)
    totalGamesPlayed.grid(row=4, column=1)
    totalWinsLabel = tk.Label(scoreBoard, text='Total Wins:')
    totalWinsLabel.grid(row=5, column=0)
    totalWins = tk.Label(scoreBoard, text=gb.wins)
    totalWins.grid(row=5, column=1)
    totalLossesLabel = tk.Label(scoreBoard, text='Total Losses:')
    totalLossesLabel.grid(row=6, column=0)
    totalLosses = tk.Label(scoreBoard, text=gb.losses)
    totalLosses.grid(row=6, column=1)
    totalTiesLabel = tk.Label(scoreBoard, text='Total Ties:')
    totalTiesLabel.grid(row=7, column=0)
    totalTies = tk.Label(scoreBoard, text=gb.ties)
    totalTies.grid(row=7, column=1)

def waitingForConnection():
    global clientSocket, clientAddress
    global decoded
    clientSocket, clientAddress = serverSocket.accept()
    receiveData()
    

container = tk.Frame(master)
container.grid(row=0, column=5)
askForHostInfo = tk.Label(container, text='Provide the host information')
askForHostInfo.grid(row=0, column=0)
serverAddressLabel = tk.Label(container, text='Server Address')
serverAddressLabel.grid(row=1, column=0)
serverAddressEntry = tk.Entry(container, textvar=address)
serverAddressEntry.grid(row=2, column=0)
portNumberLabel = tk.Label(container, text='Port Number')
portNumberLabel.grid(row=1, column=1)
portNumberEntry = tk.Entry(container, textvar=port)
portNumberEntry.grid(row=2, column=1)
submitHostInfoButton = tk.Button(container, text='Submit', command=lambda: submitHostInfo())
submitHostInfoButton.grid(row=2, column=2)

message = tk.Label(container, text='')
message.grid(row=3, column=0)

player1Label = tk.Label(master, text='Player 1')
player1Label.grid(row=3, column=0)
player1Name = tk.Entry(master, width=8, textvar=player1)
player1Name.grid(row=4, column=0)
player1Submit = tk.Button(master, text='Send', command=lambda: sendUserName())
player1Submit.grid(row=5, column=0)

player2Label = tk.Label(master, text='Player 2')
player2Label.grid(row=3, column=2)
player2Name = tk.Label(master, width=8, textvar='')
player2Name.grid(row=4, column=2)

currentPlayerLabel = tk.Label(master, text='Current Player')
currentPlayerLabel.grid(row=3, column=1)
currentPlayerName = tk.Label(master, text='')
currentPlayerName.grid(row=4, column=1)

b1 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked1())
b2 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked2())
b3 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked3())

b4 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked4())
b5 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked5())
b6 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked6())

b7 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked7())
b8 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked8())
b9 = tk.Button(master, background='white', font='15', text=' ', height=9, width=18, command=lambda: clicked9())

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

quitButton = tk.Button(master, text='Quit', command=lambda: master.destroy())
quitButton.grid(row=5, column=4)

master.mainloop()
