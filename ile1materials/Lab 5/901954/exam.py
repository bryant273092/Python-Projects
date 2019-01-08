from collections import defaultdict   # If you choose to use defaultdict  

# You might use these abbreviations in your code
# c  : caller
# r  : receiver
# t  : time
# ts : list of times


def all_parties(db : {str:{str:[int]}}) -> {str}:
    
    result =[]
    for c,r in db.items():
        for x in r:
            result.append(c)
            result.append(x) 
       
    return set(result)



def read_db(file : open) -> {str:{str:[int]}}:
    
    a = file.readlines()
    b = [x.rstrip('\n').split(':') for x in a]
    Set = set()
    for x in b:
        Set.add(x[0])
    
    result = {c:{} for c in Set}
    
    for x in result:
        for y in b:
            if x == y[0]:
                result[x].update({y[1]:[]})
    
    for x in result:
        for y in b:
            if x == y[0]:
                result[x][y[1]].extend([int(num) for num in y[2:]])
    
    return result
                



def talker_frequency (db : {str:{str:[int]}}) -> [(str,int)]:

    result =[]
    
    for c,r in db.items():
        for x in r:
            result.append(c)
            result.append(x) 
       
    result2 ={c:0 for c in set(result)}
    
    for x in result2:
        for c,r in db.items():
            if x == c:
                for rs in r:
                    result2[x] += len(r[rs])
            if x in r:
                result2[x] += len(r[x])
    
    result3 = [(c,t) for c,t in result2.items()]
    
    return sorted(result3, key = lambda x:(-x[1],x[0]))
        



def mutual_callers (db : {str:{str:[int]}}) -> {(str,str)}:
    
    a = []
    
    for c,r in db.items():
        for c1,r1 in db.items():
            if c in r1:
                if c1 in r:
                    a.append((c,c1))
    
    for c in a:
        for c2 in a:
            if c[0] == c2[1] and c[1] == c2[0]:
                a.remove(c2)
    
    result = [tuple(sorted(list(c))) for c in set(a)]        
    
    return set(result)



def initiators (db : {str:{str:[int]}}) -> [str]:
    
    a = {c:[0,0] for c in db}
    
    for c,r in db.items():
        for rs in r:
            a[c][0] += len(r[rs])
    
    for x in a:
        for c,r in db.items():
            if x in r:
                a[x][1] += len(r[x])
    b= [(c,t[0],t[1]) for c,t in a.items()]
    b.sort(key = lambda x:(-x[1],x[2]))   
    result = [x[0] for x in b]
    return result




def matrix (db : {str:{str:[int]}}) -> [[int]]:
    
    a = []
    
    for c,r in db.items():
        b = []
        for c1,r1 in db.items():
            num = 0
            if c in r1:
                for num1 in r1[c]:
                    num+=num1 
                b.append(num)
            elif c1 in r:
                for num1 in r[c1]:
                    num+=num1   
                b.append(num)   
            else:
                b.append(0)
        a.append(b)
    

    
    
    return a




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

