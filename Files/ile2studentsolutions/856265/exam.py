from goody import type_as_str  # Useful in some exceptions
from builtins import KeyError


class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        for arg in args:
            if type(arg) is not dict:
                raise AssertionError
            self.dl.append(arg)
            
    def __len__(self):
        result = set()
        for d in self.dl:
            for key in d.keys():
                result.add(key)
        return len(result)
    
    def __repr__(self):
        return 'DictList(' + str(self.dl)[1:-1] + ')'
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
        return False
    
    def __getitem__(self, key):
        result = ''
        for d in self.dl:
            if key in d:
                result = d[key]
        if result == '':
            raise KeyError
        return result
    
    def __setitem__(self, key, value):
        result = None
        for x in range(len(self.dl)):
            if key in self.dl[x]:
                result = x
        if result == None:
            self.dl.append({key: value})
        else:
            self.dl[result][key] = value
        
    def __call__(self, key):
        result = []
        for x in range(len(self.dl)):
            if key in self.dl[x]:
                result.append((x, self.dl[x][key]))
        return result
    
    def __iter__(self):
        result = []
        cont = False
        for d in reversed(self.dl):
            for k in d:
                for t in result:
                    if t[0] == k:
                        cont = True
                if cont == False:
                    result.append((k, d[k]))
                cont = False
        return iter(result)
    
    def __eq__(self, right):
        result1 = []
        cont = False
        for d in reversed(self.dl):
            for k in d:
                for t in result1:
                    if t[0] == k:
                        cont = True
                if cont == False:
                    result1.append((k, d[k]))
                cont = False
        if type(right) is DictList:
            result2 = []
            cont = False
            for d in reversed(right.dl):
                for k in d:
                    for t in result2:
                        if t[0] == k:
                            cont = True
                    if cont == False:
                        result2.append((k, d[k]))
                    cont = False
            return sorted(result1) == sorted(result2)
        elif type(right) is dict:
            keys = set()
            for d in self.dl:
                for key in d.keys():
                    keys.add(key)
            if keys != right.keys():
                return False
            for v in right:
                for x in result1:
                    if v == x[0]:
                        if x[1] != right[v]:
                            return False
            return True
        else:
            raise TypeError
    
    def __add__(self, right):
        if type(right) is DictList:
            d1 = dict()
            for d in self.dl:
                for k in d.keys():
                    d1[k] = d[k]
            d2 = dict()
            for d in right.dl:
                for k in d.keys():
                    d2[k] = d[k]
            return DictList(d1, d2)
        elif type(right) is dict:
            d1 = dict()
            for d in self.dl:
                for k in d.keys():
                    d1[k] = d[k]
            return DictList(d1, right)
        else:
            raise TypeError
    
    def __radd__(self, right):
        if type(right) is dict:
            return DictList(right, self.dl[0], self.dl[1])
        else:
            raise TypeError
        



            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#    driver.default_show_exception=True
#    driver.default_show_exception_message=True
#    driver.default_show_traceback=True
    driver.driver()
