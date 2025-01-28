from typing import List
from src.testers.tester import Tester
from src.testers.math_tester import MathTester
from src.testers.array_tester import ArrayTester

def run_tests() -> None:
  testers: List[Tester] = [
    MathTester(),
    ArrayTester(),
  ]

  for tester in testers:
    tester.run()
