from goody import type_as_str  # Useful in some exceptions

class DictList:
    
    def __init__(self,*dl):
        self.dl = []
        if len(dl) == 0:
            raise AssertionError
        for i in dl:
            if type(i) != dict:
                raise AssertionError("DictList.__init__: "+str(i)+" is not a dictionary.")
            else:
                self.dl.append(i)

    def __len__(self):
        total = []
        for i in self.dl:
            for k in i.keys():
                if k not in total:
                    total.append(k)
        return len(total)
        
    def __repr__(self):
        return "DictList("+','.join(str(i) for i in self.dl)+")"

        
    def __contains__(self, key):
        for i in self.dl:
            if key in i:
                return key in i
        
    def __getitem__(self, key):
        ri = []
        if DictList.__contains__(self, key):
            if type(key) == str:
                for i in self.dl:
                    if key in i:
    #                     print(i[key])
                        ri.append(i[key])
            else:
                raise KeyError(key+' not in any dictionaries')
        else:
            raise KeyError(key+' not in any dictionaries')
                
#         ri.sort()
        return ri[-1]
    
    def __setitem__(self, key, value):
        ri = []
        if DictList.__contains__(self, key):
            for i in self.dl:
                if key in i:
                    i[key] = value
        else:
            self.dl.append({key:value})
            
    def __call__(self, key):
        present = []
        if DictList.__contains__(self, key):
            for i in range(len(self.dl)):
#                 print('test:',(i, self.dl[i][key]))
                if key in self.dl[i].keys():
                    present.append((i,self.dl[i][key]))
        
        return present
        
    def __iter__(self):
        l_dl = []
        for i in self.dl:
            for k,v in i:
                if (k,v) not in l_dl:
                    l_dl.append((k,v)) 
        l_dl.sort()
        for i in range(len(l_dl)):
            yield l_dl[-i]
    
    def __eq__(self, dict):
        pass
            
        
        
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = (DictList({'a':1, 'b':2},{'c':3,'d':4}))
    print(len(d))
    print(eval(repr(d)))
    print('f' in d)
    d['e'] = 'new'
    print('testing:',d('a'))
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
