from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        if args is '' or args is None or args is [] or args is ():
            raise AssertionError('No dictionary is found')
        for i in args:
            assert type(i) is dict, f'{i} is not a dictionary'
        self.dl = []
        for i in args:
            self.dl.append(i)
        
    def __len__(self):
        aset = set()
        for i in self.dl:
            for j in i:
                aset.add(j)
        return len(aset)
        
    def __repr__(self):
        reprstr = f'DictList('
        for i in range(len(self.dl)):
            reprstr += repr(self.dl[i])
            if i != len(self.dl) -1:
                reprstr += ', '
        reprstr += ')'
        return reprstr
    
    def __contains__(self,key):
        for i in self.dl:
            for j in i:
                if key == j:
                    return True
        return False
        
    def __getitem__(self,key):
        count = 0
        for i in self.dl:
            if key in i:
                count += 1
        if count == 0:
            raise KeyError(f'{key} appears in no dictionaries')
        for i in reversed(self.dl):
            if key in i:
                return i[key]
                
    def __setitem__(self,key,values):
        count = 0
        for i in self.dl:
            if key in i:
                count += 1
        if count == 0:
            self.dl.append({})
            self.dl[-1][key] = values
        else:
            for i in reversed(self.dl):
                if key in i:
                    i[key] = values
                    break

    def __call__(self,key):
        count,alist = 0,[]
        for i in self.dl:
            if key in i:
                count += 1
        if count == 0:
            return []
        else:
            for i in range(len(self.dl)):
                if key in self.dl[i]:
                    alist.append((i,self.dl[i][key]))
        return alist
                
    def __iter__(self):
        aset = set()
        for i in reversed(self.dl):
            for j in i:
                if j not in aset:
                    yield (j, i[j])
                    aset.add(j)
        
    def __eq__(self,right):
        if type(right) not in (DictList,dict):
            raise TypeError('The one you compare equal must be a Dictlist or a dict')
        if type(right) is DictList:
            self_list = [i for i in self]
            right_list = [i for i in right]
            if sorted(self_list) == sorted(right_list):
                return True
            else:
                return False
        elif type(right) is dict:
            self_list = [i for i in self]
            if len(self_list) != len(right):
                return False
            else:
                for i in sorted(self_list):
                    if i[0] not in right:
                        return False
                    else:
                        if right[i[0]] != i[1]:
                            return False
                return True
            
    def __add__(self,right):
        if type(right) is DictList:
            self_list,right_list = [i for i in self],[i for i in right]
            d0,d1 = {},{}
            for i in self_list:
                d0[i[0]] = i[1]
            for j in right_list:
                d1[j[0]] = j[1]
            return DictList(d0,d1)
        elif type(right) is dict:
            self_lists = [dict(i) for i in self.dl]
            self_lists.append(dict(right))
            return DictList(*list(self_lists))
        else:
            raise TypeError
        
    def __radd__(self,left):
        if type(left) is dict:
            adict = dict(left)
            self_lists = [adict]
            for i in self.dl:
                self_lists.append(i)
            return DictList(*list(self_lists))
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
