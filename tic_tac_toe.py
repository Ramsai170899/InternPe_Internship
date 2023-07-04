import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self):
        self.current_player = "X"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = [[None, None, None] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text=" ",
                    font=("Helvetica", 20),
                    width=6,
                    height=3,
                    command=lambda r=row, c=col: self.handle_move(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

        self.status_label = tk.Label(
            self.root,
            text=f"Current Player: {self.current_player}",
            font=("Helvetica", 14),
            fg="black"
        )
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

    def handle_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                self.show_message(f"Player {winner} wins!")
                self.status_label.config(
                    text=f"Player {winner} wins!", fg="green")
                self.reset_game()
            elif self.is_board_full():
                self.show_message("It's a tie!")
                self.status_label.config(text="It's a tie!", fg="green")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(
                    text=f"Current Player: {self.current_player}")

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        # No winner yet
        return None

    def is_board_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

        self.status_label.config(
            text=f"Current Player: {self.current_player}", fg="black")

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)

    def start(self):
        self.root.mainloop()


# Start the game
game = TicTacToeGUI()
game.start()
