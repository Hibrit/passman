#!/bin/python3

from curses import initscr, endwin
from os.path import exists, abspath, dirname, join
from pickle import dump, load
from sys import exit
from time import sleep
from uuid import uuid1
from base64 import b64decode, b64encode

from pyperclip import copy

from password_generator import PasswdGenerator
from passman_parser import get_arguments
from menu_entries import get_entry


PATH = dirname(abspath(__file__))


class Passman:
    def __init__(self, silence=False, options='ludp', length=16, description=get_entry('not_specified'), login_info=get_entry('not_specified'), password=None):
        if not silence:
            self.screen = initscr()
        self.silence = silence
        self.current_options = [i for i in options]
        self.old_options = None
        self.length = length
        self.old_length = None
        self.description = description
        self.old_description = None
        self.login_info = login_info
        self.old_login_info = None
        self.password_generator = None
        self.password = password
        self.page = 0
        self.uuid = None

    # * Done
    def set_length(self):
        self.screen.clear()
        message = get_entry('specify_password_length')
        self.screen.addstr(0, 0, message)
        self.screen.refresh()

        try:
            self.length = int(self.screen.getstr(0, len(message), 10))
        except ValueError:
            self.error_scr(get_entry('enter_integer'), self.set_length)

        self.set_password_options()

    # * Done
    def set_password_options(self):
        if self.old_options is None:
            self.old_options = self.current_options.copy()
        if self.old_length is None:
            self.old_length = self.length

        self.screen.clear()

        message = get_entry(
            'set_options', ["".join(self.current_options), self.length]).copy()

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'q':
            self.quit()
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
            self.error_scr(get_entry('no_such_option'),
                           self.set_password_options)

        self.set_password_options()

    # * Done
    def set_login_info(self):
        self.screen.clear()
        message = get_entry('set_login_info')
        self.screen.addstr(0, 0, message)
        self.screen.refresh()
        self.login_info = self.screen.getstr(
            0, len(message), 100).decode('UTF-8')
        self.set_info()

    # * Done
    def set_description(self):
        self.screen.clear()
        message = get_entry('set_description')
        self.screen.addstr(0, 0, message)
        self.screen.refresh()
        self.description = self.screen.getstr(
            0, len(message), 100).decode('UTF-8')
        self.set_info()

    # * Done
    def set_info(self):
        if self.old_description is None and not self.description == get_entry('not_specified'):
            self.old_description = self.description
        if self.old_login_info is None and not self.login_info == get_entry('not_specified'):
            self.old_login_info = self.login_info

        self.screen.clear()

        message = get_entry('set_information', [
                            self.login_info, self.description])

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'q':
            self.quit()
        elif usr_inp == 'i':
            self.set_login_info()
        elif usr_inp == 'd':
            self.set_description()
        elif usr_inp == 's':
            self.old_description = None
            self.old_login_info = None
            self.generate_password_menu()
        elif usr_inp == 'g':
            self.login_info = self.old_login_info
            self.old_login_info = None
            self.description = self.old_description
            self.old_description = None
            self.generate_password_menu()
        else:
            self.error_scr(get_entry('no_such_option'),
                           self.set_info)

    # * Done
    def save_current_password(self):
        if not exists(join(PATH, 'data.tnd')):
            with open(join(PATH, 'data.tnd'), 'wb') as f:
                dump([], f)

        with open(join(PATH, 'data.tnd'), 'rb') as f:
            passwords = load(f)
        if self.uuid:
            for password in passwords:
                if password['uuid'] == self.uuid:
                    password['login_info'] = b64encode(
                        self.login_info.encode('UTF-8'))
                    password['description'] = b64encode(
                        self.description.encode('UTF-8'))
                    password['password'] = b64encode(
                        self.password.encode('UTF-8'))
        else:
            passwords.append({
                'uuid': uuid1().hex,
                'login_info': b64encode(self.login_info.encode('UTF-8')),
                'description': b64encode(self.description.encode('UTF-8')),
                'password': b64encode(self.password.encode('UTF-8'))
            })

        with open(join(PATH, 'data.tnd'), 'wb') as f:
            dump(passwords, f)

        if not self.silence:
            self.screen.clear()
            message = get_entry('password_saved')
            for index, line in enumerate(message):
                self.screen.addstr(index, 0, line)

            self.screen.refresh()

            sleep(1)

            self.generate_password_menu()

    # * Done
    def copy_current_password(self, f=None):
        copy(self.password)
        if not self.silence:
            self.screen.clear()
            message = get_entry('password_copied')
            for index, line in enumerate(message):
                self.screen.addstr(index, 0, line)

            self.screen.refresh()

            sleep(1)

            f()

    # * Done
    def set_password(self):
        self.screen.clear()
        message = get_entry('set_password')
        self.screen.addstr(0, 0, message)
        self.screen.refresh()
        self.password = self.screen.getstr(
            0, len(message), 100).decode('UTF-8')
        self.generate_password_menu()

    # * Done
    def gen_rand_pass(self):
        self.password_generator = PasswdGenerator(
            options=''.join(self.current_options), length=self.length)
        self.password = self.password_generator.generate()

    # * Done
    def generate_password_menu(self, gen=False):
        self.screen.clear()
        if gen:
            self.gen_rand_pass()

        if self.password:

            message = get_entry('generate_password_menu_1', ["".join(
                self.current_options), self.length, self.login_info, self.description, self.password])
        else:

            message = get_entry('generate_password_menu_2', ["".join(
                self.current_options), self.length, self.login_info, self.description])
        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'q':
            self.quit()
        elif usr_inp == 'g':
            self.generate_password_menu(gen=True)
        elif usr_inp == 'o':
            self.set_password_options()
        elif usr_inp == 'i':
            self.set_info()
        elif usr_inp == 's':
            self.save_current_password()
        elif usr_inp == 'c':
            self.copy_current_password(self.generate_password_menu)
        elif usr_inp == 'm':
            self.main_menu()
        elif usr_inp == 'e':
            self.set_password()
        else:
            self.error_scr(get_entry('no_such_option'),
                           self.generate_password_menu)

    # * Done
    def error_scr(self, message, f):
        self.screen.clear()
        self.screen.addstr(0, 0, f'{message}')
        self.screen.refresh()
        sleep(1)
        f()

    # * Done
    def view_menu(self):
        self.screen.clear()
        if not exists(join(PATH, 'data.tnd')):
            self.error_scr(
                get_entry('dont_have_any_saved'), self.main_menu)

        with open(join(PATH, 'data.tnd'), 'rb') as f:
            passwords = load(f)
            if len(passwords) == 0:
                self.error_scr(
                    get_entry('dont_have_any_saved'), self.main_menu)

        passwords_to_show = passwords[self.page * 8: self.page * 8 + 8]

        keys = []
        buttons = []
        message = get_entry('view_menu', [self.page + 1])

        if self.page == 0 and len(passwords[(self.page + 1) * 8: (self.page + 1) * 8 + 8]) == 0:
            for index, p in enumerate(passwords_to_show):
                keys.append({str(index): p})
                description = b64decode(p['description']).decode('UTF-8')
                login_info = b64decode(p['login_info']).decode('UTF-8')
                message.append(f'({index}) {description} {login_info}')
            message.append(get_entry('main_menu_message'))
            message.append(get_entry('quit_message'))

        elif self.page == 0:
            for index, p in enumerate(passwords_to_show):
                keys.append({str(index): p})
                description = b64decode(p['description']).decode('UTF-8')
                login_info = b64decode(p['login_info']).decode('UTF-8')
                message.append(f'({index}) {description} {login_info}')
            message.append(get_entry('next_page_message'))
            buttons.append('n')
            message.append(get_entry('main_menu_message'))
            message.append(get_entry('quit_message'))

        elif not self.page == 0 and not len(passwords[(self.page + 1) * 8: (self.page + 1) * 8 + 8]) == 0:
            for index, p in enumerate(passwords_to_show):
                keys.append({str(index): p})
                description = b64decode(p['description']).decode('UTF-8')
                login_info = b64decode(p['login_info']).decode('UTF-8')
                message.append(f'({index}) {description} {login_info}')
            message.append(get_entry('next_page_message'))
            buttons.append('n')
            message.append(get_entry('previous_page_message'))
            buttons.append('p')
            message.append(get_entry('main_menu_message'))
            message.append(get_entry('quit_message'))
        else:
            for index, p in enumerate(passwords_to_show):
                keys.append({str(index): p})
                description = b64decode(p['description']).decode('UTF-8')
                login_info = b64decode(p['login_info']).decode('UTF-8')
                message.append(f'({index}) {description} {login_info}')
            message.append(get_entry('previous_page_message'))
            buttons.append('p')
            message.append(get_entry('main_menu_message'))
            message.append(get_entry('quit_message'))

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        valid_keys = []
        for pair in keys:
            for k, _ in pair.items():
                valid_keys.append(k)

        if usr_inp == 'q':
            self.quit()
        elif usr_inp == 'n' and 'n' in buttons:
            self.page += 1
            self.view_menu()
        elif usr_inp == 'p' and 'p' in buttons:
            self.page -= 1
            self.view_menu()
        elif usr_inp == 'm':
            self.main_menu()
        elif usr_inp in valid_keys:
            for pair in keys:
                for k, v in pair.items():
                    if usr_inp == k:
                        self.login_info = b64decode(
                            v['login_info']).decode('UTF-8')
                        self.description = b64decode(
                            v['description']).decode('UTF-8')
                        self.password = b64decode(
                            v['password']).decode('UTF-8')
                        self.uuid = v['uuid']
                        self.detailed_view()
        else:
            self.error_scr(get_entry('no_such_option'), self.view_menu)

    # * Done
    def delete_password(self):
        with open(join(PATH, 'data.tnd'), 'rb') as f:
            passwords = load(f)

        for index, password in enumerate(passwords):
            if password['uuid'] == self.uuid:
                passwords.pop(index)

        with open(join(PATH, 'data.tnd'), 'wb') as f:
            dump(passwords, f)
        self.screen.clear()

        message = get_entry('password_deleted')

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        sleep(1)

        self.__init__()
        self.view_menu()

    # * Done
    def detailed_view(self):
        self.screen.clear()

        message = get_entry(
            'detailed_view', [self.login_info, self.description, self.password])

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'q':
            self.quit()
        elif usr_inp == 'c':
            self.copy_current_password(self.detailed_view)
        elif usr_inp == 'e':
            self.generate_password_menu()
        elif usr_inp == 'd':
            self.delete_password()
        elif usr_inp == 'v':
            self.view_menu()
        elif usr_inp == 'm':
            self.main_menu()
        else:
            self.error_scr(get_entry('no_such_option'), self.detailed_view)

    # * Done
    def quit(self):
        self.screen.clear()
        endwin()
        exit()

    # * Done
    def main_menu(self):
        self.__init__()
        self.screen.clear()

        message = get_entry('main_menu')

        for index, line in enumerate(message):
            self.screen.addstr(index, 0, line)

        self.screen.refresh()

        usr_inp = self.screen.getkey().lower()

        if usr_inp == 'g':
            self.generate_password_menu()
        elif usr_inp == 'v':
            self.view_menu()
        elif usr_inp == 'q':
            self.quit()
        else:
            self.error_scr(get_entry('no_such_option'), self.main_menu)


if __name__ == '__main__':
    args = get_arguments()
    if args.silence:
        options = args.options
        length = args.length
        description = args.description
        info = args.info
        if args.password:
            password = args.password
            p = Passman(silence=True, description=description,
                        login_info=info, password=password)
            p.save_current_password()
        else:
            p = Passman(silence=True, options=options, length=length,
                        description=description, login_info=info)
            p.gen_rand_pass()
            p.save_current_password()
        if args.copy:
            p.copy_current_password()

    else:
        # * cli mode
        p = Passman()
        p.main_menu()
