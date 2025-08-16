
motifs = [
    "GTACAACTGT",
    "CAACTATGAA",
    "TCCTACAGGA",
    "AAGCAAGGGT",
    "GCGTACGACC",
    "TCGTCAGCGT",
    "AACAAGGTCA",
    "CTCAGGCGTC",
    "GGATCCAGGT",
    "GGCAAGTACC"
]
profile = {
    "A": [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    "C": [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    "G": [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    "T": [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
}
def Count(motifs):
    count = {}
    for i in 'ACGT':
        count[i] = []
        for j in range(len(motifs[0])):
            count[i].append(0)
    t = len(motifs)
    for i in range(t):
        for j in range(len(motifs[0])):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    profile = Count(Motifs)
    for n in profile.keys():
        for i in range(len(profile[n])):
            profile[n][i] /= len(Motifs)
    return profile



def Consensus(Motifs):
    k = len(Motifs)
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Score(Motifs):
    consensus = Consensus(Motifs)
    score = 0
    for i in range(len(consensus)):
        for j in range(len(Motifs)):
            if Motifs[j][i] != consensus[i]:
                score +=1
    return score
def consensus_from_profile(profile, order="ACGT"):
    k = len(next(iter(profile.values())))
    cons = []
    for j in range(k):
        # pick nucleotide with max probability; break ties by order
        best = max(order, key=lambda nt: (profile[nt][j], -order.index(nt)))
        cons.append(best)
    return "".join(cons)

def Pr(Text, Profile):
    p = 1
    for i,nuc in enumerate(Text):
        if Profile[nuc][i] == 0:
            return 0
        p *= Profile[nuc][i]
    return p


print(Pr('AAGTTC',profile))