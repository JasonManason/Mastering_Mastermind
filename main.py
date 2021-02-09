#Jason de Mey, Klas AI V1B, Opdracht 1: Mastering Mastermind
import random
import itertools

def random_code():
    """Creates a random code if player 1 is a bot."""
    colours = {'B':'Blue','Y':'Yellow','R':'Red','G':'Green','P':'Purple','O':'Orange'}
    code = []

    while len(code) < 4: # <= for loop needed for duplicate values
        code.append(random.choice(list(colours.items())))

    return code # <= code is a list with tuples


def random_guess():
    """Bot does a random guess as a test."""
    valid_chars = ['B', 'Y', 'R', 'G', 'P', 'O']
    all_combinations = (list(itertools.product(valid_chars, repeat=4))) # <= list with tuples of 4
    #print(all_combinations) # <= 1296 combinaties mogelijk

    tuple = all_combinations[random.randint(0, 1296)] # <= [0] == ('B', 'B', 'B', 'B')
    guess = ''

    #print(tuple)

    for i in tuple:
        guess += i

    print(guess)


    return guess


def feedback(guess, code):
    """Takes the current guess and code as input and returns feedback in the form of black and white pins.
    This is a tuple, for example: (0,1)."""
    print(f'in feedback: guess: {guess}\tcode: {code}')
    black = 0
    white = 0
    black_checked = []
    black_index_checked = []
    white_checked = []
    white_index_checked = []

    for i, value in enumerate(guess):
        if value == code[i]:
            black += 1
            black_checked.append(value)
            black_index_checked.append(i)

    for i, value in enumerate(guess):
        if value in code and i not in white_index_checked and i not in black_index_checked:
            white += 1
            white_checked.append(value)
            white_index_checked.append(i)

    print(f'feedback = {black}, {white}')
    return (black, white)


def simple_strategy():
    """A guessing algorithm for a bot (as player 2)."""
    valid_chars = ['B', 'Y', 'R', 'G', 'P', 'O']
    all_combinations = (list(itertools.product(valid_chars, repeat=4))) # <= list with tuples of 4
    #print(all_combinations) # <= 1296 combinaties mogelijk
    first_guess = True

    #black, white == (0, 0)

    if first_guess:
        return 'BBYY' # <= eerste guess hardcoded, pragmatised


    new_combinations = []


    # onthoud alle guesses en voeg die NIET in possible_new_guesses
    # neem feedback mee en pas toe op possble new guesses> haal uit wat niet kan

    print(all_combinations[0])


    return guess


def game_mode_1_player1():
    """This game mode will play when the player chooses option 1 in the menu.
    The player plays against a bot as the one who creates a code and gives feedback."""
    valid_chars = ['B', 'Y', 'R', 'G', 'P', 'O']
    code = str(input('You can now enter a code consisting of a 4 letter combination of the first letters of the colours, like so: "YGBP" for Yellow, Green, Blue, Purple.\n'
              'Your choices are:\nB: Blue\nY: Yellow\nR: Red\nG: Green\nP: Purple\nO: Orange\n'
              'The bot will try to guess your code within 10 tries.\n')).upper()

    for i in code:
        if len(code) < 4 or len(code) > 4 or i not in valid_chars:
            print('The code should be a precise length of 4 and only consist of valid colours.\n')
            game_mode_1_player1()

    guesses = 0
    easy = False
    medium = False
    hard = False

    while True:
        difficulty = input('Do you want to play on Easy, Medium or Hard?\n').capitalize()
        if difficulty == 'Easy':
            easy = True
            break
        elif difficulty == 'Medium':
            medium = True
            #game_mode = simple_strategy()
            print('Medium mode WIP')
            break
        elif difficulty == 'Hard':
            hard = True
            #looking_ahead()
            print('Hard mode WIP')
            break
        print('Please type in your wished difficulty mode.')
        continue

    #guess = function > returns random guess 'BBYY'

    while easy:
        if guesses < 11:
            guess = random_guess()
            guesses += 1
            if guess == code:
                print(f'The bot has won within {guesses} guess(es).')
                break
            print(f'The bot has guessed: {guess} and has {11-guesses} guess(es) left.')


    while medium:
        if guesses < 11:
            guess = simple_strategy()
            guesses += 1
            if guess == code:
                print(f'The bot has won within {guesses} guess(es).')
                break
            print(f'The bot has guessed: {guess} and has {11 - guesses} guess(es) left.')
            feedback(guess, code)
        break


    while hard:
        print('Hard mode WIP')
        break


def game_mode_1_player2():
    """This game mode will play when the player chooses option 1 in the menu.
    The player plays against a bot and has to guess the right code."""
    code_list = random_code()
    code = str((code_list[0][0])+(code_list[1][0])+(code_list[2][0])+(code_list[3][0]))
    #print(code)
    print('You are now allowed to guess the code, the code is 4 characters long, there may or may not be duplicate colours.\n'
          'Enter a 4 letter combination of the first letters of the colours, like so: "YGBP" for Yellow, Green, Blue, Purple.\n'
          'Your choices are:\nB: Blue\nY: Yellow\nR: Red\nG: Green\nP: Purple\nO: Orange')

    guesses = 0
    valid_chars = ['B', 'Y', 'R', 'G', 'P', 'O']

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
            black = feedback(guess, code)[0]
            white = feedback(guess,code)[1]

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