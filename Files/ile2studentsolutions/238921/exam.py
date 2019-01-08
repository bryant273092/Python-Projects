from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *d):
        self.dl = []
        if len(d) == 0:
            raise AssertionError("Empty dictionary")
        for i in d:
            if type(i) != dict:
                raise AssertionError("Not a dictionary")
            elif type(i) == dict:
                self.dl.append(i)
                
    def __len__(self):
        values = []
        count = 0
        for i in self.dl:
            for a in i:
                values.append(a)
        for x in set(values):
            count += 1
        return count

    def __repr__(self):
        s = ""
        for i in self.dl:
            s += str(i)
        return "DictList({})".format(",".join(str(i) for i in self.dl))
    
    def __contains__(self, item):
        for d in self.dl:
            for i in d:
                if item == i:
                    return True
                
    def __getitem__(self, item):
        nums = []
        for d in self.dl:
            if item in d:
                nums.append(d[item])
        return max(nums)

    
    def __setitem__(self, item, value):
        nums = []
        for d in self.dl:
            if item in d:
                nums.append(d[item])
                x = max(nums)
                if d[item] == x:
                    self.dl[self.dl.index(d)][item] = value
                    
    
    def __call__(self, item):
        l = []
        for d in self.dl:
            if item in d:
                l.append((self.dl.index(d), d[item]))
        return l
    
    def __iter__(self):
        for i in self.dl:
            for a, b in sorted(i.items()):
                yield (a, b)
                
    def __eq__(self, right):
        l = []
        if type(right) == DictList:
            for i in right.dl:
                for a, b in i.items():
                    l.append((a, b))
            for i in self.dl:
                for x in l:
                    if x[0] in i:
                        if x[1] == i[x]:
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
