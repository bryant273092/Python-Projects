from goody import type_as_str  # Useful in some exceptions
from nt import lstat

class DictList:
    def __init__(self, *dct):
        lst=[]
        if dct == None: 
            raise AssertionError("DictList.__init__:'{}'is empty.".format(dct))
        for innerdct in dct: 
            if type(innerdct) is dict: 
                lst.append(innerdct)
            else: 
                raise AssertionError("DictList.__init__:'{}'is not a dictionary.".format(dct))
        self.dl=lst
    
    def __len__(self):
        keys=[]
        for dct in self.dl: 
            for k in dct:
                keys.append(k)
        keys=set(keys)
        return len(keys)
    
    def __repr__(self):
        string=''
        for dct in self.dl: 
            string=string+str(dct)+', '                
        return "DictList({})".format(string)
    
    def __contains__(self, key):
        for dct in self.dl: 
            if key in dct.keys():
                return True
        return False
    
    def __getitem__(self, item):
        check=0
        for dct in self.dl: 
            if dct.get(item) is None:
                check+=1
#                 raise KeyError('{} is not a key in the dictionary'.format(item)) 
                #Check here, if it's not in the first dictionary, it raises an exception, it should only raise an exception
                #if it's not available for all the dictionaries
            for k in dct:
                if k==item:
                    gottem=dct[k]
            if check==len(self.dl):
                raise KeyError('{} is not a key in the dictionary'.format(item)) 
        return gottem
    
    def __setitem__(self, item, val):
#         print(self.dl)
        for dct in self.dl: 
#             print(dct)
            if item not in dct.keys(): 
                newdct=dict()
                newdct[item]=val
                self.dl.append(newdct)
            else: 
                if item in dct.keys(): 
                    dct[item]=val
                    
                    #The problem is that the item isn't the furthest index? Unsure
                    
    def __call__(self,key):
        lst=[]
        check=0
        count=-1
        for dct in self.dl:
            count+=1
            if dct.get(key) is None:
                check+=1
            for k in dct: 
#                 count+=1
                if k==key: 
                    lst.append((count, dct[k]))
                    #need to change k value into the index number
            if check==len(self.dl):
                return lst
        return lst
    
    def __iter__(self):
        #use getitem to get the value from the latest dictionary which is the highest index that would be the val to the key
        def bungen(lst):
            for tup in lst:
                yield tup
        dctnum=-1
        lst=[] 
        for dct in self.dl:
            dctnum+=1
            for k in dct: 
                value=self.__getitem__(k)
                lst.append((k,value,dctnum))    
        lst=sorted(lst, key=lambda x: (-x[2],x[0])) 
        newlst=[]
        for (a, b, _) in lst: 
            newlst.append((a,b))
        newerlst=[]
        for tup in newlst: 
            if tup in newerlst:
                pass
            else:
                newerlst.append(tup)
            
        return bungen(newerlst)  
            # I feel like I wrote my sorted wrong...;. 
            #I know it's messy but it works lmao :(
                
        
            #so what you're trying to do is reverse by index of dictionary, and then in alphabetical order for the keys and they only show up once
    
    def __eq__(self, right):
        #has to be a dictlist or dict
        #keys have to be the same
        if type(right) not in [dict, DictList]:
            raise TypeError('One of the items is not a dict or DictList')
        elif type(right) is dict: 
            for dct in self.dl: 
                if dct.keys()==right.keys():
                    for k in right: 
                        if right[k]==dct[k]:
                            return True
                else:
                    return False
        else: 
            for dct in self.dl:
                for dct2 in right.dl:  
                    if dct.keys()==dct2.keys():
                        return True
                    else: 
                        return False
#         if type(right) not in [dict, DictList]:
#             raise TypeError('One of the items is not a dict or DictList')
#         if type(right) is DictList: 
#             for dct in self.dl:
#                 for dct2 in right.dl:  
#                     if dct.keys()==dct2.keys():
#                         for k in dct():
#                             for k2 in dct2(): 
#                                 if self.__getitem__(k)==self.__getitem__(k2):
#                                     return True
#                     else: 
#                         return False
#         if type(right) is dict: 
#             lst=[]
#             for dct in self dl: 
#                 if right.keys()==dct.keys():
#                     lst.append('true')
#             if 'true' in lst:
#                 return True
#             else:
                return False
                    
    
            




            
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
