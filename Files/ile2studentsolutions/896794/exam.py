from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        self.dl = []
        assert args != ()
        for i in args:
            if type(i) == dict:
                self.dl.append(i)
            else:
                raise AssertionError
    def __len__(self):
        s = set()
        for i in self.dl:
            for k in i:
                s.add(k)
        return len(s)
    def __repr__(self):
        s = 'DictList('
        for i in self.dl:
            s += str(i) + ","
        s.rstrip(',')
        s += ')'
        return s 
    def __contains__(self,arg):
        for i in self.dl:
            for key in i:
                if key == arg:
                    return True 
        return False
    def __getitem__(self,right):
        l = []
        for i in self.dl:
            for key in i:
                if key == right:
                    l.append(i[key])
        if l == []:
            raise KeyError
        else:
            return l[-1]
    def __setitem__(self,name,value):
        count = -1
        l = []
        for i in self.dl:
            count += 1
            for key in i:
                if key == name:
                    l.append(count)
        if l != []:
            self.dl[l[-1]][name] = value
        else:
            self.dl.append({name:value})
    def __call__(self,right):
        l = []
        count = -1
        for i in self.dl:
            count += 1
            for key in i:
                if key == right:
                    l.append((count,i[key]))
        return l 
    
    def __iter__(self):
        l = []
        for i in self.dl:
            for k in i:
                if k not in l:
                    l.append((k,i[k]))
        for i in l:
            yield i
    

        
                
                        


            
if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test


    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
