# You will implement the game Mystery Word. In your game, you will be playing against the computer.
# The computer must select a word at random from the list of words in the file /usr/share/dict/words.
# This file exists on your computer already.
# The game must be interactive; the flow of the game should go as follows:
# Let the user choose a level of difficulty at the beginning of the program. Easy mode only has words
# of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.
# At the start of the game, let the user know how many letters the computer's word contains.
# Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and
# it should not matter. If a user enters more than one letter, tell them the input is invalid and let them
# try again.
# Let the user know if their guess appears in the computer's word.
# Display the partially guessed word, as well as letters that have not been guessed. For example, if the
# word is BOMBARD and the letters guessed are a, b, and d, the screen should display:
# B _ _ B A _ D
# A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
# A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's
#  word, they do not lose a guess.
import random


def open_word_file(file_name, level):
    """ The function takes in the name of the book and opens the file
        reads it in, strips away unwanted characters, changes all the case
        to lower case, splits the string upon spaces into a list and then
        checks to make sure there isn't extra list item for extra spaces.
        returns the book in list form.
    """
    word_list = []
    with open(file_name) as all_words:

        for word in all_words.readlines():
            word_len = len(word)

            if level == 'e':
                if 3 < word_len < 7:
                    word_list.append(word.lower())

            elif level == 'n':
                if 5 < word_len < 9:
                    word_list.append(word.lower())

            elif level == 'h':
                if word_len > 7:
                    word_list.append(word.lower())

    # from the word list select a random word to return
    our_word = random.choice(word_list)
    #print(our_word)

    return our_word


def put_letter_in_string(chosen_word, r_string, user_letter):

    # put our chosen word into a list
    word_list = r_string.split()
    index = 0

    # ok your letter is in the word - lets find the index and put it in our string
    for item in chosen_word:
        if item == user_letter:
            if index <= len(word_list)-1:
                word_list[index] = user_letter
        index += 1

    new_return_string = ' '.join(word_list)

    return new_return_string


def ask_user_for_letter(already_found):
    # Ask the user for a one letter guess
    user_letter = input('What is your one letter guess')

    try:
        int(user_letter)
    except ValueError:
        num_flag = False
    else:
        num_flag = True

    if len(user_letter) > 1 or num_flag:
        user_letter = ask_user_for_letter(already_found)
    elif user_letter in already_found:
        print('Try another letter - you already found that one!'+'\n')
        user_letter = ask_user_for_letter(already_found)

    return user_letter


def enter_play_mode():
    # ask the user to enter their chosen play mode
    play_mode = input('Choose your level of difficulty (E)asy (N)ormal (H)ard.').lower()

    while play_mode not in ['e', 'n', 'h']:
        play_mode = input("Choose your level of difficulty (E)asy (N)ormal (H)ard.").lower()

    return play_mode


def play_game():

    # set variables for play
    number_of_tries = 8
    found_letter_string = ''
    play_again = ''

    # let the user select their play mode
    mode = enter_play_mode()

    # read in the file of words and parse according to the play mode
    chosen_word = open_word_file("/usr/share/dict/words", mode)
    chosen_word = chosen_word.replace('\n', '')

    # let the user know how many letters are in the computer's word
    print('Your word has {} letters.'.format(len(chosen_word)))

    # construct the letter found string to display
    for each in chosen_word:
        found_letter_string += '_ '

    print(found_letter_string)

    # ok lets play
    while number_of_tries > 0 and '_' in found_letter_string:

        # ask the user for a letter and make sure its just a single letter
        letter = ask_user_for_letter(found_letter_string)

        if letter in chosen_word:
            # if the letter is in the chosen word put it in the string to print
            found_letter_string = put_letter_in_string(chosen_word, found_letter_string, letter)
            print("YES {} was found".format(letter))
        else:
            # if the letter is not found in the string decrease the number of tries left
            number_of_tries -= 1
            print("SORRY {} was not found".format(letter))

        print(found_letter_string.upper())
        print('\nyou have {} tries remaining.'.format(number_of_tries))

    if number_of_tries == 0 and '_' in found_letter_string:
        play_again = input("sorry out of tries. The word was {}.\n Type (P) to play again.".format(chosen_word.upper())).lower()

    if '_' not in found_letter_string:
        play_again = input("YOU DID IT!!!  Type (P) to play again.").lower()

    if play_again == 'p':
        play_game()


if __name__ == "__main__":

    play_game()
