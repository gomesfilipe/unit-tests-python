from src.code_snippets.tester_code_snippet import TesterCodeSnippet
from src.argsparsers.make_tester_argsparser import MakeTesterArgParser
import os

DIR: str = os.path.join('src', 'testers') 
params = MakeTesterArgParser.parse()

TesterCodeSnippet(params.class_name, DIR).run()
