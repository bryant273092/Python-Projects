from bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle, random.randint
  #random.shuffle(alist) mutates its slist argument
  #random.randint(1,10)  returns a random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
    
    def test_len(self):
        self.assertEqual(len(self.bag),7)
        size = 7
        random.shuffle(self.alist)
        for i in self.alist:
            self.bag.remove(i)
            size -= 1
            self.assertEqual(len(self.bag),size)
        self.assertEqual(len(self.bag),0)
        
    def test_unique(self):
        self.assertEqual(self.bag.unique(),4)
        random.shuffle(self.alist)
        for i in self.alist:
            self.bag.remove(i)
            self.assertEqual(self.bag.unique(),len(set(self.bag)))
        
    def test_contains(self):
        for v in ['a','b','c','d']:
            self.assertIn(v,self.bag)
        self.assertNotIn('x',self.bag)
        
    def test_count(self):
        for v,c in zip(('a','b','c','d'), (1,2, 1, 3)):
            self.assertEqual(self.bag.count(v),c)
        random.shuffle(self.alist)
        size = 7
        for i in self.alist:
            self.bag.remove(i)
            size -= 1
            sum_count = sum([self.bag.count(c) for c in ['a','b','c','d']])
            self.assertEqual(sum_count,size)
        self.assertEqual(len(self.bag),0)
        
    def test_equals(self):
        alist = [random.randint(1,10) for i in range(1000)]
        b1 = Bag(alist)
        random.shuffle(alist)
        b2 = Bag(alist)
        self.assertEqual(b1,b2)
        b1.remove(alist[0])
        self.assertNotEquals(b1,b2)
        
    def test_add(self):
        alist = [random.randint(1,10) for i in range(1000)]
        b1 = Bag(alist)
        random.shuffle(alist)
        b2 = Bag()
        for v in alist:
            b2.add(v)
        self.assertEqual(b1,b2)
        
    def test_remove(self):
        alist = [random.randint(1,10) for i in range(1000)]
        b1 = Bag(alist)
        self.assertRaises(ValueError,b1.remove,43)
        b2 = Bag(alist)
        random.shuffle(alist)
        for v in alist:
            b2.add(v)
        for v in alist:
            b2.remove(v)
        self.assertEqual(b1,b2)
