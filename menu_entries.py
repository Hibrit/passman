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
    ],
    'password_saved': ['Password saved'],
    'password_copied': ['Password copied'],
    'password_deleted': ['Password deleted'],
    'view_menu': ['============ Page {} ============'],
    'not_specified': 'not specified',
    'specify_password_length': 'please specify a password length >> ',
    'enter_integer': 'please enter an integer',
    'no_such_option': 'there is no such option',
    'set_login_info': 'please set login info >> ',
    'set_description': 'please set description >> ',
    'set_password': 'please set password >> ',
    'dont_have_any_saved': 'you don\'t have any saved passwords',
    'main_menu_message': '(m) main menu',
    'quit_message': '(q) quit',
    'next_page_message': '(n) next page',
    'previous_page_message': '(p) previous page',
}

TR = {
    'set_options': [
        '============ Ayarları Düzenle ============',
        'güncel ayarlar >> {}',
        'şifre uzunluğu >> {}',
        '(l) küçük harfi aç/kapa',
        '(u) büyük harfi aç/kapa',
        '(d) rakamları aç/kapa',
        '(p) özel karakterleri aç/kapa',
        '(x) şifre uzunluğu belirle',
        '(s) güncel ayarları tut ve şifre oluşturma menüsüne dön',
        '(g) güncel ayarları unut ve şifre oluşturma menüsüne dön',
        '(q) çık',
    ],
    'set_information': [
        '============ Bilgileri Gir ============',
        'giriş bilgisi >> {}',
        'açıklama >> {}',
        '(i) giriş bilgisini ayarla',
        '(d) açıklamayı ayarla',
        '(s) güncel ayarları tut ve şifre oluşturma menüsüne dön',
        '(g) güncel ayarları unut ve şifre oluşturma menüsüne dön',
        '(q) çık',
    ],
    'generate_password_menu_1': [
        '============ Şifre Oluşturma ============',
        'güncel ayarlar >> {}',
        'şifre uzunluğu >> {}',
        'giriş bilgisi >> {}',
        'açıklama >> {}',
        'güncel şifre >> {}',
        '(o) şifre oluşturma seçeneklerini ayarla',
        '(i) bilgilerini gir',
        '(g) şifre oluştur/yeniden oluştur',
        '(s) güncel şifreyi kaydet',
        '(c) güncel şifreyi kopyala',
        '(e) şifreyi elle gir',
        '(m) ana menü',
        '(q) çık',
    ],
    'generate_password_menu_2': [
        '============ Şifre Oluşturma ============',
        'güncel ayarlar >> {}',
        'şifre uzunluğu >> {}',
        'giriş bilgisi >> {}',
        'açıklama >> {}',
        '(o) şifre oluşturma seçeneklerini ayarla',
        '(i) bilgilerini gir',
        '(g) şifre oluştur/yeniden oluştur',
        '(s) güncel şifreyi kaydet',
        '(c) güncel şifreyi kopyala',
        '(e) şifreyi elle gir',
        '(m) ana menü',
        '(q) çık',
    ],
    'detailed_view': [
        '============ Detaylı Görünüm ============',
        'giriş bilgisi >> {}',
        'açıklama >> {}',
        'şifre >> {}',
        '(c) şifreyi kopyala',
        '(e) şifreyi düzenle',
        '(d) şifreyi sil',
        '(v) görünüm menüsü',
        '(m) ana menü',
        '(q) çık'
    ],
    'main_menu': [
        '============ Ana Menü ============',
        'Merhaba ben sizin kişisel şifre yöneticinizim',
        '(g) yeni bir şifre oluştur',
        '(v) kaydedilmiş şifreleri gör',
        '(q) çık',
    ]
}


def get_entry(entry, variables=None) -> list:
    """
        Send variables in a list to this function
    """

    #! make this toggleable for languages

    if type(EN[entry]) == list:
        message = EN[entry].copy()
    else:
        message = EN[entry]

    if not variables is None:
        for index, line in enumerate(message):
            if '{}' in line:
                message[index] = line.replace('{}', str(variables.pop(0)))

    return message
