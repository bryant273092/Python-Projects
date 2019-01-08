from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        length = len(args)
        assert length > 0, "Empty"
        self.dl = []
        for i in args:
            try:
                item = dict(i)
                assert len(item) >0, "Empty"
            except TypeError:
                assert False, "cannot dict"
            except ValueError:
                assert False, "Not a dict"
            else:
                self.dl.append(item)
    
    def __len__(self):
        key_set = set()
        for item in self.dl:
            for key in item:
                key_set.add(key)
        return len(key_set)
    
    def __repr__(self):
        answer = ", ".join(str(item) for item in self.dl)
        return "DictList("+answer+")"
    
    def __contains__(self, new_key):
        for item in self.dl:
            if new_key in item:
                return True
        return False
    
    def __getitem__(self, new_key):
        for index in range(len(self.dl)- 1,-1, -1):
            if new_key in self.dl[index]:
                return self.dl[index][new_key]
        raise KeyError
    
    def __setitem__(self, new_key, value):
        ok = False
        for index in range(len(self.dl)-1, -1, -1):
            if new_key in self.dl[index]:
                self.dl[index][new_key] = value
                ok = True
                break
        if not ok:
            self.dl.append({new_key:value})
            
    def __call__(self, new_key):
        answer = []
        for index in range(len(self.dl)):
            if new_key in self.dl[index]:
                answer.append((index, self.dl[index][new_key]))
        return answer
                
    
    def __iter__(self):
        key_set = set()
        for index in range(len(self.dl)-1,-1,-1):
            for item in sorted(self.dl[index].items()):
                if item[0] not in key_set:
                    key_set.add(item[0])
                    yield item
            
    
    def __eq__(self, right):
        if type(right) is DictList or type(right) is dict:
            for key, value in self:
                if key not in right or right[key] != value:
                    return False
            return True
        else:
            raise TypeError
    
    
    def __add__(self, right):
        if type(right) is DictList:
            return DictList(dict(self.__iter__()), dict(right.__iter__()))
        elif type(right) is dict:
            args = [dict(item) for item in self.dl]
            args.append(dict(right))
            return DictList(*args)
        else:
            raise TypeError
        
    def __radd__(self, left):
        if type(left) is dict:
            args = [dict(left)]
            for item in self.dl:
                args.append(dict(item))
            return DictList(*args)
        elif type(left) is DictList:
            return self+left
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
