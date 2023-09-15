'''--------------------------------------------------------------------------------------------------
                        CSC 3510 Introduction to Artificial Intelligence
                                    Florida Southern College
                            HW1: Getting Started with AI in Python

                                        Hunter Odom
                                              &
                                          Tre Cobb
                                                                                                     '''
'''--------------------------------------------------------------------------------------------------
                                    IMPORTANT PROJECT INFORMATION:
   --------------------------------------------------------------------------------------------------
    The following repository wordle, is a sub-repository of wordleAI. This sub-repository has been 
    cloned inside this repo and its credit goes to github user meicholtz at the following link:
    https://github.com/meicholtz/wordle. 

    In order to utilize the commands to play the game one must navigate using ls and cd to the directory
    wordle to be able to run them or else it will result in error. 

    For example: if you are on the main repository, execute ls to see the directories available, and then
    execute cd wordle to enter the right repository to run the commands for the game.

    Additonally in order to execute git, commit, and push commands, you must ensure that you are in
    the wordleAI repository in order to push the changes. If you are in wordl directory then try to run
    those commands it actually tries to send the changes to the meicholz world repository which access
    will be immediately denied.

    Execute cd .. to go back to wordleAI directory if in wordle directory
   ---------------------------------------------------------------------------------------------------'''
'''--------------------------------------------------------------------------------------------------
                                    WordleAI Project Commands:
   --------------------------------------------------------------------------------------------------
                        Use the following commands to play the game:

    To play Wordle as a human player:

    python wordle.py

    To play Wordle using our AI player:

    python wordle.py -ai twinsnakes

   ---------------------------------------------------------------------------------------------------'''

'''--------------------------------------------------------------------------------------------------
                                    WordleAI Project Description:
   --------------------------------------------------------------------------------------------------
    This project is a Python-based AI player for the game Wordle which can be played at the following
     link: https://www.nytimes.com/games/wordle.

     The game Wordle operates as followed: the goal is to guess a randomly selected 5-letter word 
     with a maximum of 6 total guesses. After making a guess, the user will receive feedback to guide
     future guesses;

     GREEN if its in the world and in the correct position

     YELLOW if its in the word, but in the wrong position

     WHITE/GRAY if its not in the word

     Each guess must be a valid word, so for example, guessing AEIOU will not work.

   ---------------------------------------------------------------------------------------------------'''

'''--------------------------------------------------------------------------------------------------
                                            Imports Section:
   --------------------------------------------------------------------------------------------------'''
import utils
import argparse
'''--------------------------------------------------------------------------------------------------
                                            Program Start:
   --------------------------------------------------------------------------------------------------'''

# -------------------------------------------------------------------------------------------------------
#                                   Make Guess Method
# -------------------------------------------------------------------------------------------------------



def makeguess(wordlist, guesses=[], feedback=[]):
    """Guess a word from the available wordlist, (optionally) using feedback
    from previous guesses.
    Parameters
    ----------
    wordlist : list of str
        A list of the valid word choices. The output must come from this list.
    guesses : list of str
        A list of the previously guessed words, in the order they were made,
        e.g. guesses[0] = first guess, guesses[1] = second guess. The length
        of the list equals the number of guesses made so far. An empty list
        (default) implies no guesses have been made.
    feedback : list of lists of int
        A list comprising one list per word guess and one integer per letter
        in that word, to indicate if the letter is correct (2), almost
        correct (1), or incorrect (0). An empty list (default) implies no
        guesses have been made.
    Output
    ------
    word : str
        The word chosen by the AI for the next guess.
    """

    '''--------------------------------------------------------------------------------------------------
                                                Global Variables:
       --------------------------------------------------------------------------------------------------'''
    # global saves the vars in whatever state we leave them in, not matter how many times we call a function

    global alphabet  # used for storing letters of the alphabet and to be removed when used in a guess
    global listOfWords  # used as a listing variable to use the list of words within the file.
    global priority  # used for a list of common letters that should be prioritized to help with smart guessing
    '''--------------------------------------------------------------------------------------------------

       --------------------------------------------------------------------------------------------------'''

    # Create a variable called guess to be used for guesses and have it saved as 'SOARE' for the first word to guess
    guess = 'TRACE' # or use SALET

    if not len(guesses):  # if no guesses have been made, guess 'SOARE"

        # Create a variable called alphabet that contains a string of the letters of the alphabet.
        # alphabet will be used to remove letters from the string as guesses are being made
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # the following is a list called priority and have it contain letters that appear often in words to be used
        # for potential likelier guesses
        priority = ['I', 'T', 'N', 'L', 'C', 'U']

        # Create a variable list called listOfWords that contains the wordlist with the 12k+ words for wordle
        listOfWords = wordlist

        # Create a loop that iterates through the guess and replaces the corresponding letter at its place in the word
        # within the alphabet string with empty space, effectively removing it.

        # iterate through the guess:
        for i in range(len(guess)):
            # replace the letters used in the guess with empty space to remove it from the alphabet string
            alphabet = alphabet.replace(guess[i], '')

        # return the guess
        return guess


    else:
        # # this sorts out all the bad guess base off feed back received
        listOfWords = sortOutBadGuesses(listOfWords, feedback, guesses)

        maxCount = 0
        maxIndexes = [0]
        i = 0
        for word in listOfWords:
            u = getUniqueCharacters(word)
            if u > maxCount:
                maxCount = u
                maxIndexes = [i]
            elif u == maxCount:
                maxIndexes.append(i)
            i += 1
        # Find all words with the most unique characters
        maxScore = 0
        maxScoreIndex = 0
        for i in maxIndexes:
            score = 0
            for char in priority:
                if char in listOfWords[i]:
                    score += 1
            if score > maxScore:
                maxScore = score
                maxScoreIndex = i
        guess = listOfWords[maxScoreIndex]
        listOfWords = listOfWords[:maxScoreIndex] + listOfWords[maxScoreIndex + 1:]
        return guess


