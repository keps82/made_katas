# number to LCD

UPRIGHT = '|'
HORIZONTAL = '_'
FILLER = ' '


class LCD_line():


    def __init__(self, first, middle, final):
        self.first = first
        self.middle = middle
        self.final = final
        


class LCD_char():


    def __init__(self, char, lcd_lines, scale=[1,1]):
        self.char = char
        self.scale = scale
        self.lcd_lines = self.scale_lines(lcd_lines, scale)


    @staticmethod
    def x_scale_lines(lcd_lines, x_scale):
        """
        >>> print_lcd_lines(LCD_char.x_scale_lines(['___'],3))
        _____
        """
        scaled_lcd_lines = lcd_lines.copy()

        for index,line in enumerate(lcd_lines):
            x_scale_line = line[0] + line[1]*x_scale + line[2]
            #print(x_scale_line)
            scaled_lcd_lines[index] = x_scale_line

        return scaled_lcd_lines


    @staticmethod
    def y_scale_lines(lcd_lines, y_scale):
        """
        >>> print_lcd_lines(LCD_char.y_scale_lines([' ','| |','|_|'],2))
        <BLANKLINE>
        | |
        | |
        | |
        |_|
        """
        scaled_lcd_lines = lcd_lines.copy()

        bottom_element_extension = [lcd_lines[2].replace(HORIZONTAL, FILLER)]*(y_scale-1) # ['','','']
        middle_element_extension = [lcd_lines[1].replace(HORIZONTAL, FILLER)]*(y_scale-1)

        scaled_lcd_lines = [lcd_lines[0]] + middle_element_extension + [lcd_lines[1]] + bottom_element_extension + [lcd_lines[2]]

        return scaled_lcd_lines


    @staticmethod
    def scale_lines(lcd_lines, scale):
        """
        >>> print_lcd_lines(LCD_char.scale_lines([' _ ','| |','|_|'], [3,2]))
         ___ 
        |   |
        |   |
        |   |
        |___|
        """
        x_scale_factor = scale[0]
        y_scale_factor = scale[1]

        scaled_lcd_lines = LCD_char.y_scale_lines(LCD_char.x_scale_lines(lcd_lines, x_scale_factor), y_scale_factor)
#        scaled_lcd_lines = LCD_char.x_scale_lines(lcd_lines, x_scale_factor)

        return scaled_lcd_lines




one   = LCD_char('1', ['   ', '  |', '  |'])
two   = LCD_char('2', [' _ ', ' _|', '|_ '])
three = LCD_char('3', [' _ ', ' _|', ' _|'])
four  = LCD_char('4', ['   ', '|_|', '  |'])
five  = LCD_char('5', [' _ ', '|_ ', ' _|'])
six   = LCD_char('6', [' _ ', '|_ ', '|_|'])
seven = LCD_char('7', [' _ ', '  |', '  |'])
eight = LCD_char('8', [' _ ', '|_|', '|_|'])
nine  = LCD_char('9', [' _ ', '|_|', ' _|'])
zero  = LCD_char('0', [' _ ', '| |', '|_|'])


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




