# number to LCD

UPRIGHT = '|'
HORIZONTAL = '_'
FILLER = ' '


class LCDHorizontalTriple():


    def __init__(self, left, middle, right):
        self.first = left
        self.middle = middle
        self.final = right
        

class LCDElements():


    def __init__(self, top: LCDHorizontalTriple, middle: LCDHorizontalTriple, bottom: LCDHorizontalTriple):
        self.top = top
        self.middle = middle
        self.bottom = bottom        


class LCDChar():


    def __init__(self, char, lcd_lines, scale=[1,1]):
        self.char = char
        self.scale = scale
        self.lcd_lines = self.scale_lines(lcd_lines, scale)


    @staticmethod
    def x_scale_lines(lcd_lines, x_scale):
        """
        >>> print_lcd_lines(LCDChar.x_scale_lines(['___'],3))
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
        >>> print_lcd_lines(LCDChar.y_scale_lines([' ','| |','|_|'],2))
        <BLANKLINE>
        | |
        | |
        | |
        |_|
        """
        scaled_lcd_lines = lcd_lines.copy()

        bottom_element_extension = [lcd_lines[2].replace(HORIZONTAL, FILLER)]*(y_scale-1)
        middle_element_extension = [lcd_lines[1].replace(HORIZONTAL, FILLER)]*(y_scale-1)

        scaled_lcd_lines = [lcd_lines[0]] + middle_element_extension + [lcd_lines[1]] + bottom_element_extension + [lcd_lines[2]]

        return scaled_lcd_lines


    @staticmethod
    def scale_lines(lcd_lines, scale):
        """
        >>> print_lcd_lines(LCDChar.scale_lines([' _ ','| |','|_|'], [3,2]))
         ___ 
        |   |
        |   |
        |   |
        |___|
        """
        x_scale_factor = scale[0]
        y_scale_factor = scale[1]

        scaled_lcd_lines = LCDChar.y_scale_lines(LCDChar.x_scale_lines(lcd_lines, x_scale_factor), y_scale_factor)

        return scaled_lcd_lines



one   = LCDChar('1', ['   ', '  |', '  |'])
two   = LCDChar('2', [' _ ', ' _|', '|_ '])
three = LCDChar('3', [' _ ', ' _|', ' _|'])
four  = LCDChar('4', ['   ', '|_|', '  |'])
five  = LCDChar('5', [' _ ', '|_ ', ' _|'])
six   = LCDChar('6', [' _ ', '|_ ', '|_|'])
seven = LCDChar('7', [' _ ', '  |', '  |'])
eight = LCDChar('8', [' _ ', '|_|', '|_|'])
nine  = LCDChar('9', [' _ ', '|_|', ' _|'])
zero  = LCDChar('0', [' _ ', '| |', '|_|'])


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



def number_to_LCD(number, scale = [1,1]):
    """
    >>> number_to_LCD(123456789)
        _  _     _  _  _  _  _ 
      | _| _||_||_ |_   ||_||_|
      ||_  _|  | _||_|  ||_| _|
    """
    number_str = str(number)
    lcd_lines = [' ']*3*scale[1]

    for digit in number_str:
        lcd_digit_lines = LCDChar.scale_lines(digits_dict[digit], scale)
        for index, line in enumerate(lcd_digit_lines):
            lcd_lines[index] += lcd_digit_lines[index]

    print_lcd_lines(lcd_lines)




