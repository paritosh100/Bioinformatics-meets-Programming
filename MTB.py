
Dna = {'A':[  0.4 , 0.3,  0.0,  0.1,  0.0,  0.9],
      'C':  [0.2,  0.3,  0.0,  0.4,  0.0,  0.1],
      'G':  [0.1,  0.3,  1.0,  0.1,  0.5,  0.0],
      'T':  [0.3,  0.1,  0.0,  0.4,  0.5,  0.0]}
t = len(Dna)

def Pr(Text, Profile):
    p = 1
    for i,nuc in enumerate(Text):
        if Profile[nuc][i] == 0:
            return 0
        p *= Profile[nuc][i]
    return p
def Count(motifs):
    count = {}
    for i in 'ACGT':
        count[i] = []
        for j in range(len(motifs)):
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
def ProfileMostProbableKmer(text, k, profile):
    text = text.upper()
    if k > len(text):
        return ""
    best = text[:k]
    best_score = Pr(best, profile)
    for i in range(1, len(text) - k + 1):
        pat = text[i:i + k]
        score = Pr(pat, profile)
        if score > best_score:
            best, best_score = pat, score
    return best
def GreedyMotifSearch(Dna, k, t):
    bestMotif = []
    for i in range(t):
        bestMotif.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1,t):
            p = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j],k,p))
        if Score(Motifs) < Score(bestMotif):
            bestMotif = Motifs
    return bestMotif


print(Pro(Dna))
