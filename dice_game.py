import random

dice_art = {

    1 :"⚀",
    2 :"⚁",
    3 :"⚂",
    4 :"⚃",
    5 :"⚄",
    6 :"⚅",
}

computer_total = 0
user_total = 0

while True:
    try:
        user_input = input("BEAT THE COMPUTER \nENTER HOW MANY DICE YOU WANT TO ROLL: ")
        
        if user_input == "":  # If left blank
            user_input = 6
            break
        
        user_input = int(user_input)  # Try converting input to integer
        if user_input <= 0:
            print("Please enter a positive number.")
            continue
        
        break  # Exit loop if input is valid
    
    except ValueError:
        print("That's not a number. Please enter a valid number")
        
# print(dice[user_input])

def roll_dice():

    global dice_art ,user_input ,user_total

    dice = []
    
    
    for die in range(int(user_input)):

        random_dice = random.randint(1 ,6)
        dice.append(random_dice)
        print(dice_art[random_dice])

    user_total += sum(dice)
    return user_total 



def computer_roll():
    global user_input ,computer_total

    dice = []

    for die in range(int(user_input)):

        random_dice = random.randint(1 ,6)
        dice.append(random_dice)
        # print(dice_art[random_dice])

    computer_total += sum(dice)
    return computer_total

def check_win():
    global user_total ,computer_total
    roll_dice() 
    computer_roll()
    if user_total > computer_total:
        print(f"You won !Your points {user_total} computer points {computer_total}")
    else:
        print(f"Computer won !Your points {user_total} computer points {computer_total}")

        

check_win()

