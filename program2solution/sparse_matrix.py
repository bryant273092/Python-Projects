class Sparse_Matrix:
    def __init__(self,rows,cols,*rcv_triples):
        assert type(rows) is int and type(cols) is int and\
               rows > 0 and cols > 0, 'Sparse_Matrix.__init__:rows('+str(rows)+') and cols('+str(cols)+') must be integers > 0'
        self.rows   = rows
        self.cols   = cols
        self.matrix = {}
        # Could use self.matrix for seen, but wouldn't catch problem with ... (0,0,0), (0,0,0)
        seen = set()
        for r,c,v in rcv_triples:
            assert r in range(self.rows) and c in range(self.cols),'Sparse_Matrix.__init__: Index not in size: '+str((r,c))
            assert type(v) in [int,float],'Sparse_Matrix.__init__: illegal value '+str(v)
            assert (r,c) not in seen,'Sparse_Matrix.__init__: repeated index '+str((r,c))
            seen.add((r,c))
            if v != 0:
                self.matrix[(r,c)] = v

    
    def size(self):
        return (self.rows,self.cols)
    

    def __len__(self):
        return self.rows*self.cols
    
 
    def __bool__(self):
        return len(self.matrix) > 0
    
 
    def __repr__(self):
        return 'Sparse_Matrix('+str(self.rows)+','+str(self.cols)+','+','.join(tuple(str((r,c,v)) for (r,c),v in self.matrix.items()))+')'


    def __getitem__(self,index):
        if type(index) is not tuple or len(index) != 2 or\
           type(index[0]) is not int or type(index[1]) is not int or\
           index[0] not in range(self.rows) or index[1] not in range(self.cols):
            raise TypeError('Sparse_Matrix.__getitem__: illegal index: ' + str(index))
        return self.matrix.get(index,0)

    
    def __setitem__(self,index,value):
        if type(index) is not tuple or len(index) != 2 or\
           type(index[0]) is not int or type(index[1]) is not int or\
           index[0] not in range(self.rows) or index[1] not in range(self.cols):
            raise TypeError('Sparse_Matrix.__setitem__: illegal index: ' + str(index))
        if type(value) not in [int,float]:
            raise TypeError('Sparse_Matrix.__setitem__: illegal value: ' + str(value))
        if value == 0:
            if index in self.matrix:
                del self.matrix[index]
        else:
            self.matrix[index] = value
        

    def __delitem__(self,index):
        if type(index) is not tuple or len(index) != 2 or\
           type(index[0]) is not int or type(index[1]) is not int or\
           index[0] not in range(self.rows) or index[1] not in range(self.cols):
            raise TypeError('Sparse_Matrix.__delitem__: illegal index: ' + str(index))
        if index in self.matrix:
            del self.matrix[index]

        
    def row(self,r):
        assert type(r) is int and r in range(self.rows),\
            'Sparse_Matrix.row: illegal row #: ' + str(r)
        return tuple(self[r,c] for c in range(self.cols))
        

    def col(self,c):
        assert type(c) is int and c in range(self.cols),\
              'Sparse_Matrix.col: illegal co #l: ' + str(c)
        return tuple(self[r,c] for r in range(self.rows))

 
    def details(self):
#         return str(self.rows)+'x'+str(self.cols)+' -> '+str(self.matrix)+' ->\n'+\
#                str(tuple(tuple(self[r,c] for c in range(self.cols)) for r in range(self.rows)))
        return str(self.rows)+'x'+str(self.cols)+' -> '+str(self.matrix)+' -> '+\
               str(tuple(tuple(self[(r,c)] for c in range(self.cols)) for r in range(self.rows)))


    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by writing self[...] which calls __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'

    def __call__(self,new_r,new_c):
        assert type(new_r) is int and type(new_c) is int and\
               new_r > 0 and new_c > 0, 'Sparse_Matrix.__call__: rows('+str(new_r)+') and cols('+str(new_c)+') must be integers > 0'
        # Using __dict__ bypasses __setattr__
        self.__dict__['rows'] = new_r
        self.__dict__['cols'] = new_c
        for (r,c),_v in list(self.matrix.items()): # iterate over copy so can delete
            if r >= new_r or c >= new_c:
                del self.matrix[(r,c)]
                
