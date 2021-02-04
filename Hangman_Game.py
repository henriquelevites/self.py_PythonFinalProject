def launch_game():
    'The function prints the "Welcome Screen" designed for the Hangman game.'
    
    HANGMAN_ASCII_ART = """                             
           _    _                                            
          | |  | |                                           
          | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     
          |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    
          | |  | | (_| | | | | (_| | | | | | | (_| | | | |   
          |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   
                               __/ |                         
                              |___/  
    \n\n
    """							  
							  
    MAX_TRIES = 6
    # Print how many (failed) guessing attempts are allowed for the player in the game:
    print(HANGMAN_ASCII_ART, "You will have " + str(MAX_TRIES) + " attempts to guess the word\n\n") 

# ==============================================================================================
    
def print_hangman(num_of_tries):
    """The function prints one of the seven states of the hangman, according to number of wrong letters guessed.
       :param num_of_tries: number of times user guessed wrong
       :type num_of_tries: int
       :return: the state of the hangman
       :rtype: str
    """
    hangman_photos = {}    # Type of hangman_photos is dictionary.
    hangman_photos[0] = "    x-------x\n"
    hangman_photos[1] = """
    x-------x
    |
    |
    |
    |
    |\n"""
    hangman_photos[2] = """         
    x-------x  
    |       |
    |       0
    |
    |
    |\n"""
    hangman_photos[3] = """         
    x-------x  
    |       |
    |       0
    |       |
    |
    |\n"""
    hangman_photos[4] = """         
    x-------x  
    |       |
    |       0
    |      /|\\
    |
    |\n"""
    hangman_photos[5] = """         
    x-------x  
    |       |
    |       0
    |      /|\\
    |      /
    |\n"""
    hangman_photos[6] = """         
    x-------x  
    |       |
    |       0
    |      /|\\
    |      / \\
    |\n"""
    print(hangman_photos[num_of_tries])                                  

# =====================================
                                
def choose_word(file_path, index):
    """The function receives a path to a file containing words, 
       and an index that will point to the position of a word in the file which will be the secret word to guess. 
       :param file_path: path to text file
	   :param index: position of the word in the file
	   :type file_path: string
	   :type index: int
	   :return secret_word: word in the position received as index, which will be used as the secret word
       :rtype: string
	"""
    with open(file_path,'r') as words:                  # Open file entered by user in read mode only.
        words_one_string = words.read()                 # Return all file content as one string, and assign to parameter 'words_one_string'.
        splited_words = words_one_string.split(" ")     # Split the string 'words_one_string' in a list, and assign the list to parameter 'splited_words'.
        index = (index % len(splited_words)) - 1        # Locate the position in the list according to index entered by user. 
                                                        #  The modulo operator (%) is used in case user enters a value equal to zero or
                                                        #  greater than the total number of words in words file.
        secret_word = splited_words[index]              # The word in 'splited_words' list in the position of the index is assigned to string 'secret_word'. 
        
    return secret_word  

# ==========================================================

def check_valid_input(letter_guessed, old_letters_guessed):
    """The function receives an input character from the player and a list of letters the player guessed so far. 
       The function checks two things: the input validity, and if the player already guessed this input before,
       and returns a boolean value that represents whether the character is valid or not.
       :param letter_guessed: the character entered by the player.
       :param old_letters_guessed: the list contains the letters the player has guessed so far.
       :type letter_guessed: string
       :type old_letters_guessed: list[string]
       :return: True if character is valid, or False otherwise
       :rtype: boolean
       """
    if (len(letter_guessed) > 1)     or (not letter_guessed.isalpha())      or (letter_guessed in old_letters_guessed):
    # If string has 2 or more chars  or if string has non-English character or if string is already in the old_letters_guessed list
                                                                               #  (i.e. this string was guessed in the past so it's illegal to guess it again):
        return False

    else:                                                                      # If the string letter_guessed is valid:
        return True

# =================================================================

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Function's logic: 
       If the input letter is correct (i.e. one English letter) and was not guessed before, 
       the function will add the letter to the list of guessed letters. 
       If the input letter is incorrect (i.e. not a single English letter) or is already in the list of guessed letters, 
       the function will print the character X (the uppercase X) and the list of guessed letters sorted alphabetically and separated by arrows.
       The list's print is to remind the player which letters he has already guessed.
       :param letter_guessed: the character entered by the player.
       :param old_letters_guessed: the list containing the letters the player has guessed so far.
       :type letter_guessed: string
       :type old_letters_guessed: list[string]
       :return: True if the adding of character to list was successful, or False otherwise
       :rtype: boolean
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):    # Call the function 'check_valid_input' in case the input is not valid.
        print("\nX")                                                  # Print the character X (the uppercase X). 
        arrow = ' -> '                                                # String used to separate elements in 'old_letters_guessed' list.
        print(arrow.join(sorted(old_letters_guessed)))                # Print the list of guessed letters sorted alphabetically and separated by arrows.
        return False
    else:                                                             # If the string letter_guessed is valid:
        old_letters_guessed += letter_guessed.lower()                 #  add the input letter to the list of guessed letters.
        return True

# =====================================================

