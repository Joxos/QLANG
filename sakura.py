from command_line_helper import args
from lexical_analysis import tokenize
from runtime import Runtime


runtime = Runtime()
for current in tokenize(args.file_name):
    runtime.execute(current)

# for current in tokenize(args.file_name):
#     print("Line number:", current.line_number)
#     print("Indent spaces:", current.indents)
#     print("Rare line:", current.rare_line)
#     print("Tokens:")
#     for token in current.tokenize():
#         print(token.token, end=':')
#         print(token.type)
#     print()
