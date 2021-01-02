from collections import OrderedDict
from sys import exit

import colorama

from command_line_helper import args
from lexical_analysis import lexical_analysis
from pre_checker import check_all
colorama.init(autoreset=True)



# read the target file
with open(args.file, 'r') as reader:
    msg = reader.read()

# lexical analysis
res = lexical_analysis(msg)
# for i in res:
# print(i)

# pre-check the codes
status = check_all(res)
if not status[0]:
    print(colorama.Fore.RED+"Error when checking " +
          str(status[1]) + " at line " + str(status[2]) + ", exit.")
    exit(0)

# runtime
variables = OrderedDict()
functions = OrderedDict()
