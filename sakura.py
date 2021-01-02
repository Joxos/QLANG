from lexer import lexer
from command_line_helper import args


print("Target file:", args.file)

print("Reading the file...", end='')
with open(args.file, 'r') as reader:
    msg = reader.read()
print("Done.")

print("Doing lexical analysis...", end='')
res = lexer(msg)
print("Done.")

for i in res:
    print(i[0], "indent:", i[1])
