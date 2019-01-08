from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *dicts):
        assert len(dicts) !=  0 ,'not a dictionary'
        self.dl = []
        for arg in dicts:
            if type(arg) is dict:
                self.dl.append(arg)
            else:
                raise AssertionError('not a dict')

    def __len__(self):
        ulist = []
        for arg in self.dl:
            for k,v in arg.items():
                if k not in ulist:
                    ulist.append(k)
        return len(ulist)
    
    def __repr__(self):
        s = ''
        for arg in self.dl:
            if self.dl.index(arg) != len(self.dl) -1 :
                s += str(arg) + ', '
            else:
                s += str(arg)
        return 'DictList(' + s + ')'
    
    def __contains__(self,item):
        for arg in self.dl:
            for k,v in arg.items():
                if k == item:
                    return True
        return False
        
    def __getitem__(self,index):
        ulist = []
        for arg in self.dl:
            for k,v in arg.items():
                if k == index:
                    ulist.append(v)
        if len(ulist) == 0:
            raise KeyError('index is not in any of the dictionaries')
        
        return max(ulist)
        
    def __setitem__(self, name, value):
#         dlcopy = self.dl 
#         for arg in self.dl:
#             for k,v in arg.items():
#                 if k == name:
#                     arg[name] = value
#         if dlcopy == self.dl:
#             self.dl.append(dict(name = value))
#         i = len(self.dl)
#         while i > 0 :
#             for k,v in self.dl[i].items():
#                 if k == name and k not in self.d:
#                     self.dl[i][k] = value
#             i -= 1
        vlist = []
        if any(name in arg for arg in self.dl):
            for arg in self.dl:
                for k,v in arg.items():
                    if k == name:
                        vlist.append(self.dl.index(arg))
            m = max(vlist)
            self.dl[m][name] = value
            
        else:
            DictList(dict(name = value))
            
#         for arg in self.dl:
#             if name in any(arg):
#                 print('yes')
#             else:
#                 print('no')
        
    def __call__(self,item):
        clist = []
        for arg in self.dl:
            for k,v in arg.items():
                if k == item:
                    clist.append((self.dl.index(arg), v))
        return sorted(clist, key = (lambda t: t[0]))
                        
    
    def __iter__(self):
#         idict = dict
#         ilist = []
#         i = len(self.dl)
#         while i > 0:
#             for k,v in self.dl[i].items():
#                 if k not in idict:
#                     idict[k] = v
#             i -= 1
#             for k,v in sorted(idict.items()):
#                 yield(k,v)
        
        plist = []
        for arg in self.dl:
            for k,v in arg.items():
                if k not in plist:
                    plist.append(k, v)
                else:
                    for item in plist:
                        if item[0] == k:
                            del plist[item]
                    plist.append(k,v)
            for item in sorted(plist):
                yield item
#         
#         plist = []
#         for arg in self.dl:
#             for k,v in arg.items():
#                 if k not in plist:
#                     plist.append(k, v)
#             for item in sorted(plist):
#                 yield item
                
                    
                
    
    def __eq__(self, right):
        if type(right) is DictList:
            for arg in self.dl:
                for rarg in right.dl:
                    if arg.keys() != rarg.keys():
                        return False
                    else:
                        return all(self.__getitem__(k) == right.__getitem__(k) for k,v in arg.items())
            return True
        elif type(right) is dict:
            for arg in self.dl:
                return arg.items() == right.items()
        
        else:
            raise TypeError('not right type')
        

if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
   
    #d['a']
    #print(repr(d))
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a=1,b=12), dict(c=13))
   # d1 == d2
    d1 == dict(a=1,b=12,c=13)
    
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
