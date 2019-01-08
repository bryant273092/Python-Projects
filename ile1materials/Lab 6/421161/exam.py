from collections import defaultdict   # If you choose to use defaultdict  

# You might use these abbreviations in your code
# c  : caller
# r  : receiver
# t  : time
# ts : list of times


def all_parties(db : {str:{str:[int]}}) -> {str}:
    di={ k for k in db}
    for i in db:
        for value in db[i]:
            if value not in di:
                di.add(value)
    return di



def read_db(file : open) -> {str:{str:[int]}}:
    defa = defaultdict(dict)
    
    for lines in file:
        new_line = lines.rstrip().split(':')
        key = new_line[0]
        name = new_line[1]
        numbers= new_line[2:]
        num=[]
        for i in numbers:
            num.append(int(i))
        di={}
        
        di[name]= [i for i in num]
        defa[key].update(di)
    return dict(defa)
            
        
        



def talker_frequency (db : {str:{str:[int]}}) -> [(str,int)]:
    li=[]
    for i, v in db.items():
        times=[ k for j in db[i].values() for k in j]
        for j in db[i]:
            if i in db[j]:
                coo=[k for k in db[j].values() ]
        li.append((i, len(times+coo)))
    return li  




def mutual_callers (db : {str:{str:[int]}}) -> {(str,str)}:
    li= [i for i in db]
    be=set()
    num=0
    while num < len(li)-4:
        if li[num] in db[li[num+1]] and li[num+1] in db[li[num]]:
            be.add(( li[num], li[num+1])) 
        if li[num] in db[li[num+2]] and li[num+2] in db[li[num]]:
            be.add(( li[num], li[num+2])) 
        if li[num] in db[li[num+3]] and li[num+3] in db[li[num]]:
            be.add(( li[num], li[num+3])) 
        if li[num] in db[li[num+4]] and li[num+4] in db[li[num]]:
            be.add(( li[num], li[num+4])) 
        if num > 1:
            if li[num] in db[li[num+1]] and li[num+1] in db[li[num]]:
                be.add(( li[num], li[num+1])) 
            if li[num] in db[li[num+2]] and li[num+2] in db[li[num]]:
                be.add(( li[num], li[num+2])) 
            if li[num] in db[li[num+3]] and li[num+3] in db[li[num]]:
                be.add(( li[num], li[num+3])) 
            if li[num] in db[li[num+4]] and li[num+4] in db[li[num]]:
                be.add(( li[num], li[num+4])) 
            if li[0] in db[li[num+1]] and li[num+1] in db[li[0]]:
                be.add(( li[0], li[num+1])) 
            
        
        num+=1
    return be
    
        




def initiators (db : {str:{str:[int]}}) -> [str]:
    return [i for i in sorted(sorted(db), key=lambda t:len(db[t]), reverse=True) ]



def matrix (db : {str:{str:[int]}}) -> [[int]]:
    pass





