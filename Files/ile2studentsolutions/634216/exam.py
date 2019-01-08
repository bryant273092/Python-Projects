from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) > 0
        self.dl = []
        for arg in args:
            assert type(arg) == dict
            self.dl.append(arg)
    def __len__(self):
        l = []
        i = 0
        for diction in self.dl:
            for key in diction.keys():
                if key not in l:
                    i += 1
                    l.append(key)
        return i

    def __repr__(self):
        t = tuple(self.dl)
        return 'DictList' + str(t)
    
    def __contains__(self, item):
        boo = False
        for dict in self.dl:
            if item in dict:
                return True
            else:
                boo = True
        if boo == True:
            return False
        
    def __getitem__(self, item):
        boo = False
        for dict in reversed(self.dl):
            if item in dict:
                return dict[item]
            else:
                boo = True
        if boo == True:
            raise KeyError
    
    def __setitem__(self, item, value):
        boo = False
        for dict in reversed(self.dl):
            if item in dict:
                dict[item] = value
                boo = False
                break
            else:
                boo = True
                
        if boo == True:
            self.dl.append({item:value})
            
    def __call__(self, item):
        l = []
        for num, dict in enumerate(self.dl):
            if item in dict:
                l.append((num, dict[item]))
        return l
    
    def __iter__(self):
        l = []
        for dict in reversed(self.dl):
            for k,v in sorted(dict.items()):
                if k not in l:
                    l.append(k)
                    yield((k,v))
        
    def __eq__(self, right):
        if type(right) == DictList:
            for dic in right.dl:
                boo = False
                for k,v in dic.items():
                    for di in self.dl:
                        if k in di:
                            if di[k] == v:
                                boo = True
                                break
                            else:
                                l = (di[k], v)
                                boo = False
                    if boo == False:
                        return False
                    
            return True
                        
                        
                        
        elif type(right) == dict:
            boo = False
            l = []
            for d in self.dl:
                for k in d.keys():
                    if k not in l:
                        l.append(k)
                    
            for k,v in right.items():
                for di in self.dl:
                    if k in di:
                        if di[k] == v:
                            boo = True
                        else:
                            boo = False
                if boo == False:
                    return False
            for item in l:
                if item not in right:
                    return False
            
            
            return True
        else:
            raise TypeError("Wrong Type")
        
    def __add__(self, right):
        if type(right) == DictList:
            tup = ()
            temp1 = dict()
            for dic in self.dl:
                for k,v in dic.items():
                    if k in temp1:
                        temp1[k] = v
                    else:
                        temp1.setdefault(k, v)
            temp2 = dict()
            
            for dic in right.dl:
                for k,v in dic.items():
                    if k in temp2:
                        temp2[k] = v
                    else:
                        temp2.setdefault(k, v)
       
            return 'DictList(' + str(temp1) + ', ' + str(temp2) + ')'
                
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
