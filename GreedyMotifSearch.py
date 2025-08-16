from count_motifs import Profile, Score

from ProfileMostProbableKmer import ProfileMostProbableKmer
dna = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']


# Profile(dna)

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


print(GreedyMotifSearch(dna, 3,5))