from src.testers.tester import Tester, test, expect
from src.utils.math_utils import summ, sub

class MathTester(Tester):
  @test('Sum of Integers')
  def test_1(self):
    expect(summ(2, 5))\
      .to_be(7)\
      .to_be_truthy()\
      .to_be_greater_than(5)
    
    expect(summ(100, 5))\
      .to_be(105)\
      .to_be_truthy()\
      .to_be_greater_than_or_equal(104)
    
  @test('Subtraction of Integers')
  def test_2(self):
    expect(sub(2, 5))\
      .to_be(-3)\
      .to_be_truthy()\
      .to_be_less_than(0)
    
    expect(sub(100, 100))\
      .to_be(0)\
      .to_be_falsy()\
      .nott().to_be_truthy()\
      .to_be_greater_than_or_equal(-0.9)
