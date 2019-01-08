from builtins import KeyError

class DictList:
    def __init__(self, *args):
        self.dl = list()
        assert len(args) != 0
        for arg in args:
            assert isinstance(arg, dict)
            self.dl.append(arg)
            
    def __len__(self):
        result = set()
        for d in self.dl:
            result = result | set(d.keys())
        return len(result)

    def __repr__(self) -> str:
        return  f"DictList({str(self.dl)[1:-1]})"
       
    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
        return False

    def __getitem__(self, k):
        for i in range(len(self.dl)-1, -1, -1):
            if k in self.dl[i]:
                return self.dl[i][k]
        raise KeyError("the key is not exist in this DictList")
                               
    def __setitem__(self, key, value):
        if self.__contains__(key):
            for i in range(len(self.dl)-1, -1, -1):
                if key in self.dl[i]:
                    self.dl[i][key] = value
                    break
        else:
            self.dl.append({key : value})
            
    def __call__(self, key):
        result = list()
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                result.append((i, self.dl[i][key]))
        return result
    
    def __iter__(self):
        produced = set()
        for i in range(len(self.dl)-1, -1, -1):
            for key in sorted(self.dl[i].keys()):
                if key not in produced:
                    produced.add(key)
                    yield (key, self.dl[i][key])
                    
    def __eq__(self, another):
        if isinstance(another, DictList):
            if len(self) != len(another):
                return False
            for k in another:
                if not self.__contains__(k[0]) or not self.__getitem__(k[0]) == k[1]:
                    return False
        elif isinstance(another, dict):
            if len(self) != len(another.keys()):
                return False
            for k in another:
                if not self.__contains__(k) or not self.__getitem__(k) == another[k]:
                    return False
        else:
            raise TypeError("DictList object can only equal to a Dictlist object or dict object")
        return True
    
    def __add__(self, another):
        if isinstance(another, DictList):
            left = {l[0]: l[1] for l in self}
            right = {r[0]: r[1] for r in another}
            return DictList(left, right)
        elif isinstance(another, dict):
            arguments = [{x: a[x] for x in a} for a in self.dl]
            arguments.append({x : another[x] for x in another})
            return DictList(*arguments)
        else:
            raise TypeError("unsupported type for adding")
        
    def __radd__(self, another):
        if isinstance(another, dict):
            arguments = [{x : another[x] for x in another}]
            for a in self.dl:
                arguments.append({x: a[x] for x in a})
            return DictList(*arguments)
        else:
            raise TypeError("unsupported type for adding")
        
        
        
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
