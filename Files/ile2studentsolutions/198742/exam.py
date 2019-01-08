from goody import type_as_str  # Useful in some exceptions
from _operator import index

class DictList:
    
    def __init__(self, *args):
        
        if len(args) < 1:
            raise AssertionError
        self.dl = []
        
        for dict in args:
            if type(dict) in (str, list, int, float):
                 raise AssertionError
            self.dl.append(dict)
            
    def __len__(self):
        count = []
        for i in self.dl:
            for k in i:
                if k not in count:
                    count.append(k)
        return len(count)

    def __repr__(self):
        return "DictList({Param})".format(Param = ','.join(str(x) for x in self.dl))
    
    def __contains__(self, key):
        for i in self.dl:
            if key in i.keys():
                return True
        return False
                
    def __getitem__(self, key):
        for i in self.dl[::-1]:
            if key in i.keys():
                return i[key]
        raise KeyError
    
    def __setitem__(self, key, value):
        for i in self.dl[::-1]:
            if key in i.keys():
                i[key] = value
                return
        for i in self.dl:        
            if key not in i.keys():
                self.dl.append({key: value})
                
    def __call__(self, key):
        l = []
        real_list = []
        for i in self.dl:
            for k,v in i.items():
                if k == key:
                    l.append((self.dl.index(i),v))
      
        return list(l)
                 

    def __iter__(self):
        l = []
        k_list = []
        for i in self.dl[::-1]:
            sorted(i)
            for k,v in i.items():
                if k not in k_list:
                    l.append((k,v))
                    k_list.append(k)
        for i in l:
            yield i

    def __eq__(self, right):
        if type(right) not in (dict, DictList):
            raise TypeError
        for i in self.dl:
            for k,v in i.items():
                if self.__getitem__(k) == right.__getitem__(k):
                    return True
                else:
                    return False


            
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
