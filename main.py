from typing import List
from src.testers.tester import Tester
from src.testers.math_tester import MathTester

testers: List[Tester] = [
  MathTester(),  
]

for tester in testers:
  tester.run()
