
from game import game
from verbs import add_verb


option = int(
    input("Enter 1 to start a game\n 2 to resume a game\n 3 to add a verb\n"))

if option == 1:
    pseudo = input("enter your pseudo")
    score = 0
    game(pseudo, 0)

elif option == 2:
    pseudo = input("enter your pseudo")
    score_file = open("scores.txt", "r")

    # search score in the file
    lines = score_file.readlines()
   
    for line in lines:
        line = line.rstrip()
        str = line.split(" ")
        if (str[0] == pseudo):
            found = True
            game(pseudo, str[1])
            break
    else:
            print("No player with this pseudonyme")
    
        


elif option == 3:
    add_verb()

else:
    print("please enter a valid option")
