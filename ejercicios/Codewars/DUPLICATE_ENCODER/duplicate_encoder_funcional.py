def duplicate_encode(word):

    return ''.join([')' if word.lower().count(characters) > 1 else '(' for characters in word.lower()])

if __name__ == '__main__':

    assert duplicate_encode("din"),"((("
    assert duplicate_encode("recede"),"()()()"
    assert duplicate_encode("Success"),")())())"
    assert duplicate_encode("(( @"),"))(("