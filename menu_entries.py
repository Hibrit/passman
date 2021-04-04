from locale import getdefaultlocale


EN = {
    'set_options': [
        '============ Set Options ============',
        'current options are >> {}',
        'password length >> {}',
        '(l) to toggle option lowercase',
        '(u) to toggle option uppercase',
        '(d) to toggle option digits',
        '(p) to toggle option puctuation',
        '(x) to set password length',
        '(s) save current settings and return to generation',
        '(g) discard current settings and return to generation',
        '(q) quit',
    ],
    'set_information': [
        '============ Set Information ============',
        'login info >> {}',
        'description >> {}',
        '(i) set login info',
        '(d) set description',
        '(s) save information and return to generation',
        '(g) discard information and return to generation',
        '(q) quit',
    ],
    'generate_password_menu_1': [
        '============ Password Generation ============',
        'current options are >> {}',
        'password length >> {}',
        'login info >> {}',
        'description >> {}',
        'current password >> {}',
        '(o) set password generating options',
        '(i) set information',
        '(g) generate or regenerate password',
        '(s) save current password',
        '(c) copy current password',
        '(e) edit password manually',
        '(m) main menu',
        '(q) quit',
    ],
    'generate_password_menu_2': [
        '============ Password Generation ============',
        'current options are >> {}',
        'password length >> {}',
        'login info >> {}',
        'description >> {}',
        '(o) set password generating options',
        '(i) set information',
        '(g) generate or regenerate password',
        '(s) save current password',
        '(c) copy current password',
        '(e) edit password manually',
        '(m) main menu',
        '(q) quit',
    ],
    'detailed_view': [
        '============ Detailed View ============',
        'login info >> {}',
        'description >> {}',
        'password >> {}',
        '(c) copy password',
        '(e) edit password',
        '(d) delete',
        '(v) view menu',
        '(m) main menu',
        '(q) quit'
    ],
    'main_menu': [
        '============ Main Menu ============',
        'Hi I am your personal password manager',
        '(g) generate a new password',
        '(v) view saved passwords',
        '(q) quit',
    ]

}


def get_entry(entry, variables=None) -> list:
    """
        Send variables in a list to this function
    """

    #! make this toggleable for languages
    message = EN[entry].copy()

    if not variables is None:
        for index, line in enumerate(message):
            if '{}' in line:
                message[index] = line.replace('{}', str(variables.pop(0)))

    return message
