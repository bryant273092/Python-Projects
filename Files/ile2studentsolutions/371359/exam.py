from goody import type_as_str  # Useful in some exceptions
import copy

class DictList:
    def __init__(self,*args):
        assert len(args)>0, self.__class__.__name__+".__init__: must be one or more dictionaries"
        assert all(type(a)==dict for a in args), self.__class__.__name__+".__init__: "+str(args)+" one of them is not a dictionary"   
        self.dl=[]
        for arg in args:
            self.dl.append(arg)

    def __len__(self):
        result=set()
        for d in self.dl:
            for k in d.keys():
                result.add(k)
        return len(result)
    
    def __repr__(self):
        return 'DictList('+','.join(str(d) for d in self.dl)+')'
    
    def __contains__(self,arg):
        return any(arg in d for d in self.dl)
    
    def __getitem__(self,arg):
        result=None
        for d in self.dl:
            result = d[arg] if arg in d else result
        if result==None:
            raise KeyError( self.__class__.__name__+".__getitem__: key "+str(arg)+" does not exist in "+str(self))
        return result
    
    def __setitem__(self,arg,value):
        if not self.__contains__(arg):
            self.dl.append({arg:value})
        else:
            for d in reversed(self.dl):
                if arg in d:
                    d[arg]=value
                    break
    
    def __call__(self,arg):
        result=[]
        for i in range(len(self.dl)):
            if arg in self.dl[i]:
                result.append((i,self.dl[i][arg]))
        return result
        
    def __iter__(self):
        def gen(dictlist):
            yielded=set()
            for d in reversed(dictlist):
                for k in sorted(d):
                    if k not in yielded:
                        yielded.add(k)
                        yield (k,d[k])
        return gen(self.dl.copy())
    
    def __eq__(self,arg):
        
        if type(arg)==DictList:
            arg_list=list(d for d in arg)
            self_list=list(d for d in self)           
            return all(i in self_list for i in arg_list) and all(i in arg_list for i in self_list)
        elif type(arg)==dict:
            arg_list=list((k,arg[k]) for k in arg)
            self_list=list(d for d in self)
            return all(i in self_list for i in arg_list) and all(i in arg_list for i in self_list)
        else:
            raise TypeError(self.__class__.__name__+'.__eq__: argument must be a dict or DictList')
        
    def __add__(self,arg):
        if type(arg)==dict:
            copy=self.dl.copy()
            copy.append(arg)
            return eval('DictList('+str(copy)[1:-1]+')')
        elif type(arg)==DictList:
            self_dict=dict(list(d for d in self))
            arg_dict=dict(list(d for d in arg))
            return DictList(self_dict,arg_dict)
        else:
            raise TypeError(self.__class__.__name__+".__add__: '+' no supported between DictList and "+type_as_str(arg))
    
    def __radd__(self,arg):
        if type(arg)==dict:
            copy=[arg]
            copy.extend(self.dl.copy())
            return eval('DictList('+str(copy)[1:-1]+')')
        elif type(arg)==DictList:
            self_dict=dict(list(d for d in self))
            arg_dict=dict(list(d for d in arg))
            return DictList(arg_dict,self_dict)
        else:
            raise TypeError(self.__class__.__name__+".__add__: '+' not supported between DictList and "+type_as_str(arg))
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
