import colorama
from sys import exit
colorama.init(autoreset=True)


class IndentError:
    def __init__(self, line_number, rare_line):
        print(colorama.Fore.RED+"Unexpectly indent at line "+str(line_number)+":")
        print(colorama.Fore.RED+'    '+rare_line.lstrip())
        exit(0)
