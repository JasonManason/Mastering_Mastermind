#Jason de Mey, Klas AI V1B, Opdracht 1: Mastering Mastermind
import random
import itertools

def random_code():
    """
    Creates a random code if player 1 is a bot.
    Returns:
        a random code as a string list with tuples, like [('B', 'Blue'), ('B', 'Blue'), ('Y', 'Yellow'), ('Y', 'Yellow')].
    """
    colours = {'B': 'Blue', 'G': 'Green', 'O': 'Orange', 'P': 'Purple', 'R': 'Red', 'Y': 'Yellow'}
    code = []

    while len(code) < 4:
        code.append(random.choice(list(colours.items())))

    return code


def possible_combinations():
    """
    Creates a list with possible code combinations.
    Returns:
        List with possible combinations as a list with tuples.
    """
    valid_chars = ['B', 'Y', 'R', 'G', 'P', 'O']
    return (list(itertools.product(valid_chars, repeat=4)))


def new_combinations(number_of_guesses):
    """
    Takes in a list of all combinations, the guess and feedback on the guess.
    Reduces the list of possible combinations and returns this.
    Returns:
        A list with combinations as a tuples, like: [('B','B','B','B'),('B','B','B','Y'), etc.]
    """
    all_combinations = possible_combinations()
    new_combinations = []
    last_guesses = []
    guess = simple_strategy(number_of_guesses) # <= string 'BBBB'
    feedback = (guess, ask_code())

    print(feedback)
    print(guess)

    for combo in all_combinations:
        if feedback == (0,0): # <= alles fout. probeer andere kleuren.
            for char in guess:
                if char not in combo:
                    new_combinations.append(combo)
                    last_guesses.append(guess)
                    return new_combinations

        elif feedback == (0,4) or feedback == (2,2) or feedback == (1,3) or feedback == (3,1): # <= sum of 4! Only return list of combo's with the current colours of guess.
            for char in guess:
                if char in combo:
                    new_combinations.append(combo) #>>> NOT INCLUDING LAST GUESS(ES)!
                    return new_combinations

        elif feedback == (0,1) or feedback == (1,0):
            for char in guess:
                if char == combo[0]:
                    new_combinations.append(combo)
                    return new_combinations


        else:
            print('Not yet made, WIP.')

        # FEEDBACK THAT'S NOT SUM 4 OR 0:

        # count 1:
        # elif feedback == (0,1):        # elif feedback == (1,0):
        #SO: keep 1 char > try next combo


        # count 2:
        # elif feedback == (2,0):        # elif feedback == (1,1):
        #SO: keep 2 chars > try next combo


        # count 3:
        # elif feedback == (2,1):        # elif feedback == (1,2):
        # DUS: bewaar 3 chars > probeer next combo

        #try next combo, in order


def ask_code():
    """
    Keeps asking user for a viable code as an input until it's the right format.

    Returns:
        A code as a string, like 'BBYY'
    """
    valid_chars = ['B', 'Y', 'R', 'G', 'P', 'O']
    code = str(input('You can now enter a code consisting of a 4 letter combination of the first letters of the colours, like so: "YGBP" for Yellow, Green, Blue, Purple.\n'
              'Your choices are:\nB: Blue\nY: Yellow\nR: Red\nG: Green\nP: Purple\nO: Orange\n'
              'The bot will try to guess your code within 10 tries.\n')).upper()

    for i in code:
        if len(code) < 4 or len(code) > 4 or i not in valid_chars:
            print('The code should be a precise length of 4 and only consist of valid colours.\n')
            game_mode_1_player1()

    return code


def feedback(guess:str, code:str):
    """
    Takes the current guess and code as input and returns feedback in the form of black and white pins.
    Args:
        guess: The guess of either a player or bot as a string, like 'BBYY'.
        code: The code made by either a player or a bot as a string, like 'BBYY'.
    Returns:
        Feedback on the guess as a tuple, like (0,0).
    """
    #print(f'in feedback: guess: {guess}\tcode: {code}')
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

    #print(f'feedback = {black}, {white}')
    return (black, white)


def random_guess():
    """
    Bot does a random guess as a test, it does not take feedback in consideration.
    Returns:
        A random guess in the form of a string, like 'BBYY'.
    """
    all_combinations = possible_combinations()
    tuple = all_combinations[random.randint(0, 1296)]
    guess = ''

    for i in tuple:
        guess += i

    return guess


def simple_strategy(number_of_guesses):
    """
    A guessing algorithm for a bot (as player 2).

    Returns:
        A guess in the form of a string, like 'BBYY'.
    """
    all_options = possible_combinations()
    guess = ''

    for option in all_options:
        if option in new_combinations(number_of_guesses):
            for char in all_options[number_of_guesses]:
                while len(guess) < 4:
                    guess += char


    print(f'guess:\t {guess}')

    return guess


def looking_ahead():
    """
    The 'Looking one step ahead' strategy.
    Returns:
        A guess in the form of a string, like 'BBYY'.
    """

    return guess


def game_mode_1_player1():
    """
    This game mode will play when the player chooses option 1 in the menu.
    The player plays against a bot as the one who creates a code and gives feedback.
    """
    code = ask_code()
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
            print('Medium mode WIP')
            break
        elif difficulty == 'Hard':
            hard = True
            print('Hard mode WIP')
            break
        print('Please type in your preferred difficulty mode.')
        continue


    while easy:
        if guesses < 11:
            guess = random_guess()
            guesses += 1
            if guess == code:
                print(f'The bot has won within {guesses} guess(es).')
                break

            black = feedback(guess, code)[0]
            white = feedback(guess, code)[1]
            print(f'The bot has guessed: {guess} and has {11 - guesses} guess(es) left.\nYou have {black} black pin(s) and {white} white pin(s).\n')


    while medium and guesses < 11:
        guesses += 1
        guess = simple_strategy(guesses - 1)
        if guess == code:
            print(f'The bot has won within {guesses} guess(es).\nThe guess was: {guess}.')
            break
        black = feedback(guess, code)[0]
        white = feedback(guess, code)[1]
        #print(f'The bot has guessed: {guess} and has {11 - guesses} guess(es) left.\nYou have {black} black pin(s) and {white} white pin(s).\n')

    while hard:
        print('Hard mode WIP')
        break


def game_mode_1_player2():
    """
    This game mode will play when the player chooses option 1 in the menu.
    The player plays against a bot and has to guess the right code.
    Raises:
        ValueError: when a player tries to enter a guess with invalid and/or too less/many characters.
    """
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
    """
    This game mode will play when the player chooses option 2 in the menu.
    The player plays against another player as player 1.
    """


    print('Chosen game mode: 2, player 1')


def game_mode_2_player2():
    """
    This game mode will play when the player chooses option 2 in the menu.
    The player plays against another player as player 2.
    """


    print('Chosen game mode: 2, player 2')


def menu():
    """
    Welcomes the player and asks for what game mode the player(s) want(s) to play.
    The game can be played with 2 players, with one player against a bot or you can watch 2 bots play.
    Raises:
        ValueError: when a player types in an invalid character.
    """

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