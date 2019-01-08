
class DictList:
    def __init__(self,*args):
        self.dl = []
        for a in args:
            if type(a) != dict:
                raise AssertionError(f"DictList.__init__:{a} is not a dictionary")
            else: self.dl.append(a)
    
    def __len__(self):
        se = set()
        for i in self.dl:
            for v in i.keys():
                if v not in se:
                    se.add(v)
        return len(se)
    
    def __repr__(self):
        st = []
        for i in self.dl:
            l = []
            for k,v in i.items():
                l.append(f"'{k}': {v}")
            st.append("{" + ", ".join(l)+"}"   ) 
        return ( f"DictList({', '.join(st)} )")
    
    def __contains__(self,check):
        for i in self.dl:
            for v in i.keys():
                if check == v:
                    return True
        return False

    def __getitem__(self,it):
        for i in sorted(range(len(self.dl)), reverse = True):
            for k,v in self.dl[i].items():
                if it == k:
                    return v
        raise KeyError(f"{it} appears in no dictionaries")
    
    def __setitem__(self,key,value):
        for i in sorted(range(len(self.dl)), reverse = True):
            for k,v in self.dl[i].items():
                if key == k:
                    self.dl[i][k] = value
                    return
        self.dl.append({key:value})
        return

    
    def __call__(self,check):
        l = []
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if check == k:
                    l.append((i,v))
        return l
    
    def __iter__(self):
        l = []
        for i in sorted(range(len(self.dl)), reverse = True):
            for k,v in sorted(self.dl[i].items()):
                if k not in l:
                    l.append(k)
                    yield ((k,v))

    def __eq__(self,right):
        if type(right) == DictList: return sorted([x for x in self.__iter__()]) == sorted([x for x in right.__iter__()])
        elif type(right) == dict: return sorted([x for x in self.__iter__()]) == sorted(right.items())
        else: raise TypeError(f"{right} is not of type DictList or Dict")
    

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
