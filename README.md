## <span style="color:tan"> CSC 101 Final Project W2025: High Score Poker Game
### Jeremy Lopanec, Ruben Moulton Huber

### <span style="color:tan"> Purpose 
The purpose of this project is to utilize skills developed in this course and test out 
the capabilities Python has when it comes to coding games, performing tests to ensure things
are working as intended. 

### <span style="color:tan"> Description
This project is Poker game where you can bet your points starting at 500 and see how 
long you can continuously win or lose before you exceed your personal high score or lose with 0 points.

### <span style="color:tan"> Project Files
Below is a written description of all the included project files.

    README.md - This is the markdown file that documents the majority of the project, inluding data types, file uses, etc.

    data.py - This is the file which holds the class data for the 'Card' class and initalizes the deck of 'Card' objects.

    data_tests - This file contains the necessary tests to ensure functionallity of the 'Card' class

    play_poker - This is the 'driver file' where the game will be executed.

    poker_code - This file contains all the background functions of the poker game. These functions allow the player to recieve a deck of cards and make a bet against the dealer.

    poker_tests - This file contains the necessary tests to ensure functionality of the poker game. Tests verfify the length of the hand, the comparing betwen hands, and the betting process.

### <span style="color:tan"> Data Structures To Be Used
We will utilize Classes, Lists, Dictionaries, Strings, and Control Structures in the project.

    Class: Card - Will set up object 'Card' that contains a suit and a rank. 

    Dictionary: Rank Order - This dictionary contains the value of the ranks.

    Dictionary: Hand Order - This dictionary contains the values of the types of hand.

    List: Deck - This list hold the 52 cards of a traditional deck in a randomly suffled order. 

### <span style="color:tan"> Function Descriptions

    shuffle - Shuffles a deck of 52 cards. Input = deck, Output = deck
    
    sort_ranks - Sorts a hand of five cards in order of descending rank. Input = list of Cards, Output = list of Cards

    hand_type - Determines the highest type of the hand of the input hand. Input = list of Cards, Output = string

    dealer_hand - Determines the type of hand held by the dealer. Input = list of Cards, Output = string

    your_hand - Determines the type of hand held by the player. Input = list of Cards, Output = string

    get_hand_value - Determines the hand value held by the player by finding its type in a dictionary of hand values. Input = list of Cards, Output = int

    get_dealer_hand_value - Determines the hand value held by the dealer by finding its type in a dictionary of hand values. Input = list of Cards, Output = int

    win_or_lose - 

    betting - 

    play game - 

    game_statrt - 

    


### <span style="color:tan"> <ins> Credits and Distribution
    Repository Setup - Ruben 

    Class Initialization - Jeremy

    Deal Hand Function - Jeremy / Ruben

    Compare Hands Function - Jeremy

    Main Game Initialization - Jeremy

    Main Game Implementation - Ruben

    Bet Function - Ruben

    Data Test Cases - Jeremy

    Poker Game Test Cases - Ruben

    Markdown - Ruben





