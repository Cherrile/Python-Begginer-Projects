import random
min_val = 1
max_val = 6
roll_again = "yes"
#to loop rolling thro user input

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are :")
   
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    
    #any other inpput b user other than yes or y will terminate game
    roll_again = input("Roll the Dices Again?")

