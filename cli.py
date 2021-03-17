#!/bin/python3

from curses import initscr
from sys import exit


class CLI:
    def __init__(self):
        self.screen = initscr()
        self.current_options = [i for i in 'ludp']
        self.length = 16
        self.description = None
        self.current_password = None

    def set_password_options(self):
        # TODO construct a menu that will control password options
        pass

    def set_description(self):
        # TODO construct a menu that will set password description for the current password
        pass

    def save_current_password(self):
        # TODO construct a function that will save the current password to a sqlite database
        pass

    def copy_current_password(self):
        # TODO construct a function that will copy the current password to the clipboard
        pass

    def generate_password_menu(self):
        self.screen.clear()
        # TODO if there is a description make it appear in the message
        message = [
            '============ Password Generation ============',
            f'current options are >> {"".join(self.current_options)}',
            f'password length >> {self.length}',
            # TODO all of this options will be inside of set password generation options
            # '(l) to toggle option lowercase',
            # '(u) to toggle option uppercase',
            # '(d) to toggle option digits',
            # '(p) to toggle option puctuation',
            # '(x) to set password length',
            '(o) set password generating options',
            '(d) add description',
            '(g) generate or regenerate password',
            '(s) save current password',
            '(c) copy current password',
            '(m) main menu',
            '(q) quit',
        ]

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'q':
            quit()
        elif usr_inp == 'g':
            # TODO generate or regenerate password
            #! call itself recursively with an extra option that will make this fuction generate and show password
            pass
        elif usr_inp == 'o':
            self.set_password_options()
        elif usr_inp == 'd':
            self.set_description()
        elif usr_inp == 's':
            self.save_current_password()
        elif usr_inp == 'c':
            self.copy_current_password()
        elif usr_inp == 'm':
            self.main_menu()
        else:
            self.error_scr('there is no such option')

    def error_scr(self, message):
        # TODO construct an error screen
        pass

    def main_menu(self):
        self.screen.clear()
        message = [
            '============ Main Menu ============',
            'Hi I am your personal password manager',
            '(g) generate a new password',
            '(v) view saved passwords',
            '(q) quit',
        ]

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'g':
            self.generate_password_menu()
        elif usr_inp == 'v':
            # TODO view passwords menu
            pass
        elif usr_inp == 'q':
            exit()
        else:
            self.error_scr('there is no such option')


if __name__ == '__main__':
    c = CLI()
    c.main_menu()
