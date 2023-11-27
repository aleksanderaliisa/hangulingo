
from new_game import new_game
from resume import resume
from verbs import add_verb


option = int(input("Enter 1 to start a game\n 2 to resume a game\n 3 to add a verb\n"))

if option==1:
     new_game()
    
elif option ==2:
    resume()
        
elif option ==3:
    add_verb()
        
else:
    print("please enter a valid option")


