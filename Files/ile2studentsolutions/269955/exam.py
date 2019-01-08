from goody import type_as_str  # Useful in some exceptions
from goody import irange

class DictList:
    def __init__(self, *args):
        self.dl = []
        if args == ():
            raise AssertionError
        for arg in args:
            if type(arg) != dict:
                raise AssertionError
            else:
                self.dl.append(arg)
        
    def __len__(self):
        S = set()
        for dl in self.dl:
            for i in dl:
                S.add(i)
        return len(S)
        
    def __repr__(self):
        final = "DictList("
        for i in self.dl:
            final += str(i)+","
        return final[:-1]+")"
    
    def __contains__(self, item):
        for dl in self.dl:
            if item in dl.keys():
                return True
        return False
                
    def __getitem__(self, item):
        L = []
        for dl in self.dl:
            if item in dl:
                L.append(dl)
        if L == []:
            raise KeyError
        return L[-1][item]
    
    def __setitem__(self, key, value):
        L = []
        for dl in self.dl:
            if key in dl:
                L.append(dl)
        if L == []:
            self.dl.append({key:value})
        else:
            L[-1][key] = value
            
    def __call__(self, item):
        L = []
        for dl in self.dl:
            if item in dl:
                L.append(dl)
        if L == []:
            return []
        else:
            tl = []
            for num, dl in enumerate(self.dl):
                if item in dl:
                    tl.append((num, dl[item]))
            return tl
                
    def __iter__(self):
        L = []
        for r in irange(len(self.dl)):
            L.append(self.dl[-r])
        used = []
        for dl in L:
            for k, v in dl.items():
                if k not in used:
                    yield (k, v)
                    used.append(k)
                    
    def __eq__(self, right):
        if type(right) not in [DictList, dict]:
            raise TypeError
        else:
            self_keys = set()
            right_keys = set()
            for dl in self.dl:
                for i in dl.keys():
                    self_keys.add(i)
            if type(right) == DictList:
                for dl in right.dl:
                    for k in dl.keys():
                        right_keys.add(k)
            elif type(right) == dict:
                for k in right.keys():
                    right_keys.add(k)
            if self_keys != right_keys:
                return False
            else:
                if type(right) == DictList:
                    self_list = [i for i in self]
                    right_list = [i for i in right]
                    return set(self_list) == set(right_list)
                elif type(right) == dict:
                    self_list = [i for i in self]
                    right_list = [i for i in right.items()]
                    return set(self_list) == set(right_list)
                        
    def __add__(self, right):
        if type(right) not in [DictList, dict]:
            raise TypeError
        elif type(right) == DictList:
            left_dict = {}
            right_dict = {}
            left_list = [i for i in self]
            right_list = [i for i in right]
            for k, v in left_list:
                left_dict[k] = v
            for k, v in right_list:
                right_dict[k] = v
            return DictList(left_dict, right_dict)
        elif type(right) == dict:
            L = []
            for dl in self.dl:
                L.append(dl)
            L.append(right)
            return DictList(*L)
        
        
    def __radd__(self, right):
        if type(right) == dict:
            L = []
            L.append(right)
            for dl in self.dl:
                L.append(dl)
            
            return DictList(*L)
        else:
            raise TypeError
        
    
                
            
                    
            
                
            
                
        
            
            
        




            
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
