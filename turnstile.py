import unittest


def lights_on(is_on):
    pass


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


    def _lock(self): # private
        self.is_locked = True
        return self


    def _unlock(self): # private
        self.is_locked = False
        return self


    def _sound_alarm(self):
        print(self.alarm_sound)


    def _print_thanks(self):
        print(self.thank_you_message)


    def print_state(self):
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


    def insert_coin(self):
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
            self._print_thanks()
        else:
            self._unlock()

        return self


    def pass_through(self):
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
            self._sound_alarm()

        self.is_locked = True
        return self


class TestTurnstile(unittest.TestCase):
    
    
    test_turnstile = Turnstyle(is_locked=False, alarm_sound='ZZZ')
    

    def test_deactivate(self):
        self.test_turnstile.deactivate()
        self.assertTrue(self.test_turnstile.is_locked)


    def test_activate(self):
        self.test_turnstile.activate()
        self.assertFalse(self.test_turnstile.is_locked)


    def test_entrance(self):
        self.test_turnstile.activate()
        self.test_turnstile.insert_coin()
        self.assertFalse(self.test_turnstile.is_locked)
        self.test_turnstile.pass_through()
        self.assertTrue(self.test_turnstile.is_locked)


    def test_alarm(self):
        self.test_turnstile.deactivate()
        self.test_turnstile.pass_through()
        self.test_turnstile.activate()
        self.test_turnstile.pass_through()
        self.test_turnstile.pass_through()
        self.assertTrue(self.test_turnstile.is_locked)

if __name__ == 'MAIN':
    unittest.main()


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