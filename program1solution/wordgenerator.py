import goody
from goody import irange
import prompt
from random import choice
#from collections import defaultdict

# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
                yield item
                
def read_corpus(os : int, file : open) -> {(str):[str]}:
                    
    corpus = dict() # defaultdict(list)
    file = word_at_a_time(file)
    key =[next(file) for _i in irange(os)]
    for w in file:
        if tuple(key) not in corpus or w not in corpus[tuple(key)]: # w not in corpus[tuple(key)]:
            corpus.setdefault(tuple(key),list()).append(w)
        key.pop(0)
        key.append(w)
    return corpus


def corpus_as_str(corpus : {(str):[str]}) -> str:
#     answer = ''
#     for k,v in sorted(corpus):
#         answer += '  '+str(k)+' can be followed by any of '+str(v)+'\n'
    answer= '\n'.join('  '+str(k)+' can be followed by any of '+str(v) for k,v in sorted(corpus.items()))+'\n'
    mins = min(len(v) for v in corpus.values())
    maxs = max(len(v) for v in corpus.values()) 
    return answer+'max/min list lengths = '+str(maxs)+'/'+str(mins)+'\n'


def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]:
    os,start = len(start),list(start)
    for _word_count in irange(count):
        key = tuple(start[-os:])
        if key not in corpus:
            start.append(None)
            return start
        start.append(choice(corpus[key]))
    return start    


def check(corpus,os,random):
    return all(random[i]==None or random[i] in corpus[tuple(random[i-os:i])] for i in range(os,len(random)))




        
if __name__ == '__main__':
    os = prompt.for_int('Enter order statistic',is_legal=lambda x : x >= 1)
    corpus = read_corpus(os, goody.safe_open('Enter file to process', 'r', 'Cannot find that file'))
    print('Corpus\n'+corpus_as_str(corpus))
      
    print('Enter '+str(os)+' words to start with')
    start = [prompt.for_string('Enter word '+str(i)) for i in irange(os)]
    how_many = prompt.for_int('Enter # of words to generate',is_legal=lambda x : x > 0)
    print('Random text =',produce_text(corpus,start,how_many))
         
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()