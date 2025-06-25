import tkinter as tk
from tkinter import messagebox
import random

PLAYER = 'O'
AI = 'X'
board = [[' ']*3 for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
difficulty = 3
current_turn = PLAYER
status_label = None

# Game Logic
def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True, [(board.index(row), i) for i in range(3)]
    for col_idx in range(3):
        col = [board[row][col_idx] for row in range(3)]
        if all(cell == player for cell in col):
            return True, [(i, col_idx) for i in range(3)]
    if all(board[i][i] == player for i in range(3)):
        return True, [(i, i) for i in range(3)]
    if all(board[i][2 - i] == player for i in range(3)):
        return True, [(i, 2 - i) for i in range(3)]
    return False, []

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def heuristic(board):
    score = 0
    lines = [
        [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
    ]
    for line in lines:
        x_count = o_count = empty = 0
        for i, j in line:
            if board[i][j] == AI: x_count += 1
            elif board[i][j] == PLAYER: o_count += 1
            else: empty += 1
        if x_count == 2 and empty == 1: score += 10
        elif o_count == 2 and empty == 1: score -= 10
        elif x_count == 1 and empty == 2: score += 1
        elif o_count == 1 and empty == 2: score -= 1
    return score

def minimax(board, depth, is_max, alpha, beta):
    if is_winner(board, PLAYER)[0]: return -100
    if is_winner(board, AI)[0]: return 100
    if is_full(board) or depth == 0: return heuristic(board)

    if is_max:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    score = minimax(board, depth-1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, score)
                    alpha = max(alpha, score)
                    if beta <= alpha: break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    score = minimax(board, depth-1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, score)
                    beta = min(beta, score)
                    if beta <= alpha: break
        return min_eval

def best_move():
    if difficulty == 1:
        return random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(board, difficulty, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# UI Functions
def handle_click(i, j):
    global current_turn
    if board[i][j] != ' ' or current_turn != PLAYER:
        return
    board[i][j] = PLAYER
    buttons[i][j].config(text=PLAYER, state='disabled', disabledforeground='#00cec9', bg='#193441')
    current_turn = AI
    update_status("AI's turn")
    won, line = is_winner(board, PLAYER)
    if won: 
        return end_game("You win!", line)
    if is_full(board): 
        return end_game("It's a tie!", [])
    root.after(400, ai_turn)

def ai_turn():
    global current_turn
    move = best_move()
    if move:
        i, j = move
        board[i][j] = AI
        buttons[i][j].config(text=AI, state='disabled', disabledforeground='#ff6b6b', bg='#4a2f30')
    current_turn = PLAYER
    update_status("Your turn")
    won, line = is_winner(board, AI)
    if won: 
        return end_game("AI wins!", line)
    if is_full(board): 
        return end_game("It's a tie!", [])

def end_game(message, win_line):
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state='disabled')
    for i, j in win_line:
        buttons[i][j].config(bg='#32cd32')
    update_status(message)
    messagebox.showinfo("Game Over", message)
    replay_button.config(state='normal')  # Enable Play Again button after game ends

def reset_game():
    global board, current_turn
    board = [[' ']*3 for _ in range(3)]
    current_turn = PLAYER
    update_status("Your turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state='normal', bg='#4a90e2')
    replay_button.config(state='disabled')  # Disable Play Again during active game

def update_status(msg):
    status_label.config(text=msg)

def set_difficulty(value):
    global difficulty
    difficulty = {'Easy': 1, 'Medium': 3, 'Hard': 5}[value]
    reset_game()

# GUI Setup
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg='#1e2a38')

header = tk.Label(root, text="Tic-Tac-Toe", font=('Segoe UI', 32, 'bold'), bg='#1e2a38', fg='#f0f0f0')
header.pack(pady=10)

difficulty_menu = tk.StringVar(root)
difficulty_menu.set("Medium")
dropdown = tk.OptionMenu(root, difficulty_menu, "Easy", "Medium", "Hard", command=set_difficulty)
dropdown.config(font=('Segoe UI', 12), bg='#223447', fg='#f0f0f0', width=10, activebackground='#3a5068', highlightthickness=0)
dropdown["menu"].config(bg='#223447', fg='#f0f0f0')
dropdown.pack(pady=5)

status_label = tk.Label(root, text="Your turn", font=('Segoe UI', 14), bg='#1e2a38', fg='#f0f0f0')
status_label.pack(pady=5)

frame = tk.Frame(root, bg='#1e2a38')
frame.pack()

for i in range(3):
    for j in range(3):
        btn = tk.Button(
            frame, text=' ', font=('Segoe UI', 28, 'bold'), width=5, height=2,
            bg='#4a90e2', activebackground='#6ea8fe',
            command=lambda i=i, j=j: handle_click(i, j),
            relief='raised', bd=3
        )
        btn.grid(row=i, column=j, padx=8, pady=8)
        buttons[i][j] = btn

button_frame = tk.Frame(root, bg='#1e2a38')
replay_button = tk.Button(button_frame, text="Play Again", font=('Segoe UI', 14), bg='#27ae60', fg='white', activebackground='#2ecc71', command=reset_game)
reset_button = tk.Button(button_frame, text="Reset Game", font=('Segoe UI', 14), bg='#e67e22', fg='white', activebackground='#d35400', command=reset_game)
replay_button.pack(side='left', padx=10, pady=10)
reset_button.pack(side='left', padx=10, pady=10)
button_frame.pack(pady=5)

# Disable Play Again at start
replay_button.config(state='disabled')

root.mainloop()
