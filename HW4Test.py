# Ambreen Chaudhri
# HW 4 Sorting Algorithm Tests


import unittest
import HW4sort
import random

correct_order = [1,2,3,4,5,6,7,8,9,10]
reverse_order = [10,9,8,7,6,5,4,3,2,1]
not_list = 210
not_sorted = [7,4,5,9,2,3,6,8,10,1]
random_list = random.sample(range(1,11),10)

class sortTest(unittest.TestCase):

	def test_quicksort1(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.quicksort(correct_order))

	def test_quicksort2(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.quicksort(reverse_order))
		
	def test_quicksort3(self):
		self.assertEqual("Please provide a list of elements as your input.  For instance [1,2,3,4].", HW4sort.quicksort(not_list))

	def test_quicksort4(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.quicksort(not_sorted))
		
	def test_quicksort5(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.quicksort(random_list))
		
	def test_bubblesort1(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.bubblesort(correct_order))

	def test_bubblesort2(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.bubblesort(reverse_order))
		
	def test_bubblesort3(self):
		self.assertEqual("Please provide a list of elements as your input.  For instance [1,2,3,4].", HW4sort.bubblesort(not_list))

	def test_bubblesort4(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.bubblesort(not_sorted))
		
	def test_bubblesort5(self):
		self.assertEqual([1,2,3,4,5,6,7,8,9,10], HW4sort.bubblesort(random_list))




if __name__ == '__main__':
    unittest.main()