from src.testers.tester import Tester, test, expect
from src.utils.math_utils import summ, sub, div

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
  def test_2(self) -> None:
    expect(sub(2, 5))\
      .to_be(-3)\
      .to_be_truthy()\
      .to_be_less_than(0)
    
    expect(sub(100, 100))\
      .to_be(0)\
      .to_be_falsy()\
      .nott().to_be_truthy()\
      .to_be_greater_than_or_equal(-0.9)
  
  @test('Division of Integers')
  def test_3(self) -> None:
    expect(div(10, 2)).to_be(5)

    expect(div(5, 4)).to_be(1.25)\
      .to_be_greater_than(1)\
      .to_be_less_than(1.5)

    expect(lambda: div(1, 0)).to_throw(ZeroDivisionError)
