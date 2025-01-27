from abc import ABC, abstractmethod
from typing import List
from src.enums.color import Color
import time

class CodeSnippet(ABC):
  def __init__(self, filename: str):
    self._filename = filename

  @abstractmethod
  def _handle(self) -> List[str]:
    pass

  def run(self) -> None:
    try:
      Color.YELLOW.print(f'Creating file {self._filename}...')
      time.sleep(0.2)

      with open(self._filename, 'x') as file:
        file.write('\n'.join(self._handle()))
      
      Color.GREEN.print(f'File {self._filename} created successfully!')
      
    except FileExistsError as exception:
      Color.RED.print(f'The file {self._filename} already exists.')