# Create a method that removes words not related to the potential daily word and removes all the bad guesses that could
# be made. This method uses the feedback from the previous guesses and works to eliminate words in the wordlist to
# enhance chance of success of guessing the right word
def sortOutBadGuesses(listofwords, feedback, lastGuess):
    feedback = feedback[len(feedback) - 1]  # getting the lastest feedback in the list
    lastGuess = lastGuess[len(lastGuess) - 1]  # getting the lastest guess in the list
    lastGuessString = ''.join(lastGuess)
    oneAndTwoLetters = []
    copyOfList = listofwords.copy()
    if 2 in feedback:
        # First look at 2s
        for i in range(len(feedback)):
            if feedback[i] == 2:
                if lastGuessString[i] not in oneAndTwoLetters:
                    oneAndTwoLetters.append(lastGuessString[i])
                    # Add the letter found in twos to the ignore list for zeros
                # Go through all the twos first, they are the highest priority
                for word in copyOfList:
                    if word[i] != lastGuessString[i]:
                        # If a word doesnt have the same letter at the same position of a one, remove it
                        if word in listofwords:
                            listofwords.remove(word)
                        # print("Word removed")
                    # else:
                    #     print(word, i, lastGuessString)

        # print(listofwords, "After twos")

    if 1 in feedback:
        # Then look at 1s
        # These will never be the same letter as a two
        # Meaning we are safe to remove everything that doesn't match
        for i in range(len(feedback)):
            if feedback[i] == 1:
                if lastGuessString[i] not in oneAndTwoLetters:
                    oneAndTwoLetters.append(lastGuessString[i])
                    # Add the letter found in ones to the ignore list for zeros
                for word in copyOfList:
                    if word[i] == lastGuessString[i]:
                        # If the word has the same letter at the same position of a one, remove it
                        if word in listofwords:
                            listofwords.remove(word)
                        pass
                    elif lastGuessString[i] not in word:
                        # If the word doesnt contain the letter at all remove it
                        if word in listofwords:
                            listofwords.remove(word)

        # print(listofwords, "After ones")
    # print(oneAndTwoLetters)
    if 0 in feedback:
        # Finally look at 0s
        # This part we have to be careful of, it can occur at the same time as either a two or a one.
        for i in range(len(feedback)):
            if feedback[i] == 0:
                if lastGuessString[i] not in oneAndTwoLetters:
                    # print("Not in")
                    for word in copyOfList:
                        if lastGuessString[i] in word:
                            if word in listOfWords:
                                listofwords.remove(word)

        # print(listOfWords, "After zeros")
    # print(listofwords)
    return listofwords

def getUniqueCharacters(word):
    currentChars = []
    count = 0
    for char in word:
        if char not in currentChars:
            currentChars.append(char)
            count += 1
    return count



if __name__ == "__main__":
    wordlist = utils.readwords('./wordle/')
    print(f"AI: \"My next choice would be {makeguess(wordlist)}\"")

'''--------------------------------------------------------------------------------------------------
                                            Program End:
   --------------------------------------------------------------------------------------------------'''