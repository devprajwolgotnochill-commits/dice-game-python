# 🎲 Beat the Computer - Dice Game  

A simple Python command-line dice game where you compete against the computer. You roll a set number of dice, and whoever has the higher total wins!  

---

## 📌 Features  
- Roll as many dice as you choose.  
- Each dice roll is displayed with Unicode dice faces ⚀ ⚁ ⚂ ⚃ ⚄ ⚅.  
- The computer rolls the same number of dice.  
- The winner is decided based on the total points.  

---

## 🚀 How to Play  
1. Run the script in a terminal:  
   ```bash
   python dice_game.py
   ```
2. Enter the number of dice you want to roll when prompted.  
   ```
   BEAT THE COMPUTER 
   ENTER HOW MANY DICE YOU WANT TO ROLL : 3
   ```
3. Watch your dice rolls and compare with the computer’s.  

Example output:  
```
⚁
⚄
⚃
You won! Your points 12, computer points 10
```

---

## 🛠 Code Structure  
- **`roll_dice()`** → Handles the player’s dice rolls and displays them.  
- **`computer_roll()`** → Handles the computer’s dice rolls (hidden).  
- **`check_win()`** → Compares totals and declares the winner.  

---

## 📂 File Structure  
```
dice_game/
│── dice_game.py   # Main game script
│── README.md      # Project description
```

---

## ✅ Requirements  
- Python 3.x  
- No external libraries (only built-in `random`)  

---

## 🎯 Future Improvements  
- Add multiple rounds (best of 3, best of 5).  
- Display computer’s dice faces.  
- Add score history tracking.  
- Option to play again without restarting.  
