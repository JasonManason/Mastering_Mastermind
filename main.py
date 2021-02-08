#Jason de Mey, Klas AI V1B, Opdracht 1: Mastering Mastermind
import random
import strategies as strats
import game_rules as rules
import game_modes as gm
def random_code():
    """Creates a random code if player 1 is a bot."""
    colours = {'B':'Blue','Y':'Yellow','R':'Red','G':'Green','P':'Purple','O':'Orange'}
    code = []

    while len(code) < 4: # <= for loop needed for duplicate values
        code.append(random.choice(list(colours.items())))

    return code # <= code is a list with tuples


# def feedback():
#     """Function for giving feedback on the guesses a player makes.
#     Function is only called if player 1 is a bot."""
#     guess = guessing()
#
#
#     #return feedback [1,2,0,1]
#
#
# def guessing():
#     """Let's player 2 do a maximum of 10 tries to guess the code of player 1.
#     Calls on function feedback if player 1 is a bot. Else it asks for manual feedback."""
#
#     #return guess 'GBYP'


def game_mode_1_player1():
    """This game mode will play when the player chooses option 1 in the menu.
    The player plays against a bot as the one who creates a code and gives feedback."""
    print('Chosen game mode: 1, player 1')


def game_mode_1_player2():
    """This game mode will play when the player chooses option 1 in the menu.
    The player plays against a bot and has to guess the right code."""
    code_list = random_code()
    print(f'code to guess: {code_list[0][1]}, {code_list[1][1]}, {code_list[2][1]}, {code_list[3][1]}') # <=cheatsheet
    code = str((code_list[0][0])+(code_list[1][0])+(code_list[2][0])+(code_list[3][0]))
    print(code)

    print('You are now allowed to guess the code, the code is 4 characters long, there may or may not be duplicate colours.\n'
          'Enter a 4 letter combination of the first letters of the colours, like so: "YGBP" for Yellow, Green, Blue, Purple.\n'
          'Your choices are:\nB: Blue\nY: Yellow\nR: Red\nG: Green\nP: Purple\nO: Orange')

    guesses = 0
    black = 0
    white = 0

    while guesses < 11:
        try:
            guess = str(input('Take a guess:\n')).upper()
            guesses += 1
            if guess == code:
                print(f'Congratulations, you won within {guesses} guess(es)!')
                break
            elif len(guess) > 4 or len(guess) < 4:
                print('Your guess should consist of 4 letters.')
                continue

            white = 0  # <= stands for number of equal pins in wrong place
            black = 0  # <= stands for number of equal pins in right place

            for i in guess:
                print(f'{guess.index(i)} and {code.index(i)}')
                if i in code and code.index(i) == guess.index(i): #<= bugged: if 2 following characters are equal, it looks at the first input and compares it to the input of the code?
                    black += 1

                elif i in code and code.index(i) != guess.index(i): #<= bugged: if 2 following characters are equal, it looks at the first input and compares it to the input of the code?
                    white += 1

            print(f'You have {white} white pin(s) and {black} black pin(s).\nYou have {10-guesses} guesses left.\n')

        except ValueError:
            print('Sorry, that is not a viable input.')
            continue


def game_mode_2_player1():
    """This game mode will play when the player chooses option 2 in the menu.
    The player plays against another player as player 1."""


    print('Chosen game mode: 2, player 1')


def game_mode_2_player2():
    """This game mode will play when the player chooses option 2 in the menu.
    The player plays against another player as player 2."""


    print('Chosen game mode: 2, player 2')


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
            if game_mode == 1 or game_mode == 2:
                player = int(input('Do you want to play as player 1 or 2?\n'))
                if player != 1 and player != 2:
                    print('That is not an option')
                    continue
                break
            break
        except ValueError:
            print('I\'m sorry, I couldn\'t quite understand your input, please select a game mode (1-3).')
            continue


    if game_mode == 1 and player == 1:
        game_mode_1_player1()
    elif game_mode == 1 and player == 2:
        game_mode_1_player2()
    elif game_mode == 2 and player == 1:
        game_mode_2_player1()
    elif game_mode == 2 and player == 2:
        game_mode_2_player2()


menu()