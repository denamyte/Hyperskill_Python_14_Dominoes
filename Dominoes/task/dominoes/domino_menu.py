from Dominoes.task.dominoes.domino_game import DominoGame, Status

STATUS_MAP = {Status.COMPUTER: '\nStatus: Computer is about to make a move. Press Enter to continue...',
              Status.PLAYER: "\nStatus: It's your turn to make a move. Enter your command.", }


class DominoMenu:
    def __init__(self, game: DominoGame):
        self._game = game

    def show_status(self):
        self._header()
        self._stock_size()
        self._computer_pieces()
        self._snake()
        self._player_pieces()
        self._status()

    @staticmethod
    def _header():
        print('=' * 70)

    def _stock_size(self):
        print('Stock size:', self._game.stock_size)

    def _computer_pieces(self):
        print('Computer pieces:', self._game.comp_size)

    def _snake(self):
        print(', '.join(str(p) for p in self._game.snake_pieces))

    def _player_pieces(self):
        print('\nYour pieces:')
        for i, p in enumerate(self._game.player_pieces):
            print(f'{i + 1}:{p}')

    def _status(self):
        print(STATUS_MAP[self._game.status])
