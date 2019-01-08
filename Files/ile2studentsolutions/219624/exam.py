from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError()
        else:
            for i in args:
                if type(i) != dict:
                    raise AssertionError()
                else:
                    self.dl.append(i)
                    
    def __len__(self):
        keys = []
        for i in self.dl:
            for k in i.keys():
                if k not in keys:
                    keys.append(k)
        return len(keys)
        
    def __repr__(self):
        answer = 'DictList('
        for i in self.dl:
            answer += str(i)+','
        answer = answer.rstrip(',')
        return answer + ')'
    
    def __contains__(self,value):
        for i in self.dl:
            if value in i.keys():
                return True
        return False

    def __getitem__(self,index):
        value = 0
        if self.__contains__(index):
            for i in self.dl:
                if index in i.keys():
                    value = i[index]
            return value
        
        raise KeyError()
    
    def __setitem__(self,index,value):
        if self.__contains__(index):
            item = self[index]
            for i in self.dl:
                if index in i.keys():
                    if i[index] == item:
                        i[index] = value
        else:
            self.dl.append({index:value})
            
        
    def __call__(self,index):
        answer = []
        for i in range(len(self.dl)):
            if index in self.dl[i].keys():
                answer.append((i,self.dl[i][index]))
        return answer
    
    def __iter__(self):
        def count(value):
            keys_list = []
            for i in reversed(value):
                for k in i.keys():
                    if k not in keys_list:
                        keys_list.append(k)
                        yield((k,i[k]))
        return count(self.dl)
                    
                    
    def __eq__(self,right):
        if type(right) is DictList:
            for i in self.dl:
                for k in i.keys():
                    if right.__contains__(k) != True:
                        return False
                    else:
                        if self[k] != right[k]:
                            return False
            return True
                        
        elif type(right) is dict:
            for i in self.dl:
                for k in i.keys():
                    if k not in right.keys():
                        return False
                    else:
                        if self[k] != right[k]:
                            return False
            return True
        else:
            raise TypeError()
                    
        
        

            
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
