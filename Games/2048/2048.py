
import tkinter as tk
import random
import colors as c


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048')

        self.__main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.__main_grid.grid(pady=(100, 0))

        self.__make_GUI()
        self.__start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    def __make_GUI(self):
        # make grid
        self.__cells = []
        for i in range(16):
            row = []
            for j in range(16):
                cell_frame = tk.Frame(
                    self.__main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=100,
                    height=100)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.__main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.__cells.append(row)

        # make score header
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=40, anchor="center")
        tk.Label(
            score_frame,
            text="Score",
            font=c.SCORE_LABEL_FONT).grid(row=0)

        self.__score_label = tk.Label(score_frame, text="0", font=c.SCORE_FONT)
        self.__score_label.grid(row=1)

    def __start_game(self):
        # create matrix of zeroes
        self.__matrix = [[0] * 16 for _ in range(16)]

        # fill 2 random cells with 2s
        row = random.randint(0, 15)
        col = random.randint(0, 15)

        self.__matrix[row][col] = 2
        self.__cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.__cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text="2"
        )

        while(self.__matrix[row][col] != 0):
            row = random.randint(0, 15)
            col = random.randint(0, 15)

        self.__matrix[row][col] = 2
        self.__cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.__cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text="2"
        )

        self.score = 0

    # Matrix Manipulation Functions
    def __stack(self):
        new_matrix = [[0] * 16 for _ in range(16)]
        for i in range(16):
            fill_position = 0
            for j in range(16):
                if self.__matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.__matrix[i][j]
                    fill_position += 1
        self.__matrix = new_matrix

    def __combine(self):
        for i in range(16):
            for j in range(15):
                if (self.__matrix[i][j] != 0 and
                        self.__matrix[i][j] == self.__matrix[i][j + 1]):
                    self.__matrix[i][j] *= 2
                    self.__matrix[i][j + 1] = 0
                    self.score += self.__matrix[i][j]

    def __reverse(self):
        new_matrix = []
        for i in range(16):
            new_matrix.append([])
            for j in range(16):
                new_matrix[i].append(self.__matrix[i][15 - j])
        self.__matrix = new_matrix

    def __transpose(self):
        new_matrix = [[0] * 16 for _ in range(16)]
        for i in range(16):
            for j in range(16):
                new_matrix[i][j] = self.__matrix[j][i]
        self.__matrix = new_matrix

    # Add a new 2 or 4 tile randomly to an empty cell
    def __add_new_tile(self):
        row = random.randint(0, 15)
        col = random.randint(0, 15)
        while(self.__matrix[row][col] != 0):
            row = random.randint(0, 15)
            col = random.randint(0, 15)
        self.__matrix[row][col] = random.choice([2, 4])

    # Update the GUI to match the matrix
    def __update_GUI(self):
        for i in range(16):
            for j in range(16):
                cell_value = self.__matrix[i][j]
                if cell_value == 0:
                    self.__cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.__cells[i][j]["number"].configure(
                        bg=c.EMPTY_CELL_COLOR, text="")
                else:
                    self.__cells[i][j]["frame"].configure(
                        bg=c.CELL_COLORS[cell_value])

                    self.__cells[i][j]["number"].configure(
                        bg=c.CELL_COLORS[cell_value],
                        fg=c.CELL_NUMBER_COLORS[cell_value],
                        font=c.CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value))
        self.__score_label.configure(text=self.score)
        self.update_idletasks()

    # Arrow-Press Functions
    def left(self, event):
        self.__stack()
        self.__combine()
        self.__stack()
        self.__add_new_tile()
        self.__update_GUI()
        self.__game_over()

    def right(self, event):
        self.__reverse()
        self.__stack()
        self.__combine()
        self.__stack()
        self.__reverse()
        self.__add_new_tile()
        self.__update_GUI()
        self.__game_over()

    def up(self, event):
        self.__transpose()
        self.__stack()
        self.__combine()
        self.__stack()
        self.__transpose()
        self.__add_new_tile()
        self.__update_GUI()
        self.__game_over()

    def down(self, event):
        self.__transpose()
        self.__reverse()
        self.__stack()
        self.__combine()
        self.__stack()
        self.__reverse()
        self.__transpose()
        self.__add_new_tile()
        self.__update_GUI()
        self.__game_over()

    # Check if any moves are possible
    def __horizontal_move_exists(self):
        for i in range(16):
            for j in range(15):
                if self.__matrix[i][j] == self.__matrix[i][j + 1]:
                    return True
        return False

    def __vertical_move_exists(self):
        for i in range(15):
            for j in range(16):
                if self.__matrix[i][j] == self.__matrix[i + 1][j]:
                    return True
        return False

    # Check if Game is Over (Win/Lose)
    def __game_over(self):
        if any(2048 in row for row in self.__matrix):
            game_over_frame = tk.Frame(self.__main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="You win!",
                bg=c.WINNER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT).pack()
        elif (not any(0 in row for row in self.__matrix) and
                not self.__horizontal_move_exists() and
                not self.__vertical_move_exists()):
            game_over_frame = tk.Frame(self.__main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="Game over!",
                bg=c.LOSER_BG,
                fg=c.GAME_OVER_FONT_COLOR,
                font=c.GAME_OVER_FONT).pack()

    def run(self):
        try:
            Game()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")



if __name__ == "__main__":
    game_2048 = Game()
    game_2048.run()




# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
"""
If you want to change the size of the game, you will need to modify several parts of the code. Here are the steps to follow to change the size of the game:

    In the `__init__` method, change the `width` and `height` of `self.__main_grid` to match the desired size of the game.

    In the `__make_GUI` method, change the range of the for loops that create the grid to match the desired size of the game.

    In the `__start_game` method, change the size of `self.__matrix` to match the desired size of the game.
        Also, change the range of the random integers for `row` and `col` to match the desired size of the game.

    In all methods that manipulate the matrix (`__stack`, `__combine`, `__reverse`, and `__transpose`),
        change the range of the for loops to match the desired size of the game.

    In all methods that check for moves (`__horizontal_move_exists` and `__vertical_move_exists`),
        change the range of the for loops to match the desired size of the game.

    
    *!* For example, if you want to change the size of the game from 16x16 to 8x8, you can make these changes:

    In the __init__ method, change width=400, height=400 to width=200, height=200.
    In the __make_GUI method, change both ranges in for i in range(16): and for j in range(16): to range(8).
    In the __start_game method, change self.__matrix = [[0] * 16 for _ in range(16)] to self.__matrix = [[0] * 8 for _ in range(8)].
        Also, change both ranges in row = random.randint(0, 15) and col = random.randint(0, 15) to (0, 7).
    In all methods that manipulate the matrix (__stack, __combine, __reverse, and __transpose), change all ranges from (16) to (8).
    In all methods that check for moves (__horizontal_move_exists and __vertical_move_exists), change all ranges from (15) or (16) to (7).
"""