#         # Alternative __setattr__ solution
#         # Temporarily save/delete the __setattr__ method object to allow changing
#         temp = Sparse_Matrix.__setattr__
#         del Sparse_Matrix.__setattr__
#         
#         self.rows = new_r
#         self.cols = new_c
#         for (r,c),_v in list(self.matrix.items()): # copy so can delete
#             if r >= new_r or c >= new_c:
#                 del self.matrix[(r,c)]
# 
#         # Restore the __setattr__ method object
#         Sparse_Matrix.__setattr__ = temp

                
    def __iter__(self):
        for (r,c),v in sorted(self.matrix.items(), key=lambda kv: kv[1]):
            yield (r,c,v)
 
 
    def __pos__(self):
        return Sparse_Matrix(self.rows, self.cols, *[(r,c,v) for (r,c),v in self.matrix.items()])       

    
    def __neg__(self):
        return Sparse_Matrix(self.rows, self.cols, *[(r,c,-v) for (r,c),v in self.matrix.items()])       

    
    def __abs__(self):
        return Sparse_Matrix(self.rows, self.cols, *[(r,c,abs(v)) for (r,c),v in self.matrix.items()])       

    
    def __add__(self,right):
        if type(right) not in [Sparse_Matrix,int,float]:
            raise TypeError("TypeError: unsupported operand type(s) for +: '"+str(type(self))+"' and'"+str(type(right))+"'")
        if type(right) is Sparse_Matrix:
            assert self.size() == right.size(),\
              'Sparse_Matrix.__add__: illegal sizes: self is ' + str(self.size()) + '; right is ' + str((right.size()),)
            result = Sparse_Matrix(self.rows,self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    result[r,c] = self[r,c] + right[r,c]
            return result
        else:
            result = Sparse_Matrix(self.rows,self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    result[r,c] = self[r,c] + right
            return result

    def __radd__(self,left):
        return self + left # Commutative for int/float
 
    
    def __sub__(self,right):
        if type(right) not in [Sparse_Matrix,int,float]:
            raise TypeError("TypeError: unsupported operand type(s) for -: '"+str(type(self))+"' and'"+str(type(right))+"'")
        if type(right) is Sparse_Matrix:
            assert self.size() == right.size(),\
              'Sparse_Matrix.__sub__: illegal sizes: self is ' + str(self.size()) + '; right is ' + str((right.size()),)
        return self + -right
    
    def __rsub__(self,left):
        return -self + left # Almost commutative: use unary - on self then binary +
 
    
    def __mul__(self,right):
        if type(right) not in [Sparse_Matrix,int,float]:
            raise TypeError("TypeError: unsupported operand type(s) for *: '"+str(type(self))+"' and'"+str(type(right))+"'")
        if type(right) is Sparse_Matrix:
            assert self.cols == right.rows,\
            'Sparse_Matrix.__mul__: illegal sizes: self is ' + str((self.rows,self.cols),) + '; right is ' + str((right.rows,right.cols),)
            result = Sparse_Matrix(self.rows,right.cols)
            for r in range(self.rows):
                for c in range(right.cols):
                    result[r,c] = sum(v1*v2 for v1,v2 in zip(self.row(r),right.col(c)))
            return result
        else:
            if right == 0:
                return Sparse_Matrix(self.rows,self.cols)
            else:
                return Sparse_Matrix(self.rows,self.cols,*[(r,c,right*v) for (r,c),v in self.matrix.items()])

    def __rmul__(self,left):
        return self * left # Commutative for int/float


    def __pow__(self,right):
        assert self.rows == self.cols,\
            'Sparse_Matrix.__exp__: matrix is not square size: ' + str(self.size)
        if type(right) is not int:
            raise TypeError('Sparse_Matrix.__exp__: right argument not int: ' + str(right))
        assert right >= 1,\
            'Sparse_Matrix.__exp__: illegal non-positive power: ' + str(right)
        result = +self # + to create new Sparse_Matrix; not share
        for _i in range(right-1):
            result = result*self  # + to create new one; not share
        return result


    def __eq__(self,right):
        if type(right) in [int,float]:
            if right == 0:
                return len(self.matrix) == 0
            else:
                return len(self) == len(self.matrix) and all(v==right for v in self.matrix.values() )
        elif type(right) is Sparse_Matrix:
            return self.size() == right.size() and self.matrix == right.matrix
        else:
            return False
    
    def __ne__(self,right):
        return not (self == right)
    
    
    def __setattr__(self,a,v):
        assert 'matrix' not in self.__dict__, 'Sparse_Matrix.__setattr__ attempted to set/reset attribute'
        self.__dict__[a] = v

#         # Code from Chan, Nygaard (do this, but nothing interesting in __call__)
#         # [1] is the frame object whose [3] is the method/function calling this method 
#         import inspect
#         assert a in ('rows', 'cols', 'matrix'), 'Invalid attribute name'
#         if inspect.stack()[1][3] in ('__init__', '__call__'):
#             super(Sparse_Matrix, self).__setattr__(a, v)
#         else:
#             assert False, 'Sparse_Matrix.__setattr__ attempted to set/reset attribute'
            
            
if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Spars_eMatrix before doing the bsc tests
    #Debugging problems with these tests is simpler

    print('Printing')
    m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
    print(m)
    print(repr(m))
    print(m.details())
  
    print('\nlen and size')
    print(len(m), m.size(),)
    
    print('\ngetitem and setitem')
    print(m[1,1])
    m[1,1] = 0
    m[0,1] = 2
    print(m.details())

    print('\niterator')
    for r,c,v in m:
        print((r,c),v)
    
    print('\nm, m+m, m+1, m==m, m==1')
    print(m)
    print(m+m)
    print(m+1)
    print(m==m)
    print(m==1)
    print()
    
    import driver
    driver.default_file_name = 'bscp22F18.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
