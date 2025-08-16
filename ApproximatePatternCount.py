Pattern = 'GAGG'
Text = 'TTTAGAGCCTTCAGAGG'
d = 2
def HammingDistance(p,q):
    hd = 0
    if len(p) != len(q):
        return("Lengths dont match")
    for i in range(len(p)):
        if p[i] != q[i]:
            hd +=1
    return hd

def ApproximatePatternCount(Text, Pattern, d):
    positions = []
    pl = len(Pattern)
    tl = len(Text)
    for i in range(tl - pl+1):
        substring = Text[i:i+pl]
        if HammingDistance(Pattern, substring) <= d:
            positions.append(i)
    return len(positions)

print(ApproximatePatternCount(Text,Pattern,d))

print(8.7//4)