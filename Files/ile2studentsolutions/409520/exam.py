
class DictList:
    def __init__(self,*args):
        assert len(args) != 0, 'Argument should not be empty'
        self.dl = []
        for i in args:
            assert type(i) == dict, '{} is not a dictionary'.format(i)
            self.dl.append(i)
    
    def __len__(self):
        final = []
        for i in self.dl:
            for x in i:
                if x not in final: final.append(x)
        return(len(final))
    
    def __repr__(self):
        return 'DictList{}'.format(tuple(i for i in self.dl))
    
    def __contains__(self,item):
        return any(item in x for x in self.dl)
    
    def __getitem__(self,item):
        if item not in self: raise KeyError('{} appears in not dictionaries'.format(item))
        else:
            for i in self.dl:
                if item in i: track_new = i
            return(track_new[item])
    
    def __setitem__(self,item,value):
        if item in self:
            for i in self.dl: 
                if item in i: track_new = i
            track_new[item]= value
        else:
            self.dl.append({item:value})
    
    def __call__(self,item):
        final = []
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                final.append((i,self.dl[i][item]))
        return final
    
    def __iter__(self):
        it_list = []
        for i in sorted(list(range(len(self.dl))),reverse = True):
            for key in sorted(self.dl[i]):
                if key not in it_list:
                    it_list.append(key)
                    yield (key,self.dl[i][key])
    
    def __eq__(self,right):
        if type(right) in (dict, DictList):
            for i in self:
                if i[0] not in right or right[i[0]] != i[1]:
                    return False
            return True
        else: raise TypeError('== does not support DictList and {}'.format(type(right)))
    
    def __add__(self,right):
        if type(right) ==DictList:
            return(DictList({i[0]:i[1] for i in self},{i[0]:i[1] for i in right}))
        elif type(right) ==dict:
            return(DictList(*self.dl,right))
        else: raise TypeError('+ does not support DictList and {}'.format(type(right)))
    
    def __radd__(self,left):
        if type(left)==dict:
            return(DictList(left,*self.dl))
        else: return(self+left)
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
