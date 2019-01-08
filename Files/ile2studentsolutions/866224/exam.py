from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        for a in args:
            if type(a) != dict:
                raise AssertionError('DictList.__init__:',a,"' is not a dictionary")
        
            else:
                self.dl.append(a)
                
    def __len__(self):
        keys = []
        for i in self.dl:
            for j in i:
                if j not in keys:
                    keys.append(j)
        
        return len(keys)
        
    def __repr__(self):
        return str('DictList(' + ','.join(str(i) for i in self.dl) + ")")
    
    def __contains__(self, arg):
        for i in self.dl:
            for j in i:
                if arg == j:
                    return True
        return False
                
    def __getitem__(self, arg):
        value = 0
        for i in self.dl:
            if arg in i.keys():
                value = i[arg]
        if value != 0:
            return value
        else:
            raise KeyError(str(arg), "appears in no dictionaries")
        
    def __setitem__(self, k, v):
        pass
#         count = 0
#         while count != -(len(self.dl)):
#             count -= 1
#             stop = 0
#             for i in self.dl[count]:
#                 if k in i and self.dl.index(i) == -1:
#                     i[k] = v
# #                 elif k in i and self.dl.index(i) < count:
# #                     i[k] = v
#                 if k not in i:
#                     self.dl.append({k:v})
       
                    
                    
                
                
    def __call__(self, k):
        l = []
        for i in range(len(self.dl)):
            if k in self.dl[i]:
                l.append((i, self.dl[i][k]))
        return l
        
            
    def __iter__(self):
        def gen(data):
            n = 0
            while n != -(len(data)):
                n -= 1
                for i in data[n]: #data is list, i is dict
                    
                    for k in sorted(i):
                        yield ((k, i[k]))
            
                
        return gen(self.dl)
    
    def __eq__(self, right):
        if type(right) == DictList:
            for d in self.dl:
                for j in right.dl:
                    for dkeys in d.keys():
                        for jkey in j:
                            if dkeys != jkey:
                                return False
                   
                            elif d[dkeys] != j[jkey]:
                                return False
                   
                            else:
                                return True
                
            
        elif type(right) == dict:
            for i in self.dl:
                for k in right.keys():
                    for j in i: #for keys in dict i
                        if j != k or i[j] != right[k]:
                            return False
                    
                        
                        else:
                            return True
                
                 
        




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d= DictList({'a': 1, 'b': 2})
    d2 = dict({'a': 1, 'c':3})
    print(d == d2)
    
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
