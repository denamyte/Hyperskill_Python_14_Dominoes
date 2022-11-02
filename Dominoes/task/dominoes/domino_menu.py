from Dominoes.task.dominoes.domino_game import DominoGame


class DominoMenu:
    def __init__(self, game: DominoGame):
        self._game = game

    def first_move(self):
        print('Stock pieces: ' + self._game.stock_str)
        print('Computer pieces: ' + str(self._game.get_player(0)))
        print('Player pieces: ' + str(self._game.get_player(1)))
        print('Domino snake: ' + str(self._game.snake_str))
        print('Status: ' + self._game.get_player(self._game.move_index).name)
