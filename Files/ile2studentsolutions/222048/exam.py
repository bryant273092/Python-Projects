from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self, *args):
        assert len(args) != 0,"no dictionaries found"
        for i in args:
            assert type(i) is dict, "{0} is not a dictionary".format(i)
        self.dl = list(args)

    def __len__(self):
        aset = set()
        for d in self.dl:
            for k in d:
                aset.add(k)
        return len(aset)
    
    def __repr__(self):
        astr = str(self.dl).strip('[]')
        return "DictList({0})".format(astr)

    def __contains__(self, item):
        abool = False
        for d in self.dl:
            for k in d:
                if item == k:
                    abool = True
        return abool

    def __getitem__(self, item):
        value = None
        for d in self.dl:
            if item in d:
                value = d[item]
        if value == None:
            raise KeyError
        else:
            return value

    def __setitem__(self, item, value):
        rdl = (self.dl)[::-1]
        abool = False
        for d in rdl:
            if item in d:
                abool = True
                d[item] = value
                break
        if not abool:
            rdl.insert(0, {item:value})
        self.dl = rdl[::-1]

    def __call__(self, item):
        alist = []
        for i in range(len(self.dl)):
            if item in self.dl[i]:
                alist.append((i, self.dl[i][item]))
        return alist

    def __iter__(self):
        aset = set()
        rdl = (self.dl)[::-1]
        for d in rdl:
            for t in sorted(d.items(),reverse=False):
                if t[0] not in aset:
                    aset.add(t[0])
                    yield t

    def __eq__(self,right):
        alist = set()
        aset = set()
        rlist = set()
        rset = set()
        for d1 in (self.dl)[::-1]:
            for item1 in d1.items():
                if item1[0] not in aset:
                    aset.add(item1[0])
                    alist.add(item1)
        if type(right) is DictList:
            rrdl = (right.dl)[::-1]
            for d2 in rrdl:
                for item2 in d2.items():
                    if item2[0] not in rset:
                        rset.add(item2[0])
                        rlist.add(item2)
            return alist==rlist
        elif type(right) is dict:
            for item2 in list(right.items())[::-1]:
                if item2[0] not in rset:
                    rset.add(item2[0])
                    rlist.add(item2)
            return alist==rlist
        else:
            raise TypeError("right operand must be a Dictlist or a dict")


            
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