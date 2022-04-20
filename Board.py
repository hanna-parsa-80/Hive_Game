from Player import Player
from Piece import Piece
from Bee import Bee


class Cell:
    def __init__(self):
        self.bug = None


class Board:
    def __init__(self, rows, columns):
        self.ground = []
        self.full_positions_map = {}  # (x, y) -> Piece
        self.rows = rows
        self.columns = columns
        for _ in range(rows * 2):
            row = []
            for _ in range(columns * 2):
                row.append(Cell())
            self.ground.append(row)

    def __str__(self, **kwargs):
        res = " "
        for j in range(self.columns):
            res += 3 * "_" + 5 * " "
        res += "\n"

        for i in range(self.rows):
            for j in range(self.columns):
                piece_label = 3 * " "

                piece = self.ground[2 * i][2 * j]
                # if piece is None and (i, j) in selects.keys():
                #     color_name = selects.get((i, j))
                #     color = colors.get(color_name)
                #     piece_label = color + "NON" + colors.get('Normal')
                if not piece.bug:
                    piece_label = "   "
                else:
                    temp = len(piece.bug.piece)
                    piece_label = piece.bug.piece + piece.bug.player.color[0] + " " * (2 - temp)

                res += "/" + piece_label + "\\" + 3 * "_"

            res += "\n"

            for j in range(self.columns):

                piece = self.ground[2 * i + 1][2 * j + 1]
                if not piece.bug:
                    piece_label = "   "
                else:
                    temp = len(piece.bug.piece)
                    piece_label = piece.bug.piece + piece.bug.player.color[0] + " " * (2 - temp)
                res += "\\" + 3 * "_" + "/" + piece_label

            res += "\n"

        return res

    def add_piece_place(self, x, y, color, piece, player):
        self.ground[x][y].bug = Piece(color, piece, self.ground)
        self.ground[x][y].bug.pos = {
            'x': x,
            'y': y
        }
        self.ground[x][y].bug.player = player
        self.full_positions_map[(x, y)] = self.ground[x][y].bug

    def show_possible_places(self, color):
        output = set()
        # insert in the middle of the board
        if len(self.full_positions_map) == 0:
            output.add((self.rows - 1, self.columns - 1))
        elif len(self.full_positions_map) == 1:
            output.add((8, 10))
            output.add((12, 10))
            output.add((9, 9))
            output.add((11, 11))
            output.add((9, 11))
            output.add((11, 9))
        else:
            for et, piece in self.full_positions_map.items():
                neighbors = self.get_neighbors(piece.pos['x'], piece.pos['y'])
                for neighbor in neighbors:
                    x = neighbor[0]
                    y = neighbor[1]
                    if 0 <= x - 2 < self.columns * 2 and 0 <= y < self.rows * 2:
                        n = self.ground[x - 2][y]
                        if n.bug and n.bug.player.color != color:
                            continue
                    if 0 <= x + 2 < self.columns * 2 and 0 <= y < self.rows * 2:
                        s = self.ground[x + 2][y]
                        if s.bug and s.bug.player.color != color:
                            continue
                    if 0 <= x - 1 < self.columns * 2 and 0 <= y - 1 < self.rows * 2:
                        n_w = self.ground[x - 1][y - 1]
                        if n_w.bug and n_w.bug.player.color != color:
                            continue
                    if 0 <= x - 1 < self.columns * 2 and 0 <= y + 1 < self.rows * 2:
                        n_e = self.ground[x - 1][y + 1]
                        if n_e.bug and n_e.bug.player.color != color:
                            continue
                    if 0 <= x + 1 < self.columns * 2 and 0 <= y - 1 < self.rows * 2:
                        s_w = self.ground[x + 1][y - 1]
                        if s_w.bug and s_w.bug.player.color != color:
                            continue
                    if 0 <= x + 1 < self.columns * 2 and 0 <= y + 1 < self.rows * 2:
                        s_e = self.ground[x + 1][y + 1]
                        if s_e.bug and s_e.bug.player.color != color:
                            continue
                    output.add((x, y))

        return output

    def get_neighbors(self, x, y):
        neighbors = []
        n = self.ground[x - 2][y]
        s = self.ground[x + 2][y]
        n_w = self.ground[x - 1][y - 1]
        n_e = self.ground[x - 1][y + 1]
        s_w = self.ground[x + 1][y - 1]
        s_e = self.ground[x + 1][y + 1]
        if n.bug is None:
            neighbors.append((x - 2, y))
        if s.bug is None:
            neighbors.append((x + 2, y))
        if n_w.bug is None:
            neighbors.append((x - 1, y - 1))
        if n_e.bug is None:
            neighbors.append((x - 1, y + 1))
        if s_w.bug is None:
            neighbors.append((x + 1, y - 1))
        if s_e.bug is None:
            neighbors.append((x + 1, y + 1))
        return neighbors

    # remove the chosen piece
    def remove_piece(self, x, y, color, piece, player):
        self.ground[x][y].bug = Piece(None, None, self.ground)
        self.full_positions_map[(x, y)].remove(piece)


# ------------------------------------------------------------------------------

if __name__ == '__main__':
    turn = 0
    P1 = Player("P1", "black")
    P2 = Player("P2", "red")
    b = Board(11, 11)
    while True:
        # show the board
        print(str(b))
        print("add or move")
        func = input()
        player_turn = P1 if turn % 2 == 0 else P2
        if player_turn == 0:
            player = P1
        else:
            player = P2
        # turn is even P1 else P2
        color = "black" if turn % 2 == 0 else "red"
        if func == "add":
            print("choose your piece: ")
            piece = input()
            print(b.show_possible_places(player_turn.color))
            print("enter the position: ")
            # 10, 10 for the first time
            num = input().split(" ")
            x = int(num[0])
            y = int(num[1])
            # pieces:QB S B G A
            b.add_piece_place(x, y, color, piece, player_turn)
        if func == "move":
            print("choose your piece: ")
            piece = input()
            if piece == "QB":
                qb = Bee(player, piece, b)
                print(qb.possible_movements(qb.pos['x'], qb.pos['y'], color, piece, player))
                x, y = map(int, input('enter destination: ').split())
                b.remove_piece(x, y, color, piece, player)
                print("enter the position: ")
                num = input().split(" ")
                x = int(num[0])
                y = int(num[1])
                b.add_piece_place(x, y, color, piece, player_turn)
                # show the board without the removed piece
        turn += 1
