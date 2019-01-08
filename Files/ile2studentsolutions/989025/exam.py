from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *arg):
        self.dl=list()
        for i in arg:
            if type(i)!= dict:
                raise AssertionError
            else:
                self.dl.append(i)
    
    def __len__(self):
        answer = list()
        for i in self.dl:
            for k in i.keys():
                if k not in answer:
                    answer+=k
        return len(answer)
    
    def __repr__(self):
        for i in self.dl:
            return 'DictList({})'.format(i)
    
    def __contains__(self, key):
        answer = list()
        for i in self.dl:
            for k in i.keys():
                if k not in answer:
                    answer+=k
        return key in answer
            
    
    def __getitem__(self, key):
        answer =0
        if type(key)==str:
            for i in self.dl:
                for k, v in i.items():
                    if key in k:
                        answer+=v
                        return answer
                    else:
                        raise KeyError
        else:
            KeyError
            
    
    def __setitem__(self, key, value):
        k_list = list()
        for i in self.dl:
            for k in i.keys():
                if k not in k_list:
                    k_list+=k
        if key in k_list:
            i[key]=value
        else:
            self.dl.append({key:value})

    
   
            
    def __call__ (self, key):
        answer = list()
        if self.__contains__(key):
            for i in self.dl:
                answer.append((0, i[key]))
                return answer
        else:
            return[]
    





            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d=DictList(dict(a=1, b=2, c=3), dict(c=13, d=14, e=15), dict(e=25, f=26, g=27))
    print(d.dl)
    print(len(d))
    print(d)
    print('a' in d)
    d['x'] ='test'
    print(d)
    print(d('a'))

    
    
    
    
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
