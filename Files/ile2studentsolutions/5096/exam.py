from goody import type_as_str  # Useful in some exceptions
from unittest.mock import right

class DictList:
    def __init__(self, *args):
        if len(args) == 0:
            raise AssertionError('There are no inputs in the __init__ method')
        self.dl = []
        for item in args:
            self.dl.append(item)
            if type(item) != dict:
                raise AssertionError(f'DictList.__init__ \'{item}\' is not a dictionary.')
            
    def __len__(self):
        list_d = []
        for item in self.dl:
            list_d.extend(item.keys())
        return len(set(list_d))
    
    def __repr__(self):
        return_str = ''
        for item in self.dl:
            return_str += str(item)+','
        return f'DictList({return_str[:-1]})'
    
    def __contains__(self, key):
        for item in self.dl:
            if key in item.keys():
                return True
        return False
    
    def __getitem__(self, key):
        assert_list = set([key not in item.keys() for item in self.dl])
        if assert_list == {True}:
            raise KeyError(f'\'{key}\' appears in no dictionaries')
        return_list = []
        for item in self.dl:
            if key in item.keys():
                return_list.append(item[key])
        return return_list[-1]
    
    def __setitem__(self, key, value):
        assert_list = []
        for item in reversed(self.dl):
            if key in item.keys():
                item[key] = value
                assert_list = True
                break
            else:
                assert_list.append(False)
        if assert_list:
            pass
        elif set(assert_list) == {False}:
            self.dl.append(dict(key = value))
        
        
    def __call__(self, value):
        return_list = []
        for i in range(len(self.dl)):
            if value in self.dl[i].keys():
                return_list.append((i, self.dl[i][value]))
        return return_list

    def __iter__(self):
        key_list = []
        for item in reversed(self.dl):
            consider_list = sorted(item.items())
            for i in consider_list:
                if i[0] not in set(key_list):
                    key_list.append(i[0])
                    yield(i)

    def __eq__(self, right):
        if type(self)!= DictList or type(right) not in {DictList, dict}:
            raise TypeError('type of right or self incorrect')
        else:
            if type(right) == DictList:
                self_list = []
                for item in self.dl:
                    for i in item.keys():
                        self_list.append((i, self.__getitem__(i)))
                right_list = []
                for item in right.dl:
                    for i in item.keys():
                        right_list.append((i, right.__getitem__(i)))
                self_list = sorted(list(set(self_list)))
                right_list = sorted(list(set(right_list)))
                return right_list == self_list
            
                        
            elif type(right) == dict:
                right = DictList(right)
                self_list = []
                for item in self.dl:
                    for i in item.keys():
                        self_list.append((i, self.__getitem__(i)))
                right_list = []
                for item in right.dl:
                    for i in item.keys():
                        right_list.append((i, right.__getitem__(i)))
                self_list = sorted(list(set(self_list)))
                right_list = sorted(list(set(right_list)))
                return right_list == self_list
            
            
    def __add__(self, right):
        def tuple_dict(value):
            return_dict = dict()
            for item in value:
                return_dict[item[0]] = item[1]
            return return_dict
        if type(self) == DictList:
            if type(right) == DictList:
                self_list =sorted( [ i for i in self])
                right_list =sorted( [i for i in right])
                return DictList(tuple_dict(self_list), tuple_dict(right_list))
        
        
            elif type(right) == dict:
                return_str = ''
                for item in self.dl:
                    return_str += str(item) + ','
                return_str += right
                return eval(f'DictList({return_str})')
            else:
                raise TypeError('incorrect type of right')
        elif type(self) == dict:
            if type(right) == DictList:
                a = self
                b = right
                right= self
                self = b
                return_str = ''
                for item in self.dl:
                    return_str += str(item) + ','
                return_str += right
                return eval(f'DictList({return_str})')
    
    
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d2 = dict(e=25,f=26,g=27)
    d = DictList(d0,d1,d2)
    d['b'] = 'new1'
    d + d
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
