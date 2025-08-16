import numpy as np
a = [0.2,0.2,0.6,0.2,0.1,0.7,0.9,0.1,0.9,0.1,0.9,0.1,0.1,0.4,0.5,0.1,0.1,0.8,0.1,0.2,0.7,0.3,0.4,0.3,0.6,0.4]
def entropyNFkb(a):
    entropy = 0
    for i in a:
        if i > 0:
            entropy += -i*(np.log2(i))
    return entropy

def profile_entropy(a):
    total_entropy = 0
    for i in range(len(profile['A'])):
        column = [profile[nuc][i] for nuc in 'ACGT']
        total_entropy += entropyNFkb(column)
    return total_entropy
# print(entropyNFkb(a))

profile = {
    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}

print(profile_entropy(profile))