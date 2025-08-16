p = 'CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT'
q = 'CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'


def HammingDistance(p,q):
    hd = 0
    if len(p) != len(q):
        return("Lengths dont match")
    for i in range(len(p)):
        if p[i] != q[i]:
            hd +=1
    return hd

print(HammingDistance(p,q))