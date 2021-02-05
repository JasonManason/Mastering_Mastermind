#Jason de Mey, Klas AI V1B, Opdracht 1: Mastering Mastermind
import strategies as strats
import game_rules as rules
import game_modes as gm

def menu():
    """Welcomes the player and asks for what game mode the player(s) want(s) to play.
    The game can be played with 2 players, with one player against a bot or you can watch 2 bots play."""

    while True:
        try:
            game_mode = int(input('Welcome to Mastermind, please pick a way to play:\n'
                              '1: I want to play against a bot.\n'
                              '2. I want to play with another player, against eachother.\n'
                              '3: I want to watch two bots play against eachother.\n')) # <= This functionality will be implemented given there's enough time left.
            if game_mode < 1 or game_mode > 3:
                print('I\'m sorry, that\'s not a correct number, please select a game mode (1-3).')
                continue
            else:
                break
        except ValueError:
            print('I\'m sorry, I couldn\'t quite understand your input, please select a game mode (1-3).')
            continue

    return game_mode

menu()