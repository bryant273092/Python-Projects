#Submitter: bryanth1(Hernandez, Bryant)
import prompt

class Sparse_Matrix:

    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by writing self[...] which calls __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'
    def __init__(self, rows, cols, *arg):
        if type(rows) != int or type(cols) != int:
            raise AssertionError
        elif rows <= 0 or cols <= 0:
            raise AssertionError
        else:
            self.rows = rows
            self.cols = cols
            self.matrix = {}
        
        #self.matrix = {tuple([value[0],value[1]]): value[2] for value in arg if value[2] != 0}
        for value in arg:
            if len(value) != 3:
                raise AssertionError
            elif type(value[0]) not in (int, float) or type(value[1]) not in (int, float) or type(value[2]) not in (int,float):
                raise AssertionError
            elif value[2] == 0:
                pass
            elif value[0] < 0 or value[1] < 0:
                raise AssertionError
            elif value[0] >= self.rows or value[1] >=self.cols:
                raise AssertionError
            elif tuple([value[0],value[1]]) in self.matrix:
                raise AssertionError
            else: 
                self.matrix[tuple([value[0],value[1]])] = value[2]
    def size(self):
        return tuple([self.rows, self.cols])
    def __len__(self):
        return self.rows * self.cols
    def __bool__(self):
        return bool(self.matrix)
    def __repr__(self):
        value_list = [self.rows, self.cols] + [tuple([value[0], value[1], item]) for value, item in self.matrix.items()]
        return 'Sparse_Matrix'+str(tuple(value_list))
    def __getitem__(self, coord):
        if len(coord) != 2 or type(coord[0]) != int or type(coord[1]) != int:
            raise TypeError
        elif coord[0] >= self.rows or coord[1] >=self.cols:
            raise TypeError
        elif coord[0] < 0 or coord[1] < 0:
            raise TypeError
        return self.matrix[coord] if coord in self.matrix else 0
    def __setitem__(self, coord, value):
        if len(coord) != 2 or type(coord[0]) != int or type(coord[1]) != int:
            raise TypeError
        elif coord[0] >= self.rows or coord[1] >=self.cols:
            raise TypeError
        elif coord[0] < 0 or coord[1] < 0:
            raise TypeError
        elif type(value) not in (int, float):
            raise TypeError
        else: 
            self.matrix[coord] = value
    def __delitem__(self, coord):
        if len(coord) != 2 or type(coord[0]) != int or type(coord[1]) != int:
            raise TypeError
        elif coord[0] >= self.rows or coord[1] >=self.cols:
            raise TypeError
        elif coord[0] < 0 or coord[1] < 0:
            raise TypeError
        else:
            self.matrix[coord] = 0
    def row(self, row_num):
        row_list = []
        col_num = 0
        coord = [row_num, col_num]
        for i in range(self.rows):
            if type(row_num) != int or row_num < 0 or row_num>=self.rows:
                raise AssertionError
            
            elif tuple(coord) in self.matrix:
                row_list.append(self.matrix[tuple(coord)])
            else:
                row_list.append(0)
            coord[1] += 1
        return tuple(row_list)
    def col(self, col_num):
        col_list = []
        row_num = 0
        coord = [row_num, col_num]
        for i in range(self.cols):
            if type(col_num) != int or col_num < 0 or col_num>=self.cols:
                raise AssertionError
            
            elif tuple(coord) in self.matrix:
                col_list.append(self.matrix[tuple(coord)])
            else:
                col_list.append(0)
            coord[0] += 1
        return tuple(col_list)
    def details(self):
        return str(self.rows)+'x'+str(self.cols) + ' -> ' + str(self.matrix) + ' -> ' + str(tuple(self.row(i) for i in range(self.rows)))
    def __call__(self, new_row, new_col):
        coord_to_del = []
        if type(new_row) != int or type(new_col) != int or new_row < 0 or new_col < 0:
            raise AssertionError
        else:
            self.rows, self.cols = new_row, new_col
            for coord in self.matrix.keys():
                if coord[0] >= self.rows or coord[1] >= self.cols:
                    coord_to_del.append(coord)
        for coord in coord_to_del:
            del self.matrix[coord]
    def __iter__(self):
        matrix1 = self.matrix
        def coord_gen(matrix1):
            for coord, value in sorted(matrix1.items(), key = (lambda coord: coord[1])):
                yield tuple([coord[0], coord[1], value])
        return coord_gen(matrix1)
    def __pos__(self):
        return Sparse_Matrix(self.rows, self.cols, *((coord[0], coord[1], value) for coord, value in self.matrix.items()))
    def __neg__(self):
        return Sparse_Matrix(self.rows, self.cols, *((coord[0], coord[1], -value) for coord, value in self.matrix.items()))
    def __abs__(self):
        return Sparse_Matrix(self.rows, self.cols, *((coord[0], coord[1], abs(value)) for coord, value in self.matrix.items()))
    def __add__(self, matrix2):
        if type(matrix2) not in (Sparse_Matrix, int, float):
            raise TypeError

        elif type(matrix2) in (int, float):
            return Sparse_Matrix(self.size()[0], self.size()[1],*((coord[0], coord[1], int(value + matrix2)) for coord, value in self.matrix.items()))
        
        else:
            if self.size() != matrix2.size():
                raise AssertionError
            new_values = []
            for coord, value in self.matrix.items():
                if coord in matrix2.matrix:
                    if value + matrix2[coord] != 0:
                        new_values.append(tuple([coord[0], coord[1], value + matrix2[coord]]))
                else:
                    new_values.append(tuple([coord[0], coord[1], value]))
            for coord, value in matrix2.matrix.items():
                if coord not in self.matrix:
                    new_values.append(tuple([coord[0], coord[1], value]))
            return Sparse_Matrix(matrix2.size()[0], matrix2.size()[1], *new_values)
    def __radd__(self, matrix2):
        if type(matrix2) not in (Sparse_Matrix, int, float):
            raise TypeError

        elif type(matrix2) in (int, float):
            return Sparse_Matrix(self.size()[0], self.size()[1],*((coord[0], coord[1], int(value + matrix2)) for coord, value in self.matrix.items()))
        
        else:
            if self.size() != matrix2.size():
                raise AssertionError
            new_values = []
            for coord, value in self.matrix.items():
                if coord in matrix2.matrix:
                    if value + matrix2[coord] != 0:
                        new_values.append(tuple([coord[0], coord[1], value + matrix2[coord]]))
                else:
                    new_values.append(tuple([coord[0], coord[1], value]))
            for coord, value in matrix2.matrix.items():
                if coord not in self.matrix:
                    new_values.append(tuple([coord[0], coord[1], value]))
            return Sparse_Matrix(matrix2.size()[0], matrix2.size()[1], *new_values)    
                    
                
                    
    def __sub__(self, matrix2):
        if type(matrix2) not in (Sparse_Matrix, int, float):
            raise TypeError

        elif type(matrix2) in (int, float):
            return Sparse_Matrix(self.size()[0], self.size()[1],*((coord[0], coord[1], int(value - matrix2)) for coord, value in self.matrix.items()))
        
        else:
            if self.size() != matrix2.size():
                raise AssertionError
            new_values = []
            for coord, value in self.matrix.items():
                if coord in matrix2.matrix:
                    if value - matrix2[coord] != 0:
                        new_values.append(tuple([coord[0], coord[1], value - matrix2[coord]]))
                else:
                    new_values.append(tuple([coord[0], coord[1], value]))
            for coord, value in matrix2.matrix.items():
                if coord not in self.matrix:
                    new_values.append(tuple([coord[0], coord[1], value]))
            return Sparse_Matrix(matrix2.size()[0], matrix2.size()[1], *new_values)  
    def __rsub__(self, matrix2):
        if type(matrix2) not in (Sparse_Matrix, int, float):
            raise TypeError
        elif type(matrix2) in (int, float):
            return Sparse_Matrix(self.size()[0], self.size()[1],*((coord[0], coord[1], int(matrix2 - value)) for coord, value in self.matrix.items()))
        else:
            if self.size() != matrix2.size():
                raise AssertionError
            new_values = []
            for coord, value in self.matrix.items():
                if coord in matrix2.matrix:
                    if  matrix2[coord] - value != 0:
                        new_values.append(tuple([coord[0], coord[1],  matrix2[coord] - value]))
                else:
                    new_values.append(tuple([coord[0], coord[1], value]))
            for coord, value in matrix2.matrix.items():
                if coord not in self.matrix:
                    new_values.append(tuple([coord[0], coord[1], value]))
            return Sparse_Matrix(matrix2.size()[0], matrix2.size()[1], *new_values)    
