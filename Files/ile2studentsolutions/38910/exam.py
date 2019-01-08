# Submitter: ggabrich(Gabricht, George)

from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args: (dict, )) -> None:
        assert args and len(args) > 0, "DictList.__init__: must pass 1 or more Dicts to init."
        self.dl = []
        for item in args: 
            assert isinstance(item, dict), f"DictList.__init__: '{item}' is not a dictionary."
            self.dl.append(item)
    
    def __len__(self) -> int:
        sumset = set()
        for item in self.dl: sumset.update(set(item.keys()))
        return len(sumset)
    
    def __repr__(self) -> str: return f"DictList({','.join([str(item) for item in self.dl])})"
    
    def __contains__(self, key) -> bool:
        for item in self.dl: 
            if key in item.keys(): return True
        return False
    
    def __getitem__(self, key):
        for ndx in range(len(self.dl)-1, -1, -1):
            if key in self.dl[ndx]: return self.dl[ndx][key]
        raise KeyError(f"DictList.__getitem__: key {key} is not a key in any of the dicts.")
    
    def __setitem__(self, key, value) -> None:
        for ndx in range(len(self.dl)-1, -1, -1):
            if key in self.dl[ndx]: 
                self.dl[ndx][key] = value
                return
        self.dl.append({key:value})
    
    def __call__(self, key) -> [(int, )]:
        result = []
        for ndx in range(len(self.dl)):
            if key in self.dl[ndx]: result.append((ndx, self.dl[ndx][key]))
        return result
    
    def __iter__(self):
        unique = set()
        for ndx in range(len(self.dl)-1, -1, -1):
            for item in sorted(self.dl[ndx].items()):
                if item[0] not in unique:
                    unique.add(item[0])
                    yield item
    
    def __eq__(self, right: dict or 'DictList') -> bool:
        lk, rk = [], []
        if isinstance(right, dict): rk = sorted(right.items())
        elif isinstance(right, DictList): rk.extend([item for item in right])
        else: raise TypeError(f"DictList.__eq__: cannot compare type DictList and type {type_as_str(right)}.")
        
        lk.extend([item for item in self])
        if len(lk) != len(rk): return False
        for item in lk:
            if item[0] not in right or self[item[0]] != right[item[0]]: return False
        return True
    
    def __add__(self, right: dict or 'DictList') -> 'DictList':
        if isinstance(right, dict): return eval(f"DictList({','.join([str(item) for item in (list(self.dl) + [right])])})")
        elif isinstance(right, DictList):
            dl, dr = dict(), dict()
            for item in self: dl[item[0]] = item[1]
            for item in right: dr[item[0]] = item[1]
            return DictList(dl, dr)
        else: raise TypeError(f"DictList.__add__: cannot add type DictList and type {type_as_str(right)}.")
    
    def __radd__(self, left: dict) -> 'DictList':
        if isinstance(left, dict): return eval(f"DictList({','.join([str(item) for item in ([left] + list(self.dl))])})")
        else: raise TypeError(f"DictList.__radd__: cannot add type {type_as_str(left)} and type DictList.")





if __name__ == '__main__':
    #Put code here to test DictList before doing bsc test
    d1 = {'a':1, 'b':2, 'c':3}
    d2 = {'c':13, 'd': 14, 'e': 15}
    d3 = {'e':25, 'f':26, 'g':27}
    
    dList = DictList(d1, d2, d3)
    print(len(dList))
    print(repr(dList))
    
    dListRep = eval(repr(dList))
    print(len(dListRep))
    print(repr(dListRep))
    
    print(dList['a'])
    dList['c'] = 20
    print(dList['c'])
    dList['q'] = 100
    print(dList['q'])
    print(repr(dList))
    
    print(dList('c'))
    print(dList('z'))
    
    for item in dList: print(f'item: {item}')
    
    print(dList == dListRep)
    print(dList == d1)
    print(dList == eval(repr(dList)))
    
    print(dList + dListRep)
    print(dList + {'z':150})
    print(d1 + dList)
    
    #driver tests
    import driver
    driver.default_file_name = 'bscile2F18.txt'
    #Uncomment the following lines to see MORE details on exceptions
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
