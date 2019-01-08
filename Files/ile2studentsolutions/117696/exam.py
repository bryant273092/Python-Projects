from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError
        else:
            for each in args:
                if type(each) == dict:
                    self.dl.append(each)
                else:
                    raise AssertionError("DictList.__init__:{} is not in a dictionary".format(str(each)))
 
    def __len__(self):
        unique = []
        for each in self.dl:
            for k in each.keys():
                unique.append(k)
        return len(set(unique))

    def __repr__(self):
        return "DictList({})".format(str(self.dl).strip("[]"))
    
    def __contains__(self, index): 
        keys = []
        for each in self.dl:
            for k in each.keys():
                keys.append(k)
        return index in keys #boolean
        
    def __getitem__(self, index):
        if self.__contains__(index):
            final = ""
            for each in self.dl:
                for k in each.keys():
                    if index == k:
                        final = each[k]
            return final
        else:
            raise KeyError("{} appears in no dictionaries".format(index))
    
    def __setitem__(self,index,value): #fix for highest value
        #i = 0 
        for each in self.dl:
            if index in each.keys():
                #i = self.dl.index(each)
                each[index] = value
                #self.dl[i][index] = value
            else:
                self.dl.append({index:value})

    def __call__(self, item):
        dl_tup = []
        for each in self.dl:
            for k,v in each.items():
                if item == k:
                    dl_tup.append((self.dl.index(each),v))
        return dl_tup
    
    def __iter__(self): #need to get rid of lower value keys!!
        it_list = []
        keys = []
        for each in self.dl:
            for k,v in each.items():
                it_list.append((k,v))
        for x in it_list:
            if x[0] not in keys:
                yield x
                keys.append(x[0])
            
    def __eq__(self, right): #Q_Q
        if type(right) == DictList:
            return True
        elif type(right) == dict:
            return True
        else:
            raise TypeError("types do not match.")
            
    
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
#     d = DictList(dict(a=1,b=2), dict(c=13,d=14))
#     print(d.dl)
#     print(d.__repr__())
#     d.dl[0]['a'] = 3
#     print(d.dl[0]['a'])
#     for i in d:
#         print(i)
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
