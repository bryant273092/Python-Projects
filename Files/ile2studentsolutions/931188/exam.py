from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        self.dl = []
        if len(args) == 0:
            raise AssertionError(f"DictList.__init__: no dictionaries were passed as arguments")
        else:
            for d in args:
                if not type(d) == dict:
                    raise AssertionError(f"DictList.__init__: '{d}' is not a dictionary")
                else:
                    self.dl.append(d)
    
    
    def __len__(self):
        distinct = set()
        for d in self.dl:
            for k in d:
                distinct.add(k)
        return len(distinct)
    
        
    def __repr__(self):
        result = ""
        for d in self.dl:
            result += f"{d}, "
        return f"DictList({result[:-2]})"
    
    
    def __contains__(self, item):
        for d in self.dl:
            if item in d:
                return True
        return False
    
    
    def __getitem__(self, item):
        result = ""
        times = 0
        for d in self.dl:
            for k in d:
                if k == item:
                    result = d[k]
                    times += 1
        if times == 0:
            raise KeyError(f"DictList.__getitem__: '{item}' appears in no dictionaries")
        return result
    
    
    def __setitem__(self, item, value):
        indict = False
        inum = len(self.dl) - 1
        for d in reversed(self.dl):
            for k in d:
                if k == item:
                    self.dl[inum][k] = value
                    indict = True
                    break
            if indict:
                break
            inum -= 1
        if not indict:
            self.dl.append({item: value})
    
    
    def __call__(self, item):
        result = []
        idx = 0
        for d in self.dl:
            if item in d:
                result.append((idx, self.dl[idx][item]))
            idx += 1
        return result
    
    
    def __iter__(self):
        used_keys = set()
        result = []
        for d in reversed(self.dl):
            order = []
            for k in d:
                if k not in used_keys:
                    used_keys.add(k)
                    order.append((k, d[k]))
            for o in sorted(order):
                result.append(o)
        for pair in result:
            yield pair
    
    
    def __eq__(self, right):
        if type(right) not in [dict, DictList]:
            raise TypeError(f"DictList.__eq__: '{right}' was type {type_as_str(right)}, should be dict or DictList")
        else:
            current, compare = set(), set()
            for i in self:
                current.add(i)
            if type(right) == dict:
                for k in right:
                    compare.add((k, right[k]))
            else:
                for k in right:
                    compare.add(k)
            if current == compare:
                return True
            return False
    
    
    def __add__(self, right):
        if type(right) not in [dict, DictList]:
            raise TypeError(f"DictList.__add__: '{right}' was type {type_as_str(right)}, should be dict or DictList")
        else:
            ltemp, rtemp = [], []
            lresult, rresult = {}, {}
            if type(right) == DictList:
                for k in self:
                    ltemp.append(k)
                for t in ltemp:
                    lresult[t[0]] = t[1]
                for k in right:
                    rtemp.append(k)
                for t in rtemp:
                    rresult[t[0]] = t[1]
                return DictList(lresult, rresult)
            else:
                results = []
                for d in self.dl:
                    results.append(d)
                results.append(dict(right))
                return DictList(*results)
    
    
    def __radd__(self, right):
        if not type(right) == dict:
            raise TypeError(f"DictList.__radd__: '{right}' was type {type_as_str(right)}, should be dict or DictList")
        else:
            results = []
            results.append(dict(right))
            for d in self.dl:
                results.append(d)
            return DictList(*results)
    


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
