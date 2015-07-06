from demon_words import *


def test_update_found_string():

    # test the put letter in string method
    found_letter_string = 'G _ _ _'
    new_found = '_ O O _'

    assert update_found_string(found_letter_string, new_found) == 'G O O _'
    
    
def test_into_families():
    
    words = ['birds', 'river', 'steam', 'knees',  'cooks',
             'sneak', 'brain']
    letter = 'a'

    assert into_families(words, letter) == ('_ _ _ _ _', ['birds', 'river', 'knees', 'cooks'])