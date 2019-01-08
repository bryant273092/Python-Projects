from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*params):
        self.dl = []
        if params == ():
            raise AssertionError
        for param in params:
            if type(param) == dict:
                self.dl.append(param)
            else:
                raise AssertionError
    def __len__(self):
        seen = set()
        lenght = 0
        for dics in self.dl:
            for key in dics:
                if key not in seen:
                    lenght+=1
                    seen.add(key)
        return lenght
    def __repr__(self):
        string = 'DictList('
        for dic in self.dl:
            string+= str(dic)+','
        string.rstrip(',')
        string+=')'
        return string
    
    def __contains__(self,key):
        for dic in self.dl:
            if key in dic:
                return True
        return False
    
    def __getitem__(self,value):
        for i in range(len(self.dl)):
            if value in self.dl[-(i+1)]:
                return self.dl[-(i+1)][value]
        raise KeyError
            
    def __setitem__(self,key,value):
        for i in range(len(self.dl)):
            if key in self.dl[-(i+1)]:
                self.dl[-(i+1)][key] = value
                return
        self.dl.append({key:value})
        
    def __call__(self,key):
        lst = []
        for i in range(len(self.dl)):
            if key in self.dl[i]:
                lst.append((i,self.dl[i][key]))
        return lst
        
    def __iter__(self):
        seen = set()
        for i in range(len(self.dl)):
            for key in sorted(self.dl[-(i+1)]):
                if key not in seen:
                    yield (key,self.dl[-(i+1)][key])
                    seen.add(key)
                    
    def __eq__(self,right):
        checked = set()
        to_be_checked = set()
        if type(self) == DictList and type(right) == DictList:
            for dic in self.dl:
                for key in dic:
                    for dic2 in right.dl:
                        if key in dic2:
                            if key not in checked:
                                if dic[key] == dic2[key]:
                                    checked.add(key)
                                    if key in to_be_checked:
                                        to_be_checked.remove(key)
                                    break
                                elif key not in checked:
                                    to_be_checked.add(key)
                                else:
                                    return False
            if len(to_be_checked)==0:
                return True
            else:
                return False
        elif type(self) == DictList and  type(right) == dict:
            for dic in self.dl:
                for key in dic:
                     if key in right:
                         if key not in checked:
                             if dic[key] == right[key]:
                                 checked.add(key)
                                 if key in to_be_checked:
                                     to_be_checked.remove(key)
                             elif key not in checked:
                                 to_be_checked.add(key)
                             else:
                                return False
                     else:
                         to_be_checked.add(key)
            if len(to_be_checked)==0:
                return True
            else:
                return False
        elif type(right) != dict or type(right) != DictList:
            raise TypeError
                    
                    
                    
        
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = DictList(dict(a=1,b=2), dict(b=12,c=13))
    d2 = DictList(dict(a=1,b=12), dict(c=13))
    d1 == dict(a=1,c=13)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
