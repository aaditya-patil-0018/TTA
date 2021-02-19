def choose(paragraphs, select, k):
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
print(choose(ps, s, 2))