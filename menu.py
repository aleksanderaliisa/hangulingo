
from game import game
from verbs import add_verb


option = int(input("Enter 1 to start a game\n 2 to resume a game\n 3 to add a verb\n"))

if option==1:
    pseudo = input("enter your pseudo")
    score = 0  
    game(pseudo, 0)
    
elif option ==2:
    pseudo = input("enter your pseudo")
    score_file = open("scores.txt","r")
    #search score in the file
    game(pseudo, score)

        
elif option ==3:
    add_verb()
        
else:
    print("please enter a valid option")


