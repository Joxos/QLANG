import argparse
from collections import OrderedDict
from reserved_names import reserved_names


def split_a_line(msg):
    delimiters = reserved_names['operators']+reserved_names['delimiters']
    words = []
    word = ""
    for char in msg:
        if char == ' ' and word != '':
            words.append(word)
            word = ""
        elif char in delimiters:
            if word:
                words.append(word)
            words.append(char)
            word = ""
        else:
            word += char
    if word:
        words.append(word)
    return words


def split(msg):
    res = []
    for line in msg.split('\n'):
        res.append((len(line)-len(line.lstrip()), split_a_line(line.lstrip())))
    return res


# command line helper
parser = argparse.ArgumentParser(
    description="Compiler for Sakura.")
parser.add_argument('file', type=str, help="file to compile")
args = parser.parse_args()
print("Target file:", args.file)
with open(args.file, 'r') as reader:
    msg = reader.read()
for i in split(msg):
    print(i[0], "indent:", i[1])
