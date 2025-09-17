import random


dice_art = {
    1 :"⚀",
    2 :"⚁",
    3 :"⚂",
    4 :"⚃",
    5 :"⚄",
    6 :"⚅",
}

user_input = int(input("BEAT THE COMPUTER \nENTER HOW MANY DICE YOU WANT TO ROLL :"))
computer_total = 0
user_total = 0

# print(dice[user_input])

def roll_dice():

    global dice_art ,user_input ,user_total

    dice = []
    
    
    for die in range(user_input):

        random_dice = random.randint(1 ,6)
        dice.append(random_dice)
        print(dice_art[random_dice])

    user_total += sum(dice)
    return user_total 



def computer_roll():
    global user_input ,computer_total

    dice = []

    for die in range(user_input):

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

