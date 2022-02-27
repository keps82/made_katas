#turnstile

def lights_on(is_on):
    pass

#audi.show()     # same output as car.show(audi)
#ferrari.show()  # same output as car.show(ferrari)
class Turnstyle():

    def __init__(
        self, 
        is_locked = True, # read only
        is_activated = True, # read only
        alarm_sound = 'BZZZZZZZZZZZZZZZZZ', 
        thank_you_message = 'Thanks!'
    ):
        self.is_activated = is_activated
        self.is_locked = is_locked or not is_activated
        self.alarm_sound = alarm_sound
        self.thank_you_message = thank_you_message
        

    def activate(self):
        lights_on(True)
        self.is_activated = True
        return self


    def deactivate(self):
        lights_on(False)
        self.is_activated = False
        self.is_locked = True
        return self


    def lock(self): # private
        self.is_locked = True
        return self


    def unlock(self): # private
        self.is_locked = False
        return self


    def sound_alarm(self):
        print(self.alarm_sound)


    def print_thanks(self):
        print(self.thank_you_message)


    def print_state(self): # public
        """
        >>> Turnstyle(is_locked=True).print_state()
        ACTIVE, LOCKED
        >>> Turnstyle(is_locked=False).print_state()
        ACTIVE, UNLOCKED
        >>> Turnstyle(is_locked=False, is_activated=False).print_state()
        INACTIVE, LOCKED
        """
        state = 'ACTIVE' if self.is_activated else 'INACTIVE'
        state += ', LOCKED' if self.is_locked else ', UNLOCKED'
        print(state)


    def insert_coin(self): # public
        """
        >>> Turnstyle().lock().insert_coin().print_state()
        ACTIVE, UNLOCKED
        >>> Turnstyle(thank_you_message = 'XX').unlock().insert_coin().print_state()
        XX
        ACTIVE, UNLOCKED
        """
        if not self.is_activated:
            return
        elif not self.is_locked:
            self.print_thanks()
        else:
            self.unlock()

        return self


    def pass_through(self): # public
        """
        >>> Turnstyle(alarm_sound = 'Z').pass_through().print_state()
        Z
        ACTIVE, LOCKED
        >>> Turnstyle().unlock().pass_through().print_state()
        ACTIVE, LOCKED
        >>> Turnstyle(alarm_sound = 'Z').deactivate().unlock().pass_through().print_state()
        Z
        INACTIVE, LOCKED
        >>> Turnstyle(alarm_sound = 'Z').unlock().deactivate().pass_through().print_state()
        Z
        INACTIVE, LOCKED
        """
        if self.is_locked or not self.is_activated:
            self.sound_alarm()

        self.is_locked = True
        return self


# Only these methods should be exposed.  Other ones are internal
def test_turnstile():
    test_turnstile = Turnstyle(is_locked=False, alarm_sound='ZZZ')
    print('New turnstile is unlocked')
    test_turnstile.print_state()
    print('Insert coin')
    test_turnstile.insert_coin()
    test_turnstile.print_state()
    print('Pass through')
    test_turnstile.pass_through()
    test_turnstile.print_state()
    print('Try to pass through')
    test_turnstile.pass_through()
    test_turnstile.print_state()
    print('Insert coin')
    test_turnstile.insert_coin()
    print('Deactivate turnstile')
    test_turnstile.deactivate()
    test_turnstile.insert_coin()
    print('Try to pass through')
    test_turnstile.pass_through()
    test_turnstile.print_state()

    test_turnstile = Turnstyle(is_locked = False, is_activated = False, alarm_sound='ZZZ')
    print('New turnstile unlocked but deactivated')
    test_turnstile.print_state()

test_turnstile()