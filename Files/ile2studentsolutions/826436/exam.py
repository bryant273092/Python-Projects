from goody import type_as_str  # Useful in some exceptions
from _operator import index

class DictList:
    def __init__(self, *args):
        self.dl = list()
        assert len(args) != 0, 'DictList.__init__: parameter cannot be empty'
        
        for i in args:
            assert type(i) is dict, "DictList.__init__: '" + str(i) + "' is not a dictionary"
            
            self.dl.append(i)
            
    def __len__(self):
        return len({a for b in self.dl for a in b.keys()})
    
    def __repr__(self):
        gen_dictlist = ','.join(str(i) for i in self.dl)

        return 'DictList(' + gen_dictlist + ')'
    
    def __contains__(self, key):
        for i in self.dl:
            if key in i.keys():
                return True
        return False

    def __getitem__(self, index):
        temp = str()
        for i in self.dl:
            for j in i.keys():
                if index == j:
                    temp = i[index]
        
        if temp == '':
            raise KeyError
        
        return temp
    
    def __setitem__(self, index, value):
        in_a_dict = False
        for i in reversed(self.dl):
            if index in i.keys():
                in_a_dict = True
                i[index] = value
                break
                
        
        if not in_a_dict:
            self.dl.append(dict())
            self.dl[-1][index] = value
            
    def __call__(self, key):
        temp = list()
        
        for i in range(len(self.dl)):
            if key in self.dl[i].keys():
                temp.append((i, self.dl[i][key]))
                
        return temp

    def __iter__(self):
        temp = set()
        temp2 = list()
        
        for i in reversed(self.dl):
            temp2.append([])
            for j in i.keys():
                if j not in temp:
                    temp.add(j)
                    temp2[-1].append((j, i[j]))
        
        for i in range(len(temp2)):
            for j in temp2[i]:
                yield(j)
            
    def __eq__(self, right):
        if isinstance(right, DictList):
            l = set()
            r = set()
            for i in self.dl:
                for j in i.items():
                    l.add(j)
            
            for i in right.dl:
                for j in i.items():
                    r.add(j)
            
            if len(l) <= len(r):
                for i in l:
                    if i not in r:
                        return False
     
            else:
                for i in r:
                    if i not in l:
                        return False
            return True
              
            
        
        elif isinstance(right, dict):
            l = list()
            r = list()
            temp = dict()
            
            for i in self.dl:
                for j in i.items():
                    l.append(j)
                    
            for i in right.items():
                r.append(i)
            
            for i in l:
                if i not in temp.keys():
                    temp[i[0]] = 0
                temp[i[0]] = i[1] 
                
            return temp == right  
        
        else:
            raise TypeError('== must only compare between another DictList or dict')
            

            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,c=13))
    d2 = DictList(dict(a=1,b=12),dict(c=13))
    print(d1 == d2)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
