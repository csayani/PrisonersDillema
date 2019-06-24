# Prisoner's Dilemma 
# Based upon the psychological/economic theory of a
# prisoner's dilemma, we have designed a game where
# the player engages with various chosen AI strategies
# to score points over a randomly determined number of
# rounds to either win, lose, or tie the game.
# It also utilizes the graphics.py module, which is in the folder.
# By: Chait Sayani and Trevor Hughes 

from random import *
from graphics import *

class Game:

    def __init__(self):
        """ establishes many key variables to be used throughout the class
        in various functions or respective AI strategies """

        # creates the window and various lists that hold objects and text that
        # are drawn to the program throughout the course of the game 
        self.window = GraphWin("Prisoners Dillema", 700,700)
        self.instructionText = []
        self.texts = []
        self.buttonList = []
        self.objectList = []
        self.startText = []
        self.endingText = []
        self.strategy = 0

        # creates two lists to store both the player and bot moves and
        # intializes player score and bot score to zero 
        self.playerHistory = []
        self.botHistory = []
        self.playerScore = 0
        self.botScore = 0
        self.playerMove = ""
        self.botMove = ""
        self.payoff = 0

        # sets the number of runs randomly between 1 and 50 and intializes
        # variables that count and interact with the runs
        self.runs = randint(6, 20)
        self.randCount = 1
        self.randMoves = randint(1, self.runs)
        self.grudge = False
        self.turn = 0
        self.round = 1

        # initializes variables that will calculate the average score for each
        # type of move to be used in the adaptive AI 
        self.cAvg = []
        self.dAvg = []
        self.strat = ""

    def instructions(self):
        """ prints initial instructions to the screen that the user can read to learn 
        the game as well as a button they can press to start the actual game """

        # creates text that intructs the player on how to play the game 
        self.instructionText.append(Text(Point(350, 50), "Welcome to the Prisoner's Dilemma!\n\nYou get to test your abilities as a captive."))
        self.instructionText.append(Text(Point(350, 200), "The police will offer you the ability to cooperate or defect\n\nThey will do the same to a fellow captive "))
        self.instructionText.append(Text(Point(350, 300), "Depending on how you respond, you will get points"))
        self.instructionText.append(Text(Point(350, 400), "Try to get the most points against all six of your fellow captives\n\nGoodluck!"))

        # creates a button that allows the player to move on from the instruction
        # screen and play the game when they are ready
        playButton = Rectangle(Point(300, 500), Point(400, 600))
        playButton.setFill("gold2")
        self.instructionText.append(Text(Point(350, 550), "Ready?"))

        # draws the play button and colors the intruction text 
        playButton.draw(self.window)
        textColors = ["cyan4", "firebrick4", "DarkSeaGreen4", "DarkSeaGreen4", "black"]
        for t in range(len(self.instructionText)):
            self.instructionText[t].setSize(25)
            self.instructionText[t].setFill(textColors[t])
            self.instructionText[t].draw(self.window)

        # waits for the user to click on the button and then erases the instructions
        click1 = self.window.getMouse()
        while not 300 <= click1.x <= 400 or not 500 <= click1.y <= 600:
            click1 = self.window.getMouse()

        playButton.undraw()
        for t in self.instructionText:
            t.undraw()

    def buttons(self):
        """ creates a start screen they introduces the player to the 
        game and lets them choose the strategy they wish to face """
        startWin = self.window

        # creates text to sit at the top and bottom of the screen and instruct
        # the player to choose a strategy 
        self.texts.append(Text(Point(350, 50), "Welcome to Prisoner's Dilemma:\nChoose Your Strategy..."))
        self.texts[0].setFill("aquamarine4")
        self.texts[0].setSize(25)
        self.texts.append(Text(Point(350, 650), "Can You Beat Them All?"))
        self.texts[1].setFill("aquamarine4")
        self.texts[1].setSize(25)

        # creates the six different buttons to represent the six different
        # coded AI strategies the player can play against
        self.buttonList.append(Rectangle(Point(100, 100), Point(300, 200)))
        self.buttonList.append(Rectangle(Point(400, 100), Point(600, 200)))
        self.buttonList.append(Rectangle(Point(100, 300), Point(300, 400)))
        self.buttonList.append(Rectangle(Point(400, 300), Point(600, 400)))
        self.buttonList.append(Rectangle(Point(100, 500), Point(300, 600)))
        self.buttonList.append(Rectangle(Point(400, 500), Point(600, 600)))

        # creates a list of colors and fills in each button with the corresponding
        # color to represent its specific AI strategy 
        colors = ["DarkOliveGreen4", "dark orange", "gold2", "brown4", "DarkSlateGray2", "RosyBrown2"]
        for b in range(len(self.buttonList)):
            self.buttonList[b].setFill(colors[b])

        # creates text to sit within each button and define to
        # the user which strategy each button represents 
        self.texts.append(Text(Point(200, 150), "Random Strategy"))
        self.texts.append(Text(Point(500, 150), "Tit-for-Tat Strategy"))
        self.texts.append(Text(Point(200, 350), "Random Tit-for-Tat Strategy"))
        self.texts.append(Text(Point(500, 350), "Grudge Strategy"))
        self.texts.append(Text(Point(200, 550), "PeaceMaker Strategy"))
        self.texts.append(Text(Point(500, 550), "Adaptive Strategy"))

        # changes the size of all the texts so they fit appropriately within the button 
        for t in range(2, len(self.texts)):
            self.texts[t].setSize(17)
        self.texts[4].setSize(15)

        # draws all of the previously created buttons and text to
        # the window so that the user can interact with them
        for b in self.buttonList:
            b.draw(startWin)
        
        for t in self.texts:
            t.draw(startWin)

    def playerChoice(self):
        """ allows the player to click on a specific button and play against
        their chosen AI strategy """

        # awaits a for a click from the user and initializes a boolean 
        checkValid = False 
        clickInitial = self.window.getMouse()

        # loop ensures that the game does not crash if the player
        # does not click on one of the six buttons and waits for
        # another click if they do so
        while checkValid == False:
            if 100 <= clickInitial.x <= 300 and 100 <= clickInitial.y <= 200:
                self.strategy = 1
                return 1
            elif 400 <= clickInitial.x <= 600 and 100 <= clickInitial.y <= 200:
                self.strategy = 2
                return 2
            elif 100 <= clickInitial.x <= 300 and 300 <= clickInitial.y <= 400:
                self.strategy = 3
                return 3
            elif 400 <= clickInitial.x <= 600 and 300 <= clickInitial.y <= 400:
                self.strategy = 4
                return 4
            elif 100 <= clickInitial.x <= 300 and 500 <= clickInitial.y <= 600:
                self.strategy = 5
                return 5
            elif 400 <= clickInitial.x <= 600 and 500 <= clickInitial.y <= 600:
                self.strategy = 6
                return 6
            else:
                clickInitial = self.window.getMouse()

    def buttonsErase(self):
        """ erases all of the previously created buttons and text in the 
        buttons() function so that the startScreen() function can run without
        drawing over the previously created objects """
        for b in self.buttonList:
            b.undraw()
        for t in self.texts:
            t.undraw()

    def startScreen(self):
        """ creates the screen for the actual game itself, including the gameboard, 
        score boxes, and actual buttons for the player to interact with """

        # sets the background of the gameboard to an appropriate color
        self.window.setBackground("bisque2")

        # creates two buttons at the bottom of the screen that the player uses to
        # select their move and text to go inside the buttons to describe them
        self.objectList.append(Rectangle(Point(100,550), Point(300,650)))
        self.objectList.append(Rectangle(Point(400,550), Point(600,650)))
        self.startText.append(Text(Point(200,600),"Cooperate"))
        self.startText[0].setSize(20)
        self.startText.append(Text(Point(500,600),"Defect"))
        self.startText[1].setSize(20)
        self.objectList[0].setFill("LightBlue2")
        self.objectList[1].setFill("red4")

        # creates the actual gameboard to the screen by drawings lots of lines
        # to represent the different scoring and payoff options to the player 
        self.objectList.append(Rectangle(Point(175,50), Point(525,400)))
        self.objectList.append(Line(Point(350,50), Point(350,400)))
        self.objectList.append(Line(Point(175,225), Point(525,225)))
        self.objectList.append(Line(Point(175,50), Point(350,225)))
        self.objectList.append(Line(Point(350,50), Point(525,225)))
        self.objectList.append(Line(Point(175,225), Point(350,400)))
        self.objectList.append(Line(Point(350,225), Point(525,400)))

        # creates text to depict both the player and opponent side of the gameboard 
        self.startText.append(Text(Point(350,15), "Bot's Move"))
        self.startText[2].setSize(15)
        self.startText.append(Text(Point(88,225),"Player's Move"))
        self.startText[3].setSize(15)

        # creates text on the left side of the gameboard to distinguish the
        # outcome for the player of cooperating or defecting
        self.startText.append(Text(Point(133,133),"Cooperate"))
        self.startText.append(Text(Point(132,313),"Defect"))
        self.startText.append(Text(Point(263,30),"Cooperate"))
        self.startText.append(Text(Point(438,30),"Defect"))

        # sizes this cooperate or defect text appropriately
        for t in range(4, len(self.startText)):
            self.startText[t].setSize(13)

        # creates the payoff text to sit within the gameboard triangles at
        # various colors to represent the worth of each choice the player makes
        self.startText.append(Text(Point(218,138),"2"))
        self.startText.append(Text(Point(218,313),"3"))
        self.startText.append(Text(Point(306,138),"2"))
        self.startText.append(Text(Point(394,138),"0"))
        self.startText.append(Text(Point(481,138),"3"))
        self.startText.append(Text(Point(306,313),"0"))
        self.startText.append(Text(Point(394,313),"1"))
        self.startText.append(Text(Point(481,313),"1"))

        # creates a list of colors and fills in the appropriate
        # payoff text with the correct color 
        payoffTextColors = ["SlateGray3", "gold3", "SlateGray3", "black", "gold3", "black", "saddle brown", "saddle brown"]
        for t in range(8, len(self.startText)):
            self.startText[t].setSize(22)
            self.startText[t].setFill(payoffTextColors[t - 8]) 

        # creates both the player's and bot's score boxes in the
        # upper left corner to display their scores after each move 
        self.objectList.append(Rectangle(Point(44,65),Point(94,115)))
        self.startText.append(Text(Point(69,38),"Player Score"))
        self.startText[16].setSize(15)
        self.objectList.append(Rectangle(Point(600,65),Point(650,115)))
        self.startText.append(Text(Point(625,38),"Bot Score"))
        self.startText[17].setSize(15)

        # draws the previously created shapes and text objects to the
        # window to create the start screen 
        for o in self.objectList:
            o.draw(self.window)

        for t in self.startText:
            t.draw(self.window)

    def playerCoop(self):
        """ activates if the player selects the cooperate button, updating
        their move for the program and storing it in a list of player move history """
        self.playerMove = 'C'
        self.playerHistory.append(self.playerMove)
        return self.playerMove, self.playerHistory

    def playerDefect(self):
        """ activates if the player selects the defect button, updating their 
        their move for the program and storing it in a list of player move history """
        self.playerMove = 'D'
        self.playerHistory.append(self.playerMove)
        return self.playerMove, self.playerHistory

    def botCoop(self):
        """ activiates if the bot chooses to cooperate, updating its move for
        the program and storing the move in a list of bot move history """
        self.botMove = 'C'
        self.botHistory.append(self.botMove)
        return self.botMove, self.botHistory

    def botDefect(self):
        """ activates if the bot chooses to defect, updating its move for the 
        program and storing it in a list of bot move history """
        self.botMove = 'D'
        self.botHistory.append(self.botMove)
        return self.botMove, self.botHistory

    def randMove(self):
        """ represents the random AI strategy, using the random module to randomly 
        choose between cooperating or defecting """
        move = choice([1,2])
        if move == 1:
            self.botDefect()
        else:
            self.botCoop()

    def titForTat(self):
        """ represents an AI strategy that simply mimics the last move of the player 
        by indexing through a list of their past moves and choosing the 2nd to last 
        index as the AI's move """

        # this handles the edge case at the start of the game where the player has not
        # chosen enough moves for indexing by -2 to work
        if len(self.playerHistory) < 2:
            self.botMove = self.playerHistory[-1]
            self.botHistory.append(self.botMove)
        else:
            self.botMove = self.playerHistory[-2]
            self.botHistory.append(self.botMove)
        return self.botMove, self.botHistory

    def randomTitForTat(self):
        """ creates another AI strategy that, depending on a randomly determined 
        intervalat the start of the game, either mimics the player's last move or 
        chooses a random move """
        if self.randCount % self.randMoves == 0:
            self.randMove()
        else:
            self.titForTat()

        # updates the interval after each turn so that the AI will switch
        # between a random or mimicked move
        self.randCount += 1

    def implementAdaptive(self, avg):
        """ implements specific scoring functions for the adaptive
        AI function that are used in updateScore() """
        if len(avg) < 6:
            avg.append(self.botScore)
        else:
            avg.remove(avg[0])
            avg.append(self.botScore)
                
    def updateScore(self, lastPlayerScore, lastBotScore, lastMove):
        """ updates each player's score based on the last moves made by both the bot and
        the player and displays these updated scores to the main game screen """

        # when both the player and AI choose to cooperate, their score increases
        # by 2 points each
        if self.playerMove == 'C' and self.botMove == 'C':
            self.playerScore += 2
            self.botScore += 2
            self.implementAdaptive(self.cAvg)
                    
        # when the player chooses to defect and the AI chooses to cooperate, 3 points
        # are added to the player's score, but the AI receives 0 points. 
        elif self.playerMove == 'D' and self.botMove == 'C':
            self.playerScore += 3
            self.botScore += 0
            self.implementAdaptive(self.dAvg)
            
        # if the player chooses to cooperate but the AI chooses to defect, the player
        # then receives 0 points while the AI receives 3 points 
        elif self.playerMove == "C" and self.botMove == "D":
            self.playerScore += 0
            self.botScore += 3
            self.implementAdaptive(self.cAvg)

        # if both the player and the bot choose to defect, the player and the bot will each
        # receive 1 points added to their score 
        elif self.playerMove == 'D' and self.botMove == 'D':
            self.playerScore += 1
            self.botScore += 1
            self.implementAdaptive(self.dAvg)

        # undraws all of the previously displayed player and bot scores, as well as the
        # bot's last move so that the new scores and move can be displayed 
        lastPlayerScore.undraw()
        lastBotScore.undraw()
        lastMove.undraw()

        # updates the display with the new player score, bot score, and bot move and assigns
        # them to new variables so they are not immediatley overwritten 
        playerScoreDisp = Text(Point(69,90), str(self.playerScore))
        botScoreDisp = Text(Point(625,90), str(self.botScore))
        display = "Bot's Move: " + str(self.botMove)
        displayText = Text(Point(350,475), display)
        displayText.setSize(15)
        lastPlayerScore = playerScoreDisp
        lastBotScore = botScoreDisp
        lastMove = displayText

        # draws the updated player score, bot score, as well as the bot's last move to
        # the main game screen 
        playerScoreDisp.draw(self.window)
        botScoreDisp.draw(self.window)
        displayText.draw(self.window)

        # adds 1 so that the number of turns that have occured can be counted
        self.round += 1

        return lastPlayerScore, lastBotScore, lastMove

    def playerTurn(self):
        """ registers the player's mouse click, ensuring it is in the right range, and 
        returns which button they have selected as their move choice """
        click1 = self.window.getMouse()

        # initializes error text to display if the player makes an invalid click 
        errorText = Text(Point(350, 500),"Error: Please Click on a Button")
        errorText.setFill("red")
        errorText.setSize(15)

        # checks to make sure the player's click is valid, and if it is not, displays
        # error text and awaits another mouse click from the user 
        while not 100 <= click1.x <= 300 and not 550 <= click1.y <= 650 or not 400 <= click1.x <= 600 and not 550 <= click1.y <= 650:
            errorText.undraw()
            errorText.draw(self.window)
            click1 = self.window.getMouse()

        errorText.undraw()

        # if the player chooses the first, leftmost button, registers the player's move
        # as a cooperation 
        if 100 <= click1.x <= 300 and 550 <= click1.y <= 650:
            self.playerCoop()

        # otherwise, if the player chooses the rightmost button, registers the player's
        # move as a defection 
        elif 400 <= click1.x <= 600 and 550 <= click1.y <= 650:
            self.playerDefect()
            
        self.turn += 1

    def grudges(self):
        """ represents the AI strategy of a grudge, where the AI cooperates until defected on, 
        and then precedes to defect """
        if self.playerHistory[-1] == 'D':
            self.grudge = True
        if self.grudge:
            self.botDefect()
        else:
            self.botCoop()

    def peaceMaker(self):
        """ represents the peacemaker AI strategy that mimics the plays randomly until defected 
        on twice, then defects, and then mimics the player's moves, but will occasionally 
        cooperate instead of defecting """
        defectCount = 0

        # loops through and counts the number of defections made by the player
        for item in self.playerHistory:
            if item == 'D':
                defectCount += 1

        # defects if the player has defected twice 
        if defectCount == 2:
            self.botDefect()

        # if the player has defected twice, the AI either cooperates or mimics the player's
        # last move 
        elif defectCount > 2:
            stratMove = choice([1,2])
            if stratMove == 1:
                self.botCoop()
            else:
                self.titForTat()

        # the AI plays randomly until the player has defected twice 
        else:
            self.randMove()

    def adaptive(self):
        """ functions as an adaptive AI strategy that uses the average score
        from the past six moves, and after registering which one is higher, uses
        that as their move to have the best shot at winning """

        # calculates the averages of both cooperations and defections over the last 6 rounds
        cAvg = sum(self.cAvg)/6
        dAvg = sum(self.dAvg)/6

        # defects for the first three rounds of the game, cooperating the next 3
        if 1 <= self.round <= 3:
            self.botDefect()
        elif 4 <= self.round <= 6:
            self.botCoop()

        # then precedes to calculate the average score benefits of both cooperating and
        # defecting over the last 6 rounds, using that to play the better move 
        elif cAvg > dAvg:
            self.botCoop()
        else:
            self.botDefect()

    def eraseStartScreen(self, a, b, c):
        """ erases the gameboard, scoreboard, and buttons so that the endscreen game
        data can be displayed """
        for o in self.objectList:
            o.undraw()

        for t in self.startText:
            t.undraw()
        
        a.undraw()
        b.undraw()
        c.undraw()

    def keepScore(self, curGame):
        """ registers the players current wins against all the different AI 
        strategies throughout all of their runs in the game """

        # runs if this is after the player's first game, opening the score.txt file
        # and splitting into a list to prepare it to be overwritten
        if curGame >= 1:
            scoreHistory = open("scores.txt")
            scoreHistoryStr = scoreHistory.read()
            scoreHistoryList = scoreHistoryStr.split()

        # if this is the player's first game, then it creates the scoreHistoryList to be
        # written into a new file 
        else: 
            scoreHistoryList= ["Random: ", 0, "Tit-for-Tat: ", 0, "Random-Tit-for-Tat: ", 0, "Grudge: ", 0, "PeaceMaker: ", 0, "Adaptive: ", 0]
            
        # if the player won, adds a point to their wins under the strategy they played against
        if self.playerScore > self.botScore:         
            scoreHistoryList[(self.strategy*2) - 1] = int(scoreHistoryList[(self.strategy*2) - 1]) + 1

        # opens the file and writes the newly updated data of scoreHistoryList to the file
        scoreFile = open("scores.txt", "w")
        for item in scoreHistoryList:
            scoreFile.write(str(item) + " ")
            
        scoreFile.close()
        curGame += 1
        return curGame

    def endScreen(self):
        """ creates and endscreen to play once the randomly determined number of 
        rounds has been reached, displaying both the bot and player history, their
        respective scores, and if the player has either won, tied, or lost """

        # resets the background back to white to display data effectively
        self.window.setBackground("white")
        
        # creates the window for the endgame score screen and converts the lists of
        # move history and respective scores for both the bot and player to strings 
        playerHistoryStr = " ".join(self.playerHistory)
        botHistoryStr = " ".join(self.botHistory)
        playerScoreStr = str(self.playerScore)
        botScoreStr = str(self.botScore)

        # creates text to display at te top of screen and inform the user
        # of the window's purpose 
        self.endingText.append(Text(Point(350, 50), "Endgame Statistics: "))
        self.endingText[0].setFill("aquamarine4")
        self.endingText[0].setSize(25)

        # creates displayable text for the both the player score and move history
        # and the bot score and move history 
        self.endingText.append(Text(Point(350, 100), "Player History:\n\n" + playerHistoryStr))
        self.endingText.append(Text(Point(350, 200), "Bot History:\n\n" + botHistoryStr))
        self.endingText.append(Text(Point(350, 300), "Player Score:\n\n" + playerScoreStr))
        self.endingText.append(Text(Point(350, 400), "Bot Score:\n\n" + botScoreStr))

        # checks if the player either won, tied, or lost by comparing the scores of the bot
        # and player, displaying different text at the bottom of the screen depending on each case
        if self.playerScore > self.botScore:
            self.endingText.append(Text(Point(350, 625), "Congragulations! You Won!\n\nNow Try Against Another Strategy"))
            self.endingText[5].setFill("forest green")
            self.endingText[5].setSize(25)
        elif self.playerScore < self.botScore:
            self.endingText.append(Text(Point(350, 625), "You Lost...\nRematch Against the Same Strategy!"))
            self.endingText[5].setFill("firebrick4")
            self.endingText[5].setSize(25)
        else:
            self.endingText.append(Text(Point(350, 625), "You Tied.\nTry Again to Prove Your Mastery!"))
            self.endingText[5].setFill("cadet blue")
            self.endingText[5].setSize(25)

        # creates a play again or quit button so that the user can either try again against
        # the same or different strategy or quit the game 
        self.endingText.append(Rectangle(Point(75, 375), Point(225, 475)))
        self.endingText[6].setFill("gold2")
        self.endingText.append(Text(Point(150, 425), "Play Again?"))
        self.endingText[7].setSize(25)
        self.endingText.append(Rectangle(Point(475, 375), Point(625, 475)))
        self.endingText[8].setFill("firebrick4")
        self.endingText.append(Text(Point(550, 425), "Quit"))
        self.endingText[9].setSize(25) 

        # opens the scores file and adds it the endgame screen to display their number of wins
        # against various strategies
        scoreFile = open("scores.txt", "r")
        scoreFileStr = scoreFile.read()
        self.endingText.append(Text(Point(350, 520), "Career Average (in wins):\n\n" + scoreFileStr))
        self.endingText[10].setFill("aquamarine4")
        self.endingText[10].setSize(15)
        scoreFile.close()
        
        # draws all the the previously created text and buttons to the endscreen window
        for t in self.endingText:
            t.draw(self.window)

        # waits for a mouse click by the user
        clickFinal = self.window.getMouse()

        # checks if the mouse click is in the range of either button, either playing again
        # or closing the window, or waits until a mouse click is within one of the valid ranges
        again = False
        while again == False: 
            if 75 <= clickFinal.x <= 225 and 375 <= clickFinal.y <= 475:
                again = True
                break
            elif 475 <= clickFinal.x <= 625 and 375 <= clickFinal.y <= 475:
                break
            else: 
                clickFinal = self.window.getMouse() 

        return again
                
