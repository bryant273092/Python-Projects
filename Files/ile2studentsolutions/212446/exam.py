#from goody import type_as_str  # Useful in some exceptions
from collections import defaultdict

class DictList:
    def __init__(self, *args):
        assert len(args) != 0, "DictList class needs atleast one argument"
        assert all(type(a) == dict for a in args), "DictList class only takes arguments of type dict"
        self.dl = [a for a in args]
    
    def __len__(self):
        count = []
        for d in self.dl:
            count = count + [k for k in d.keys()]
        return len(set(count))
    def __repr__(self):
        #print("DictList({d})".format(d= ','.join(str(d) for d in self.dl)))
        return "DictList({d})".format(d= ','.join(str(d) for d in self.dl))
    def __contains__(self,key):
        for d in self.dl:
            if key in d.keys():
                return True
        return False
    def __getitem__(self,key):  
        if not self.__contains__(key):
            raise KeyError("{} is not a key in any of the dictionaries in the dictlist".format(key))
        else:
            val = ''
            for d in self.dl:
                if key in d.keys():
                    val = d[key]
            return val  
    def __setitem__(self,key,val):   
        #print(sorted(self.dl, reverse=True), self.dl)
        if not self.__contains__(key):
            self.dl.append({key:val})  
        else:
            ind = ''
            for d in range(len(self.dl)):
                if key in self.dl[d].keys():
                    ind = d
            self.dl[ind][key] = val  
            
    def __call__(self, key):
        l = []
        for d in range(len(self.dl)):   
            if key in self.dl[d].keys():
                l.append((d,self.dl[d][key]))
        return l  
    
    def __iter__(self):  
        ks = []
        for d in self.dl[::-1]:
            ds = sorted(d)
            for key in ds:
                if key not in ks:
                    yield (key,d[key])
                    ks.append(key)

    def __eq__(self,other):
        if type(other) != DictList and type(other) != dict:
            raise TypeError("Argument must be of type DictList or dict")
        if type(other) == DictList:
            for d in self.dl:
                for k in d.keys():
                    if not other.__contains__(k):
                        return False
                    elif self[k] != other[k]:
                        return False
                    
            return True        
        else:
            for d in self.dl:
                for k in d.keys():
                    if k not in other.keys():
                        return False
                    elif self[k] != other[k]:
                        return False
            return True
        
    def __add__(self,other):
        if type(other) != DictList and type(other) != dict:
            raise TypeError("Argument must be of type DictList or dict")
        d0 = defaultdict(str)
        d1 = defaultdict(str)
        for d in self.dl:
            for k in d.keys():
                d0[k] = d[k]
        if type(other) == DictList:
            for d in other.dl:
                for k in d.keys():
                    d0[k] = d[k] 
            return DictList(dict(d0),dict(d1))
        if type(other) == dict:
            new_args = [d.copy() for d in self.dl]
            new_args.append(other.copy())
            return DictList(*tuple(new_args))
    def __radd__(self,other):
        if type(other) != DictList and type(other) != dict:
            raise TypeError("Argument must be of type DictList or dict")
        if type(other) == dict:
            new_args = [other.copy()] + [d.copy() for d in self.dl]
            return DictList(*tuple(new_args))
        
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
