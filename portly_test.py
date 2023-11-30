import unittest
from importA import containsDuplicate 

class Test_TestImportedA(unittest.TestCase):    
    def test_duplicate(self):
        self.assertEqual(containsDuplicate([1,2,3,4]), False)
        
        
        
if __name__ == '__main__':
    unittest.main()