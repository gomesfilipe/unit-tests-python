from typing import List, Any, Callable, Optional, Dict

def array_first_where(arr: List[Any], fn_condition: Callable[[Any], bool]) -> Optional[Any]:
  for item in arr:
    if fn_condition(item):
      return item

  return None

def array_where(arr: List[Any], fn_condition: Callable[[Any], bool]) -> List[Any]:
  return [item for item in arr if fn_condition(item)]

def array_sort(arr: List[Any], fn: Callable[[Any], Any] = None) -> List[Any]:
  return sorted(arr, key = fn)

def array_count(arr: List[Any], fn: Optional[Callable[[Any], Any]] = None) -> Dict[Any, int]:
  counter: Dict[Any, int] = {}

  for item in arr:
    key = item if fn is None else fn(item)
    counter[key] = counter.get(key, 0) + 1
  
  return counter
