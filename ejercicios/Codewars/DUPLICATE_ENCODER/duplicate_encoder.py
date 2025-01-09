def duplicate_encode(word):

    new_word = ""
    lower_word = word.lower()
    for characters in lower_word:

        if lower_word.count(characters) > 1:
            new_word += ')'

        else:
            new_word += '('
        
    return new_word

if __name__ == '__main__':

    assert duplicate_encode("din"),"((("
    assert duplicate_encode("recede"),"()()()"
    assert duplicate_encode("Success"),")())())"
    assert duplicate_encode("(( @"),"))(("