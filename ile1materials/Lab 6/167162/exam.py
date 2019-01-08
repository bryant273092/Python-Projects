from collections import defaultdict   # If you choose to use defaultdict  

# You might use these abbreviations in your code
# c  : caller
# r  : receiver
# t  : time
# ts : list of times


def all_parties(db : {str:{str:[int]}}) -> {str}:
    result=set()
    for key,value in db.items():
        if key not in result:
            result.add(key)
        for k,v in value.items():
            if k not in result:
                result.add(k)
    return result
            

def read_db(file : open) -> {str:{str:[int]}}:
    result=defaultdict(dict)
    for line in file.readlines():
        i=line.strip().split(':')
        if i[0] not in result:
            result.setdefault(i[0],{i[1]:[int(x) for x in i[2:]]})
        else:
            if i[1] not in result[i[0]]:
                result[i[0]].setdefault(i[1],[int(x) for x in i[2:]])
            else:
                result[i[0]][i[1]].extend([int(x) for x in i[2:]])
    return dict(result)
            

def talker_frequency (db : {str:{str:[int]}}) -> [(str,int)]:
    result=defaultdict(int)
    for key,value in db.items():
        key_number=0
        for x in db[key].values():
            key_number+=len(x)
        result[key]+=key_number
        for k,v in value.items():
                result[k]+=len(db[key][k])
    return sorted(sorted([(x,y) for x,y in result.items()]),key=lambda x:x[1], reverse=True)


def mutual_callers (db : {str:{str:[int]}}) -> {(str,str)}:
    result=set()
    match=[]
    for key,value in db.items():
        for k,v in value.items():
            match.append((key,k))
    for x in match:
        if (x[1],x[0]) in match:
            result.add(tuple(sorted(x)))
    return result

def initiators (db : {str:{str:[int]}}) -> [str]:
    count=defaultdict(list)
    for key,value in db.items():
        if key not in count:
            count[key]=[0,0]
        for x in db[key].values():
            count[key][0]+=len(x)
        for k,v in value.items():
            if k not in count:
                count[k]=[0,0]
            count[k][1]+=len(v)
    return [x[0] for x in sorted(sorted([(k,[v1,v2]) for k,[v1,v2] in count.items()],key=lambda x:x[1][1]),key=lambda x:x[1][0],reverse=True)]
    

def matrix (db : {str:{str:[int]}}) -> [[int]]:
    people=sorted(all_parties(db))
    result=[]
    match=defaultdict(int)
    match2=defaultdict(int)
    for key,value in db.items():
        for k,v in value.items():
            match[tuple(sorted([key,k]))]+=sum([x for x in v])
    for (x,y),z in match.items():
        if x not in match2:
            match2[x]={y:z}
        else:
            match2[x].update({y:z})
    return match2
    #for x in people:
        
        






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

