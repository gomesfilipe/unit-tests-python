import traceback
from typing import Union, List
from src.utils.debug_utils import dd
import sys
import pandas as pd

class FailedTestException(Exception):
  def format_exception(self) -> str:
    exception_type, exception_value, exception_tb = sys.exc_info()

    tb: List[str, Union[str, int]] = [
      {
        'filename': item.filename,
        'line': item.lineno,
        'method': item.name, 
      } for item in traceback.extract_tb(exception_tb)
    ]

    return pd.DataFrame(tb).to_string()
