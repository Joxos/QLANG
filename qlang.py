import argparse

import antlr4
from loguru import logger
from Lexer.SakuraLexer import SakuraLexer
from Lexer.SakuraParser import SakuraParser

parser = argparse.ArgumentParser(description="Interpreter for Sakura.")
parser.add_argument('file_name', type=str, help="file to compile")
args = parser.parse_args()

logger.info(f"File name: {args.file_name}")
input_stream = antlr4.FileStream(args.file_name)
