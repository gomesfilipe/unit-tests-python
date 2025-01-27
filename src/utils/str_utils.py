def upper_first(string: str) -> str:
  if string:
    return string[0].upper() + string[1:]
  
  return string

def to_snake_case(string: str) -> str:
  return ''.join([f'_{i.lower()}' if i.isupper() else i for i in string]).lstrip('_')

def to_pascal_case(string: str) -> str:
  return ''.join([upper_first(word) for word in string.split('_')])

