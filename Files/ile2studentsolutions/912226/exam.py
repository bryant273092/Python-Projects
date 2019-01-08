from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        for i in args:
            assert type(i) == dict
            self.dl.append(i)
        if self.dl == []:
            raise AssertionError("Operands are not complete")

        
    def __len__(self):
        lst = []
        sum = 0
        for i in self.dl:
            for k,v in i.items():
                lst.append(k)
        lst = set(lst)
        for i in lst:
            sum += 1  
        return sum

    def __repr__(self):
        return 'DictList(' + ','.join(str(i) for i in self.dl) + ')' 

    def __contains__(self, key):
        for i in self.dl:
            for k,v in i.items():
                if key == k:
                    return True
        return False
        

    def __getitem__(self, key):
        contains = []
        if self.__contains__(key) == False:
            raise KeyError ("Key not in any of dictionaries")
        for i in self.dl:
            for k,v in i.items():
                if k == key:
                    contains.append(v)
        return contains[-1]
        
    def __setitem__(self, name, value):
        contains = []
        for i in self.dl:
            for k,v in i.items():
                if k == name:
                    contains.append( (i, k, v) )
        if len(contains) >= 1:
            contains = contains[-1]
            for i in self.dl:
                if i == contains[0]:
                    i[name] = value
            
        if self.__contains__(name) == False:
            self.dl.append({name:value})
        
    
    def __call__(self, key):
        lst = []
        if self.__contains__(key) == False:
            return []
        
        for i in range(len(self.dl)):
            for k,v in self.dl[i].items():
                if k == key:
                    lst.append( (i, v) )
        return lst
  
    def __iter__(self):
        current = []
        for i in self.dl[::-1]:
            for k,v in sorted(i.items()):
                if k not in current:
                    current.append(k)
                    yield (k, v)           
                current.append(k)

       

    def __eq__(self, right):
        fst = []
        snd = []
        if type(right) == DictList:
            current = []
            currently = []
            for i in self.dl:
                for k,v in i.items():
                    if k not in current:
                        current.append(k)
                        fst.append( (k,v) )
                    else:
                        current.append(k)
            for i in right.dl:
                for k,v in i.items():
                    if k not in currently:
                        currently.append(k)
                        snd.append( (k,v) )
                    else:
                        currently.append(k)
            for i, ii in zip( sorted(fst), sorted(snd)):
                if i[0] == ii[0]:
                    if i[1] == ii[1]:
                        pass
                else:
                    return False
            return True
            
                
        if type(right) is dict:
            currenter = []
            want = []
            for i in self.dl:
                for k,v in i.items():
                    if k not in currenter:
                        currenter.append(k)
                        want.append( (k,v) )
    
                    else:
                        currenter.append(k)
            
            
            temp = []
            for k,v in right.items():
                temp.append( (k,v) )

            for i, ii in zip(temp, want):
                if i[0] == ii[0]:
                    if i[1] == ii[1]:
                        pass
                    else:
                        return False
                return True
            
        
        else:
            raise TypeError ('Not accepted type of operand')


                
                
                
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test\
#     d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
#     d2 = DictList(dict(a=1,b=12), dict(c=13))
#     print(d1 == d2)
#     d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
#     d2 = DictList(dict(a=1,b=12), dict(c=13))
#     print(dict(a=1,b=12,c=13))
#     print(d1 == dict(a=1,b=2,c=13))

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
