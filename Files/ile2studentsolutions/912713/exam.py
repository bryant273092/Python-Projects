from goody import type_as_str  # Useful in some exceptions


class DictList:
    def __init__(self, *args):
        self.dl = []
        assert len(args) >0,"No arguments in Dict" 
        for i in args:
            assert type(i) is dict,"DictList.__init__:{x} is not a dictionary".format(x = i)
            self.dl.append(i)
            
    def __len__(self):
        num_of_elem =set()
        for i in self.dl:
            for k in i:
                num_of_elem.add(k)    
        return len(num_of_elem)
    
    def __repr__(self):
        d_rep = "DictList("
        for i in self.dl:
            d_rep += str(i) + ','
        return d_rep[:-1] +')'
    
    def __contains__(self, value):
        for i in self.dl:
            for k in i:
                if k == value:
                    return True
        return False
    
    def __getitem__(self, index):
        if index not in self:
            raise KeyError("DictList.__getitem__:{x} was not in the DictList".format(x = index))
        h_ind = 0
        for i in range(len(self.dl)):
            if index in self.dl[i] and i>h_ind:
                h_ind = int(i)
        return self.dl[h_ind][index]
    
    def __setitem__(self,index,value):
        if index in self:
            h_ind = 0
            for i in range(len(self.dl)):
                if index in self.dl[i] and i>h_ind:
                    h_ind = int(i)
            self.dl[h_ind][index] = value
        else:
            self.dl.append({index: value})
    
    def __call__(self, k):
        k_in = []
        if k in self:
            for i in range(len(self.dl)):
                if k in self.dl[i]:
                    k_in.append((i,self.dl[i][k]))
            return k_in
        else:
            return k_in
        
    def __iter__(self):
        def gen(dl):
            elem_prod = set()
            dl.reverse()
            for i in dl:
                for k in i:
                    if k not in elem_prod:
                        elem_prod.add(k)
                        yield (k, i[k])
        return gen(list(self.dl))
    
    def __eq__(self, d):
        if type(d) not in (DictList, dict):
            raise TypeError("DictList.__eq__: {x} was not type DictList or dict but type {t}".format(x = d, t = type_as_str(d)))
        elif type(d) == DictList:
            elem_self = set()
            elem_d = set()
            for i in self.dl:
                for k in i:
                    elem_self.add(k)
            for i in d.dl:
                for k in i:
                    elem_d.add(k)
            if elem_self == elem_d:
                return all([self[i] == d[i] for i in elem_d])
            else:
                return False
        elif type(d) == dict:
            elem_self = set()
            elem_d = set()
            for i in self.dl:
                for k in i:
                    elem_self.add(k)
            for i in d:
                elem_d.add(i)
            if elem_d == elem_self:
                return all([self[i] == d[i] for i in elem_d])
            else:
                return False
            
    def __add__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError("DictList.__add__: {x} was not type DictList or dict but type {t}".format(x = right, t = type_as_str(right)))
        elif type(right) == DictList:
            elem_left = set()
            for i in self.dl:
                for k in i:
                    elem_left.add(k)
            dict_left= {}
            for i in elem_left:
                dict_left.update({i: self[i]})
            
            elem_right = set()
            for i in right.dl:
                for k in i:
                    elem_right.add(k)
            dict_right= {}
            for i in elem_right:
                dict_right.update({i: right[i]})
            return DictList(dict_left, dict_right)
        elif type(right) == dict:
            new_dl = []
            for i in self.dl:
                new_dl.append(i)
            new_dl.append(dict(right))
            return DictList(*new_dl)
        
    def __radd__(self, left):
        if type(left) == dict:
            new_dl = [dict(left)]
            for i in self.dl:
                new_dl.append(dict(i))
            return DictList(*new_dl)
        else:
            raise TypeError("DictList.__radd__: {x} was not type DictList or dict but type {t}".format(x = left, t = type_as_str(left)))
                
                
      
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
