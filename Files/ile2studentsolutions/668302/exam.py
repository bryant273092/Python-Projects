from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        for i in args:
            assert type(i) == dict, f"DictList:__init__:{args} is not a dictionary "
        lis = []
        for i in args:
            lis.append(i)
        self.dl = lis
    
    def __len__(self):
        count = 0
        seen = set()
        for i in self.dl:
            for j in i:
                for k in j:
                    if k not in seen:
                        count += 1
                        seen.add(k)
        return count
    
    def __repr__(self):
        stri = ''
        for i in self.dl:
            stri = stri  + str(i) +', '
        stri = stri[:-2]
        return ("DictList({})".format(stri) )
    
    def __contains__(self, item):
        for i in self.dl:
            for j in i:
                if item in j:
                    return True
                else:
                    continue

    def __getitem__(self, item):
        val = []
        for d in self.dl:
            for key in d:
                if item == key:
                    val.append(d[key])

        if len(val) > 0:
            return val[-1]
        else:
            raise KeyError
    
    def __setitem__(self, k, v):
        count = -1
        dic = []
        for d in self.dl:
            count +=1
            for key in d:
                if k == key:
                    dic.append(count)
        if len(dic) > 0:
            for i in self.dl[(dic[-1])]:
                if i == k:
                    self.dl[(dic[-1])][k] = v
                    return 
        else:
            self.dl.append({k:v})
    
    def __call__(self, k):
        count = -1
        tlis = []
        tup = ()
        for d in self.dl:
            count +=1
            for key in d:
                if key == k:
                    tup = (count,d[k])
                    tlis.append(tup)
        return tlis
                    
    def __iter__(self):
        tup = ()
        
        return tup
            
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
