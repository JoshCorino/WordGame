import WordGame
#
# Test code
#

def test_get_word_score():
    """
    Unit test for get_word_score
    """

    # dictionary of words and scores
    message = "\tExpected {0} points but got '{1}' for word '{2}', n={3}"
    
    words = {("", 7):0, ("it", 7):2, ("was", 7):54, ("weed", 6):176,
             ("scored", 7):351, ("WaYbILl", 7):735, ("Outgnaw", 7):539,
             ("fork", 7):209, ("FORK", 4):308}
    for (word, n) in words.keys():
        score = WordGame.get_word_score(word, n)
        assert score == words[(word, n)], message.format(words[(word, n)],str(score), word, n)

# end of test_get_word_score


def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = WordGame.update_hand(handCopy, word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    
    message = "\tReturned: {0}\n\t-- but expected:{1} or {2}"
    print("test_update_hand('"+ word +"', " + str(handOrig) + ")")
    assert hand2 == expected_hand1 or hand2 == expected_hand2, message.format(hand2, expected_hand1, expected_hand2)

    assert handCopy == handOrig, "\timplementation of update_hand mutated the original hand!"
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "Evil"

    hand2 = WordGame.update_hand(handCopy, word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    
    print("test_update_hand('"+ word +"', " + str(handOrig) + ")")
    assert hand2 == expected_hand1 or hand2 == expected_hand2, message.format(hand2, expected_hand1, expected_hand2)

    assert handCopy == handOrig, "\timplementation of update_hand mutated the original hand!"

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "HELLO"

    hand2 = WordGame.update_hand(handCopy, word)
    expected_hand1 = {}
    expected_hand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    
    print("test_update_hand('"+ word +"', " + str(handOrig) + ")")
    assert hand2 == expected_hand1 or hand2 == expected_hand2, message.format(hand2, expected_hand1, expected_hand2)

    assert handCopy == handOrig, "\timplementation of update_hand mutated the original hand!"

    print("SUCCESS: test_update_hand()")

# end of test_update_hand

def test_is_valid_word():
    """
    Unit test for is_valid_word
    """
    word_list = WordGame.load_words()
    
    # test 1
    word = "hello"
    handOrig = WordGame.get_frequency_dict(word)
    handCopy = handOrig.copy()

    message = "\tExpected {0}, but got {1} for word: '{2}' and hand:{3}"
    assert WordGame.is_valid_word(word, handCopy, word_list), message.format(True, False, word, handOrig)

    # Test a second time to see if word_list or hand has been modified
    assert WordGame.is_valid_word(word, handCopy, word_list), "\timplementation of is_valid_word mutated the original hand or word_list"

    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "Rapture"

    assert not WordGame.is_valid_word(word, hand, word_list), message.format(False, True, word, hand)

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    assert WordGame.is_valid_word(word, hand, word_list), message.format(True, False, word, hand)

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    assert not WordGame.is_valid_word(word, hand, word_list), message.format(False, True, word, hand)

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "EVIL"
    
    assert  WordGame.is_valid_word(word, hand, word_list), message.format(True, False, word, hand)
        
    # test 6
    word = "Even"

    assert not WordGame.is_valid_word(word, hand, word_list), message.format(False, True, word, hand)

    print("SUCCESS: test_is_valid_word()")

# end of test_is_valid_word

def test_wildcard():
    """
    Unit test for is_valid_word
    """
    word_list = WordGame.load_words()

    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    word = "e*m"

    message = "\tExpected {0}, but got {1} for word: '{2}' and hand:{3}"
    assert not WordGame.is_valid_word(word, hand, word_list), message.format(False, True, word, hand)

    # test 2
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    assert not WordGame.is_valid_word(word, hand, word_list),message.format(False, True, word, hand)

    # test 3
    hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "h*ney"

    assert WordGame.is_valid_word(word, hand, word_list), message.format(True, False, word, hand)

    # test 4
    hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    word = "c*wz"

    assert not WordGame.is_valid_word(word, hand, word_list), message.format(False, True, word, hand)

    # dictionary of words and scores WITH wildcards
    message = "\tExpected {0} points but got '{1}' for word '{2}', n={3}"
    words = {("h*ney", 7):290, ("c*ws", 6):176, ("wa*ls", 7):203}
    for (word, n) in words.keys():
        score = WordGame.get_word_score(word, n)
        assert score == words[(word, n)], message.format(words[(word, n)], score, word, n)

    print("SUCCESS: test_wildcard()")

def test_handlen():
    """
    Unit test for calculate_handlen
    """
    
    message = "\tExpected {0} letters in hand but got '{1}'"
    # test 1
    hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    handlen = 7
    result = WordGame.calculate_handlen(hand)
    assert handlen == result, message.format(handlen, result)

    # test 2
    hand = {'a': 0, 'r': 0, 'e': 2, 'j': 2, 'm': 1, '*': 0}
    handlen = 5
    result = WordGame.calculate_handlen(hand)
    assert handlen == result, message.format(handlen, result)
    
    # test 3
    hand = {'e': 2, 'j': 2, 'm': 1}
    handlen = 5
    result = WordGame.calculate_handlen(hand)
    assert handlen == result, message.format(handlen, result)

##Uncoment for run the test without the unittest plugin
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word()
print("----------------------------------------------------------------------")
print("Testing wildcards...")
test_wildcard()
print("Testing calculate handlen...")
test_handlen()
print("All done!")
