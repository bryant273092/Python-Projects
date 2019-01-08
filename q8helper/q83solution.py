from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle,random.randint

#random.shuffle(alist) mutates its alist argument to be a random permutation
#random.randint(1,10)  returns a random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
    
    def test_len(self):
        length = 7
        self.assertEqual(len(self.bag), length)
        for i in self.alist:
            self.bag.remove(i)
            length -= 1
            self.assertEqual(len(self.bag), length)
            
    def test_unique(self):
        self.assertEqual(self.bag.unique(), 4)
        temp_list = [i for i in self.alist]
        while True:
            self.bag.remove(temp_list.pop(random.randint(0,len(temp_list)-1)))
            bag =self.bag.unique()
            self.assertEqual(bag, len(set(temp_list)))
            if len(temp_list) == 0:
                break
    
    def test_contains(self):
        self.assertFalse('x' in self.bag)
        value_list = ['a', 'b', 'c', 'd']
        for i in value_list:
            self.assertTrue(i in self.bag)
    
    def test_count(self):
        temp_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'x':0}
        temp_list = [i for i in self.alist]
        for i in range(7):
            for key in self.bag.counts.keys():
                self.assertEqual(temp_dict[key], self.bag.count(key))
            key = temp_list.pop(random.randint(0,len(temp_list)-1))
            temp_dict[key] -= 1
            self.bag.remove(key)
    
    def test_eq(self):
        test_values = [random.randint(1, 10) for i in range(1000)]
        new_bag = Bag(test_values)
        new_bag2 = Bag(test_values)
        self.assertTrue(new_bag==new_bag2)
        new_bag.remove(1)
        self.assertFalse(new_bag == new_bag2)
    def test_add(self):
        test_values = [random.randint(1, 10) for i in range(1000)]
        new_bag = Bag(test_values)
        new_bag2 = Bag([])
        random.shuffle(test_values)
        for i in test_values:
            new_bag2.add(i)
        self.assertTrue(new_bag == new_bag2)
    def test_remove(self):
        test_values = [random.randint(1, 10) for i in range(1000)]
        new_bag = Bag(test_values)
        self.assertRaises(ValueError, new_bag.remove, 43)
        new_bag1 = Bag(test_values)
        random.shuffle(test_values)
        for i in test_values:
            new_bag1.add(i)
        for i in test_values:
            new_bag1.remove(i)
        self.assertTrue(new_bag == new_bag1)