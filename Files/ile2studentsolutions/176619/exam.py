
class DictList:
    
    def __init__(self,*args):
        self.dl = []
        if len(args) >= 1:
            for i in args:
                assert type(i) is dict, str(i) + "is not a dictionary."
                self.dl.append(i)
        else:
            raise AssertionError
                
    def __len__(self):
        count = 0
        acessed = []
        for i in self.dl:
            for key in i:
                if key not in acessed:
                    acessed.append(key)
                    count+= 1 
        return count

    def __repr__(self):
        string = "DictList("
        for i in self.dl:
            string += str(i) + ", "
        string = string[:-2] + ")"
        return string
        
    def __contains__(self,ky):
        for i in self.dl:
            if ky in i:
                return True
        return False
    
    def __getitem__(self,k):
        val = 0
        sit = False
        for i in self.dl:
            if k in i:
                sit = True
        if sit == True:
            for i in self.dl:
                
                if k in i:
                    val = i[k]
        else:
            raise KeyError
        return val
                
    def __setitem__(self,k,val):
        hindx = 0
        sit = False
        for i in self.dl:
            if k in i:
                sit = True
        if sit:
            for i in range(len(self.dl)):
                if k in self.dl[i]:
                    hindx = i
            self.dl[hindx][k] = val
        else:
            a = dict()
            a[k] = val
            self.dl.append(a)
    
    def __call__(self,ky):
        lst = []
        count = 0
        for i in self.dl:
            if ky in i:
                lst.append((count,i[ky]))
            count += 1
        return lst
    
    def __iter__(self):
        indx = len(self.dl) - 1
        hist = []
        while indx != -1:
            dct = sorted(self.dl[indx].keys(), key = lambda item:item)
            for i in dct:
                if i not in hist:
                    yield(i,self.dl[indx][i])
                    hist.append(i)
            indx -= 1
            
    def __eq__(self,right):
        if type(right) is DictList:
            ogkeys = set()
            rkeys = set()
            ans = True
            for i in self.dl:
                for ky in i.keys():
                    ogkeys.add(ky)
            for ir in right.dl:
                for kyr in ir.keys():
                    rkeys.add(kyr)
            for og in ogkeys:
                if og not in rkeys:
                    ans = False
                else:
                    if self.__getitem__(og) != right.__getitem__(og):
                        ans = False
            return ans
        elif type(right) is dict:
            ogkeys = set()
            rkeys = set()
            ans = True
            for i in self.dl:
                for ky in i.keys():
                    ogkeys.add(ky)
            for ir in right.keys():
                rkeys.add(ir)
            for og in ogkeys:
                if og not in rkeys:
                    ans = False
                else:
                    if self.__getitem__(og) != right[og]:
                        ans = False
            return ans
        else:
            raise TypeError

        
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
