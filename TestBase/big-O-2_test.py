import unittest


class TestContainsDuplicate(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue([1,1])
        
    def test_false(self):
        self.assertFalse([1])
    

if __name__ == '__main__':
    unittest.main()