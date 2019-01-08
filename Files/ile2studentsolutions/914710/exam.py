from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if args == None:
            raise AssertionError
        else:
            for i in args:
                if type(i)!= dict:
                    raise AssertionError
            for i in args:
                self.dl.append(i)
            
    
    def __len__(self):
        distinct = set()
        for i in self.dl:
            for key in i.keys():
                distinct.add(key)
        return len(distinct)
    
    def __repr__(self):
        name = str(self.dl)[1:]
        name = name.strip(']')
        return('DictList('+name+')')
    
    def __contains__(self, other):
        for i in self.dl:
            for key in i.keys():
                if key == other:
                    return True
        return False
    
    def __getitem__(self, other):
        answer = ''
        all = set()
        for i in self.dl:
            for key in i.keys():
                all.add(key)
        if other not in all:
            raise KeyError    
        for i in self.dl:
            for key in i.keys():
                if key == other:
                    answer = i[key]
        return answer

    def __setitem__(self, other, value):
        all = set()
        place = 0
        for i in self.dl:
            for key in i.keys():
                all.add(key)
        if other in all:
            for i in range(len(self.dl)):
                for key in self.dl[i].keys():
                    if other == key:
                        place = i 
            self.dl[place][other] = value
        elif other not in all:
            new = {}
            new[other] = value
            self.dl.append(new)    
    
    def __call__(self, other):
        result = []
        for i in range(len(self.dl)):
            for key in self.dl[i].keys():
                if key == other:
                    result.append((i, self.dl[i][key]))
        return result
    
    def __iter__(self):
        result = []
        already = set()
        count = len(self.dl)-1
        while count >=0:
            values = set()
            for key in self.dl[count].keys():
                values.add(key)
            for j in sorted(values):
                if j not in already:
                    result.append((j, self.dl[count][j]))
                    already.add(j)
            count = count-1
        for i in result:
            yield i
        
            
    
    def __eq__(self, other):
        if type(other)!= dict and type(other)!= DictList:
            raise TypeError
        return True
            
    
            
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
