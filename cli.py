#!/bin/python3

from curses import initscr
from sys import exit
from password_generator import PasswdGenerator
from pyperclip import copy
from time import sleep


class CLI:
    def __init__(self):
        self.screen = initscr()
        self.current_options = [i for i in 'ludp']
        self.old_options = None
        self.length = 16
        self.old_length = None
        self.description = None
        self.login_info = None
        self.password_generator = None
        self.password = None

    # * Done
    def set_length(self):
        self.screen.clear()
        self.screen.addstr(0, 0, 'please specify a password length >> ')
        self.screen.refresh()
        self.length = int(self.screen.getstr(0, 36, 10))
        self.set_password_options()

    # * Done
    def set_password_options(self):
        if self.old_options is None:
            self.old_options = self.current_options.copy()
        if self.old_length is None:
            self.old_length = self.length

        self.screen.clear()
        message = [
            '============ Set Options ============',
            f'current options are >> {"".join(self.current_options)}',
            f'password length >> {self.length}',
            '(l) to toggle option lowercase',
            '(u) to toggle option uppercase',
            '(d) to toggle option digits',
            '(p) to toggle option puctuation',
            '(x) to set password length',
            '(s) save current settings and return to generation',
            '(g) discard current settings and return to generation',
            '(q) quit',
        ]

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'q':
            quit()
        elif usr_inp == 'g':
            self.current_options = self.old_options.copy()
            self.old_options = None
            self.length = self.old_length
            self.old_length = None
            self.generate_password_menu()
        elif usr_inp == 's':
            self.old_options = None
            self.old_length = None
            self.generate_password_menu()
        elif usr_inp == 'x':
            self.set_length()
        elif usr_inp == 'l':
            if 'l' not in self.current_options:
                self.current_options.append('l')
            else:
                self.current_options.remove('l')
        elif usr_inp == 'u':
            if 'u' not in self.current_options:
                self.current_options.append('u')
            else:
                self.current_options.remove('u')
        elif usr_inp == 'd':
            if 'd' not in self.current_options:
                self.current_options.append('d')
            else:
                self.current_options.remove('d')
        elif usr_inp == 'p':
            if 'p' not in self.current_options:
                self.current_options.append('p')
            else:
                self.current_options.remove('p')
        else:
            self.error_scr('there is no such option',
                           self.set_password_options)

        self.set_password_options()

    #! In progress
    def set_info(self):
        self.screen.clear()
        message = [
            '============ Set Information ============',
            # TODO show info here if possible
            '(n) set name',
            '(d) set description',
            '(s) save information and return to generation',
            '(g) discard information and return to generation',
            '(q) quit',
        ]

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'q':
            quit()
        elif usr_inp == 'n':
            #! set name
            pass
        elif usr_inp == 'd':
            #! set description
            pass
        elif usr_inp == 's':
            #! save info and return generation
            pass
        elif usr_inp == 'g':
            #! discard info and return generation
            pass

    #! In progress
    def save_current_password(self):
        # TODO construct a function that will save the current password to a sqlite database
        pass

    # * Done
    def copy_current_password(self):
        copy(self.password)
        self.screen.clear()
        message = [
            'Password copied'
        ]
        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        sleep(1)

        self.generate_password_menu()

    #! In progress
    def generate_password_menu(self, gen=False):
        self.screen.clear()
        if gen:
            self.password_generator = PasswdGenerator(
                options=''.join(self.current_options), length=self.length)
            self.password = self.password_generator.generate()
            message = [
                '============ Password Generation ============',
                f'current options are >> {"".join(self.current_options)}',
                f'password length >> {self.length}',
                # TODO if there is a description make it appear in the message
                f'current password >> {self.password}',
                '(o) set password generating options',
                '(d) add description',
                '(g) generate or regenerate password',
                '(s) save current password',
                '(c) copy current password',
                '(m) main menu',
                '(q) quit',
            ]
        elif self.password:
            message = [
                '============ Password Generation ============',
                f'current options are >> {"".join(self.current_options)}',
                f'password length >> {self.length}',
                # TODO if there is a description make it appear in the message
                f'current password >> {self.password}',
                '(o) set password generating options',
                '(d) add description',
                '(g) generate or regenerate password',
                '(s) save current password',
                '(c) copy current password',
                '(m) main menu',
                '(q) quit',
            ]
        else:
            message = [
                '============ Password Generation ============',
                f'current options are >> {"".join(self.current_options)}',
                f'password length >> {self.length}',
                # TODO if there is a description make it appear in the message
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
            self.generate_password_menu(gen=True)
        elif usr_inp == 'o':
            self.set_password_options()
        elif usr_inp == 'd':
            self.set_info()
        elif usr_inp == 's':
            self.save_current_password()
        elif usr_inp == 'c':
            self.copy_current_password()
        elif usr_inp == 'm':
            self.main_menu()
        else:
            self.error_scr('there is no such option',
                           self.generate_password_menu)

    #! In progress
    def error_scr(self, message, function):
        # TODO construct an error screen which will be continued after if possible
        pass

    #! In progress
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
            self.error_scr('there is no such option', self.main_menu)


if __name__ == '__main__':
    c = CLI()
    c.main_menu()
