from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl= []
        assert len(args) != 0, 'DictList.__init__: {x} is not a dictionary'.format(x=args)
        #assert len(args) != 0, f'DictList.__init__: {args} is not a dictionary'
        for item in args:
            #assert type(item) == dict, f'DictList.__init__: {item} is not a dictionary'
            assert type(item) == dict, 'DictList.__init__: {x} is not a dictionary'.format(x=item)
            self.dl.append(item)
            
    def __len__(self):
        output= []
        for dict in self.dl:
            for item in dict.keys():
                if item not in output:
                    output.append(item)
        return len(output)
        
    def __repr__(self):
        output= 'DictList('
        for item in self.dl:
            output= output + str(item) + ','
        output= output[:-1] +')'
        return output
        
#         for d in self.dl:
#             result+= str(d) + ','
#         result.strip(',')
#         return result
    
    def __contains__(self, key):
        for item in self.dl:
            if key in item.keys():
                return True
        return False
    
    def __getitem__(self, key):
        result= None
        for d in self.dl:
            if key in d.keys():
                result= d[key]
        if result == None:
            #raise KeyError 'DictList.__init__: {x} is not a dictionary'.format(x=key)
            raise KeyError (f'DictList.__init__: {key} is not a dictionary')
        return result
        
    
    def __setitem__(self, key, value):
        num= 0
        l= list()
        for item in self.dl:
            if key in item.keys():
                l.append(num)
            num= num + 1
        if l == list():
            item= {key:value}
            self.dl.append(item)
        else:
            self.dl[l[-1]][key]= value
            
    
    def __call__(self, key):
        output= []
        num= 0
        for item in self.dl:
            if key in item.keys():
                output.append((num, item[key]))
            num= num + 1
        return output
    
    def __iter__(self):
        output= {}
        num= 0
        for i in range(len(self.dl)):
            for key in sorted(self.dl[num].keys()):
                if key not in output.keys():
                    output[key] = self.dl[num][key]
            num= num - 1
        output= list(output.items())
        for num in output:
            yield num
            
            
    def __eq__(self, right):
        if type(right) in [DictList, dict]:
            return True
        else:
            raise TypeError
        l= list()
        for item in self.dl:
            for i in item.keys():
                if i not in l:
                    l.append(i)
        for i in l:
            try:
                if self[i] != right[i]:
                    return False
            except:
                return False
        return True
        





            
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
