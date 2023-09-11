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
                        
    To play Wordle using an AI player:
                    
    python wordle.py -ai ai_player

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
import pdb # import a python debugger




'''--------------------------------------------------------------------------------------------------
                                            Program Start:
   --------------------------------------------------------------------------------------------------'''

 # Create a method called makeguess that takes in the allwords5.txt word list, the guesses,
 # as well as the feedback of those guesses.
def makeguess(wordlist, guesses=[], feedback=[]):
    """Guess a word from the available wordlist, (optionally) using feedback
     from previous guesses."""



def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'\nYes! {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('\nWordleAI test is a success')

'''--------------------------------------------------------------------------------------------------
                                            Program End:
   --------------------------------------------------------------------------------------------------'''