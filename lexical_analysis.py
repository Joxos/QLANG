from reserved_names import reserved_names


class Token(object):
    def __init__(self, token):
        self.token = token
        self.type = self.find_token(self.token)

    def find_token(self, word):
        if word in reserved_names['types']:
            return "keyword"
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

class Line(object):
    def __init__(self, line, line_number):
        self.rare_line = line
        self.indents = len(line)-len(line.lstrip())
        self.line_number = line_number

    def tokenize(self):
        delimiters = reserved_names['operators']+reserved_names['delimiters']
        current = ""
        for char in self.rare_line.lstrip():
            if char == ' ' and current != '':
                yield Token(current.lstrip())
                current = ""
            elif char in delimiters:
                if current:
                    yield Token(current.lstrip())
                yield Token(char)
                current = ""
            else:
                current += char
        # if something were left in the variable word
        if current:
            yield Token(current.lstrip())


def tokenize(file_name):
    line_number = 1
    with open(file_name, 'r') as reader:
        content = reader.read()
    for line in content.split('\n'):
        yield Line(line, line_number)
        line_number += 1
