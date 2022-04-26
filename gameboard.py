class gameBoard():
    currentBoard = [['', '', ''],
                    ['', '', ''],
                    ['', '', '']]
    player1Name = 0
    player2Name = 0
    lastPlayer = 0
    games = 0
    wins = 0
    ties = 0
    losses = 0
    turn = True

    def __init__(self):
        self.currentBoard = [['', '', ''],
                             ['', '', ''],
                             ['', '', '']]
        self.player1Name = 0
        self.player2Name = 0
        self.lastPlayer = 0
        self.games = 0
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.turn = True

    def resetGameBoard(self):
        for row in self.currentBoard:
            row.clear()
        for numAdd in range(3):
            for numAdd2 in range(3):
                self.currentBoard[numAdd].append('')
                
    def playMoveOnBoard(self, position):
        global turn
        if self.turn == True and position == 1 and self.currentBoard[0][0] == '':
            self.currentBoard[0][0] = 'X'
            self.turn = False
            return('1')
        elif self.turn == True and position == 2 and self.currentBoard[0][1] == '':
            self.currentBoard[0][1] = 'X'
            self.turn = False
            return('2')
        elif self.turn == True and position == 3 and self.currentBoard[0][2] == '':
            self.currentBoard[0][2] = 'X'
            self.turn = False
            return('3')
        elif self.turn == True and position == 4 and self.currentBoard[1][0] == '':
            self.currentBoard[1][0] = 'X'
            self.turn = False
            return('4')
        elif self.turn == True and position == 5 and self.currentBoard[1][1] == '':
            self.currentBoard[1][1] = 'X'
            self.turn = False
            return('5')
        elif self.turn == True and position == 6 and self.currentBoard[1][2] == '':
            self.currentBoard[1][2] = 'X'
            self.turn = False
            return('6')
        elif self.turn == True and position == 7 and self.currentBoard[2][0] == '':
            self.currentBoard[2][0] = 'X'
            self.turn = False
            return('7')
        elif self.turn == True and position == 8 and self.currentBoard[2][1] == '':
            self.currentBoard[2][1] = 'X'
            self.turn = False
            return('8')
        elif self.turn == True and position == 9 and self.currentBoard[2][2] == '':
            self.currentBoard[2][2] = 'X'
            self.turn = False
            return('9')
        elif self.turn == False and position == 1 and self.currentBoard[0][0] == '':
            self.currentBoard[0][0] = 'O'
            self.turn = True
            return('1')
        elif self.turn == False and position == 2 and self.currentBoard[0][1] == '':
            self.currentBoard[0][1] = 'O'
            self.turn = True
            return('2')
        elif self.turn == False and position == 3 and self.currentBoard[0][2] == '':
            self.currentBoard[0][2] = 'O'
            self.turn = True
            return('3')
        elif self.turn == False and position == 4 and self.currentBoard[1][0] == '':
            self.currentBoard[1][0] = 'O'
            self.turn = True
            return('4')
        elif self.turn == False and position == 5 and self.currentBoard[1][1] == '':
            self.currentBoard[1][1] = 'O'
            self.turn = True
            return('5')
        elif self.turn == False and position == 6 and self.currentBoard[1][2] == '':
            self.currentBoard[1][2] = 'O'
            self.turn = True
            return('6')
        elif self.turn == False and position == 7 and self.currentBoard[2][0] == '':
            self.currentBoard[2][0] = 'O'
            self.turn = True
            return('7')
        elif self.turn == False and position == 8 and self.currentBoard[2][1] == '':
            self.currentBoard[2][1] = 'O'
            self.turn = True
            return('8')
        elif self.turn == False and position == 9 and self.currentBoard[2][2] == '':
            self.currentBoard[2][2] = 'O'
            self.turn = True
            return('9')

    def isBoardFull(self):
        for row in self.currentBoard:
            if '' in row:
                return False
        return True

    def isGameFinished(self):
        #checks for win conditions
        if self.currentBoard[0].count('X') == 3:
            return ('X wins!')
        elif self.currentBoard[1].count('X') == 3:
            return ('X wins!')
        elif self.currentBoard[2].count('X') == 3:
            return ('X wins!')
        elif self.currentBoard[0][0] == 'X' and self.currentBoard[1][0] == 'X' and self.currentBoard[2][0] == 'X':
            return ('X wins!')
        elif self.currentBoard[0][1] == 'X' and self.currentBoard[1][1] == 'X' and self.currentBoard[2][1] == 'X':
            return ('X wins!')
        elif self.currentBoard[0][2] == 'X' and self.currentBoard[1][2] == 'X' and self.currentBoard[2][2] == 'X':
            return ('X wins!')
        elif self.currentBoard[0][0] == 'X' and self.currentBoard[1][1] == 'X' and self.currentBoard[2][2] == 'X':
            return ('X wins!')
        elif self.currentBoard[0][2] == 'X' and self.currentBoard[1][1] == 'X' and self.currentBoard[2][0] == 'X':
            return ('X wins!')
        elif self.currentBoard[0].count('O') == 3:
            return ('O wins!')
        elif self.currentBoard[1].count('O') == 3:
            return ('O wins!')
        elif self.currentBoard[2].count('O') == 3:
            return ('O wins!')
        elif self.currentBoard[0][0] == 'O' and self.currentBoard[1][0] == 'O' and self.currentBoard[2][0] == 'O':
            return ('O wins!')
        elif self.currentBoard[0][1] == 'O' and self.currentBoard[1][1] == 'O' and self.currentBoard[2][1] == 'O':
            return ('O wins!')
        elif self.currentBoard[0][2] == 'O' and self.currentBoard[1][2] == 'O' and self.currentBoard[2][2] == 'O':
            return ('O wins!')
        elif self.currentBoard[0][0] == 'O' and self.currentBoard[1][1] == 'O' and self.currentBoard[2][2] == 'O':
            return ('O wins!')
        elif self.currentBoard[0][2] == 'O' and self.currentBoard[1][1] == 'O' and self.currentBoard[2][0] == 'O':
            return ('O wins!')

    def computeStats(self):
        return self.player1Name, self.player2Name, self.lastPlayer, self.games, self.wins, self.ties, self.losses

    def setPlayer1Name(self, username):
        self.player1Name = username

    def setPlayer2Name(self, username):
        self.player2Name = username

    def setLastPlayer(self, username):
        self.lastPlayer = username
        
    def getPlayer1Name(self):
        return self.player1Name

    def getPlayer2Name(self):
        return self.player2Name

    def resetTurn(self):
        self.turn = True
    
    def recordGamePlayed(self):
        self.games += 1

    def incrementTotalWins(self):
        self.wins += 1

    def incrementTotalTies(self):
        self.ties += 1

    def incrementTotalLosses(self):
        self.losses += 1
