import random
import time
import os

#found at https://www.delftstack.com/howto/python/python-clear-console/
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

def main(): 
    #local variables, I probably should have used appendages but this is when I started to learn coding, list.append()
    grade = ["", "", "", "", "", "", "", "", "", ""]
    nums = [0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0]
    userAnswers = [0, 0, 0, 0, 0,
    0, 0, 0, 0, 0]
    userScore = 0
    leaderboard = []
    startPoints = [2, 12, 22] #Gives the starting points of the different skill levels for the numbers to be used
    endPoints = [10, 40, 70] #Gives the ending points of the different skill levels for the numbers to be used
    opp = [0, 0, 0, 0] #Opponents scores

    time.sleep(1)
    print("Welcome to Math Competition vs Bots!") #Welcoming statement and inputs to be used.
    noresponse = input("Press Enter to continue... ")
    print("The objective of the game is to do multiplication math.\nWhile you attempt your math problems, you will be facing opponents.\nReady!")
    time.sleep(7)
    clearConsole()
    print("Loading game...")
    clearConsole()
    skillLevel = input("Which math level are you?\nThe level you are determines the numbers multiplied together\nA) Beginner\nB) Intermediate\nC) Expert\nD) Choose your own numbers to multiply\nYour choice: ")
    clearConsole()
    st = 0
    end = 0
    # Grabbing the statement for skill level then using for loops to create the questions and answer banks into a list which will be used to determine if the user is correct.
    if (skillLevel.lower() == "a"):
        st  = startPoints[0]
        end = endPoints[0]
        userScore = 0
        isReady = input("Type go to start ")
        if (isReady.lower() == "go"):
            start_time = time.time()
            for i in range(20):
                nums[i] = random.randint(st, end)
            for z in range(10):
                userAnswers[z] = int(input(str(nums[z]) + " * " + str(nums[19-z]) +" "))
                if (userAnswers[z] == (nums[z] * nums[19-z])):
                    userScore += 1
                    grade[z] = "Question " + str(z + 1) + ": Correct"
                else: 
                    grade[z] = "Question " + str(z + 1) + ": Incorrect"
        end_time = time.time()
    if (skillLevel.lower() == "b"):
        st  = startPoints[1]
        end = endPoints[1]
        userScore = 0
        isReady = input("Type go to start ")
        if (isReady.lower() == "go"):
            start_time = time.time()
            for i in range(20):
                nums[i] = random.randint(st, end)
            for z in range(10):
                userAnswers[z] = int(input(str(nums[z]) + " * " + str(nums[19-z]) +" "))
                if (userAnswers[z] == (nums[z] * nums[19-z])):
                    userScore += 1
                    grade[z] = "Question " + str(z + 1) + ": Correct"
                else: 
                    grade[z] = "Question " + str(z + 1) + ": Incorrect"
            end_time = time.time()

    if (skillLevel.lower() == "c"):
        st  = startPoints[2]
        end = endPoints[2]
        userScore = 0
        isReady = input("Type go to start ")
        if (isReady.lower() == "go"):
            start_time = time.time()
            for i in range(20):
                nums[i] = random.randint(st, end)
            for z in range(10):
                userAnswers[z] = int(input(str(nums[z]) + " * " + str(nums[19-z]) +" = "))
                if (userAnswers[z] == (nums[z] * nums[19-z])):
                    userScore += 1
                    grade[z] = "Question " + str(z + 1) + ": Correct"
                else: 
                    grade[z] = "Question " + str(z + 1) + ": Incorrect"
            end_time = time.time()
    for p in range (0, 3):
        opp[p] = random.randint(0, 8)
    totalTime = round(end_time - start_time)
    addScore = totalTime / 4
    userScore -= addScore
    leaderboard.append("Your Score: " + str(userScore))
    for u in range (0, 3): 
        leaderboard.append("Opponent " + str(u+1) + "  score: " + str(opp[u]))
    for y in range (10):
        print(grade[y])
    print(leaderboard)
    # Printing the leaderboard.
    print("Your Score Was: " + str(userScore))
    print("Time: " + str(totalTime))
main()
