import unittest

class Sorting(unittest.TestCase):
    
    def setUp(self):
        self.original = [4, 1, 2, 5, 3]
        self.sorted   = list(self.original)
        list.sort(self.sorted)
    
    def test_order(self):
        self.assertTrue(self._is_ordered(), 'List is not in order')
    
    def test_permutation(self):
        self.assertCountEqual(self.original,self.sorted,
                              'List is not a permutation of the original')
    
    def _is_ordered(self):
        for i in range(len(self.sorted)-1):
            if self.sorted[i] > self.sorted[i+1]:
                return False
        return True 
