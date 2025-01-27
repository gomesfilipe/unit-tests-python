from typing import Any, Optional, Type, Union
from src.exceptions.failed_test_exception import FailedTestException
from src.utils.debug_utils import dd

class Expect():
  def __init__(self, value: Any):
    self.__value = value
    self.__positive: bool = True

  def __throw_if(self, expr: bool) -> 'Expect':
    if self.__eval(expr):
      raise FailedTestException()

    self.__positive = True

    return self

  def __eval(self, expr: bool) -> bool:
    return expr if self.__positive else not expr

  def nott(self) -> 'Expect':
    self.__positive = False
    return self

  def to_be(self, value: Any) -> 'Expect':
    return self.__throw_if(self.__value != value)
  
  def to_be_truthy(self) -> 'Expect':
    return self.__throw_if(not self.__value)
  
  def to_be_falsy(self) -> 'Expect':
    return self.__throw_if(self.__value)
  
  def to_be_none(self) -> 'Expect':
    return self.__throw_if(self.__value is not None)
  
  def to_be_greater_than(self, value: Union[int, float]) -> 'Expect':
    return self.__throw_if(not (self.__value > value))
  
  def to_be_greater_than_or_equal(self, value: Union[int, float]) -> 'Expect':
    return self.__throw_if(not (self.__value >= value))
  
  def to_be_less_than(self, value: Union[int, float]) -> 'Expect':
    return self.__throw_if(not (self.__value < value))
  
  def to_be_less_than_or_equal(self, value: Union[int, float]) -> 'Expect':
    return self.__throw_if(not (self.__value <= value))
  
  def to_contain(self, value: Any) -> 'Expect':
    return self.__throw_if(value not in self.__value)
  
  def to_throw(self, exception_class: Type[Exception]) -> 'Expect':
    try:
      self.__value()
      return self.__throw_if(True)

    except exception_class as exception:
      return self.__throw_if(False)

    except Exception as exception:
      return self.__throw_if(True)
    
  def to_have_len(self, value: int) -> 'Expect':
    return self.__throw_if(len(self.__value) != value)
  
  def to_have_attr(self, attr: str) -> 'Expect':
    return self.__throw_if(not hasattr(self.__value, attr))
