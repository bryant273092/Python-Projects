from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert args != ()
        for x in args:
            assert type(x) == dict, 'DictList.__init__:{0} is not a dictionary'.format(str(x))
        self.dl = [x for x in args]

    def __len__(self):
        keys = set()
        for x in self.dl:
            for k in x.keys():
                keys.add(k)
        return len(keys)
    
    def __repr__(self):
        dl = [str(x) for x in self.dl]
        return 'DictList({0})'.format(', '.join(dl))

    def __contains__(self, arg):
        for x in self.dl:
            for k in x.keys():
                if arg == k:
                    return True
        return False
    
    def __getitem__(self, arg):
        if self.__contains__(arg):
            self.dl.reverse()
            for x in self.dl:
                if arg in x.keys():
                    self.dl.reverse()
                    return x[arg]
        else:
            raise KeyError(str(arg) + ' appears in no dictionaries.')
        
    def __setitem__(self, k, v):
        done = set()
        if self.__contains__(k):
            self.dl.reverse()
            for x in self.dl:
                if k in x.keys():
                    if k not in done:
                        done.add(k)
                        x[k] = v
            self.dl.reverse()
        else:
            self.dl.append({k:v})
        
    def __call__(self, arg):
        result = []
        if self.__contains__(arg):
            count = -1
            for x in self.dl:
                count += 1
                if arg in x.keys():
                    result.append((count, x[arg])) 
        return result
    
    def __iter__(self):
        yielded = set()
        self.dl.reverse()
        for x in self.dl:
            for k in sorted(x.keys()):
                if k not in yielded:
                    yielded.add(k)
                    yield (k, x[k])
        self.dl.reverse()
                
    def __eq__(self, arg):
        if type(arg) == DictList:
            keys = set()
            for x in self.dl:
                for k in x.keys():
                    keys.add(k)
            d1 = dict()
            d2 = dict()
            for k in keys:
                d1[k] = self.__getitem__(k)
                d2[k] = arg.__getitem__(k)
            if d1 == d2:
                return True
            else:
                return False
        elif type(arg) == dict:
            keys = set()
            for x in self.dl:
                for k in x.keys():
                    keys.add(k)
            d1 = dict()
            d2 = arg
            for k in keys:
                d1[k] = self.__getitem__(k)
            if d1 == d2:
                return True
            else:
                return False
        else:
            raise TypeError(str(arg) + ' must be type DictList or dict.')
            
            
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    #driver.default_show_exception=True
    #driver.default_show_exception_message=True
    #driver.default_show_traceback=True
    driver.driver()
