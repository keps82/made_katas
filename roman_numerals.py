#roman_numerals


MAX_NUMERAL = 3999

def roman_numeral_base_symbols():

    simple_numerals = {
        1:'I',
        5:'V',
        10:'X',
        50:'L',
        100:'C',
        500:'D',
        1000:'M'
    }


    subtracted_numerals = {
        4:'IV',
        9: 'IX',
        40: 'XL',
        45: 'VL',
        90: 'XC',
        400: 'CD',
        450: 'LD',
        900: 'CM',
    }

    sorted_keys = sorted(list(subtracted_numerals) + list(simple_numerals), reverse=True)

    numerals = {}

    for key in sorted_keys:
        try:
            numerals[key] = simple_numerals[key]
        except KeyError:
            numerals[key] = subtracted_numerals[key]
        except KeyError:
            pass
    
    return numerals


NUMERALS = roman_numeral_base_symbols()
 


def highest_numeral_less_than(number):
    """
    >>> highest_numeral_less_than(30)
    10
    """
    for key in NUMERALS:
        if key < number:
            return key




def number_to_numeral(number):
    """
    >>> number_to_numeral(1)
    'I'
    >>> number_to_numeral(4)
    'IV'
    >>> number_to_numeral(10)
    'X'
    >>> number_to_numeral(49)
    'XLIX'
    >>> number_to_numeral(948)
    'CMVLIII'
    """
    if number > MAX_NUMERAL:
        return large_number_to_numeral(number)

    try:
        return NUMERALS[number]
    except KeyError:
        pass
    
    

    numeral = ''

    key = highest_numeral_less_than(number)
        
    divisor, remainder = divmod(number, key)
    numeral = divisor * NUMERALS[key]

    if remainder > 0:
        numeral += number_to_numeral(remainder)
        
    return numeral


        
def large_number_to_numeral(number):
    print(f'number {number} is out of range')