

import utils

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

    # global saves the vars in whatever state we leave them in, not matter how many times we call a function
    global alphabet
    global listOfWords


    if not len(guesses): #if no guesses have been made, guess 'SOARE"
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        listOfWords = wordlist
        guess = 'SOARE'
        for i in range(len(guess)):
            alphabet = alphabet.replace(guess[i], '')
        guess = guess.lower()
        return guess
    
    else:
        # this sorts out all the bad guess base off feed back received 
        listOfWords = sortOutBadGuesses(listOfWords, feedback, guesses)
        # This is how far i got, still needs word




    return 'Loser' 
    
    
def sortOutBadGuesses(listofwords, feedback, lastGuess):

    feedback = feedback[len(feedback) - 1] #getting the lastest feedback in the list
    lastGuess = lastGuess[len(lastGuess) - 1] #getting the lastest guess in the list
    lastGuessString = ''.join(lastGuess) 
    # variables below makes a list of where the 2 or 1 is in the guess word based off feedback
    # for ex. below is the guess word 'soare', notices the 2's are at index 0 and 4
    # 1 is at index 2
    # [(2, 'S'), (0, 'o'), (1, 'a'), (0, 'r'), (2, 'e')]
    # [0, 4] [2]
    twos = [i for i ,e in enumerate(feedback) if e == 2]
    ones = [i for i ,e in enumerate(feedback) if e == 1]
    
    # if feedback returns all 0's, Im delete every word with those letters out the list
    if not len(twos) and not len(ones):
        for i in range(len(listofwords)):

            word = listofwords[i]

            for i in lastGuessString:
                if i in word:
                    del listofwords[i]
                    break
    
    # else im going through all the words in the list and matching the letters from feedback
    else:
        for i in range(len(listofwords)):
            continue_outer_loop = False
            word = listofwords[i]

            #if there are 2's in feedback, im checking them against the words in the list 
            if len(twos):
                for j in range(len(twos)):
                    if word[twos[j]] != lastGuess[twos[j]]: #if the position of the letter does not match the word, im deleting word
                        del listofwords[i]
                        #If im deleting the word, theres no need to check for 1's. So i made a continue onto the next word flag
                        continue_outer_loop = True
                        break
                if continue_outer_loop:
                    continue

            #if there are 1's in feedback, im checking them against the words in the list 
            if len(ones):
                for j in range(len(ones)):
                    if lastGuess[ones[j]] not in word:
                        del listofwords[i]
                        break
    return listofwords

if __name__ == "__main__":
    wordlist = utils.readwords('wordle/allwords5.txt')
    print(f"AI: \"My next choice would be {makeguess(wordlist)}\"")
