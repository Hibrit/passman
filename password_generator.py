#!/bin/python

from random import choices
from string import (ascii_lowercase, ascii_uppercase, digits,
                    punctuation)
from json import dumps, loads
from pyperclip import copy


class PasswdGenerator:
    """
    This class is our main generator class that will work with options
    if no options given password will generated with puctuation digits and ascii letters
    give:
    l for lowercase
    u for uppercase
    d for digits
    p for puctuation
    if no length given it will be 16 characters

    usage PasswdGenerator('lud', 20)
    """

    def __init__(self, options=None, length=16):
        if options is None:
            self.options = 'ludp'
        else:
            self.options = options
        if length < 4:
            length = 4
        elif length > 95:
            length = 95
        self.passwd_len = length
        self.keyset = ''
        self.generate_keyset()
        self.passwd = None
        self.description = None

    def add_description(self, description):
        self.description = description

    def add_user_name(self, name):
        self.name = name

    def generate_keyset(self):
        if 'l' in self.options:
            self.keyset += ascii_lowercase
        if 'u' in self.options:
            self.keyset += ascii_uppercase
        if 'd' in self.options:
            self.keyset += digits
        if 'p' in self.options:
            self.keyset += punctuation

    def control(self):
        """
        if this control function returns True you should generate new pass
        """
        if self.passwd is None:
            return True
        regen = False
        if 'l' in self.options:
            for char in ascii_lowercase:
                if char in self.passwd:
                    # * this point character exists in password
                    break
            else:
                regen = True
        if 'u' in self.options:
            for char in ascii_uppercase:
                if char in self.passwd:
                    # * this point character exists in password
                    break
            else:
                regen = True
        if 'd' in self.options:
            for char in digits:
                if char in self.passwd:
                    # * this point character exists in password
                    break
            else:
                regen = True
        if 'p' in self.options:
            for char in punctuation:
                if char in self.passwd:
                    # * this point character exists in password
                    break
            else:
                regen = True
        return regen

    def generate(self):
        while self.control():
            self.passwd = ''.join(choices(self.keyset, k=self.passwd_len))
        return self.passwd

    def copy_passwd(self):
        copy(self.passwd)

    def save(self):
        #! save password to a json file
        all_pass = None
        with open('passwd.json', 'r') as f:
            data = f.read()
            all_pass = loads(data)
        indexes = [int(i) for i in all_pass.keys()]
        index = max(indexes) + 1

        all_pass[index] = {
            'description': self.description,
            'name': self.name,
            'password': self.passwd
        }
        with open('passwd.json', 'w') as f:
            f.write(dumps(all_pass))
        # print(self.passwd)

    def __repr__(self):
        return self.passwd

#! make it more secure and portable with a database and ssh encription
