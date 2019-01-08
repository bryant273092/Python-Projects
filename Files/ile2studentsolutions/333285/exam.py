from goody import type_as_str  # Useful in some exceptions
# from prompt import value

class DictList:
    

    def __init__(self, *args):
        self.dl = []
        if(args == None or args == "" or args == {}):
            raise AssertionError
        for i in args:
            if(type(i) != dict):
                raise AssertionError("DictList.__init__:",type_as_str(i),"is not a dictionary.")                
            else:
                self.dl.append(i)

    def __len__(self):
        result = []
        for i in self.dl:
            for k in i:
                result.append(k)
        return len(list(set(result)))
            
    def __repr(self):
        return 'DictList({params})'.format(params = self.dl)
    
    def __contains__(self, item):
        try:
            for i in self.dl:
                for k in i.keys():
                    if(item in k):
                        return True
        except:
            return False
    
    def __getitem__(self, item):
        result = []
        for i in reversed(self.dl):
            if(item not in i):
                result.append(False)
            else:
                for k,v in i.items():
                    if(item == k):
                        return v   
        if(all(result) is False):
            raise KeyError

    
    def __setitem__(self, key, value):
        result = []
        for i in reversed(self.dl):
            if(key in i):
                i[key] = value
                break
            else:
                result.append(False)
        if(all(result) is True):
            self.dl.append({key:value})
            
    def __call__(self, item):
        result = []
        for i in range(len(self.dl)):
            if(item in self.dl[i]):
                result.append((i, self.dl[i][item]))
                
        return result
    
    
    def __iter__(self):
        result = []
        for i in reversed(self.dl):
            for k in i.keys():
                if(len(result) == 0):
                    result.append((k, i[k]))
                else:
                    if(k in [j[0] for j in result]):
                        pass
                    else:
                        result.append((k, i[k]))
        return iter(result)

    def __eq__(self, item):
        if(type(item) is DictList):
#             key_result = []
#             val_result = []
#             for i in self.dl.keys():
#                 if(i in item):
#                     key_result.append(True)
            return True    
                 
        elif(type(item) is dict):
              return True
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
