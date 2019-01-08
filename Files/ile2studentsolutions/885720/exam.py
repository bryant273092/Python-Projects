from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        for values in args:
            assert type(values) == dict, 'Incorrect Type'
            self.dl.append(values)
    def __len__(self):
        total = set()
        for values in self.dl:
            total.update(values.keys())
        return len(total)
    def __repr__(self):
        big = 'DictList({})'.format(str(self.dl).strip('[').strip(']'))
        return big
            
    def __contains__(self,value):
        new= []
        for values in self.dl:
            for k,v in values.items():
                new.append(k)
        if value in new:
            return True
        else:
            return False
    def __getitem__(self,value):
        if type(value) == str:
            if value in self.dl[-1]:
                return self.dl[-1][value]
    
            else:
                for x in range(len(value)):
                    if value in self.dl[x]:
                        return self.dl[x][value]
                    else:
                        raise KeyError('Wrong Key')
        else:
            raise KeyError('Wrong Type')
    def __setitem__(self,value,item):
        if type(value) == str:
            new = dict()
            for dic in self.dl:
                if value in dic:
                    dic[value] = item
                else:
                    new[value] = item
                    self.dl.append(new)
    def __call__(self,item):
        total= []
        for x in range(len(self.dl)):
            if item in self.dl[x]:
                total.append((x, self.dl[x][item]))
        return total
    def __iter__(self):
        new = []
        total = set()
        for values in self.dl:
            for x in range(len(self.dl)):
                new.append(x)
            start = max(new)
            new.pop(start)
            for k,v in self.dl[start].items():
                total.add((k,v))
                start = max(new)
        for i in total:
            yield i
    def __eq__(self,right):
        total_s = []
        total_r = []
        if type(right) not in [DictList, dict]:
            raise TypeError('Not Right Type')
        else:
            if type(right) == DictList:
                for x in range(len(self.dl)):
                    total_s.append(self.__call__(x))
                for y in range(len(right.dl)):
                    total_r.append(self.__call__(y))
                if total_r in total_s or total_s in total_r:
                    return True
                else:
                    return False
            else:
                for x in range(len(self.dl)):
                    total_s.append(self.__call__(x))
                for k,v in right.items():
                    total_r.append((k,v))
                if total_r in total_s or total_s in total_r:
                    return True
                else:
                    return False
    
    

        
                
            




            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d  = DictList(d0)
    e = DictList(d1)
    d == e
    
    #assert type(repr(d)) is str and len(drep.dl) == 2 and all(x == y for x,y in zip((d0,d1),drep.dl))
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
