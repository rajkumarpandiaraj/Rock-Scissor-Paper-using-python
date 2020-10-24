import random
def startGame() :
    computerChoice = getComputerChoice()
    userChoice = input('Enter your Choice : ')
    winner = checkForWinner(userChoice, computerChoice)
    if not winner :
        print('InValid valid selection')
        return 'n'
    else :
        print('Computer Choice is', computerChoice)
        if winner == 'computer' :
            print('Oops,You lose')
        elif winner == 'user' :
            print('Congrats,You Won')
        else :
            print("It's Draw")
        print('Your Score is :', userScore)
        print('Computer Score is :', computerScore)
        return input('Do you want to continue ? (Y/N) : ')



def getComputerChoice() :
    randomNum = random.random()

    if randomNum < 0.3 :
        return 'R'
    elif randomNum < 0.6 :
        return 'P'
    else :
        return 'S'

def checkForWinner(user, computer) :
    global userScore
    global computerScore
    if user.upper() == computer :
        return 'Draw'
    if user.upper() == 'R' :
        if computer == 'P' :
            computerScore +=1
            return 'computer'
        else :
            userScore +=1
            return 'user'
    elif user.upper() == 'P' :
        if computer == 'S' :
            computerScore +=1
            return 'computer'
        else : 
            userScore +=1
            return 'user'
    elif user.upper() == 'S' :
        if computer == 'R' :
            computerScore +=1
            return 'computer'
        else : 
            userScore +=1
            return 'user'
    else :
        return ''


print('R/r -> Rock')
print('P/p -> Paper')
print('S/s -> Scissor')
print('Press S to start the Game')
isGameStarted = input()
userScore = 0
computerScore = 0
if isGameStarted.upper() == 'S' :
    for i in range(0, 1000) :
        wantToContinue = startGame()
        if wantToContinue.upper() == 'N' :
            print('Thanks for playing')
            break 
else :
    print('Thank you')

