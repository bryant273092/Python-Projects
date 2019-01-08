
class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError('No dictionary')
        else:
            for d in args:
                if type(d) != dict:
                    raise AssertionError(str(d) + ' is not a dictionary')
                else:
                    self.dl.append(d)
    
    def __len__(self):
        k_list = []
        for d in self.dl:
            for k in d:
                k_list.append(k)
        return len(set(k_list))
    
    def __repr__(self):
        return 'DictList' + str(tuple(self.dl))
    
    def __contains__(self, key):
        for d in self.dl:
            if key in d:
                return True
        return False
    
    def __getitem__(self, key):
        result = []
        for d in self.dl:
            if key in d:
                result.append(d[key])
        if len(result) == 0:
            raise KeyError(str(key) + ' appears in no dictionaries')
        else:
            return result[-1]
    
    def __setitem__(self, key, value):
        index_list = []
        for num in range(len(self.dl)):
            if key in self.dl[num]:
                index_list.append(num)
        if len(index_list) == 0:
            new_dict = dict()
            new_dict[key] = value
            self.dl.append(new_dict)
        else:
            self.dl[index_list[-1]][key] = value
    
    def __call__(self, key):
        result = []
        for num in range(len(self.dl)):
            if key in self.dl[num]:
                result.append((num, self.dl[num][key]))
        return result
    
    def __iter__(self):
        result = []
        num_list = []
        for i in range(len(self.dl)):
            num_list.append(i)
        for num in sorted(num_list, reverse=True):
            d = sorted(self.dl[num])
            for i in d:
                count = 0
                for tup in result:
                    if i == tup[0]:
                        count += 1
                if count == 0:
                    result.append((i, self.dl[num][i]))
        return iter(result)
        
    def __eq__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError(str(right) +' is not a DictList')
        else:
            g = self.__iter__()
            dict_list = [i for i in g]
            for d in dict_list:
                try:
                    if self.__getitem__(d[0]) != right.__getitem__(d[0]):
                        return False
                except KeyError:
                    return False
            return True
    
    def __add__(self, right):
        if type(right) not in (DictList, dict):
            raise TypeError(str(right) + ' is not a DictList or a dictionary')
        elif type(right) == DictList:
            gs = self.__iter__()
            ls = [i for i in gs]
            ds = dict()
            for tup in ls:
                ds[tup[0]] = tup[1]
            gr = right.__iter__()
            lr = [j for j in gr]
            dr = dict()
            for tup in lr:
                dr[tup[0]] = tup[1]
            return DictList(ds, dr)
        else:
            new_dictlist = DictList(self.dl[0])
            if len(self.dl)==1:
                new_right = dict()
                for k in right:
                    new_right[k] = right[k]
                new_dictlist.dl.append(new_right)
                return new_dictlist
            else:
                for num in range(1, len(self.dl)):
                    new_dictlist.dl.append(self.dl[num])
                new_right = dict()
                for k in right:
                    new_right[k] = right[k]
                new_dictlist.dl.append(new_right)
                return new_dictlist
    
    def __radd__(self, left):
        if type(left) not in (DictList, dict):
            raise TypeError(str(left) + ' is not a DictList or a dictionary')
        elif type(left) == DictList:
            return left + self
        else:
            new_left = dict()
            for k in left:
                new_left[k] = left[k]
            new_dictlist = DictList(new_left)
            for d in self.dl:
                new_dictlist.dl.append(d)
            return new_dictlist





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
