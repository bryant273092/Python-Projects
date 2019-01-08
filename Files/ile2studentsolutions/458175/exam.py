from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        else:
            for a in args:
                if type(a) != dict:
                    raise AssertionError('DictList.__init__:{} is not a dictionary'.format(a))
                else:
                    self.dl.append(a)
                    
    def __len__(self):
        newlist = []
        for a in self.dl:
            for b in a.keys():
                newlist.append(b)
        return len(set(newlist))
    
    def __repr__(self):
        return 'DictList(' + ','.join(str(a) for a in self.dl) + ")"
    
    def __contains__(self, item):
        if any(item in a for a in self.dl):
            return True
        else:
            return False
            
    def __getitem__(self, item):
        if self.__contains__(item) == True:
            newlist = []
            for a in self.dl:
                if item in a:
                    newlist.append(a[item])
                else:
                    pass
            return newlist[-1]
        else:
            raise KeyError
        
    def __setitem__(self, item, value):
        if self.__contains__(item) == True:
            for a in self.dl[::-1]:
                if item in a:
                    a[item] = value
        else:
            self.dl.append({item:value})
    
            
    def __call__(self,item):
        newlist = []
        if self.__contains__(item) == True:
            for a in self.dl:
                if item in a:
                    newlist.append((self.dl.index(a),a[item]))
                else:
                    pass
            return newlist
        else:
            return newlist

    def __iter__(self):
        newlist = []
        for a in self.dl[::-1]:
            for k, v in a.items():
                if k not in newlist:
                    newlist.append(k)
                    yield k,v
                else:
                    pass
    
    def __eq__(self,right):
        if type(right) == DictList:
            newlist = []
            for a in self.dl:
                for b in a.keys():
                    newlist.append(b)
                    newlist1 = list(set(newlist))
                    for c in newlist1:
                        if self.__getitem__(c) == right.__getitem__(c):
                            return True
                        else:
                            return False
        elif type(right) == dict:
            newlist = []
            newlist2 = [d for d in right.keys()]
            for a in self.dl:
                for b in a.keys():
                    newlist.append(b)
                    newlist1 = list(set(newlist))
                    if sorted(newlist1) == sorted(newlist2):
                        for c in newlist1:
                            if self.__getitem__[c] == right[c]:
                                return True
                            else:
                                return False
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
