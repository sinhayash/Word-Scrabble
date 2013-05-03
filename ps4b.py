from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all possible 
    permutations of lengths 1 to HAND_SIZE.

    If all possible permutations are not in wordList, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = '.'   #In MITx it was None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        checkletter = True
        handcopy = hand.copy()
        for letter in word:            
            if(handcopy.get(letter, 0)==0):
                checkletter = False
                break
            else:
                handcopy[letter] -= 1
        if(checkletter == True):
            # Find out how much making that word is worth
            score = getWordScore(word, HAND_SIZE)
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = word
    # return the best word you found.
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    """
    # DONE...TO DO ... <-- Remove this comment when you code this function
    n = HAND_SIZE
    lettersleft = calculateHandlen(hand)
    score = 0
    # As long as there are still letters left in the hand:
    while(lettersleft > 0):
        # Display the hand
        print 'Current Hand: ',
        displayHand(hand)
        # Ask user for input
        userinput = compChooseWord(hand, wordList)
        print('Enter word, or a "." to indicate that you are finished: '+userinput)
        # If the input is a single period:
        if(userinput == '.'):
            # End the game (break out of the loop)
            print 'Goodbye!',
            break    
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if(isValidWord(userinput, hand, wordList)==False):
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(userinput, n)
                print userinput+' earned '+str(getWordScore(userinput, n))+' points. Total: '+str(score)
                print
                # Update the hand
                hand = updateHand(hand, userinput)
                lettersleft = calculateHandlen(hand)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if not(lettersleft > 0):
        print 'Run out of letters.',
    print ' Total score: '+str(score)+' points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # DONE...TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    inputchar =''
    n = HAND_SIZE
    lasthand = {}
    while not(inputchar == 'e'):
        n = random.randrange(3, 10)
        inputchar = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if inputchar == 'n':
            hand = dealHand(n)
            lasthand = hand.copy()
            userOrComputerPlay(hand, wordList, n)
            #print 'jhfg'
        elif inputchar == 'r':
            if lasthand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                hand = lasthand.copy()
                userOrComputerPlay(hand, wordList, n)
                #print 'uyg'
        elif inputchar == 'e':
            break
        else:
            print 'Invalid command.'
    print

def userOrComputerPlay(hand, wordList, n):
    inputchar = ''
    while not((inputchar == 'u') or (inputchar == 'c')):
        inputchar = raw_input('If you want to play enter u, or if you want to let computer play enter c: ')
        if inputchar == 'u':
            playHand(hand, wordList, n)
        elif inputchar == 'c':
            compPlayHand(hand, wordList)
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

    #print "Goodbye!"
