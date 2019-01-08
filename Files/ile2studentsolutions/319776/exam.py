from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*dl):
        if dl == ():
            raise AssertionError
        self.dl = []
        for i in dl:
            self.dl.append(i)
            if type(i) is not dict:
                raise AssertionError
        
    def __len__(self):
        length = set()
        for i in self.dl:
            for q in i:
                length.add(q)
        return(len(length))

    def __repr__(self):
        result = ""
        for i in self.dl:
            result+=str(i)
            result+=', '
        result = result.rstrip(', ')
        return("DictList(" + result + ")")
    
    def __contains__(self,key):
        for i in self.dl:
            if key in i.keys():
                return True
        return False
    
    def __getitem__(self,key):
        if self.__contains__(key) == False:
            raise KeyError
        temp = None
        for i in self.dl:
            if key in i.keys():
                temp = i[key]
        return temp
    
    def __setitem__(self,key,value):
        if self.__contains__(key):
            for i in self.dl:
                if key in i.keys():
                    temp = self.dl.index(i)
            self.dl[temp][key] = value
        else:
            self.dl.append({key:value})
            
    def __call__(self,key):
        if self.__contains__(key):
            ant = []
            for i in self.dl:
                if key in i.keys():
                    temp = self.dl.index(i)
                    ant.append((temp,self.dl[temp][key]))
            return ant
        else:
            return []
        
    def __iter__(self):
        times = len(self.dl)
        start = -1
        temp = []
        while start >= -times:
            temp.extend(sorted(self.dl[start].items()))
            start -= 1
        temp2 = set()
        for i in temp:
            if i[0] not in temp2:
                temp2.add(i[0])
                yield i 
            else:
                pass
            
    def __eq__(self,right):
        if type(right) not in (dict,DictList):
            raise TypeError
        if type(right) is dict:
            for i in right.items():
                if self.__contains__(i[0]) == False:
                    return False
                if self.__getitem__(i[0]) != i[1]:
                    return False
            length = set()
            for i in self.dl:
                for q in i:
                    length.add(q)
            if length != set(right.keys()):
                return False
            return True
        if type(right) is DictList:
            length1 = set()
            for i in self.dl:
                for q in i:
                    length1.add(q)
            length2 = set()
            for i in right.dl:
                for q in i:
                    length2.add(q)
            if length1 == length2:
                length = list(length1)
                for item in length:
                    if self.__getitem__(item) != right.__getitem__(item):
                        return False
            else:
                return False
            return True
            
    def __add__(self,right):
        if type(right) not in (dict, DictList):
            raise TypeError
        if type(right) is DictList:
            length1 = set()
            for i in self.dl:
                for q in i:
                    length1.add(q)
            length2 = set()
            for i in right.dl:
                for q in i:
                    length2.add(q)
            sub_result1 = {}
            sub_result2 = {}
            for i in length1:
                sub_result1.update({i:(self.__getitem__(i))})
            for i in length2:
                sub_result2.update({i:(right.__getitem__(i))})
            return DictList(sub_result1,sub_result2)
        if type(right) is dict:
            length1 = set()
            for i in self.dl:
                for q in i:
                    length1.add(q)
            length2 = set()
            for i in right:
                length2.add(i)
            sub_result1 = {}
            sub_result2 = {}
            for i in length1:
                sub_result1.update({i:(self.__getitem__(i))})
            for i in length2:
                sub_result2.update({i:(right[i])})
            return DictList(sub_result1,sub_result2)
                
    def __radd_(self,right):
        if type(right) not in (dict, DictList):
            raise TypeError
        if type(right) is DictList:
            length1 = set()
            for i in self.dl:
                for q in i:
                    length1.add(q)
            length2 = set()
            for i in right.dl:
                for q in i:
                    length2.add(q)
            sub_result1 = {}
            sub_result2 = {}
            for i in length1:
                sub_result1.update({i:(self.__getitem__(i))})
            for i in length2:
                sub_result2.update({i:(right.__getitem__(i))})
            return DictList(sub_result1,sub_result2)
        if type(right) is dict:
            length1 = set()
            for i in self.dl:
                for q in i:
                    length1.add(q)
            length2 = set()
            for i in right:
                length2.add(i)
            sub_result1 = {}
            sub_result2 = {}
            for i in length1:
                sub_result1.update({i:(self.__getitem__(i))})
            for i in length2:
                sub_result2.update({i:(right[i])})
            return DictList(sub_result1,sub_result2)

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
