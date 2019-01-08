from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0: raise AssertionError('No arguments were passed in.')
        for a in args:
            if type(a) != dict:
                raise AssertionError(f'{a} is not a dictionary.')
            else:
                self.dl.append(a)
                
    def __len__(self):
        distinct = []
        count = 0
        
        for d in self.dl:
            for k in d:
                if k not in distinct:
                    distinct.append(k)
                    count += 1
        
        return count
    
    def __repr__(self):
        dicts = ','.join(str(d) for d in self.dl)
        return type_as_str(self)+'('+dicts+')'
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
            
        return False
                    
    def __getitem__(self, item):
        in_d = []
        for d in self.dl:
            if item in d:
                in_d.append(d)
            
        if len(in_d) == 0:
            raise KeyError(f'{item} does not appear in any of the dictionaries')
        
        return in_d[-1][item]
    
    def __setitem__(self, key, value):
        in_d = []
        for d in self.dl:
            if key in d:
                in_d.append(d)
        
        if len(in_d) == 0:
            self.dl.append({key:value})
            
        else:
            in_d[-1][key] = value
            
    def __call__(self, key):
        count = 0
        in_d = []
        for d in self.dl:
            if key in d:
                value = d[key]
                position = count 
                in_d.append((position, value))
                
            count += 1
        
        return in_d
        
    def __iter__(self):
        key_check = []
        copy = self.dl[0:]
        
        while len(copy) != 0:
            d = copy.pop(-1)
            
            for k in d:
                if k in key_check:
                    pass
                else: 
                    yield (k, self.__getitem__(k))
                    key_check.append(k)

        
        
    
    def __eq__(self, right):
        shared_keys = []
        
        if type(right) == type(self):
            for d in self.dl:
                for k in d:
                    if k not in shared_keys: shared_keys.append(k)
            
            for d in right.dl:
                for k in d:
                    if k not in shared_keys: return False
        
        elif(type(right)) == dict:
            for d in self.dl:
                for k in d:
                    if k not in right: return False
                    shared_keys.append(k)
                    
        else:
            raise TypeError(f'type of {right} is not DictList nor dictionary')
                    
        for k in shared_keys:
            if self.__getitem__(k) != right[k]: return False
                
        return True
    
    def __add__(self, right):
        if type(right) == type(self):
            new_DL = DictList(dict(a=1))
            new_DL.dl = self.dl + right.dl
            
            return new_DL
        
        elif type(right) == dict:
            new_DL = DictList(dict(a=1))
            new_DL.dl = self.dl[0:] + [dict(right)]
            
            return new_DL
        
        else:
            raise TypeError(f'Type of {right} is not DictList nor dictionary')
    
    def __radd__(self, right):
        if type(right) == type(self):
            new_DL = DictList(dict(a=1))
            new_DL.dl = self.dl + right.dl
            
            return new_DL
        
        elif type(right) == dict:
            new_DL = DictList(dict(a=1))
            new_DL.dl = [dict(right)] + self.dl[0:]
            
            return new_DL
        
        else:
            raise TypeError(f'Type of {right} is not DictList nor dictionary')
                
                
            
                    



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    
#     c = DictList(dict(a=1,b=2))
#     
#     x = [{1: 'a'}, {2: 'b'}]
#     
#     y = [{3: 'c'}, {4: 'a'}]
#     
#     z = {'a': 'dict'}
#     
#     a = dict(z)
#     
# #     print(a)
#     
#     print(a is z)
#     
#     print(a+c)
    
#     
#     y = x[0:]
#     
#     print('Copy y is', y)
#     print(x is y)
#     
#     print(x.pop(-1))
#     print(x.pop(-1))
#     print(x.pop(-1))
#     
    print()
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
