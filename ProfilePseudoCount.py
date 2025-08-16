Motifs = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    # your code here
    count = CountWithPseudocounts(Motifs)

    for base in 'ACGT':
        profile[base] = [count[base][i] / (t + 4) for i in range(k)]
    return profile

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

print(ProfileWithPseudocounts(Motifs))