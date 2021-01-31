from sys import exit
import errors


def indent_checker(res):
    for i in res:
        if i[0] % 4 != 0:
            errors.IndentError(i[2], i[3])
            exit(0)


def check_all(res):
    indent_checker(res)
