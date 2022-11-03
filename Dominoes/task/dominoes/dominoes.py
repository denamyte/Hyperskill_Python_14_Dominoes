from Dominoes.task.dominoes.domino_game import DominoGame
from Dominoes.task.dominoes.domino_menu import DominoMenu

if __name__ == '__main__':
    game = DominoGame()
    menu = DominoMenu(game)
    menu.menu_loop()
