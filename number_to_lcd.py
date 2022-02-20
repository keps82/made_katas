# number to LCD

class LCD_char():

    def __init__(self, char, lcd_lines, fill=3):
        self.char = char
        self.fill = fill
        self.lcd_lines = lcd_lines


one   = LCD_char('1', ['   ', '  |', '  |'])
two   = LCD_char('2', [' _ ', ' _|', '|_ '])
three = LCD_char('3', [' _ ', ' _|', ' _|'])
four  = LCD_char('4', ['   ', '|_|', '  |'])
five  = LCD_char('5', [' _ ', '|_ ', ' _|'])
six   = LCD_char('6', [' _ ', '|_ ', '|_|'])
seven = LCD_char('7', [' _ ', '  |', '  |'])
eight = LCD_char('8', [' _ ', '|_|', '|_|'])
nine  = LCD_char('9', [' _ ', '|_|', ' _|'])
zero  = LCD_char('0', [' _ ', '| |', ' _ '])


digits = [one, two, three, four, five, six, seven, eight, nine, zero]


digits_dict = {digit.char: digit.lcd_lines for digit in digits}


def print_lcd_lines(lcd_lines):
    """
    >>> print_lcd_lines(one.lcd_lines)
    <BLANKLINE>
      |
      |
    """
    for line in lcd_lines:
        print(line)


def number_to_LCD(number):
    """
    >>> number_to_LCD(123456789)
        _  _     _  _  _  _  _ 
      | _| _||_||_ |_   ||_||_|
      ||_  _|  | _||_|  ||_| _|
    """
    number_str = str(number)
    lcd_lines = ['', '', '']

    for digit in number_str:
        lcd_digit_lines = digits_dict[digit]
        for index, line in enumerate(lcd_lines):
            lcd_lines[index] += lcd_digit_lines[index]

    print_lcd_lines(lcd_lines)




