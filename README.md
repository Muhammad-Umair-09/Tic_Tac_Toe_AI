# 🧠 Tic-Tac-Toe AI Challenge

A visually engaging and competitive **Tic-Tac-Toe** game where you challenge an AI opponent. Built using Python and Tkinter, this project showcases a minimax-based AI that scales across difficulty levels — from beginner-friendly to brain-bending.

## 🎮 Gameplay Overview

You play as **O**, the AI plays as **X**. Take turns on the grid to try to win or block your opponent. The game ends when someone wins or all cells are filled. 

Features include:
- ✅ Three difficulty levels: Easy, Medium, Hard
- ✅ AI using Minimax with Alpha-Beta Pruning
- ✅ Responsive GUI with move highlighting
- ✅ Reset and Play Again options
- ✅ Win detection with visual feedback

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** for GUI
- **Minimax Algorithm** with **Alpha-Beta Pruning**

## 📸 Screenshots

![Screenshot](capture.png)



## 🧠 AI Strategy

- **Easy**: Random moves.
- **Medium**: Shallow minimax tree search (depth = 2).
- **Hard**: Deep minimax tree with alpha-beta pruning (depth = 5).
- **Heuristic Function**: Scores board positions based on potential wins/losses.

## 📂 Project Structure

```
tic-tac-toe-ai/
├── tic_tac_toe.py     # Main GUI and AI logic
├── README.md          # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3 installed
- No external libraries needed

### Running the Game

```bash
python tic_tac_toe.py
```

1. Select a difficulty from the dropdown.
2. Play by clicking any empty cell.
3. View result and choose "Play Again" or "Reset Game".


Enjoy outsmarting the AI!
