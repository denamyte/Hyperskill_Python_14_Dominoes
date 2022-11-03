from typing import List

from Dominoes.task.dominoes.domino_game import DominoGame, Status
from Dominoes.task.dominoes.domino_items import DominoPiece

STATUS_MAP = {Status.COMPUTER: '\nStatus: Computer is about to make a move. Press Enter to continue...',
              Status.PLAYER: "\nStatus: It's your turn to make a move. Enter your command.",
              Status.WIN: '\nStatus: The game is over. You won!',
              Status.LOOSE: '\nStatus: The game is over. The computer won!',
              Status.DRAW: "\nStatus: The game is over. It's a draw!"}
END_GAME_STATUSES = (Status.WIN, Status.LOOSE, Status.DRAW)


class DominoMenu:
    def __init__(self, game: DominoGame):
        self._game = game

    def menu_loop(self):
        while True:
            self._show_menu()
            if self._game.status not in END_GAME_STATUSES:
                self._next_move_prompt()
            else:
                break

    def _show_menu(self):
        self._header()
        self._stock_size()
        self._computer_pieces()
        self._snake()
        self._player_pieces()
        self._status()

    def _next_move_prompt(self):
        if self._game.status == Status.PLAYER:
            while True:
                try:
                    move = int(input())
                    if abs(move) <= self._game.player_size:
                        if not self._game.move_matches_snake(move):
                            self._illegal_move()
                            continue
                        self._game.player_move(move)
                        break
                except ValueError:
                    pass
                self._invalid_input()
        else:
            input()
            self._game.computer_move()

    @staticmethod
    def _header():
        print('=' * 70)

    def _stock_size(self):
        print('Stock size:', self._game.stock_size)

    def _computer_pieces(self):
        print('Computer pieces:', self._game.comp_size)

    def _snake(self):
        pieces = self._game.snake_pieces
        if len(pieces) > 6:
            self._snake_detail(pieces[:3])
            print('...', end='')
            self._snake_detail(pieces[-3:])
        else:
            self._snake_detail(pieces)
        print()

    @staticmethod
    def _snake_detail(pieces: List[DominoPiece]):
        print(''.join(str(p) for p in pieces), end='')

    def _player_pieces(self):
        print('\nYour pieces:')
        for i, p in enumerate(self._game.player_pieces):
            print(f'{i + 1}:{p}')

    def _status(self):
        print(STATUS_MAP[self._game.status])

    @staticmethod
    def _invalid_input():
        print('Invalid input. Please try again.')

    @staticmethod
    def _illegal_move():
        print('Illegal move. Please try again.')
