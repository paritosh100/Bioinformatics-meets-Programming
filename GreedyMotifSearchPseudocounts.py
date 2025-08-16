
from ProfilePseudoCount import ProfileWithPseudocounts, CountWithPseudocounts
dna = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']


def Score(Motifs):
    consensus = Consensus(Motifs)
    k = len(consensus)
    t = len(Motifs)
    score = 0

    for j in range(k):
        for i in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1

    return score


def Count(Motifs):
    count = {}
    k = len(Motifs[0])

    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count


def Profile(Motifs):
    count = Count(Motifs)
    profile = {}

    k = len(Motifs[0])
    t = len(Motifs)

    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(count[symbol][j] / t)

    return profile


def Consensus(Motifs):
    profile = Profile(Motifs)
    consensus = ""

    k = len(Motifs[0])
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if profile[symbol][j] > m:
                m = profile[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol

    return consensus


def CountWithPseudocounts(Motifs):
    count = {symbol: [1] * len(Motifs[0]) for symbol in "ACGT"}
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4
    count = CountWithPseudocounts(Motifs)
    profile = {symbol: [float(c) / t for c in count[symbol]] for symbol in "ACGT"}
    return profile


def ScoreWithPseudocounts(Motifs):
    count = CountWithPseudocounts(Motifs)
    score = 0
    for j in range(len(Motifs[0])):
        max_count = max(count[symbol][j] for symbol in "ACGT")
        score += sum(count[symbol][j] for symbol in "ACGT") - max_count
    return score


def ProfileMostProbablePattern(Text, k, profile):
    max_prob = -1
    most_probable = ""
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i + k]
        prob = 1
        for j in range(k):
            prob *= profile[pattern[j]][j]
        if prob > max_prob:
            max_prob = prob
            most_probable = pattern
    return most_probable


def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [string[:k] for string in Dna]

    for i in range(len(Dna[0]) - k + 1):
        Motifs = [Dna[0][i:i + k]]

        for j in range(1, t):
            profile = ProfileWithPseudocounts(Motifs)
            motif = ProfileMostProbablePattern(Dna[j], k, profile)
            Motifs.append(motif)

        if ScoreWithPseudocounts(Motifs) < ScoreWithPseudocounts(BestMotifs):
            BestMotifs = Motifs

    return BestMotifs
print(GreedyMotifSearch(dna,3,5))