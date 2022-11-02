from typing import Iterable, Tuple
from random import shuffle


class DominoPiece:
    def __init__(self, left: int, right: int):
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __str__(self):
        return f'[{self._left}, {self._right}]'


class DominoPile:
    def __init__(self, pieces: Iterable[DominoPiece]):
        self._pieces = list(pieces)

    def read_piece(self, index: int) -> DominoPiece | None:
        return None \
            if index < 0 or index >= len(self._pieces) \
            else DominoPiece(self._pieces[index].left, self._pieces[index].right)

    def pop_piece(self, index: int) -> DominoPiece | None:
        return None \
            if index < 0 or index >= len(self._pieces) \
            else self._pieces.pop(index)

    def add_piece(self, piece: DominoPiece):
        self._pieces.append(piece)

    def __str__(self):
        return '[{}]'.format(', '.join(str(p) for p in self._pieces))


class DominoStock(DominoPile):
    def __init__(self, pieces: Iterable[DominoPiece]):
        super().__init__(pieces)

    def shuffle(self):
        shuffle(self._pieces)

    def pop_first_n(self, n: int) -> Iterable[DominoPiece]:
        if n > len(self._pieces):
            return []
        popped = self._pieces[:n]
        self._pieces = self._pieces[n:]
        return popped


class DominoPlayer(DominoPile):
    def __init__(self, pieces: Iterable[DominoPiece], name: str):
        super().__init__(pieces)
        self._name = name

    def highest_double_index_value(self) -> Tuple[int, int]:
        index, value = -1, -1
        for i, p in enumerate(self._pieces):
            if p.left == p.right and p.left > value:
                index = i
                value = p.left
        return index, value

    @property
    def name(self) -> str:
        return self._name
