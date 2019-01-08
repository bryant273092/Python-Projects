from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *di):
        assert len(di) > 0
        x = {}
        self.dl = []
        for i in di:
            assert type(i) == type(x)
            self.dl.append(i)
    
    def __len__(self):
        unique = []
        total = 0
        for i in self.dl:
            for k in i.keys():
                if k not in unique:
                    total += 1
                    unique.append(k)
        return total
    
    def __repr__(self):
        return 'DictList{x}'.format(x = tuple(self.dl))
    
    def __contains__(self, item):
        for i in self.dl:
            for k in i.keys():
                if item == k:
                    return True
        return False
    
    def __getitem__(self, item):
        val = None
        for i in self.dl:
            for k in i.keys():
                if item == k:
                    val = i[k]
        if val == None:
            raise KeyError()
        else:
            return val
        
    def __setitem__(self, key, val):
        change = False
        for i in range(len(self.dl)-1,-1,-1):
            if key in self.dl[i].keys():
                self.dl[i][key] = val
                change = True
                break
        if change == False:
            self.dl.append({key:val})
    
    def __call__(self, item):
        results = []
        for i in range(0, len(self.dl)):
            if item in self.dl[i].keys():
                results.append(tuple([i,self.dl[i][item]]))
        return results
    
    def __iter__(self):
        used = []
        for i in range(len(self.dl)-1,-1,-1):
            for k,v in self.dl[i].items():
                if k not in used:
                    yield (k,v)
                    used.append(k)
        
    def __eq__(self, right):
        x = {}
        left_keys = set()
        right_keys = set()
        if type(right) not in [type(x), DictList]:
            raise TypeError()
        for i in self.dl:
            for k in i.keys():
                left_keys.add(k)
        for i in right:
            right_keys.add(i[0])
        if left_keys != right_keys:
            return False
        for i in range(0,len(left_keys)):
            t = right_keys.pop()
            if self.__getitem__(t) != right[t]:
                return False
        return True

#     def __add__(self):
#         left = []
#         left_dict = {}
#         for i in self.dl:
#             for k,v in i.items():
#                 left.append(tuple([k,v]))
#         for j in left:
#             self.dl

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
#     d0 = dict(a=1,b=2,c=3)
#     x = DictList(d0)
#     x['a'] = 2 

#     x = [1,2,3]
#     for i in range(len(x)-1,-1,-1):
#         print(x[i])
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
