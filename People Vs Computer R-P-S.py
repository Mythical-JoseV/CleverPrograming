#####R-P-S
##Jose Vest
#####2.7.2019

#Loop Start
while True:

#This is for random number values of each rock, paper, or scissor
    import random

#This is the input of the player and the outcomes
    Player1 = input("Hello Player call your outcome; Rock, Paper, Scissors.")
    
    Player2 = random.randint(1, 3)

    if Player1.lower() == "rock":
      Player1 = 1

    elif Player1.lower() == "paper":
      Player1 = 2

    elif Player1.lower() == "scissors":
      Player1 = 3

  
#Outcome Start
    if Player1 == 1  and Player2 == 1 :
      print ("Draw try agian!")
      

    if Player1 == 2 and Player2 == 1:
      print("Player 1 wins")
      

    if Player1 == 3 and Player2 == 1:
      print("Computer wins!")
      

    if Player1 == 2 and Player2 == 2:
      print("Draw try again!")
      

    if Player1 == 2 and Player2 == 3:
      print("Computer wins")

    if Player1 == 3 and Player2 == 3:
      print("Draw try again")

    if Player1 == 1 and Player2 == 2:
      print ("Computer wins")

    if Player1 == 1 and Player2 == 3:
      print ("Player 1 wins")

    if Player1 == 3 and Player2 == 2:
      print("Player 1 wins")    
    
    Cont = input("Do you want to try again?")
         
    if Cont.lower() == 'no':
      break
    
    if Cont.lower() == 'yes':
      print("Great!")
