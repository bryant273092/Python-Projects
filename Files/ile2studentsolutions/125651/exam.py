from goody import type_as_str  # Useful in some exceptions

class DictList:
    

    def __init__(self, *args):
        #fix this message to be more specific
        assert len(args) > 0 and all([type(item) == dict for item in args]), f"one or more items is not a dictionary"
        
        self.dl = [i for i in args]
        
    
    def __len__(self):
        unique_keys = set()
        for dictionary in self.dl:
            for key in dictionary.keys():
                unique_keys.add(key)
                
        return len(unique_keys)
    
    def __repr__(self):
        dict_string = ",".join([str(dictionary) for dictionary in self.dl])
        reprstring =  f"DictList({dict_string})"
        #print(reprstring)
        return reprstring
    
    def __contains__(self, key):
        return any([key in dictionary for dictionary in self.dl])
    
    def __getitem__(self, index):
        flipped = [i for i in reversed(self.dl)]
        for i in range(len(self.dl)):
            try:
               # print(f"looking for it in {flipped},\nspecifically in {flipped[i]}\nI think i found it, and it's {flipped[i][index]}")
#                 print(f"I think i found it, and it's {self.dl[-i][index]}")
               # print(f"which would make the real one at {self.dl}")
                #return
                return self.dl[-(i+1)][index]
            except KeyError:
                #print(f"looked for it in dict: {flipped[i]}\nbut I couldn't find it")

                continue
        raise KeyError(f"I gave up at index {i}")
    
    def __setitem__(self, index, value):
        flipped = [i for i in reversed(self.dl)]
        for i in range(len(self.dl)):
            try:
                if index in self.dl[-(i+1)]:
                    self.dl[-(i+1)][index] = value
                    return
            except KeyError:
                continue
        self.dl.append({index:value})
        
    def __call__(self, value):
        returnlist = []
        for index, dictionary in enumerate(self.dl):
            if value in dictionary:
                returnlist.append((index,dictionary[value]))
        return returnlist
    
    def __iter__(self):
        def iterator():
            skipset = set()
            macroresult = []
            for i in range(len(self.dl)):
                microresult = []
                for key, value in self.dl[-(i+1)].items():
                    
                    if key not in skipset:
                        skipset.add(key)
                        microresult.append((key,value))
                macroresult.extend(sorted(microresult))
            print(macroresult)
            

            while len(macroresult) > 0:
                yield macroresult[0]
                macroresult = macroresult[1:]
                
        def iter2():
            mylist = [1,2,3,4,5]
            while len(mylist) > 0:
                yield mylist[0]
                mylist = mylist[1:]
            
        return iterator()
    
    def __eq__(self, right):
        #SURELY we should be using call here.
        #print(f"{repr(self)}\nequal to\n{repr(right)}\n")
        def uniques(dictlist):
            unique_keys = set()
            for dictionary in self.dl:
                for key in dictionary.keys():
                    unique_keys.add(key)
                    
            return (unique_keys)
        
        if type(right) == DictList:
            if uniques(self) != uniques(right):
                return False
           
            return all([self[key] == right[key] for key in uniques(self)])
        
        if type(right) == dict:
            #print([key in right for key in uniques(self)])
            return len(uniques(self)) == len(right) and all([key in right for key in uniques(self)]) and all([self[key] == right[key] for key in uniques(self)])

        else:
            raise TypeError("You can't compare these for equality")

            
    def __add__(self, right):

        def uniques(dictlist):
            unique_keys = set()
            for dictionary in self.dl:
                for key in dictionary.keys():
                    unique_keys.add(key)
                    
            return (unique_keys)
        luniques= list(uniques(self))
        
        if type(right) == DictList:
            
            #print(f"unqiues: {luniques} and {runiques}")
            
            keyvalpairs = [(key, self[key]) for key in luniques]
            
            #print(f"keyvalpairs:{keyvalpairs}")
            
            leftdict = {key: value for (key, value) in keyvalpairs}
            
            keyvalpairs = [(key, right[key]) for key in uniques(right)]
            rightdict = {key: value for (key, value) in keyvalpairs}
            
            return DictList(leftdict,rightdict)
        
        if type(right) == dict:
            newdict = eval(self.__repr__())
#             newdict.dl.insert(0,right)
            newdict.dl.append(right)

            return newdict
        
        else:
            raise TypeError("Right operand must be dict or DictList")
        
    def __radd__(self, left):
        self.__add__(left)
        
        
        
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test

    td = DictList({"a":1,"b":2},{"c":3,"a":4})

    print(td['a'])

    print("this is a call!")
    print(td('a'))
    
    print([x for x in td])
    
    l = DictList({'a': 1, 'b': 2},{'b': 12, 'c': 13})

    r = {'a': 'one', 'b': 'two'}
    
    l = DictList({'a': 'one', 'b': 'two'}, {'a': 1, 'b': 2})
    
    r =  {'b': 12, 'c': 13}
    
    print(l+r)
    
    
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
