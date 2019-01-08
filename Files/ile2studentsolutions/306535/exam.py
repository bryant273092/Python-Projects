
class DictList:
    
    def __init__(self, *args):
        assert len(args) != 0, "DictList.__init__: argument is empty"
        for i in args:
            assert type(i) == dict, "DictList.__init__: '{}' is not a dictionary".format(args[0])
        self.dl = list(args)
    
    def __len__(self):
        total = []
        for i in self.dl:
            for j in i:
                total.append(j)
        return len(set(total))
    
    def __repr__(self):
        final = ''
        for i in self.dl:
            final += str(i) + ', '
        final = final.rstrip().rstrip(',')
        return 'DictList({})'.format(final)
    
    def __contains__(self, item):
        for i in self.dl:
            if item in i:
                return True
        return False
    
    def __getitem__(self, item):
        all = []
 
        for i in self.dl:
            if item in i:
                all.append(i[item])
        
        if len(all) == 0:
            raise KeyError("'{}' not in any dictionary".format(item))
        return all[-1]
    
    def __setitem__(self, item, value):
        all = []
 
        for i in self.dl:
            if item in i:
                all.append(i[item])
        
        if len(all) != 0:
            for i in self.dl[::-1]:
                if item in i:
                    i[item] = value
                    break
        elif len(all) == 0:
            d = {}
            d[item] = value
            self.dl.append(d)
    
    def __call__(self, item):
        final = []
        
        for num in range(len(self.dl)):
            if item in self.dl[num]:
                final.append((num, self.dl[num][item]))
        return final
    
    def __iter__(self):
        final = []
        check = []
        for i in self.dl[::-1]:
            for j in i:
                if j not in check:
                    check.append(j)
                    final.append((j, i[j]))
        for i in final:
            yield i
            
    def __eq__(self, other):
        self_keys = []
        other_keys = []
        test = []
        
        for i in self.dl:
            for j in i:
                self_keys.append(j)
        
        if type(other) == DictList:
            for i in other.dl:
                for j in i:
                    other_keys.append(j)
        elif type(other) == dict:
            for i in other:
                other_keys.append(i)
        else:
            raise TypeError('Not a dictionary nor DictList')
        
        if set(self_keys) != set(other_keys):
            return False
        
        for k in set(self_keys):
            test.append(self.__getitem__(k) == other.__getitem__(k))
        
        return all(test)
                    



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
