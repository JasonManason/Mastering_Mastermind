##This project is for educational purposes only.

##pseudocode:

## functie met menu aanmaken:
    vraag gebruiker of ze speler 1 of 2 willen zijn met input
    
    als speler = speler 1:
    laat code kiezen

    als speler = speler 2:
    roep functie code_genereren.

    functie geeft speler terug
    

## functie random code:
    geef key, value pairs van cijfers en kleuren waarbij:
    key = cijfer
    value = kleur
    
    de dictionary length is 6

    generate random code uit dictionary met een lengte van 4
    de code is een tekst, voorbeeld: '1234'

    functie geeft de code terug
    

## genereer bord:
    map het hele bord uit:

    bord = lengte * breedte bord 
    speelgedeelte speler 1 = zijkant 2 bij zoveel
    
    speelgedeelte speler 2 = middelste 4 bij zoveel

    functie geeft bord terug


## functie gokken:
    probeer:
        input, vraag speler 2 om gok te doen
    als de input verkeerd is:
        vraag nogmaals om gok te doen, herinner de speler aan het formaat '1234'

    functie geeft de gok terug


## functie controleer gok:
    gok = roep functie gokken aan
    feedback = een lege tekst: ''

    controleer of gok gelijk is aan antwoord
        als de gok gelijk is aan antwoord
            geef terug dat de speler heeft gewonnen

        als de gok een of meerdere van dezelfde pin op de juiste plek heeft staan
            geef feedback terug als bijv: 2,0,0,0 > 1 staat goed, 3 zitten er niet in
        als de gok een of meerdere van dezelfde pin uit het antwoord heeft EN op een andere plek:
            geef feedback terug als bijv: 1,0,1,0 > 2 zitten in het antwoord, maar op andere plek.

    functie geeft feedback terug, bijv: [1,0,2,0]


