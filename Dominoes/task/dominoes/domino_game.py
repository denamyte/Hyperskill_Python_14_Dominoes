from enum import Enum, IntEnum
from typing import List

from Dominoes.task.dominoes.domino_items import DominoPile, DominoPiece, DominoPlayer, DominoStock


class Indices(IntEnum):
    COMPUTER = 0
    PLAYER = 1


class Status(Enum):
    COMPUTER = 'computer'
    PLAYER = 'player'


class DominoGame:
    def __init__(self):
        self._stock: DominoStock | None = None
        self._players: List[DominoPlayer] = []
        self._snake: DominoPile | None = None
        self._move_index = -1
        self._generate_dominoes()
        self._status = Status.PLAYER
        self._change_status()

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
            self._snake = DominoPile([start_piece])
            self._move_index = (player_to_donate_index + 1) % len(self._players)
            break

    def _change_status(self):
        self._status = Status.COMPUTER if self._move_index == Indices.COMPUTER else Status.PLAYER

    @property
    def stock_size(self) -> int:
        return self._stock.size

    @property
    def comp_size(self) -> int:
        return self._players[Indices.COMPUTER].size

    @property
    def snake_pieces(self) -> List[DominoPiece]:
        return self._snake.pieces

    @property
    def player_pieces(self) -> List[DominoPiece]:
        return self._players[Indices.PLAYER].pieces

    @property
    def status(self) -> Status:
        return self._status
