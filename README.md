This project is for educational purposes only.


## Sources:
    Boss, R. (2021, 19 januari). HU Structured Programming - Mastermind. Youtube. https://www.youtube.com/watch?v=rSzX2TtjvHA&feature=youtu.be
    Kooi, B. (2005). YET ANOTHER MASTERMIND STRATEGY. ICGA Journal, 28(1), 13–20. https://doi.org/10.3233/icg-2005-28105
        

## Use of modules:
    random generator
    itertools


## Summary:
    Program will as the player what gamemode they want to play.
    Player confirms choice.
    Game will start in that gamemode.
    If the player plays against another player, they will have to take turns.
    If the player decides to play against the bot, they can select a difficulty, the bot will perform a different strategy based on this choice.
    If the player chooses to watch two bots play, they "guessing" bot will perform a random strategy.
    The guessing player gets 10 turns to guess the secret code combination of the other player.
    The player with the code gets to give feedback in the form of white, black or no pins or any combination thereof consisting of a maximum of 4 pins.
    A black pin means: One of the guesses is in the right place.
    A white pin means: One of the guesses was right, but sits in the wrong place.
    If the code doesn't get guessed by player 1, player 2 wins.
    If the code gets guessed within 10 turns, player 1 wins.


## pseudocode:
## Function for menu creation:
    The menu what gamemode the player wants to play
    
    if player = player 1:
        let player pick code consisting of 4 spots, with a choice of 6 colours

    if player = player 2:
        call on function to create random code for player 1

    function returns player choice
    

## Functie random code:
    Function creates random code in the form of a key, value pair
    key = number
    value = colour
    
    the dictionary length is 6

    generate random code from dictionary with a lengte of 4
    This is still a key, value pair

    functie returns code
    

## Generate rules:
    If player 2 has guessed 10 times
        the game ends and player 1 wins
    if player 2 has guessed 8 or 9 times
        give the player a warning with how many moves are left



## Function guessing:
    try:
        input, ask player 2 to make a guess
    if the input is too long unreadable, not in the right form
        ask the player to make another guess, reminding them of the format

    function returns the guess


## Function check guess:
    guess = call on function guessing
    feedback = empty text: ''
    answer = function code


    check if guess is the same as the answer
        if the guess and the answer are the same
            return that player has won the game

        if the guess has one or more pins in the right place
            give feedback like: 2,0,0,0 > 1 is in the right place, 3 are not in the code

        if the guess has one or more of the same pin from the answer AND they are in the wrong place
            give feedback like: 1,0,1,0 > 2 of the pins are in the code, but in a different place

    function returns feedback in the form of a count of 0's, 1's and 2's
    for example: there were two 1's and two 0's    
    (keeping in mind a maximum amount of pins of 4)
