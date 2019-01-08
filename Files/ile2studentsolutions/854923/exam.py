class DictList:
    
    def __init__(self,*dicts):
        if len([*dicts]) == 0 or any([type(d) != dict for d in dicts]):
            raise AssertionError('Must provide one or more dicts as arguments')
        self.dl = [dict(d) for d in dicts]
    
    def __len__(self):
        keys = []
        for d in self.dl:
            keys += list(d.keys())
        return len(set(keys))
        
    def __repr__(self):
        return 'DictList({})'.format(','.join(['{}'.format(d) for d in self.dl]))
    
    def __contains__(self,item):
        return any([item in d for d in self.dl])
    
    def __getitem__(self,key):
        result = None
        for d in self.dl:
            if key in d:
                result = d[key]
        if result == None: raise KeyError('Key not found as a key in any of the dicts in the list of dicts')
        else: return result
    
    def __setitem__(self,name,value):
        if any([name in d for d in self.dl]):
            latest = 0
            for i in range(len(self.dl)):
                if name in self.dl[i]: latest = i
            self.dl[latest][name] = value
        else:
            self.dl.append({name:value})
    
    def __call__(self,key):
        tuplist = []
        if any([key in d for d in self.dl]):
            for i in range(len(self.dl)):# in [d for d in self.dl if key in d]:
                if key in self.dl[i]:
                    tuplist.append((i, self.dl[i][key]))
        return sorted(tuplist)
    
    def __iter__(self):
        revlist = list(self.dl)
        revlist.reverse()
        keyhistory = set()
        iterlist = []
        for d in revlist:
            for k in sorted(d.keys()):
                if k not in keyhistory:
                    iterlist.append((k,d[k]))
                    keyhistory.add(k)
        return iter(iterlist)
    
    def __eq__(self,right): 
        selfset=set().union(*[set(d.keys()) for d in self.dl])
        if type(right)==DictList:
            if selfset == set().union(*[set(d.keys()) for d in right.dl]):
                return all([self[k]==right[k] for k in selfset])
            return False
        elif type(right) == dict:
            if selfset == set(right.keys()):
                return all([self[k]==right[k] for k in selfset])
            return False
        else:
            raise TypeError("Cannot compare DictList with '{}' object".format(type(right)))
        
    def __add__(self,right):
        if type(right)== DictList:
            leftkeys = set().union(*[set(d.keys()) for d in self.dl])
            rightkeys = set().union(*[set(d.keys()) for d in right.dl])
            leftdict, rightdict = {k:self[k] for k in leftkeys}, {k:right[k] for k in rightkeys}
            return DictList(leftdict,rightdict)
        if type(right) == dict:
            return DictList(*(self.dl + [right]))
        else:
            raise TypeError
    
    def __radd__(self,left):
        if type(left) == dict:
            return DictList(*([left]+self.dl))
        else:
            return self + left

 
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
