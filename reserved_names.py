keywords = ['if', 'elif',
            'else', 'while', 'for', 'break', 'class', 'continue', 'in', 'include', 'return', 'true', 'false']
type_names = ['Int', 'Decimal', 'Fraction', 'String', 'Stack',
              'Queue', 'Map', 'List', 'File', 'Bool', 'Void', 'Tuple', 'Method']
decorator_names = ['@Template', '@Override',
                   '@Overload', '@Target', '@Decorator']
package_names = ['random', 'time', 'json', 'xml', 'hash']
operators = [
    '+', '-', '*', '/', '**', '%',  # calculate
    '==', '!=', '>', '<', '>=', '<=',  # compare
    'and', 'or', 'in', 'not',  # logical
    '=', '+=', '-=', '*=', '/=', '%='  # copy
]
delimiters = ['.', '\'', '"', ',', '(', ')', '[', ']', '{', '}']
reserved_names = {"keywords": keywords, "types": type_names, "decorators": decorator_names,
                  "packages": package_names, "operators": operators, "delimiters": delimiters}