def show_hidden_word(secret_word, old_letters_guessed):
    """The function shows the progress of the player in guessing the secret word
       :param secret_word: represents the secret word the player needs to guess
       :param old_letters_guessed: the list containing the letters the player guessed so far
       :type secret_word: string
       :type old_letters_guessed: list[string]
       :return: Letters and underscores, which display the letters from the list of guessed letters that are in the secret word
                in their respective positions, and the rest of the letters (which the player has not yet guessed) as underscores.
       :rtype: string
    """
    new_string = []                                              # Create an empty list of strings 'new_string' that will be used to compose the function's output string 'show_word'.
    for letter in secret_word:                                   # In the loop, we pass each letter in secret_word.
        if letter in old_letters_guessed:                        # If that letter is in the 'old_letters_guessed' list,
            new_string += letter                                 # append it to the list of strings 'new_string'.
        else:
            new_string += '_'                                    # If it is not, append the character '_' to the list of strings 'new_string'.
    show_word = " "                                              # Create new string 'show_word'.
    show_word = show_word.join(new_string[0:len(new_string)])    # Joins elements of 'new_string' by space (" ") and stores in string show_word
    return show_word                                             # Return letters/underscores, according to guessed/not guessed letters

# ==============================================

def check_win(secret_word, old_letters_guessed):
    """The function checks whether the player managed to guess the secret word and thus won the game!
       :param secret_word: represents the secret word the player needs to guess
       :param old_letters_guessed: the list containing the letters the player guessed so far
       :type secret_word: string
       :type old_letters_guessed: list[string]
       :return: True if player guessed the word, or False if not.
       :rtype: boolean
    """
    check_win_word = show_hidden_word(secret_word, old_letters_guessed)    # Call the function 'show_hidden_word' to assign the current string of letters and spaces 
                                                                           #  (and underscores if has) to string 'check_win_word'.
    check_win_word = check_win_word[0:len(check_win_word):2]               # Use slicing with step to change the same string to a string of letters (and underscores if has) without spaces.
    if check_win_word == secret_word:                                      # If current string 'check_win_word' and the secret word are the same:    
        return True                                                        # Means that the player wins the game.
    else:
        return False                                                       # If strings are not the same, the player still not guessed the secret word.

# ==================        
    
def main():

    MAX_TRIES = 6    # Fixed parameter that represents the maximum number of tries the player has to guess the secret word.
   
    launch_game()    # Call the function 'launch_game' to print the Welcome Screen
    
    file_path = input("Enter file path: ")   # Ask the player to enter the path to file of words.
    
    """The following try-except block is to check if file of words exists, and stop the program with a user friendly message.
       When trying to open the file 'file_path', if the path is not correct or file doesn't exist, a FileNotFoundError exception is raised
       and proper message is printed
    """
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("File not accessible. Please rerun the program and enter a valid path, including the file name.\nExample of valid path: C:\words.txt")
        return
                                               
    """The following try-except block is to check if the index is valid and stop the program with a user friendly message.
        When entering an input string, if the string cannot be converted to integer, a ValueError exception is raised and proper message is printed.
        Note: index is the position for a word in the file of words. 
              According to player's input, the secret word for the game will be selected.
    """
    try:
        index = int(input("Enter index: ")) # Ask the player to enter the index for the file of words.      
    except ValueError:
        print("Index not valid. Please rerun the program and enter an integer number")
        return
        
    print("\nLet's start!\n")
    print_hangman(0)                               # Call the function 'print_hangman' to print the initial state of the game.
    secret_word = choose_word(file_path, index)    # Call the function 'choose_word' to return the secret_word.
    
    
    print ("_ " * (len(secret_word)))              # Print the word pattern for which the player must guess letters, that is, the number of letters that make up the secret word.
    
    
    old_letters_guessed = []                       # Create an empty list that will store the letters guessed by the player. 
    num_of_tries = 1                               # Start count number of failed tries from 1.
        
    while (not check_win(secret_word, old_letters_guessed)):    # Call the function 'check_win' to run the loop while the player doesn't guess the secret word.
        letter_guessed = input("\nGuess a letter: ").lower()    # Get a character from the player and lowercase it to parameter letter_guessed.
        
        # Call the function 'try_update_letter_guessed' to print wrong guesses outputs or to add the right guessed letter to secret word:
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):       # If valid input letter was added to list of guessed letters:
            if letter_guessed in secret_word:                                    # If the input letter is in secret word:
                print('\n' + show_hidden_word(secret_word, old_letters_guessed)) # Call the function 'show_hidden_word', that returns letters/underscores, according to guessed/not guessed letters.
                if check_win(secret_word, old_letters_guessed):                  # If all letters in secret word are in list of letters guessed: 
                    print("\nWIN!")                                              # Print message 'WIN', meaning that the player guessed all the secret word.
                    break                                                        # Stop and leave the program.
            else:
                print("\n:(")
                print_hangman(num_of_tries)                                      # Print the state of the hangman.
                print(show_hidden_word(secret_word, old_letters_guessed))        # Call the function 'show_hidden_word', that returns letters/underscores, according to guessed/not guessed letters.
                if num_of_tries == MAX_TRIES:                                    # If the player guessed 6 failed attempts:     
                    print("\nLOSE :(")                                           # Print message 'LOSE', meaning that the player losed the game.
                    break                                                        # Stop and leave the program.
                num_of_tries += 1                                                # In case num_of_tries < MAX_TRIES, increment the number of tries by 1 to continue the loop.                          
            
if __name__ == "__main__":                                                       # Implementation of the function 'main' to run the main function of the program.^
   main()