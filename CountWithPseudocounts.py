Motifs = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]

def Count(motifs):
    from collections import defaultdict
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
            if motifs[i][j] == 0:
                motifs[i][j] = 1
    return count

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    counts = {'A': [1] * k, 'C': [1] * k, 'G': [1] * k, 'T': [1] * k}

    # Iterate through each position in the motifs
    for i in range(k):
        for motif in Motifs:
            counts[motif[i]][i] += 1

    return counts

print(CountWithPseudocounts(Motifs))