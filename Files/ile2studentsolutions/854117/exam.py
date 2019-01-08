from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args) != 0
        for d in args:
            if type(d) != dict:
                raise AssertionError
            else:
                self.dl = [d for d in args]
                
    
    def __len__(self):
        st = set()
        for d in self.dl:
            for k in d.keys():
                if k not in st:
                    st.add(k)
        return len(st)
    
    
    def __repr__(self):
        return 'DictList('+', '.join(str(d) for d in self.dl) +')'
    
    def __contains__(self,item):
        for d in self.dl:
            if item in d.keys():
                return True
        return False
    
    
    def __getitem__(self,key):
        for d in reversed(self.dl):
            for k in d:
                if k == key:
                    return d[k]
        raise KeyError
    
    
    def __setitem__(self,key,value):
        for d in reversed(self.dl):
            if key in d:
                d[key] = value
                return
        self.dl.append({key:value})
                
                
    def __call__(self,key):
        counter = 0
        answer = []
        for d in self.dl:
            for k,v in d.items():
                if key == k:
                    answer.append((counter,v))
            counter += 1
        return answer if len(answer) != 0 else []
                
                
    def __iter__(self):
        produced = set()
        for d in reversed(self.dl):
            for k,v in sorted(d.items()):
                if k not in produced:
                    produced.add(k)
                    yield (k,v)
                    
                    
    def __eq__(self,right):
        if type(right) not in (dict,DictList):
            raise TypeError
        self_keys = {k for d in self.dl for k in d}
        if type(right) == dict:
            right_keys = {k for k in right}
        elif type(right) == DictList:
            right_keys = {k for d in right.dl for k in d}
        for k in self_keys:
            try:
                if self[k] != right[k]:
                    return False
            except KeyError:
                return False
        return self_keys == right_keys
        
        
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
