import argparse


parser = argparse.ArgumentParser(description="Interpreter for Sakura.")
parser.add_argument('file_name', type=str, help="file to compile")
args = parser.parse_args()
