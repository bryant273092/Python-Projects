from goody import type_as_str  # Useful in some exceptions
from copy import deepcopy

class DictList:
    
    def __init__(self,*args):
        result=[]
        if len(args) == 0:
            raise AssertionError
        for i in args:
            if type(i) == dict:
                result.append(i)
            else:
                raise AssertionError
        self.dl=result


    def __len__(self):
        all = []
        for i in self.dl:
            all.extend(list(i.keys()))
        return len(set(all))
    
    def __repr__(self):
        return 'DictList('+ ','.join(f'{i}' for i in self.dl) + ')'
    
    
    def __contains__(self, item):
        all=[]
        for i in self.dl:
            if item in i:
                return True
        return False
                
    def __getitem__(self, item): 
        for i in reversed(self.dl):
            if item in i:
                return i[item]
        raise KeyError 
    
    def __setitem__(self, key, value):
        for i in reversed(self.dl):
            if key in i:
                i[key] = value
                return
        if key not in self.dl:
            self.dl.append({key:value})
        
    def __call__(self, key):
        result=[]
        ind=0
        for i in self.dl:
            if key in i:
                result.append((ind,i[key]))
            ind+=1
        return sorted(result, key=lambda x: x[0])         
                
                
    def __iter__(self):
        all=[]
        result=[]
        for i in reversed(self.dl):
            for j in sorted(i.keys()):
                if j not in all:
                    result.append((j,i[j]))
                    all.append(j)
        for i in result:
            yield i
            
    def __eq__(self,other):
        if type(other) == DictList:
            all=[]
            for i in other.dl:
                all.extend(i.keys())
            s_all=[]
            keys=False
            values=True
            for i in self.dl:
                s_all.extend(i.keys())
            s_all=list(set(s_all))
            all=list(set(all))
            if sorted(s_all) == sorted(all):
                keys=True
            for i in all:
                if self[i] != other[i]:
                    return False
            return keys and values
        elif type(other) == dict:
            all=list(other.keys())
            s_all=[]
            keys=False
            values=True
            for i in self.dl:
                s_all.extend(i.keys())
            s_all=list(set(s_all))
            all=list(set(all))
            if sorted(s_all) == sorted(all):
                keys=True
            for i in all:
                if self[i] != other[i]:
                    return False
            return keys and values
        else:
            raise TypeError
        
    def __add__(self,other):
        if type(other) == DictList:
            dict1={}
            dict2={}
            k=[]
            ok = []
            res=[{},{}]
            for i in self.dl:
                k.extend(i.keys())
            for i in other.dl:
                ok.extend(i.keys())
            k=list(set(k))
            ok=list(set(ok))
            for i in k:
                res[0][i] = self[i]
            for i in ok:
                res[1][i] = other[i]
            return DictList(res[0],res[1])
        elif type(other) == dict:
            result=[]
            new_dl=deepcopy(self.dl)
            new_dict=deepcopy(other)
            for i in new_dl:
                result.append(i)
            result.append(new_dict)
            return eval('DictList('+ ','.join(f'{i}' for i in result) + ')')
        else:
            raise TypeError

            
    def __radd__(self,other):
        if type(other) == DictList:
            return other+self
        elif type(other) == dict:
            result=[deepcopy(other)]
            new_dl=deepcopy(self.dl)
            for i in new_dl:
                result.append(i)
            return eval('DictList('+ ','.join(f'{i}' for i in result) + ')')
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
