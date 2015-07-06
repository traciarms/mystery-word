from mystery_word import *


def test_put_letter_in_string():

    # test the put letter in string method
    chosen_word = 'bird'
    r_string = '_ I _ _'
    user_letter = 'd'

    assert put_letter_in_string(chosen_word, r_string, user_letter).upper() == '_ I _ D'


# def test_ask_user_for_letter():
#     already_found = '_ _ _ _ E R'
#     already_guessed = 'E R T Z'
#
#     assert ask_user_for_letter(already_found, already_guessed) ==

# def test_easy_words():
#     assert easy_words(word_list) == \
#         ["bird", "calf", "river", "stream", "brain"]


# def test_medium_words():
#     assert medium_words(word_list) == \
#         ["stream", "kneecap", "cookbook", "language", "sneaker"]
#
#
# def test_hard_words():
#     assert hard_words(word_list) == \
#         ["cookbook", "language", "algorithm", "integration"]
#
#
# def test_random_word():
#     """This test is not very good. Testing things that are random is hard, in
#     that there's not a predictable choice. The best we can do is make sure
#     we have valid output."""
#     word = random_word(word_list)
#     assert word in word_list


# def test_display_word():
#     word = "integration"
#     assert display_word(word, []) == "_ _ _ _ _ _ _ _ _ _ _"
#     assert display_word(word, ["z"]) == "_ _ _ _ _ _ _ _ _ _ _"
#     assert display_word(word, ["g"]) == "_ _ _ _ G _ _ _ _ _ _"
#     assert display_word(word, ["i"]) == "I _ _ _ _ _ _ _ I _ _"
#     assert display_word(word, ["i", "g"]) == "I _ _ _ G _ _ _ I _ _"
#     assert display_word(word, ["i", "n", "z"]) == "I N _ _ _ _ _ _ I _ N"


# def test_is_word_complete():
#     word = "river"
#     assert not is_word_complete(word, [])
#     assert not is_word_complete(word, ["r"])
#     assert not is_word_complete(word, ["r", "e"])
#     assert not is_word_complete(word, ["r", "e", "z"])
#     assert is_word_complete(word, ["r", "e", "v", "i"])
