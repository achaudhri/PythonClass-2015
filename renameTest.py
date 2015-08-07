import unittest
import rename

class renameTest(unittest.TestCase):

	def test_rename(self):
		self.assertEqual('12th', rename.Rename(12))
		self.assertNotEqual('13th', rename.Rename(12))
		
	def test_rename2(self):
		self.assertEqual('3rd', rename.Rename(3))

	def test_rename3(self):
		self.assertEqual('111th', rename.Rename(111))

	def test_rename4(self):
		self.assertEqual('Please enter an integer.', rename.Rename('r'))
		
	def test_rename5(self):
		self.assertEqual('Please do not enter decimal places.', rename.Rename(3.2))
		
if __name__ == '__main__':
  unittest.main() 
