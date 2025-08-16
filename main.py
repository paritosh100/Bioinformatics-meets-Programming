import matplotlib.pyplot as plt
string = 'GATACACTTCCCGAGTAGGTACTG'

def minimumSkew(genome):
    skew_array = SkewArray(genome)
    min_val = min(skew_array)
    return [i for i,v in enumerate(skew_array) if v == min_val]

def SkewArray(Genome):
    skew_array = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'G':
            skew_array.append(skew_array[i] + 1)
        elif Genome[i] == 'C':
            skew_array.append(skew_array[i] - 1)
        else:
            skew_array.append(skew_array[i])
    return skew_array

# minSkew = minimumSkew(string)
#
# print(minSkew)
# plt.plot(skew_array)
# plt.show()
x=0
for y in range(0,5):
    x+=y
print(x)