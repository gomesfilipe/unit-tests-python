from src.argsparsers.argparser import ArgParser
import argparse

class MakeTesterArgParser(ArgParser):
  def __init__(self, class_name: str):
    self.class_name = class_name

  @staticmethod
  def parse() -> 'MakeTesterArgParser':
    parser = argparse.ArgumentParser(description = 'Create Unit Test Files.')

    parser.add_argument(
      '-c',
      '--class_name',
      required = True,
      help = 'Class name of tester.',
    )

    parsed_args = parser.parse_args()

    return MakeTesterArgParser(parsed_args.class_name)
