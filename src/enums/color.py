from src.enums.base_enum import BaseEnum
from typing import Dict

class Color(BaseEnum):
  WHITE = 'White'
  BLUE = 'Blue'
  YELLOW = 'Yellow'
  RED = 'Red'
  GREEN = 'Green'
  PINK = 'Pink'

  def code(self) -> str:
    colors: Dict[str, str] = {
      Color.WHITE: '\033[0m',
      Color.BLUE: '\033[94m',
      Color.YELLOW: '\033[93m',
      Color.RED: '\033[91m',
      Color.GREEN: '\033[92m',
      Color.PINK: '\033[95m',
    }

    return colors.get(self, colors[Color.WHITE])
  
  def print(self, string: str) -> None:
    print(f'{self.code()}{string}{Color.WHITE.code()}')
