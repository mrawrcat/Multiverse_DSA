import unittest   # The test framework
import A

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertNotEqual(3, 4)
        
    def test_duplicate(self):
        self.assertEqual(A.containsDuplicate([1,2,3,4]), True)
        
if __name__ == '__main__':
    unittest.main()