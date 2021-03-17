from argparse import ArgumentParser
def get_arguments():
    parser = ArgumentParser(description='advanced password manager')
    parser.add_argument('-s', '--silence', type=bool, help='if this option is specified cli will now show up')
    parser.add_argument('-o', '--options', type=str, help='password generation options lupd')
    parser.add_argument('-l', '--length', type=int, help='password length')
    parser.add_argument('-d', '--description', type=str, help='password description')
    parser.add_argument('-i', '--info', type=str, help='login information for password')
    parser.add_argument('-p', '--password', type=str, help='password to save if specified overwrites -o -l')
    parser.add_argument('-c', '--copy', type=bool, help='copies the randomly generated password')
    return parser.parse_args()
