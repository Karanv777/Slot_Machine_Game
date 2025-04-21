# 🎰 Slot Machine Game – Python CLI

A simple, text-based **slot machine game** built with Python. Deposit funds, place your bets on 1 to 3 lines, and spin the virtual slot reels to test your luck!

---

## 🚀 Features

- 🎲 Randomized slot symbols (A, B, C, D)
- 💰 Custom deposit and betting system
- ✅ Validates inputs and prevents over-betting
- 🎉 Win based on matching symbols on selected lines
- 📉 Tracks balance after each round

---

## 📁 File Structure

```
SlotMachineGame/
└── main.py           # Contains the full slot machine game logic
```

---

## 📦 Requirements

- Python 3.6+

> No third-party packages are needed — it's fully standalone!

---

## 🕹️ How to Play

1. **Clone this repository**
```bash
git clone https://github.com/Karanv777/Slot_Machine_Game.git
cd Slot_Machine_Game
```

2. **Run the game**
```bash
python main.py
```

3. **Follow the prompts**:
   - Enter an initial deposit amount.
   - Choose how many lines to bet on (1-3).
   - Enter the bet amount per line.
   - Spin the slot machine and see if you win!

---

## 🧠 Game Mechanics

- **Symbols**: A, B, C, D
- **Symbol Frequency**:  
  - A: 2  
  - B: 5  
  - C: 8  
  - D: 10

- **Payout Multipliers**:
  - A: 2x
  - B: 1.5x
  - C: 1.25x
  - D: 1x

- **Win Condition**: All 3 columns in a line (horizontal) must match the same symbol.

---

## 🖥️ Sample Gameplay

```
Enter amount to deposit : ₹1000
Enter number of lines you want to bet on (1 - 3): 2
Enter amount to Bet on each line: ₹100

You are betting ₹100 on 2 lines.
Total Bet is ₹200.
Remaining Balance is ₹800

A | C | A
B | C | B
D | B | D

You Won ₹100.0.
You Won on lines: 1

Current Balance : ₹900
```

---

## 🔮 Future Improvements

- GUI version using Tkinter or PyGame
- Save & load player profiles
- Leaderboard or scoring system
- Sound effects for win/loss

---


## 👨‍💻 Author

Made with ❤️ by [Karanv777](https://github.com/Karanv777)
```

---
