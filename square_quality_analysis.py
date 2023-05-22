import models
from functools import lru_cache
import metadataManager
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import matplotlib
import copy


N = models.BoardCellType.NORMAL
GREEN = models.BoardCellType.GREEN
RED = models.BoardCellType.RED
VOID = models.BoardCellType.VOID


class TashKalarBoard:
    square_type_matrix = [
        [VOID, VOID, N, N, N, N, N, VOID, VOID, ],
        [VOID, N, N, RED, N, N, N, N, VOID, ],
        [N, N, GREEN, N, N, N, GREEN, N, N, ],
        [N, N, N, N, N, N, N, N, GREEN, ],
        [GREEN, N, N, N, RED, N, N, N, N, ],
        [N, N, N, N, N, N, N, RED, N, ],
        [N, N, N, N, N, N, N, N, N, ],
        [VOID, N, RED, N, N, GREEN, N, N, VOID, ],
        [VOID, VOID, N, N, N, N, N, VOID, VOID, ],
    ]
    void_square_indexes = frozenset([(0, 0), (0, 1), (0, 7), (0, 8), (1, 0), (1, 8), (7, 0), (7, 8), (8, 0), (8, 1), (8, 7), (8, 8)])
    class Square:
        def __init__(self, row, col, square_type):
            self.row = row
            self.col = col
            self.square_type = square_type
            self.taxicab_neighbors = None  # square neighbours
            self.von_neuman_neighbors = None  # diamond neighbours

        def __repr__(self):
            return f"Square({self.row}, {self.col}, {self.square_type})"

        def __str__(self):
            return f"Square({self.row}, {self.col}, {self.square_type})"

        def is_green(self):
            return self.square_type == GREEN

        def is_red(self):
            return self.square_type == RED

        def is_colored(self):
            return self.is_green() or self.is_red()

        @lru_cache(maxsize=1)
        def count_red_neighbors(self) -> int:
            return len(list(filter(lambda n: n.is_red(), self.taxicab_neighbors)))

        @lru_cache(maxsize=1)
        def count_green_neighbors(self) -> int:
            return len(list(filter(lambda n: n.is_green(), self.taxicab_neighbors)))

        @lru_cache(maxsize=1)
        def count_colored_neighbors(self) -> int:
            return len(list(filter(lambda n: n.is_colored(), self.taxicab_neighbors)))

        def is_in_central_big_square(self):
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
            return self.square_type == VOID

        def count_corner_neighbors(self):
            return len([n for n in self.taxicab_neighbors if n.is_corner()])

        def count_border_neighbors(self):
            return len([n for n in self.taxicab_neighbors if n.is_on_border()])

    def __init__(self):
        self.squares = [
            [TashKalarBoard.Square(row_i, col_i, square_type) for col_i, square_type in enumerate(row)]
            for row_i, row in enumerate(self.square_type_matrix)
        ]

        self.valid_squares = frozenset([sq for row in self.squares for sq in row if sq.square_type != VOID])
        self.green_squares = frozenset([sq for sq in self if sq.is_green()])
        self.red_squares = frozenset([sq for sq in self if sq.is_red()])
        self.colored_squares = frozenset([sq for sq in self if sq.is_colored()])
        self.void_squares = frozenset([sq for sq in self.iter_all() if sq.is_void()])

        for sq in self:
            sq.taxicab_neighbors = self.get_taxicab_neighbors_for_square(sq)
            sq.von_neuman_neighbors = self.get_von_neuman_neighbors_for_square(sq)

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

    @lru_cache(maxsize=256)
    def get_von_neuman_neighbors_indexes(self, row, col) -> frozenset:
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < 8:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < 8:
            neighbors.append((row, col + 1))
        return frozenset(neighbors)

    def get_taxicab_neighbors_for_square(self, square) -> frozenset:
        return self.get_taxicab_neighbors(square.row, square.col)

    def get_von_neuman_neighbors_for_square(self, square) -> frozenset:
        return self.get_von_neuman_neighbors_indexes(square.row, square.col)

    @lru_cache(maxsize=256)
    def get_taxicab_neighbors(self, row, col) -> frozenset:
        return frozenset([self.squares[r][c]
                          for r, c in self.get_taxicab_neighbors_indexes(row, col)
                          if self.square_type_matrix[r][c] != VOID])

    def __iter__(self):
        return (sq for sq in self.valid_squares)

    def iter_all(self):
        return (sq for row in self.squares for sq in row)

    def __next__(self):
        return next(self)

    def main(self):
        get_mm = metadataManager.MetadataManager.get_manual_metadata_for_card
        tasks = [
            ("Red Legends", lambda sq: task_points if sq.is_red() else (task_points / 2.0 * sq.count_red_neighbors())),
            ("Red Conquest", lambda sq: task_points if sq.is_red() else (task_points / 2.0 * sq.count_red_neighbors())),
            ("Red Summoning", lambda sq: task_points * (sq.count_red_neighbors() + int(sq.is_red()))),

            ("Green Legends", lambda sq: task_points if sq.is_green() else (task_points / 2.0 * sq.count_green_neighbors())),
            ("Green Conquest", lambda sq: task_points if sq.is_green() else (task_points / 2.0 * sq.count_green_neighbors())),
            ("Green Summoning", lambda sq: task_points * (sq.count_green_neighbors() + int(sq.is_green()))),

            ("Rainbow Dominance", lambda sq: task_points if sq.is_colored() else (task_points / 2.0 * sq.count_colored_neighbors())),
            ("Color Conquest", lambda sq: task_points if sq.is_colored() else (task_points / 2.0 * sq.count_colored_neighbors())),
            ("Colored Summoning", lambda sq: task_points * (sq.count_colored_neighbors() + int(sq.is_colored()))),

            ("Central Dominance", lambda sq: task_points * int(sq.is_in_central_big_square())),
            ("Line Dominance", lambda sq: task_points * int(sq.is_on_central_line())),
            ("Center Cross", lambda sq: task_points * int(sq.is_in_central_big_square()) * (2 if sq.is_the_board_centre() else 1)),
            ("Diagonals", lambda sq: task_points * int(sq.is_on_diagonal()) * (2 if sq.is_the_board_centre() else 1)),
            ("Corner Chain", lambda sq: task_points if sq.is_corner() else task_points / 2.0 * sq.count_corner_neighbors()),
            ("Side Chain", lambda sq: task_points if sq.is_corner() else task_points / 2.0 * sq.count_border_neighbors()),
        ]
        available_tasks = [
            "Rainbow Dominance",
            "Green Summoning",
            "Corner Chain"
        ]
        future_task = "Heroic Devastation"

        # tasks = [
        #     ("Red Legends", lambda sq: task_points if sq.is_red() else 0),
        #     ("Green Legends", lambda sq: task_points if sq.is_green() else 0),
        #     ("Rainbow Dominance", lambda sq: task_points if sq.is_colored() else 0),
        #     ("Red Conquest", lambda sq: task_points if sq.is_red() else 0),
        #     ("Green Conquest", lambda sq: task_points if sq.is_green() else 0),
        #     ("Color Conquest", lambda sq: task_points if sq.is_colored() else 0),
        #
        #     ("Red Summoning", lambda sq: task_points * int(sq.is_red())),
        #     ("Green Summoning", lambda sq: task_points * int(sq.is_green())),
        #     ("Colored Summoning", lambda sq: task_points * int(sq.is_colored())),
        #
        #     ("Central Dominance", lambda sq: task_points * int(sq.is_in_central_big_square())),
        #     ("Line Dominance", lambda sq: task_points * int(sq.is_on_central_line())),
        #     ("Center Cross", lambda sq: task_points * (2 if sq.is_the_board_centre() else 1 if sq.is_in_central_big_square() else 0)),
        #     ("Diagonals", lambda sq: task_points * (2 if sq.is_the_board_centre() else 1 if sq.is_on_diagonal() else 0)),
        #     ("Corner Chain", lambda sq: task_points * int(sq.is_corner())),
        #     ("Side Chain", lambda sq: task_points * int(sq.is_on_border())),
        # ]


        quality_matrix = [[0.0 for _ in range(9)] for _ in range(9)]
        for t in tasks:
            task_name = t[0]
            scoring_method = t[1]
            task_points = get_mm(models.NonFactionType.TASK.value, task_name).get("points")

            for sq in self:
                multiplicator = 1 #0.5 if task_name == future_task else 1.0 if task_name in available_tasks else (1.0/(len(tasks)-4.0))
                quality_matrix[sq.row][sq.col] += scoring_method(sq) * multiplicator

        # self.plot_matrix(quality_matrix)
        # self.plot_matrix(self.blur(quality_matrix))
        # self.plot_matrix(self.blur(quality_matrix, extended=8, sigma=8, normalize=True))
        self.plot_matrix(self.blur(quality_matrix, extended=1, sigma=0.6, normalize=True))

    def blur(self, matrix, extended=2, sigma=0.5, normalize=False):
        if extended > 0:
            extended_matrix = [[0 for _ in range(len(matrix)+(2*extended))] for _ in range(len(matrix)+(2*extended))]
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    extended_matrix[i+extended][j+extended] = matrix[i][j]

            blurred_extended = gaussian_filter(extended_matrix, sigma=sigma)
            blurred = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    blurred[i][j] = blurred_extended[i+extended][j+extended]
        else:
            blurred = gaussian_filter(matrix, sigma=sigma).tolist()

        for row in self.squares:
            for sq in row:
                if sq.is_void():
                    blurred[sq.row][sq.col] = 0
                else:
                    blurred[sq.row][sq.col] = blurred[sq.row][sq.col]

        if normalize:
            max_val = -10000000
            min_val = 100000
            for row in self.squares:
                for sq in row:
                    if not sq.is_void():
                        max_val = max(max_val, blurred[sq.row][sq.col])
                        min_val = min(min_val, blurred[sq.row][sq.col])

            min_max_range = max_val - min_val
            for row in self.squares:
                for sq in row:
                    if not sq.is_void():
                        blurred[sq.row][sq.col] = (blurred[sq.row][sq.col] - min_val) / min_max_range * 100

            # convert to int
            for row in self.squares:
                for sq in row:
                    if not sq.is_void():
                        blurred[sq.row][sq.col] = int(blurred[sq.row][sq.col])
        else:
            # round
            for row in self.squares:
                for sq in row:
                    if not sq.is_void():
                        blurred[sq.row][sq.col] = round(blurred[sq.row][sq.col], 1)

        return blurred

    def plot_matrix(self, matrix):
        def set_matshow_cell_color(ax, i, j, color, filled=False):
            if filled:
                ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, color=color))
            else:
                ax.add_patch(plt.Rectangle((j - 0.48, i - 0.5), 0.94, 0.92, facecolor='none', edgecolor=color, linewidth=2.0, alpha=1))

        fig, ax = plt.subplots()
        ax.matshow(matrix, cmap=plt.cm.Blues)
        ax.set_xlabel('Column')
        ax.set_ylabel('Row')
        # ax.set_xticks(list(range(1, len(matrix)+1)))
        ax.set_xticklabels(list(map(str, range(len(matrix)+1))))
        ax.set_yticklabels(list(map(str, range(len(matrix)+1))))

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                ax.text(i, j, str(matrix[j][i]), va='center', ha='center')

        for sq in self.void_squares:
            set_matshow_cell_color(ax, sq.row, sq.col, 'black', filled=True)

        for sq in self.red_squares:
            set_matshow_cell_color(ax, sq.row, sq.col, 'red')

        for sq in self.green_squares:
            set_matshow_cell_color(ax, sq.row, sq.col, 'lime')

        plt.show()


TashKalarBoard().main()