def main():
    # runs the class to start the game, printing the instructions to
    # the start screen 
    prisGame = Game()
    prisGame.instructions()
    again = True
    curGame = 0 

    # allows the game to be played until the user decides to stop by clicking
    # a button in the endscreen 
    while again == True:
        
        # allows the user to choose their specific AI strategy to play against
        prisGame.buttons()
        x = prisGame.playerChoice()

        # erases the objects created for the selection screen and creates the main
        # game screen with the gameboard, buttons, and player and bot scores 
        prisGame.buttonsErase()
        prisGame.startScreen()

        # intializes variables for the while loop that run for the entirety of the game
        curTurn = 0
        a = Text(Point(69,75), "")
        b = Text(Point(594,75), "")
        c = Text(Point(350,475), "")

        # loop that runs turns of the game until the randomly determined number of
        # runs has been reached 
        while curTurn <= prisGame.runs:
            prisGame.playerTurn()

            # operates if the player chose the random AI strategy
            if x == 1:
                prisGame.randMove()
                prisGame.strat = "rand"

            # operates if the player chose the Tit-for-Tat AI strategy
            elif x == 2:
                prisGame.titForTat()
                prisGame.strat = "titForTat"

            # operates if the player chose the random Tit-for-Tat AI strategy
            elif x == 3:
                prisGame.randomTitForTat()
                prisGame.strat = "randomTitForTat"

            # operates if the player chose the Grudge AI strategy
            elif x == 4:
                prisGame.grudges()
                prisGame.start = "grudges"

            # operates if the player chose the PeaceMaker AI strategy 
            elif x == 5:
                prisGame.peaceMaker()
                prisGame.strat = "peaceMaker"

            # operates if the player chose the Adaptive AI Strategy
            elif x == 6:
                prisGame.adaptive()
                prisGame.strat = "adaptive"

            # passes the player's score, bot's score, and bot's move as parameters
            # in main so that they can be overwritten in the updateScore() function
            a, b, c = prisGame.updateScore(a, b, c)
            curTurn += 1

        # runs keepScore() to track the player's wins against various AI strategies
        # while also erasing the startScreen and running the endscreen data
        curGame = prisGame.keepScore(curGame)
        prisGame.eraseStartScreen(a, b, c)
        y = prisGame.endScreen()

        # if they clicked the continue button, closes this window of the game and runs
        # a new instance of the class so they can play another game
        if y:
             prisGame.window.close()
             prisGame = Game()
             again = True

        # otherwise, if they chose to quit, the game simply closes the window and ceases action
        else:
            break
        
    prisGame.window.close()

if __name__ == '__main__':
    main()