#     def __eq__(self, right):
#         if type(right) not in (Sparse_Matrix, int, float):
#             return False
#         elif type(right) == Sparse_Matrix and self.size() != right.size():
#             return False
#         elif type(right) == Sparse_Matrix:
#             for coord, value in self.matrix.items():
#                 if coord not in right.matrix or right.matrix[coord] != value:
#                     return False
#             else:
#                 return True
                     
    def __mul__(self, matrix2):
        if type(matrix2) not in (Sparse_Matrix, int, float):
            raise TypeError
        elif type(matrix2) in (int, float):
            return Sparse_Matrix(self.size()[0], self.size()[1],*((coord[0], coord[1], int(value * matrix2)) for coord, value in self.matrix.items()))    
        elif self.rows != matrix2.cols and self.cols != matrix2.rows:
            raise AssertionError
        else:
            new_coord = []
            for i in range(self.rows):
                for j in range(matrix2.cols):
                    old_row = self.row(i)
                    old_col = matrix2.col(i)
                    for x in range(self.rows):
                        if old_row[x]*old_col[x] != 0:
                            new_coord.append(tuple([i,j, old_row[x]*old_col[x]]))
                          
            return Sparse_Matrix(self.rows, matrix2.cols, *new_coord)


            
            
if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Sparse_Matrix before doing the bsc tests
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
