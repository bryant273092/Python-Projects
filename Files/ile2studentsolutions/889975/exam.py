from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if len(args) == 0 and type(args) != dict:
            raise AssertionError
        for i in args:
            if type(i) != dict:
                raise AssertionError
        self.dl = list(args)
        
    def __len__(self):
        s = set()
        for i in self.dl:
            for j in i.keys():
                s.add(j)
        return len(s)

    def __repr__(self):
        return "DictList({things})".format(things=str(self.dl).strip('[]'))

    def __contains__(self, thing):
        s = set()
        for i in self.dl:
            for j in i.keys():
                s.add(j)
        return thing in s
    
    def __getitem__(self, thing):
        if not self.__contains__(thing):
            raise KeyError(thing,'is not a key inside the DictList')
        value = 0
        for i in self.dl:
            if thing in i.keys():
                value = i[thing]
                
        return value
    
    def __setitem__(self, thing, value):
        if not self.__contains__(thing):
            self.dl.append({thing:value})
        else:
            self.dl = list(reversed(self.dl))
            end = False
            for i in self.dl:
                if end:
                    break
                for j in i.keys():
                    if thing == j:
                        i[j] = value
                        end = True
                        break
            self.dl = list(reversed(self.dl))
        
    def __call__(self, thing):
        num = 0
        result = []
        for i in self.dl:
            if thing in i:
                result.append((num, i[thing]))
            num += 1
        return result
    
    def __iter__(self):
        exp = []
        for i in self.dl:
            for j in i:
                if j not in exp:
                    exp.append((j,i[j]))
                
        tig = {}
        for i in exp:
            if i[0] not in tig.keys():
                tig[i[0]] = i[1]
            else:
                tig[i[0]] = i[1]
            
        for i in tig.items():
            yield i
    
    def __eq__(self,right):
        if type(right) not in (DictList, dict):
            raise TypeError(right,'needs to be of type DictList or Dict')
        elif type(right) == DictList:
            if len(self.dl) != len(right.dl):
                return False
            else:
                for i in range(self.dl):
                    print(self.dl[i].keys(), right.dl[i].keys())
                    if set(self.dl[i].keys()) != set(right.dl[i].keys()):
                        return False
                return True
        elif type(right) == dict:
            if len(self.dl) > 1:
                return False
            else:
                return self.dl[0] == dict
    
    def __add__(self,right):
        pass
    
    def __radd__(self, left):
        self.__add__(left)
        
            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    
    d = DictList(d0,d1)
    print(d.__iter__())
    
    '''
    d0 = dict(a=1,b=2,c=3)
    d1 = dict(c=13,d=14,e=15)
    d  = DictList(d0,d1)
    produced = [i for i in d]
    print(produced)
    len(produced)
    '''
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
