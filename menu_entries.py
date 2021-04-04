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
