import random
import unittest

# ordered (all 0) but not a permuation
def sort_not_permutation(alist):
    for i in range(len(alist)):
        alist[i] = 0
 
# permutation, but not likely ordered (last 3 values not checked)       
def sort_not_ordered(alist):
    for base in range(len(alist)-3):  # last 3 values unchecked
        for check in range(base+1,len(alist)):
            if alist[base] > alist[check]:
                alist[base], alist[check] = alist[check],alist[base]
    return None  # list is mutated

# raises exception
def sort_exception_sometimes(alist):
    for base in range(len(alist)): #-n for error
        for check in range(base+1,len(alist)):
            assert random.random() > .000001
            if alist[base] > alist[check]:
                alist[base], alist[check] = alist[check],alist[base]
    return None  # list is mutated


sorter       = list.sort #or any other sort above
size_to_sort = 100

class Test_Sorting(unittest.TestCase):
    def setUp(self):
        self.original = [4, 1, 2, 5, 3]
        self.sorted   = list(self.original)
        sorter(self.sorted)
    
    def test_order(self):
        #print('Checking for order:',self.alist)
        self.assertTrue(self._is_ordered())
    
    def test_permutation(self):
        #print('Checking for permutation:',self.alist,'vs',self.sorted)
        self.assertCountEqual(self.original,self.sorted,
                              'List is not a permutation of the original')
    
    def test_large_scale(self):
        self.original  = [i for i in range(size_to_sort)]
        random.shuffle(self.original)
        for i in range(100):
            random.shuffle(self.original)
            self.sorted = list(self.original)
            sorter(self.sorted)
            self.test_order()
            self.test_permutation()
            

    def _is_ordered(self):
        for i in range(len(self.sorted)-1):
            if self.sorted[i] > self.sorted[i+1]:
                return False
        return True
