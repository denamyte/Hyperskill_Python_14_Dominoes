from random import randint
from enum import Enum, IntEnum
from typing import List

from Dominoes.task.dominoes.domino_items import DominoPile, DominoPiece, DominoPlayer, DominoStock, DominoSnake


class Indices(IntEnum):
    COMPUTER = 0
    PLAYER = 1


class Status(Enum):
    COMPUTER = 'computer'
    PLAYER = 'player'
    WIN = 'win'
    LOOSE = 'loose'
    DRAW = 'draw'


class DominoGame:
    def __init__(self):
        self._stock: DominoStock | None = None
        self._players: List[DominoPlayer] = []
        self._snake: DominoSnake | None = None
        self._move_index = -1
        self._status = Status.PLAYER
        self._generate_dominoes()

    def _generate_dominoes(self):
        while True:
            self._stock = DominoStock(DominoPiece(left, right)
                                      for left in range(7)
                                      for right in range(left, 7))
            self._stock.shuffle()
            self._players = [DominoPlayer(self._stock.pop_first_n(7), name) for name in ('computer', 'player')]
            highest_double_indices = tuple(p.highest_double_index_value() for p in self._players)
            if sum(map(lambda x: x[0], highest_double_indices)) == -len(highest_double_indices):
                continue

            highest_value = -1
            player_to_donate_index = -1
            highest_value_index = -1
            for i, highest_double_tuple in enumerate(highest_double_indices):
                if highest_double_tuple[1] > highest_value:
                    highest_value = highest_double_tuple[1]
                    player_to_donate_index = i
                    highest_value_index = highest_double_tuple[0]

            start_piece = self._players[player_to_donate_index].pop_piece(highest_value_index)
            self._snake = DominoSnake([start_piece])
            self._move_index = player_to_donate_index
            self._adjust_move_status()
            break

    def computer_move(self):
        size = self._players[Indices.COMPUTER].size
        move = randint(-size, size)
        self._move(move)

    def player_move(self, move: int):
        self._move(move)

    def _move(self, move: int):
        player = self._players[self._move_index]
        if move == 0:
            if self._stock.size > 0:
                piece = self._stock.pop_piece(self._stock.size - 1)
                player.add_piece(piece)

            self._adjust_move_status()
        else:
            piece = player.pop_piece(abs(move) - 1)
            self._snake.add_piece(piece, move > 0)
            if not player.size:
                self._status = Status.WIN if self._status == Status.PLAYER else Status.LOOSE
            else:
                self._check_draw_status()
                if self.status != Status.DRAW:
                    self._adjust_move_status()

    def _check_draw_status(self):
        s = self._snake
        if s.size >= 7 and s.left == s.right and s.count_value_times(s.left) == 8:
            self._status = Status.DRAW

    def _adjust_move_status(self):
        self._move_index = (self._move_index + 1) % len(self._players)
        self._status = Status.COMPUTER if self._move_index == Indices.COMPUTER else Status.PLAYER

    @property
    def stock_size(self) -> int:
        return self._stock.size

    @property
    def comp_size(self) -> int:
        return self._players[Indices.COMPUTER].size

    @property
    def player_size(self) -> int:
        return self._players[Indices.PLAYER].size

    @property
    def snake_pieces(self) -> List[DominoPiece]:
        return self._snake.pieces

    @property
    def player_pieces(self) -> List[DominoPiece]:
        return self._players[Indices.PLAYER].pieces

    @property
    def status(self) -> Status:
        return self._status
