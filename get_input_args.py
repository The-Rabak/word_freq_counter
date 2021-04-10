import argparse

class ParseArguments():
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def add_input_args(self, flag, type, default = '', help = ''):
        self.parser.add_argument(flag, type=type, default=default, help=help)

    def get_parsed_args(self):
        return self.parser.parse_args()
