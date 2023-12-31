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

    '''--------------------------------------------------------------------------------------------------
                                                Global Variables:
       --------------------------------------------------------------------------------------------------'''
    # global saves the vars in whatever state we leave them in, not matter how many times we call a function

    global alphabet # used for storing letters of the alphabet and to be removed when used in a guess
    global listOfWords # used as a listing variable to use the list of words within the file.
    global priority # used for a list of common letters that should be prioritized to help with smart guessing
    '''--------------------------------------------------------------------------------------------------
                                                
       --------------------------------------------------------------------------------------------------'''

    # Create a variable called guess to be used for guesses and have it saved as 'SOARE' for the first word to guess
    guess = 'SOARE'

    if not len(guesses): #if no guesses have been made, guess 'SOARE"

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
        # this sorts out all the bad guess base off feed back received
        listOfWords = sortOutBadGuesses(listOfWords, feedback, guesses)
        print(listOfWords)
        twos = [i for i ,e in enumerate(feedback[len(feedback) - 1]) if e == 2]
        for i in range(len(listOfWords)):
            word = listOfWords[i]
            if are_indices_unique(word, twos):
                print(word)
                return word
        return listOfWords[0]
        
        # iterates over the list of words and returns a word as soon as one of the words contains the priority letter
        #
        # for word in listOfWords:
        #     for letter in priority:
        #         if letter in word:
        #             return word


# Create a method that removes words not related to the potential daily word and removes all the bad guesses that could
# be made. This method uses the feedback from the previous guesses and works to eliminate words in the wordlist to
# enhance chance of success of guessing the right word
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
    zeros = [i for i ,e in enumerate(feedback) if e == 0]
    
    copy_of_list = listofwords.copy()


    for i in range(len(copy_of_list)):
        continue_outer_loop = False
        word = copy_of_list[i]
        if len(zeros) == 5:
            for j in range(len(zeros)):
                if lastGuessString[zeros[j]] in word:
                    #breakpoint()
                    listofwords.remove(word) #If im deleting the word, theres no need to check for 2's. So i made a continue onto the next word flag
                    continue_outer_loop = True
                    break
            if continue_outer_loop: #continues onto the next word in the list
                continue
        if len(zeros):
            for j in range(len(zeros)):
                if lastGuessString[zeros[j]] == word[zeros[j]]:
                    #breakpoint()
                    listofwords.remove(word) #If im deleting the word, theres no need to check for 2's. So i made a continue onto the next word flag
                    continue_outer_loop = True
                    break
            if continue_outer_loop: #continues onto the next word in the list
                continue
        #if there are 2's in feedback, im checking them against the words in the list    
        if len(twos):
            for j in range(len(twos)):
                if word[twos[j]] != lastGuessString[twos[j]]: #if the position of the letter does not match the word, im deleting word
                    #breakpoint()
                    listofwords.remove(word)
                    #If im deleting the word, theres no need to check for 1's. So i made a continue onto the next word flag
                    continue_outer_loop = True
                    break
            if continue_outer_loop:
                continue

        #if there are 1's in feedback, im checking them against the words in the list
        if len(ones):
            for j in range(len(ones)):
                #if the letter is not in the word from the list of words or if the letter is right but in the wrong place. delete the word
                if lastGuessString[ones[j]] not in word or lastGuessString[ones[j]] == word[ones[j]]:
                    #breakpoint()
                    listofwords.remove(word)
                    break
    return listofwords

def has_unique_letters(word):
    # Create a set to store encountered letters
    letter_set = set()

    # Iterate through each letter in the word
    for letter in word:
        # If the letter is already in the set, it's not unique
        if letter in letter_set:
            return False
        # Otherwise, add it to the set
        letter_set.add(letter)

    # If we've gone through the entire word without finding a duplicate, it has unique letters
    return True

def are_indices_unique(word, indices):
    """
    Check if a list of indices are unique within the word.

    Args:
    - word (str): The input word.
    - indices (list of int): List of indices to check for uniqueness.

    Returns:
    - bool: True if all indices are unique, False otherwise.
    """
    if not indices:
        return False  # Empty list of indices

    for index in indices:
        if index < 0 or index >= len(word):
            return False  # Index out of range

    char_counts = {}
    for index in indices:
        char = word[index]
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return all(count == 1 for count in char_counts.values())
if __name__ == "__main__":
    wordlist = utils.readwords('wordle/allwords5.txt')
    print(f"AI: \"My next choice would be {makeguess(wordlist)}\"")