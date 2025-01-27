from src.code_snippets.code_snippet import CodeSnippet
from typing import List
from src.enums.color import Color
from src.utils.str_utils import to_snake_case, to_pascal_case
import os
from src.utils.debug_utils import dd

class TesterCodeSnippet(CodeSnippet):
  def __init__(self, class_name: str, dir: str = ''):
    self._class_name = to_pascal_case(class_name)
  
    super().__init__(
      filename = os.path.join(dir, to_snake_case(self._class_name)) + '.py',
    )
  
  def _handle(self) -> List[str]:
    return [
      'from src.testers.tester import Tester, test, expect',
      '',
      f'class {self._class_name}(Tester):',
      '\tdef _before_all(self) -> None:',
      '\t\treturn',
      '',
      '\tdef _after_all(self) -> None:',
      '\t\treturn',
      '',
      '\tdef _before_each(self) -> None:',
      '\t\treturn',
      '',
      '\tdef _after_each(self) -> None:',
      '\t\treturn',
      '',
      "\t@test('Test Description')",
      '\tdef example_test(self) -> None:',
      '\t\texpect(2 + 2).to_be(4)',
      '',
    ]
