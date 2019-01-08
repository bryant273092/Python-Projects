
class DictList:
    def __init__(self, *dicts):
        self.dl = []
        if len(dicts) == 0:
            raise AssertionError
        for i in dicts:
            if type(i) == dict:
                self.dl.append(i)
            else:
                raise AssertionError
    def __len__(self):
        final = []
        for d in self.dl:
            for i in d.keys():
                final.append(i)
        end = set(final)
        length = len(end)
        return length
    
    def __repr__(self):
        start = 'DictList('
        for i in self.dl:
            start+= str(i)
            start += ','
        final = start[0:-1]
        final+= ')'
        return final
    def __contains__(self, item):
        for d in self.dl:
            if item in d.keys():
                return True
        return False 

    def __getitem__(self, item):
        try:
            last = None
            for d in self.dl:
                if item in d.keys():
                    last = d[item]
            if last == None:
                raise KeyError
            return last
        except:
            raise KeyError
            
    def __setitem__(self, item, value):
        index_num = None
        for d in self.dl:
            if item in d.keys():
                index_num = self.dl.index(d)
        if index_num == None:
            self.dl.append({item:value})
        else:
            self.dl[index_num][item] = value
    
    def __call__(self, item):
        final = []
        for d in self.dl:
            if item in d.keys():
                num = self.dl.index(d)
                final.append((num, self.dl[num][item]))
        return final
    
    def __iter__(self):
        final = []
        count = 0
        for d in self.dl:
            for i in d.keys():
                final.append(i)
        fixed = set(final)
        complete = list(fixed)
        done = []
        while count < len(complete):
            highest = 0
            for d in self.dl:
                if complete[count] in sorted(d.keys()):
                    num = self.dl.index(d)
                    if num > highest or num == highest: 
                        highest = num
                    else:
                        pass
            done.append((complete[count], self.dl[highest][complete[count]]))
            count+=1
        return iter(done)
            
    def __eq__(self, item):
        keys1 = []
        keys2 = []
        if type(item) == DictList:
            for d in self.dl:
                for i in d.keys():
                    keys1.append(i)
            for s in item.dl:
                for a in s.keys():
                    keys2.append(a)
            if set(keys1) != set(keys2):
                return False
            for key in keys1:
                if self[key] != item[key]:
                    return False
        elif type(item) == dict:
            for d in self.dl:
                for i in d.keys():
                    keys1.append(i)
            for k in item.keys():
                keys2.append(k)
            if set(keys1) != set(keys2):
                return False
            for key in keys1:
                if self[key] != item[key]:
                    return False
        else:
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
