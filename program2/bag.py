#Submitter: bryanth1(Hernandez, Bryant)
from collections import defaultdict
from goody import type_as_str, irange
import prompt


class Bag:
    def __init__(self, *args)->object:
        self.args = args
        self.counts =defaultdict(int)
        for v in args:
            for i in v:
                self.counts[i] +=1
#         print('args:', args)
#         print('values', self.counts.values())
#         self.bag = defaultdict(int)
#         if args:
#             for i in args:
#                 for j in i:
#                     self.bag[j]+=1
            
#     def __call__(self, iterable):
#         pass    
# #         if iterable:
# #             for i in iterable:
# #                 self.bag[i] += 1
    def __repr__(self):
        return 'Bag'+str(self.args)
#         bag_list = []
#         for key, count in self.bag.items():
#             for i in irange(count):
#                 bag_list.append(key)
#         return 'Bag(' + str(bag_list)+')'
    def __str__(self):
        return 'Bag('+', '.join([str(k)+'['+str(v)+']' for k,v in self.counts.items()])+')'
#         bag_list =[]
#         for key, count in self.bag.items():
#             bag_list.append(str(key)+str([count]))
#         return 'Bag('+','.join(bag_list)+')'
    def __len__(self):
        return sum(self.counts.values())
#         length_count = 0
#         for count in self.bag.values():
#             length_count += count
#         return length_count
    def unique(self):
        return len(self.counts.keys()) 
              
# #         unique_count = 0
# #         for key in self.bag.keys():
# #             unique_count +=1
# #         return unique_count
    def __contains__(self, item):
        return item in self.counts
     
     
    def count(self, key):
        return self.counts[key] if self.__contains__(key) else 0
#     
#     
    def add(self, item):
        self.counts[item] +=1
# #         self.bag[item] +=1
# 
# #         return item in self.bag
# #         return self.bag[key]
    def __add__(self, bag2):
        if type(bag2) is not Bag:
            raise TypeError
        else:
            return Bag([v for v in self]+[v for v in bag2])
        
# #         if type(bag2) is not Bag:
# #             raise TypeError
# #         new_bag = Bag()
# #         for i in self.bag.keys():
# #             new_bag.bag[i] = self.bag[i]
# #         for i in bag2.bag.keys():
# #             if i in new_bag.bag:
# #                 new_bag.bag[i] += bag2.bag[i]
# #         to_delete = []
# #         for i in new_bag.bag.keys():
# #             if new_bag.bag[i] == 0:
# #                 to_delete.append(i)
# #         for i in to_delete:
# #             del new_bag.bag[i]
# #         return (new_bag)
    def remove(self, item):
        if item in self.counts.keys():
            if self.counts[item] == 1:
                del self.counts[item]
            else:
                self.counts[item]-= 1
        else:
            raise ValueError
#     def __eq__(self, right):
#         pass
# #         if type(right) is not Bag:
# #             return False
# #         for key in self.bag.keys():
# #             if self.bag[key] != 0:
# #                 if key in right.bag and self.bag[key] == right.bag[key]:
# #                     pass
# #                 else:
# #                     return False
# #             else:
# #                 pass
# #         return True  
#     def __ne__(self, right):
#         pass
# #         if type(right) is not Bag:
# #             return True
# #         return not self == right
#     def __iter__(self):
#         pass
# #         class bag_iter:
# #             def __init__(self, bag):
# #                 self._bag = bag
# #                 self._next = 0
# # 
# #             def __next__(self):
# #                 iterable = []
# #                 for key, item in self._bag.items():
# #                     for i in range(item):
# #                         iterable.append(key)       
# #                 try:
# #                     answer = iterable[self._next]
# #                     self._next += 1
# #                 except IndexError:
# #                     raise StopIteration
# #                 return answer
# # 
# #             def __iter__(self):
# #                 return self
#  
#         return bag_iter(self.bag)
#          
#             
#          
#         
#             
            
            



if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

#     b = Bag(['d','a','d','b','c','b','d'])
#     print(repr(b))
#     print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
#     #mytest
#     print(str(b))
#     print(len(b))
#     print(b.unique())
#     #endshere
#     for i in b:
#         print(i)
#   
#     b2 = Bag(['a','a','b','x','d'])
#     print(repr(b2+b2))
#     print(str(b2+b2))
#     print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
#     b = Bag(['a','b','a'])
#     print(repr(b))
#     print()
    
    import driver
    driver.default_file_name = 'bscp21F18.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
