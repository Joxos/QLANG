from runtime import Variable, Function, Class


# built-in
variables = {}
functions = {}
classes = {}

# reserved names
keywords = ['if', 'elif', 'else', 'while', 'for', 'break', 'class', 'continue',
            'in', 'include', 'return', 'true', 'false', 'pass', 'switch', 'case']
built_in_types = ['Int', 'Decimal', 'Fraction', 'String', 'Stack',
                  'Queue', 'Map', 'List', 'File', 'Bool', 'Void', 'Tuple', 'Method']
decorator_names = ['@Template', '@Override',
                   '@Overload', '@Target', '@Decorator']
package_names = ['random', 'time', 'json', 'xml', 'hash']
operators = [
    '+', '-', '*', '/', '**', '%',     # calculate
    '==', '!=', '>', '<', '>=', '<=',  # compare
    'and', 'or', 'in', 'not',          # logical
    '=', '+=', '-=', '*=', '/=', '%='  # copy
]
delimiters = ['.', '\'', '"', ',', '(', ')', '[', ']', '{', '}']
reserved_names = {"keywords": keywords, "types": built_in_types, "decorators": decorator_names,
                  "packages": package_names, "operators": operators, "delimiters": delimiters}
