from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args)!=0, 'DictList.__init__: there are no dictionaries as arguments'
        self.dl = []
        for item in args:
            assert type(item)==dict, 'DictList.__init__: {} is not a dictionary'.format(item)
            self.dl.append(item)
            
    def __len__(self):
        result = 0
        key_list = []
        for d in self.dl:
            for k in d:
                if k not in key_list:
                    key_list.append(k)
                    result+=1
        return result
    
    def __repr__(self):
        return 'DictList(' + ','.join([str(d) for d in self.dl]) + ')'
    
    def __contains__(self, item):
        for d in self.dl:
            for k in d:
                if k==item:
                    return True
        return False
    
    def __getitem__(self, item):
        result = None
        for d in self.dl:
            for k in d:
                if k==item:
                    result = d[k]
        if result == None:
            raise KeyError('DictList.__getitem__: {} appears in no dictionaries'.format(repr(item)))
        return result
    
    def __setitem__(self, k, value):
        d_num = None
        for i in range(len(self.dl)):
            if k in self.dl[i].keys():
                d_num = i
        if d_num != None:
            self.dl[d_num][k] = value
        else:
            self.dl.append({k:value})
            
    def __call__(self, key):
        result = []
        for i in range(len(self.dl)):
            for k in self.dl[i]:
                if k == key:
                    result.append((i, self.dl[i][k]))
        return result
    
    def __iter__(self):
        iterable = []
        key_list = []
        reversed_dict_list = [d for d in self.dl]
        reversed_dict_list.reverse()
        for d in reversed_dict_list:
            temp = []
            for k,v in d.items():
                if k not in key_list:
                    temp.append((k,v))
                    key_list.append(k)
            for item in sorted(temp):
                iterable.append(item)
        for item in iterable:
            yield item
            
    def __eq__(self, right):
        if type(right) == DictList or type(right) == dict:
            if len(self) != len(right):
                return False
            for k,v in self:
                if k not in right:
                    return False
                if right[k] != v:
                    return False
            return True
        else:
            raise TypeError('DictList.__eq__: DictList object cannot compare with a {} object'.format(type_as_str(right)))
        
    def __add__(self, right):
        if type(right) == DictList:
            d1 = dict((k,v) for k,v in self)
            d2 = dict((k,v) for k,v in right)
            return DictList(d1, d2)
        elif type(right) == dict:
            temp = self.dl[:]
            temp.append(dict(right))
            return DictList(*(d for d in temp))
        else:
            raise TypeError('DictList.__add__: DictList cannot add a {} object'.format(type_as_str(right)))
    
    def __radd__(self, left):
        if type(left) == dict:
            temp = []
            temp.append(dict(left))
            temp.extend(self.dl[:])
            return DictList(*(d for d in temp))
        else:
            raise TypeError('DictList.__radd__: DictList cannot add a {} object'.format(type_as_str(left)))
            




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
