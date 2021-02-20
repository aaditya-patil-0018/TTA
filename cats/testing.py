from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime

'''def choose(paragraphs, select, k):
    valid_para = []
    for para in paragraphs:
        if select(para) == True:
            valid_para.append(para)
    length = len(valid_para) - 1
    if k > length:
        return ''
    else:
        return valid_para[k]
ps = ['hi', 'how are you', 'fine']
s = lambda p: len(p) <= 4
print(choose(ps, s, 2))'''

'''li = ['apple banana', 'apple noone', 'banana cat', 'elephant ant']
li2 = ['banana', 'apple']
for i in li:
    for n in li2:
        #print(n)
        if n in i:
            print(i)
        else:
            print(0)
'''

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    #print(len(typed_words))
    reference_words = split(reference)
    #print(len(reference_words))
    #if len(typed_words) != len(reference_words):
        #print(0.0)
        #return 0.0
    '''if not typed_words:
        print('This is not typed words',0.0)
        return 0.0
    else:
        match_count, k = 0, 0
        print('this is range ', range(min(len(reference_words), len(typed_words))))
        print('This is range without min ', range(len(reference_words), len(typed_words)))
        for k in range(min(len(reference_words), len(typed_words))):
            if typed_words[k] == reference_words[k]:
                match_count += 1
            k += 1
        print(match_count / len(typed_words) * 100)
        return match_count / len(typed_words) * 100'''
    if len(typed_words) == 0 and len(reference_words) != 0:
        print('This is condition 1 ',0.0)
        return 0.0
    elif len(typed_words) == 0 and len(reference_words) == 0:
        print('This is condition 2 ',100.0)
        return 100.0
    else:
        count = 0
        for word in typed_words:
            index_of_word = typed_words.index(word)
            if len(reference_words) != index_of_word:
                if reference_words[index_of_word] == word:
                    count += 1
                else:
                    count += 0
            else:
                answer = count / len(typed_words) * 100
                print(answer)
                return answer
        answer = count / len(typed_words) * 100
        print(answer)
        return answer

accuracy('Cute Dog!', 'Cute Dog.')
accuracy('A Cute Dog!', 'Cute Dog.')
accuracy('cute Dog.', 'Cute Dog.')
accuracy('Cute Dog. I say!', 'Cute Dog.')
accuracy('Cute', 'Cute Dog.')
accuracy('', 'Cute Dog.')
accuracy('', '')
accuracy("a b c d", " a d ")
accuracy(" a b \tc" , "a b c")