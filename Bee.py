from Piece import Piece
class Bee(Piece):
    def get_neighbors(self, x, y):
     neighbors = []
     n = self.Board.ground[x - 2][y]
     s = self.Board.ground[x + 2][y]
     n_w = self.Board.ground[x - 1][y - 1]
     n_e = self.Board.ground[x - 1][y + 1]
     s_w = self.Board.ground[x + 1][y - 1]
     s_e = self.Board.ground[x + 1][y + 1]
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

    def possible_movements(self, x, y, color, piece, player):
        output = set()
        for et, piece in self.Board.full_positions_map.items():
                neighbors = self.get_neighbors( piece.pos['x'], piece.pos['y'])
                for neighbor in neighbors:
                    x = neighbor[0]
                    y = neighbor[1]
                    if 0 <= x - 2 < self.Board.columns * 2 and 0 <= y < self.Board.rows * 2:
                        n = self.Board.ground[x - 2][y]
                        if n.bug and n.bug.player.color != color:
                            continue
                    if 0 <= x + 2 < self.Board.columns * 2 and 0 <= y < self.Board.rows * 2:
                        s = self.Board.ground[x + 2][y]
                        if s.bug and s.bug.player.color != color:
                            continue
                    if 0 <= x - 1 < self.Board.columns * 2 and 0 <= y - 1 < self.Board.rows * 2:
                        n_w = self.Board.ground[x - 1][y - 1]
                        if n_w.bug and n_w.bug.player.color != color:
                            continue
                    if 0 <= x - 1 < self.Board.columns * 2 and 0 <= y + 1 < self.Board.rows * 2:
                        n_e = self.Board.ground[x - 1][y + 1]
                        if n_e.bug and n_e.bug.player.color != color:
                            continue
                    if 0 <= x + 1 < self.Board.columns * 2 and 0 <= y - 1 < self.Board.rows * 2:
                        s_w = self.Board.ground[x + 1][y - 1]
                        if s_w.bug and s_w.bug.player.color != color:
                            continue
                    if 0 <= x + 1 < self.Board.columns * 2 and 0 <= y + 1 < self.Board.rows * 2:
                        s_e = self.Board.ground[x + 1][y + 1]
                        if s_e.bug and s_e.bug.player.color != color:
                            continue
                    output.add((x, y))

        return output