if __name__ == '__main__':
    import prompt
    # checks whether answer is correct, printing appropriate information
    # Note that dict/defaultdict will compare == if they have the same keys and
    #   associated values, regardless of the fact that they print differently
    def check (answer, correct):
        if (answer   == correct):
            print ('    CORRECT')
        else:
            print ('    INCORRECT')
            print ('      was       =',answer)
            print ('      should be =',correct)
        print()
 
 
    def lol(alol):
        return '\n        '+'\n        '.join(','.join(f'{col:3}' for col in line) for line in alol)
    
    if prompt.for_bool('Test all_parties?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = all_parties(db1)
        print('  answer   =', answer)
        check(answer, {'Barb', 'Deja', 'Carl', 'Elan', 'Alan'})

        db1a = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
                'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
                'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]}
                }
        print('  argument =', db1a)
        answer = all_parties(db1a)
        print('  answer   =', answer)
        check(answer, {'Barb', 'Deja', 'Carl', 'Elan', 'Alan'})

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = all_parties(db2)
        print('  answer   =', answer)
        check(answer, {'Hope', 'Barb', 'Elan', 'Carl', 'Alan', 'Gary', 'Deja', 'Fern'})



    if prompt.for_bool('Test read_db?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument = db1.txt')
        answer = read_db(open('db1.txt'))
        print('  answer   =', answer)
        check(answer, db1)

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument = db2.txt')
        answer = read_db(open('db2.txt'))
        print('  answer   =', answer)
        check(answer, db2)


    
    if prompt.for_bool('Test talker_frequency?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = talker_frequency(db1)
        print('  answer   =', answer)
        check(answer, [('Alan', 8), ('Carl', 8), ('Barb', 7), ('Deja', 5), ('Elan', 4)])

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = talker_frequency(db2)
        print('  answer   =', answer)
        check(answer, [('Carl', 15), ('Alan', 14), ('Fern', 14), ('Gary', 14), ('Hope', 13), ('Deja', 12), ('Barb', 10), ('Elan', 8)])


 
    if prompt.for_bool('Test mutual_callers?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = mutual_callers(db1)
        print('  answer   =', answer)
        check(answer, {('Alan', 'Carl'), ('Carl', 'Elan'), ('Alan', 'Barb')})

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = mutual_callers(db2)
        print('  answer   =', answer)
        check(answer, {('Elan', 'Fern'), ('Carl', 'Gary'), ('Alan', 'Hope'), ('Deja', 'Elan'), ('Alan', 'Barb'), ('Barb', 'Gary'), ('Elan', 'Hope'), ('Alan', 'Gary')})



    if prompt.for_bool('Test initiators?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = initiators(db1)
        print('  answer   =', answer)
        check(answer, ['Barb', 'Carl', 'Alan', 'Elan', 'Deja'])

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = initiators(db2)
        print('  answer   =', answer)
        check(answer, ['Deja', 'Carl', 'Hope', 'Gary', 'Fern', 'Elan', 'Alan', 'Barb'])

    
  
    if prompt.for_bool('Test matrix?', True):  
        db1 = {'Alan': {'Barb': [10, 20], 'Carl': [10, 10]},
               'Barb': {'Alan': [10, 10], 'Deja': [5, 5, 5]},
               'Carl': {'Alan': [10, 5],  'Deja': [15],       'Elan': [5, 5]},
               'Deja': {'Elan': [5]},
               'Elan': {'Carl': [10]}
               }
        print('  argument =', db1)
        answer = matrix(db1)
        print('  answer   =', answer)
        check(lol(answer), lol([[0, 50, 35, 0, 0], [50, 0, 0, 15, 0], [35, 0, 0, 15, 20], [0, 15, 15, 0, 5], [0, 0, 20, 5, 0]]))

        db2 = {
                'Gary': {'Barb': [1], 'Carl': [19, 12, 2], 'Hope': [8], 'Alan': [25, 26]},
                'Carl': {'Hope': [10], 'Gary': [11, 8], 'Deja': [12], 'Alan': [15, 11, 4], 'Barb': [34]},
                'Elan': {'Fern': [16], 'Deja': [6, 27], 'Carl': [3], 'Hope': [29]},
                'Barb': {'Gary': [14], 'Alan': [14], 'Fern': [4]},
                'Deja': {'Gary': [30, 26], 'Barb': [25, 3], 'Fern': [10, 3, 27], 'Hope': [4], 'Elan': [5]},
                'Alan': {'Barb': [3, 15], 'Hope': [2, 46], 'Gary': [36]},
                'Fern': {'Alan': [7], 'Carl': [37, 46, 43], 'Elan': [5], 'Gary': [7]},
                'Hope': {'Elan': [15],'Fern': [9, 2, 36], 'Alan': [6, 16], 'Barb': [29]}
                }
        print('  argument =', db2)
        answer = matrix(db2)
        print('  answer   =', answer)
        check(lol(answer),lol([[0, 32, 30, 0, 0, 7, 87, 70], [32, 0, 34, 28, 0, 4, 15, 29], [30, 34, 0, 12, 3, 126, 52, 10], [0, 28, 12, 0, 38, 40, 56, 4], [0, 0, 3, 38, 0, 21, 0, 44], [7, 4, 126, 40, 21, 0, 7, 47], [87, 15, 52, 56, 0, 7, 0, 8], [70, 29, 10, 4, 44, 47, 8, 0]]))

