from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl=[]
        if len(args)==0:
            raise AssertionError("nothing in here")
        for dictt in args:
            if type(dictt)==dict:
                self.dl.append(dictt)
            else:
                 raise AssertionError("Not correct type")
            
    def __len__(self):
        counter=0
        check=set()
        for d in self.dl:
            for k in d.keys():
                check.add(k)
        return len(check)
        
            
    def __repr__(self):
        
        return "DictList({})".format(",".join(str(d) for d in self.dl))
    def __contains__(self,key):
        for d in self.dl:
            if key in d.keys():
                return True
    def __getitem__(self,key):
        best=0
        for d in range(len( self.dl)):
            if key in self.dl[d].keys():
                best=int(self.dl[d][key])
        if key not in self.dl[d].keys():
            raise KeyError
        return best
            
#     def __setitem__(self):
#         pass
    def __eq__(self,right):
        pass
            
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
