from reserved_names import reserved_names


def token_finder(word):
    if word in reserved_names['types']:
        return 'type'
    elif word in reserved_names['keywords']:
        return 'keyword'
    elif word in reserved_names['packages']:
        return 'package'
    elif word in reserved_names['operators']:
        return 'operator'
    elif word in reserved_names['decorators']:
        return 'decorator'
    elif word in reserved_names['delimiters']:
        return 'delimiter'
    else:
        try:
            int(word)
        except:
            return 'identifier'
        else:
            return 'number'


def split_a_line(line):
    delimiters = reserved_names['operators']+reserved_names['delimiters']
    words = []
    word = ""
    for char in line:
        if char == ' ' and word != '':
            words.append([word, token_finder(word)])
            word = ""
        elif char in delimiters:
            if word:
                words.append([word, token_finder(word)])
            words.append([char, token_finder(char)])
            word = ""
        else:
            word += char
    if word:
        words.append([word, token_finder(word)])
    return words


def detect_indent(line):
    return len(line)-len(line.lstrip())


def lexer(msg):
    res = []
    for line in msg.split('\n'):
        res.append((detect_indent(line), split_a_line(line.lstrip())))
    return res
