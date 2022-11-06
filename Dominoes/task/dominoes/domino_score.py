from typing import List, Dict
from dataclasses import dataclass

from Dominoes.task.dominoes.domino_items import DominoPiece


@dataclass
class IndexedDominoPiece:
    piece: DominoPiece
    index_in_player: int
    score: int

    def __str__(self):
        return f'{self.piece}, idx: {self.index_in_player}, score: {self.score}'


class DominoScore:
    def __init__(self, player_pieces: List[DominoPiece], snake_pieces: List[DominoPiece]):
        self.indexed_pieces = [IndexedDominoPiece(p, i, 0) for i, p in enumerate(player_pieces)]
        self._total_pieces: List[DominoPiece] = [*player_pieces, *snake_pieces]
        self._scores_dict: Dict[int, int] = {}

        self._make_score_dict()
        self._update_indexed_pieces()

    def _make_score_dict(self):
        values: List[int] = []
        for p in self._total_pieces:
            values.append(p.left)
            values.append(p.right)

        for i in range(7):
            self._scores_dict[i] = values.count(i)

    def _update_indexed_pieces(self):
        for ip in self.indexed_pieces:
            ip.score = sum(map(lambda i: self._scores_dict[i], (ip.piece.left, ip.piece.right,)))
        self.indexed_pieces.sort(key=lambda x: x.score, reverse=True)

    def __str__(self):
        player = '\n  '.join(str(p) for p in self.indexed_pieces)
        pl_sn = '\n  '.join(str(p) for p in self._total_pieces)
        return f'''
player: 
  {player}
player+snake: 
  {pl_sn}
scores: {self._scores_dict}'''
