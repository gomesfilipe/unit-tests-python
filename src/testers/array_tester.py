from src.testers.tester import Tester, test, expect
from typing import List
from src.utils.array_utils import array_first_where, array_where, array_count, array_sort
from src.utils.debug_utils import dd

class ArrayTester(Tester):
	def _before_each(self) -> None:
		self.__int_arr: List[int] = [2, 8, 6, 9, 7, 3]
		self.__str_arr: List[int] = ['x', 'y', 'a', 'r']

	@test('Array First Where')
	def test_1(self) -> None:
		expect(array_first_where(self.__int_arr, lambda item: item > 5))\
			.to_be(8)\
			.to_be_greater_than(5)\
			.nott().to_be_none()
		
		expect(array_first_where(self.__str_arr, lambda item: item in 'banana'))\
			.to_be('a')\
			.to_be_truthy()\
			.nott().to_be_none()
		
		expect(array_first_where(self.__int_arr, lambda item: item > 10))\
			.to_be_none()\
			.to_be_falsy()
		
		expect(array_first_where(self.__str_arr, lambda item: item in 'test'))\
			.to_be_none()\
			.nott().to_be_truthy()
		
	@test('Array Where')
	def test_2(self) -> None:
		expect(array_where(self.__int_arr, lambda item: item > 5))\
			.to_be([8, 6, 9, 7])\
			.to_have_len(4)\
			.to_contain(6)
		
		expect(array_where(self.__str_arr, lambda item: item in 'race'))\
			.to_contain('a')\
			.to_contain('r')\
			.nott().to_contain('x')\
			.nott().to_be_none()\
			.to_have_len(2)\
		
		expect(array_where(self.__int_arr, lambda item: item > 10))\
			.to_be([])\
			.to_be_falsy()\
			.nott().to_contain(1)
		
		expect(array_where(self.__str_arr, lambda item: item in 'test'))\
			.nott().to_be_none()\
			.nott().to_be_truthy()\
			.to_have_len(0)
	
	@test('Array Sort')
	def test_3(self) -> None:
		expect(array_sort(self.__int_arr))\
			.to_be([2, 3, 6, 7, 8, 9])\
			.nott().to_be(self.__int_arr)\
			.nott().to_contain(0)\
			.to_contain(3)\
			.to_contain(8)
		
		expect(array_sort(self.__int_arr, lambda item: 1 / item))\
			.to_be([9, 8, 7, 6, 3, 2])\
			.to_have_len(6)
		
		expect(lambda: array_sort(self.__int_arr + [0], lambda item: 1 / item))\
			.to_throw(ZeroDivisionError)
		
		expect(array_sort(self.__str_arr))\
			.to_be(['a', 'r', 'x', 'y'])\
			.nott().to_be(self.__str_arr)\
			.nott().to_contain('w')\
			.to_contain('r')\
			.to_contain('x')
		
	@test('Array Count')
	def test_4(self) -> None:
		int_counter = array_count(self.__int_arr + [2, 2, 8])
		str_counter = array_count(self.__str_arr + ['y', 'a'])
		
		expect(int_counter[2]).to_be(3)
		expect(int_counter[8]).to_be(2)
		expect(int_counter[7]).to_be(1)
		expect(lambda: int_counter[0]).to_throw(KeyError)

		expect(str_counter['y']).to_be(2)
		expect(str_counter['a']).to_be(2)
		expect(str_counter['x']).to_be(1)
		expect(lambda: int_counter['b']).to_throw(KeyError)
