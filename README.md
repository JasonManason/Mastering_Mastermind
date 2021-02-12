This project is for educational purposes only.


## Sources:
    Boss, R. (2021, 19 januari). HU Structured Programming - Mastermind. Youtube. https://www.youtube.com/watch?v=rSzX2TtjvHA&feature=youtu.be
    Kooi, B. (2005). YET ANOTHER MASTERMIND STRATEGY. ICGA Journal, 28(1), 13–20. https://doi.org/10.3233/icg-2005-28105
        

## Use of modules:
    random generator
    itertools
    
    
## User instructions:
    When you run the program, you can pick one of the 3 menu options by typing in the corresponing number.
    After picking a game mode, you can choose as which player you want to play.
    When picking game mode 1, player 1 you also get to pick the difficulty.
    Right now you can only play on easy.
    When picking game mode 1, player 2 you get to guess the code the bot has made.
    If you guess the code within 10 rounds, you have won, otherwise the bot wins.
    Furthermore, you get feedback in the form of black and white pins.
    A black pin means one of your guesses is in the correct spot.
    A white pin means one of your guesses is in the code, but not in the right spot.
    
    Alltogether, Make sure to have fun!



## pseudocode:
## Function for menu creation:
    The menu asks what gamemode the player wants to play
    
    if player = player 1:
        let player pick code consisting of 4 spots, with a choice of 6 colours

    if player = player 2:
        call on function to create random code for player 1

    function returns game mode and player choice
    

## Function random code:
    Function creates random code in the form of a string

    function returns code
   
   
## Function possible combinations:
    Function creates all possible combinations of colours
    
    function returns a list of possible codes
    
    
## Function new combinations
    Function reads all possible combinations of possible combinations functions
    
    With feedback on the last made guess
        if feedback is a sum of 4 pins
            create possible combinations list with only the colours of the current guess
           
        if feedback is a sum of 0 pins
            do not use any of the current colours of the current guess anymore
            
        if feedback is a sum of 1
            keep one of the colours
        
        if feedback is a sum of 2
            keep two of the colours
        
        if feedback is a sum of 3
            keep three of the colours
            
      Function returns a new list of possible combinations
      
 ## Function feedback
    Function checks both the code and the current guess and returns black or white pins according to the accuracy of the guess
    
    Function returns number of black and white pins, with a maximum total together of 4 pins
    

## Function ask player for code
    If player has chosen to play against a bot as the one who has to make a code,
    ask the player for a code
    keep asking for code until input is the right format
    
    Function returns the code
    

## Function random guess
    If the bot has to do a guess against the player
    try a random combination of colours
    
    function returns a random guess
    
 ## Function simple strategy
    Count all the possible guesses up til 10
    Ask for a list of the current possible combinations
    
    grab the first possible combination from function new combinations
    
    function returns this guess
        

