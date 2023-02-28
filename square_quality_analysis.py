import models
from functools import lru_cache
import metadataManager
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


N = models.BoardCellType.NORMAL
G = models.BoardCellType.GREEN
R = models.BoardCellType.RED
V = models.BoardCellType.VOID


class TashKalarBoard:
    square_type_matrix = [
        [V, V, N, N, N, N, N, V, V, ],
        [V, N, N, R, N, N, N, N, V, ],
        [N, N, G, N, N, N, G, N, N, ],
        [N, N, N, N, N, N, N, N, G, ],
        [G, N, N, N, R, N, N, N, N, ],
        [N, N, N, N, N, N, N, G, N, ],
        [N, N, N, N, N, N, N, N, N, ],
        [V, N, R, N, N, G, N, N, V, ],
        [V, V, N, R, N, N, N, V, V, ],
    ]
    void_square_indexes = frozenset([(0, 0), (0, 1), (0, 7), (0, 8), (1, 0), (1, 8), (7, 0), (7, 8), (8, 0), (8, 1), (8, 7), (8, 8)])
    class Square:
        def __init__(self, row, col, square_type):
            self.row = row
            self.col = col
            self.square_type = square_type
            self.neighbors = None

        def __repr__(self):
            return f"Square({self.row}, {self.col}, {self.square_type})"

        def __str__(self):
            return f"Square({self.row}, {self.col}, {self.square_type})"

        def is_green(self):
            return self.square_type == G

        def is_red(self):
            return self.square_type == R

        def is_colored(self):
            return self.is_green() or self.is_red()

        @lru_cache(maxsize=1)
        def count_red_neighbors(self) -> int:
            return len(list(filter(lambda n: n.is_red(), self.neighbors)))

        @lru_cache(maxsize=1)
        def count_green_neighbors(self) -> int:
            return len(list(filter(lambda n: n.is_green(), self.neighbors)))

        @lru_cache(maxsize=1)
        def count_colored_neighbors(self) -> int:
            return len(list(filter(lambda n: n.is_colored(), self.neighbors)))

        def is_central_square(self):
            return 3 <= self.row <= 5 and 3 <= self.col <= 5

        def is_the_board_centre(self):
            return self.row == 4 and self.col == 4

        def is_on_central_line(self):
            return 3 <= self.row <= 5 or 3 <= self.col <= 5

        def is_on_diagonal(self):
            return self.row == self.col or self.row + self.col == 8

        @lru_cache(maxsize=1)
        def is_corner(self):
            return (self.row, self.col) in {(2, 0), (1, 1), (0, 2), (0, 6), (1, 7), (2, 8),
                                            (6, 0), (7, 1), (8, 2), (8, 6), (7, 7), (6, 8)}

        def is_on_border(self):
            return self.row in {0, 8} or self.col in {0, 8}

        def is_void(self):
            return self.square_type == V

    def __init__(self):
        self.squares = [
            [TashKalarBoard.Square(row_i, col_i, square_type) for col_i, square_type in enumerate(row)]
            for row_i, row in enumerate(self.square_type_matrix)
        ]

        self.valid_squares = frozenset([sq for row in self.squares for sq in row if sq.square_type != V])
        self.green_squares = frozenset([sq for sq in self if sq.is_green()])
        self.red_squares = frozenset([sq for sq in self if sq.is_red()])
        self.colored_squares = frozenset([sq for sq in self if sq.is_colored()])
        self.void_squares = frozenset([sq for sq in self if sq.is_void()])

        for sq in self:
            sq.neighbors = self.get_taxicab_neighbors_for_square(sq)

    def get_square(self, row, col):
        return self.squares[row][col]

    @staticmethod
    def is_central_line_square(square):
        return 3 <= square.row <= 5 or 3 <= square.col <= 5

    @staticmethod
    def is_central_square(square):
        return 3 <= square.row <= 5 and 3 <= square.col <= 5

    @lru_cache(maxsize=256)
    def get_taxicab_neighbors_indexes(self, row, col) -> frozenset:
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < 8:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < 8:
            neighbors.append((row, col + 1))
        if row > 0 and col > 0:
            neighbors.append((row - 1, col - 1))
        if row > 0 and col < 8:
            neighbors.append((row - 1, col + 1))
        if row < 8 and col > 0:
            neighbors.append((row + 1, col - 1))
        if row < 8 and col < 8:
            neighbors.append((row + 1, col + 1))
        return frozenset(neighbors)

    def get_taxicab_neighbors_for_square(self, square) -> frozenset:
        return self.get_taxicab_neighbors(square.row, square.col)

    @lru_cache(maxsize=256)
    def get_taxicab_neighbors(self, row, col) -> frozenset:
        return frozenset([self.squares[r][c]
                          for r, c in self.get_taxicab_neighbors_indexes(row, col)
                          if self.square_type_matrix[r][c] != V])

    def __iter__(self):
        return (sq for sq in self.valid_squares)

    def __next__(self):
        return next(self)

    def main(self):
        get_mm = metadataManager.MetadataManager.get_manual_metadata_for_card
        get_fm = metadataManager.MetadataManager.get_fetched_metadata_for_card
        # colored Taks:
        # 1. Red Legends
        # 2. Green Legends
        # 3. Rainbow Dominance
        # 4. Green Summoning
        # 5. Red Summoning
        # 6. Red Conquest
        # 7. Green Conquest
        # 8. Red Dominance
        # 9. Green Dominance
        tasks = [
            ("Red Legends", lambda sq: task_points if sq.is_red() else (task_points / 2.0 * sq.count_red_neighbors())),
            ("Green Legends", lambda sq: task_points if sq.is_green() else (task_points / 2.0 * sq.count_green_neighbors())),
            ("Rainbow Dominance", lambda sq: task_points if sq.is_colored() else (task_points / 2.0 * sq.count_colored_neighbors())),
            ("Red Conquest", lambda sq: task_points if sq.is_red() else (task_points / 2.0 * sq.count_red_neighbors())),
            ("Green Conquest", lambda sq: task_points if sq.is_green() else (task_points / 2.0 * sq.count_green_neighbors())),
            ("Color Conquest", lambda sq: task_points if sq.is_colored() else (task_points / 2.0 * sq.count_colored_neighbors())),

            ("Red Summoning", lambda sq: task_points * (sq.count_red_neighbors() + int(sq.is_red()))),
            ("Green Summoning", lambda sq: task_points * (sq.count_green_neighbors() + int(sq.is_green()))),
            ("Colored Summoning", lambda sq: task_points * (sq.count_colored_neighbors() + int(sq.is_colored()))),

            ("Central Dominance", lambda sq: task_points * int(sq.is_central_square())),
            ("Line Dominance", lambda sq: task_points * int(sq.is_on_central_line())),
            ("Center Cross", lambda sq: task_points * int(sq.is_central_square()) * (2 if sq.is_the_board_centre() else 1)),
            ("Diagonals", lambda sq: task_points * int(sq.is_on_diagonal()) * (2 if sq.is_the_board_centre() else 1)),
            # ("Corner Chain", lambda sq: task_points * int(sq.is_on_corner()) * (2 if sq.is_the_board_centre() else 1)), # TODO check logic, because autogenerated
            # ("Side Chain", lambda sq: task_points * int(sq.is_on_side()) * (2 if sq.is_the_board_centre() else 1)),  # TODO check logic, because autogenerated
        ]

        quality_matrix = [[0 for _ in range(9)] for _ in range(9)]
        for t in tasks:
            task_name = t[0]
            scoring_method = t[1]
            task_points = get_mm(models.NonFactionType.TASK.value, task_name).get("points")

            for sq in self:
                quality_matrix[sq.row][sq.col] += scoring_method(sq)
                if scoring_method(sq) > 0:
                    print(f'{sq}\t scores {scoring_method(sq)} points for {task_name}')



        # TashKalarBoard.plot_matrix(quality_matrix)
        #TashKalarBoard.plot_matrix(self.blur(quality_matrix))
        TashKalarBoard.plot_matrix(self.blur(quality_matrix, extended=True))

    def blur(self, matrix, extended=False):
        sigma = 0.6
        if extended:
            extended_matrix = [[0 for _ in range(len(matrix)+2)] for _ in range(len(matrix)+2)]
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    extended_matrix[i+1][j+1] = matrix[i][j]

            blurred_extended = gaussian_filter(extended_matrix, sigma=sigma)
            blurred = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    blurred[i][j] = blurred_extended[i+1][j+1]
        else:
            blurred = gaussian_filter(matrix, sigma=sigma)

        for row in self.squares:
            for sq in row:
                if sq.is_void():
                    blurred[sq.row][sq.col] = 0
                else:
                    blurred[sq.row][sq.col] = round(blurred[sq.row][sq.col], 1)
        return blurred

    @staticmethod
    def plot_matrix(matrix):
        fig, ax = plt.subplots()
        ax.matshow(matrix, cmap=plt.cm.Blues)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                ax.text(i, j, str(matrix[j][i]), va='center', ha='center')
        plt.show()


TashKalarBoard().main()



