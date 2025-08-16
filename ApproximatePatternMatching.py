Pattern = "ATTCTGGA"
Text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
d = 3

def HammingDistance(p,q):
    hd = 0
    if len(p) != len(q):
        return("Lengths dont match")
    for i in range(len(p)):
        if p[i] != q[i]:
            hd +=1
    return hd

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    pl = len(Pattern)
    tl = len(Text)
    for i in range(tl - pl+1):
        substring = Text[i:i+pl]
        if HammingDistance(Pattern, substring) <= d:
            positions.append(i)
    return positions

print(ApproximatePatternMatching(Text,Pattern,d))