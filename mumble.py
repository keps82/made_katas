DELIMITER = '-'



def mumble_letters(input_string):
    """
    >>> mumble_letters("a")
    'A'
    >>> mumble_letters("abC")
    'A-Bb-Ccc'
    >>> mumble_letters("aBCd")
    'A-Bb-Ccc-Dddd'
    >>> mumble_letters("QWERTY")
    'Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy'
    >>> mumble_letters("Hello World")
    'H-Ee-Lll-Llll-Ooooo-      -Wwwwwww-Oooooooo-Rrrrrrrrr-Llllllllll-Ddddddddddd'
    >>> mumble_letters("")
    ''
    """
    
    mumbled_input_string = ""

    for index, char in enumerate(input_string):
        mumbled_input_string += char.upper() + index * char.lower() + DELIMITER
    
    return mumbled_input_string.rstrip(DELIMITER)



print(mumble_letters('I am not a robot'))
        





