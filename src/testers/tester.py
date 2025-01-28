from abc import ABC, abstractmethod
from src.exceptions.failed_test_exception import FailedTestException
from typing import List, Tuple, Callable, Type, Any
import traceback
import time
from src.utils.debug_utils import dd
from src.enums.color import Color
from src.testers.expect import Expect

def test(description: str):
  def decorator(func: Callable) -> Callable:
    def wrapper(self):
      return func(self)

    wrapper.description = description
    wrapper.is_test = True

    return wrapper
  return decorator

def expect(value: Any) -> Expect:
  return Expect(value)

class Tester(ABC):
  def __init__(self) -> None:
    self.__failed_tests: bool = False
    self.__delay: float = 0.05

  def _before_all(self) -> None:
    return

  def _after_all(self) -> None:
    return

  def _before_each(self) -> None:
    return

  def _after_each(self) -> None:
    return

  def _on_failed(self, exception: FailedTestException) -> None:
    Color.RED.print(exception.format_exception())

  def run(self) -> None:
    try:
      Color.PINK.print(f'Running {type(self).__name__}')
      self._before_all()
      time.sleep(self.__delay)

      for test_method in self.__test_methods():
        self._before_each()

        Color.YELLOW.print(f'[RUNNING] {test_method.description}')
        time.sleep(self.__delay)

        test_method(self)

        Color.GREEN.print(f'[SUCCESS] {test_method.description}')
        time.sleep(self.__delay)

        self._after_each()

    except FailedTestException as e:
      Color.RED.print(f'[FAILURE] {test_method.description}')
      self.__failed_tests = True
      self._on_failed(e)

    finally:
      self._after_all()
      Color.BLUE.print('The execution of tests has ended with failure.' if self.__failed_tests else f'All tests of {type(self).__name__} have been executed successfully!')
      Color.WHITE.print('\n')

  def __test_methods(self) -> List[Callable]:
    return [method for name, method in type(self).__dict__.items() if callable(method) and hasattr(method, 'is_test')]
