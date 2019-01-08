from goody import type_as_str  # Useful in some exceptions
from _operator import index
from audioop import reverse

class DictList:
    
    def __init__(self,*args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError("no dictionaries")
        for i in args:
            if type(i) != dict:
                raise AssertionError("not dict")
            else:
                self.dl.append(i)

    def __len__(self):
        distinct = set()
        for dict in self.dl:
            for key in dict.keys():
                distinct.add(key)
        return len(distinct)
    
    def __repr__(self):
        string = "DictList("
        for item in self.dl:
            string += str(item) + ", "
        string = string[:len(string)-2] + ")"
        return string

    def __contains__(self,arg):
        for item in self.dl:
            for key in item.keys():
                if arg == key:
                    return True
        return False

    def __getitem__(self,chosen):
        value = 0
        index = -1
        inDict = False
        for dict in self.dl:
            index += 1
            for key in dict.keys():
                if key == chosen:
                    inDict = True
                    value = self.dl[index][key]
        if inDict == False:
            raise KeyError
        return value
        
    def __setitem__(self,chosenKey,chosenValue):
        latestKey = ""
        latestindex = -1
        index = -1
        inDict = False
        for dic in self.dl:
           index +=1
           for key in dic.keys():
                if chosenKey == key:
                    inDict = True
                    latestindex = index
                    latestKey = key
        if inDict == True:
            self.dl[latestindex][latestKey] = chosenValue
        else:
            self.dl.append({chosenKey:chosenValue})
    
    def __call__(self,chosenKey):
        newLst = []
        index = -1
        for dic in self.dl:
            index += 1
            for key in dic.keys():
                if chosenKey == key:
                    newLst.append((index,self.dl[index][key]))
        return newLst
                    
    def __iter__(self):
        oldKeys = set()
        alphaList = []
        reversedList = list(self.dl)
        reversedList.reverse()
        index = -1
        for dic in reversedList:
            index += 1
            for key in dic.keys():
                if key not in oldKeys:
                    oldKeys.add(key)
                    alphaList.append((key,reversedList[index][key]))
            alphaList = sorted(alphaList, key = lambda x: x[0])
            for item in alphaList:
                yield item
            alphaList.clear()
    
    def __eq__(self,other):
        if type(other) not in (DictList,dict):
            raise TypeError("right operand is not a dictlist or dict")
        if type(other) == DictList:
            for dic in self.dl:
                for key in dic.keys():
                    if key not in other:
                        return False
                    if self[key] != other[key]:
                        return False
            for dic in other.dl:
                for key in dic.keys():
                    if key not in self:
                        return False
                    if other[key] != self[key]:
                        return False
        else:
            for dic in self.dl:
                for key in dic.keys():
                    if key not in other:
                        return False
                    if self[key] != other[key]:
                        return False
            for key in other.keys():
                if key not in self:
                    return False
                if other[key] != self[key]:
                    return False
        return True
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d = DictList(dict(a=1,b=2),dict(b = 12, c =13))
    d2 = DictList(dict(a=1,b=12),dict(c=13))
    print(d == d2)

    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
