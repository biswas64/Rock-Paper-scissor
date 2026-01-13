import data   #contains functions -> add data, show data, create table, delete table
import random

def computer_choice():
    return random.choice(choices)

def  user_choice():
    while True:
        try:
            print("""
                    Enter ->
                        1.for Rock 
                        2. for paper 
                        3. for Scissors
                  """)
            userInput = int(input("Enter your choice(1 - 3): "))
            if userInput > len(choices) or userInput  <= 0:
                print("<------------------>")
                print(f"invalid input")
                print("<------------------>")
            else:
                userChoice = choices[userInput-1]
                return userChoice
        except ValueError:
            print("<------------------>")
            print(f"invalid input")
            print("<------------------>")



def determine_round_winner(userChoice,computerChoice,wins):

    if userChoice == computerChoice:
        return "Draw"

    elif wins[userChoice] == computerChoice:
        return "Player"
    
    else:
        return "Computer"

    
def determine_game_winner(overallStats):
    if overallStats["roundWins"] > overallStats["roundLoss"]:
        return "Player"
    elif overallStats["roundWins"] < overallStats["roundLoss"]:
        return "Computer"
    else:
        return "Draw"
        




def play_game():
    overallStats = {"roundWins":0,"roundLoss":0,"roundDraws":0}
    gameStats = {"Wins":0,"Loss":0,"Draw":0,"gamesPlayed":0}

    wins = {
            "Rock":"Scissors",
            "Paper":"Rock",
            "Scissors":"Paper"
            }
    
    while True:

        rounds = 1
        totalRounds = 3
        while rounds <= totalRounds:
            userChoice = user_choice()
            computerChoice =  computer_choice()
            result = determine_round_winner(userChoice,computerChoice,wins)

            if  result == "Player":
                overallStats["roundWins"]+=1
                print_round_result(result,userChoice,computerChoice,rounds,totalRounds)

            elif  result=="Computer" :
                overallStats["roundLoss"]+=1
                print_round_result(result,userChoice,computerChoice,rounds,totalRounds)

                
            elif  result=="Draw" :
                 overallStats["roundDraws"]+=1
                 print_round_result(result,userChoice,computerChoice,rounds,totalRounds)
            
            rounds += 1

        result = determine_game_winner(overallStats)
        if  result == "Player":
            gameStats["Wins"]+=1

        elif  result=="Computer" :
            gameStats["Loss"]+=1     


        elif  result=="Draw" :
            gameStats["Draw"]+=1

        gameStats["gamesPlayed"] +=1
        update_database(gameStats)
        print_game_result(result,overallStats)

        while True:
            playAgain=input("Do you wanna play again(Y/N):").lower()
            if playAgain == "n":
                deleteRow=input("Do you wanna delete data(Y/N):").lower()
                if deleteRow =="y":
                    delete_from_database()
                return print("Have a good day!!")
            elif playAgain =="y":
                overallStats['roundDraws']=0
                overallStats['roundLoss']=0
                overallStats['roundWins'] =0
                break
            else:
                print("invalid input")

def update_database(gameStats):
    Wins = gameStats["Wins"]
    Loss = gameStats["Loss"]
    gamesPlayed = gameStats["gamesPlayed"]
  
    Draw = gameStats["Draw"]
    try:
        data.update_data(gamesPlayed,Wins,Loss,Draw)
    except Exception as e:
        print(f"error: {e}")

def delete_from_database():
    data.show_data()
    userInput = input("Enter the player id you want to delete: ")
    data.delete_data(userInput)
    data.show_data()


def print_round_result(result,userChoice,computerChoice,rounds,totalRounds):
    if result != "Draw":
        print("<------------------------>")
        print(f"Rounds: {rounds} / {totalRounds} ")
        print(f"You chose: {userChoice}")
        print(f"Computer chose: {computerChoice}")
        print(f"{result} won the round")
        print("<------------------------>")
    else:
        print("<---------------------->")
        print(f"Rounds: {rounds} / {totalRounds} ")
        print(f"You chose: {userChoice}")
        print(f"Computer chose: {computerChoice}")
        print(f"{result}")
        print("<----------------------->")


def print_game_result(result,overallStats):
    if result != "Draw":
        print("<------------------------>")
        print(f"Wins: {overallStats["roundWins"]} rounds")
        print(f"Loss: {overallStats["roundLoss"]} rounds")
        print(f"Draws: {overallStats["roundDraws"]} rounds")
        print(f"{result} won the Game")
        print("<------------------------>")
        data.show_data() #returns overall data in tabular form using pandas
    else:
        print("<---------------------------->")
        print(f"Wins: {overallStats["roundWins"]} rounds")
        print(f"Loss: {overallStats["roundLoss"]} rounds")
        print(f"Draws: {overallStats["roundDraws"]} rounds")
        print(f"<-- Game ended in a Draw -->")
        print("<---------------------------->")
        data.show_data() #returns overall data in tabular form using pandas



if __name__ =="__main__":
    choices= ["Rock","Paper","Scissors"]
    Name = input("Enter your name: ")
    initial = { "gamesPlayed" : 0,"Wins" : 0,"Loss" : 0,"Draw" :0}
    data.add_data(Name, initial["gamesPlayed"],initial["Wins"], initial["Loss"],initial["Draw"])
    play_game()
