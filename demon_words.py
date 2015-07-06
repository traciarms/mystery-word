import random
import re
from itertools import groupby
import string


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

            # if the level is easy only get the words with length of 6
            if level == 'e':
                if word_len == 6:
                    word_list.append(word.replace('\n', '').lower())

            # if the level is normal only get the words with length 8
            elif level == 'n':
                if word_len == 8:
                    word_list.append(word.replace('\n', '').lower())

            # if the level is hard only get the words with length > 8
            # but we have to choose one - so TO DO - use random to get
            # a random word length from our word list
            elif level == 'h':
                if word_len > 8:
                    word_list.append(word.replace('\n', '').lower())

    print('this is our word list length {}'.format(len(word_list)))
    return word_list


def enter_play_mode():
    """
        This method allows the user to input which mode they would like to plan in
        easy normal or hard.  If the user enters anything other than these 3 letters
        the method just repeats the request for the mode.  Once we get a good mode
        selection we return that.
    """
    # ask the user to enter their chosen play mode
    play_mode = input('Choose your level of difficulty (E)asy (N)ormal (H)ard.').lower()

    while play_mode not in ['e', 'n', 'h']:
        play_mode = input("Choose your level of difficulty (E)asy (N)ormal (H)ard.").lower()

    return play_mode


def ask_user_for_letter(already_found, already_guessed):
    """
        This function will handle asking the user for a letter.  It makes sure its valid entry
        ie just one letter not more and not numberic.  It also handles duplicate entries.
        It returns a good letter input by the user.
    """
    # Ask the user for a one letter guess
    user_letter = input('What is your one letter guess')

    try:
        int(user_letter)
    except ValueError:
        num_flag = False
    else:
        num_flag = True

    if len(user_letter) > 1 or num_flag:
        print('That\'s not a valid entry - please try again')
        user_letter = ask_user_for_letter(already_found, already_guessed)
    elif user_letter in already_found:
        print('Try another letter - you already found that one!\n')
        print('Used letters: {}'.format(already_guessed.upper()))
        user_letter = ask_user_for_letter(already_found, already_guessed)
    elif user_letter in already_guessed:
        print('Try another letter - you already guessed that one!\n')
        print('Used letters: {}'.format(already_guessed.upper()))
        user_letter = ask_user_for_letter(already_found, already_guessed)

    return user_letter


def into_families(words, letter):
    """
        This is the function that does all the evil work!  It takes in the current list
        of words and the letter the user has input.  With these two it will try to filter out
        of the list any words that were matching the users letter.  It returns this new
        filtered list.
    """
    result = {}
    for word in words:
        key = ' '.join(letter.upper() if c == letter else '_' for c in word)
        if key not in result:
            result[key] = []
        result[key].append(word)

    r_list = max(result.items(), key=lambda k_v: len(k_v[1]))

    return r_list


def update_found_string(found_letter_string, new_found):
    """
        this function updates the string of found letters that we display
        to the user after each selected letter.  We pass in the old found string
        and the letter to add to it and return the newly built found letter string.
    """

    if found_letter_string == '_':
        found_letter_string = new_found
    else:
        found_letter_list = found_letter_string.split(' ')
        new_found_letter_list = new_found.split(' ')
        index = 0

        # we have to store the new letters in the found string
        for letter in new_found_letter_list:
            if letter is not '_':
                found_letter_list[index] = letter
            index += 1

        found_letter_string = ' '.join(found_letter_list)

    return found_letter_string


def play_demon_game():
    """
        This method uses the logic for playing the game - calls the helper functions and
        decides whether to keep playing or to finish
    """

    # set variables for play
    guessed_letters = ''
    number_of_tries = 8
    found_letter_string = '_'
    play_again = ''
    chosen_word = ''
    word_tuple = ()

    # let the user select their play mode
    mode = enter_play_mode()

    # read in the file of words and parse according to the play mode
    word_list = open_word_file("/usr/share/dict/words", mode)

    while number_of_tries > 0 and '_' in found_letter_string:
        # ask the user for a letter and add it to the guessed letter string
        user_letter = ask_user_for_letter(found_letter_string, guessed_letters)
        guessed_letters += user_letter+' '

        word_tuple = into_families(word_list, user_letter)

        # if this is the first go around set the found string to the string of the largest tuple
        if found_letter_string == '_':
            found_letter_string = word_tuple[0]

        # if our size is one then we need to store the word
        if len(word_tuple[1]) == 1:
            chosen_word = ''.join(word_tuple[1])

        if user_letter.upper() in word_tuple[0]:
            print('YES {} was found:'.format(user_letter).upper())
            found_letter_string = update_found_string(found_letter_string, word_tuple[0])
        else:
            print('SORRY {} was not found:'.format(user_letter.upper()))
            number_of_tries -= 1

        word_list = word_tuple[1]

        print(found_letter_string)
        print('\nYou have {} tries remaining.'.format(number_of_tries))
        guessed_letters = guessed_letters.replace(' ', '')
        guessed_letters = ' '.join(sorted(guessed_letters))
        print('Used letters: {}'.format(guessed_letters.upper()))

    if number_of_tries == 0 and '_' in found_letter_string:
        if chosen_word == '':
            # we need to find a random one left in the tuple
            chosen_word = random.choice(word_tuple[1])

        play_again = input('YOU LOSE! The word was {}.\n Type (P) to play again.\t'.format(chosen_word.upper())).lower()

    if '_' not in found_letter_string:
        play_again = input('YOU DID IT!!!  Type (P) to play again.').lower()

    if play_again == 'p':
        play_demon_game()


if __name__ == "__main__":

    play_demon_game()
