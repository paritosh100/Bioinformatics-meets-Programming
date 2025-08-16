Profile = {'A': [0.2, 0.2, 0.3, 0.2, 0.3], 'C': [0.4, 0.3, 0.1, 0.5, 0.1], 'G': [0.3, 0.3, 0.5, 0.2, 0.4], 'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
def Pr(Text, Profile):
    p = 1
    for i,nuc in enumerate(Text):
        if Profile[nuc][i] == 0:
            return 0
        p *= Profile[nuc][i]
    return p

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

print(ProfileMostProbableKmer(text, 5,Profile))