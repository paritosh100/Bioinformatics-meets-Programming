dna_seq = ["atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccg",
           "acccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataaaaaaaaaggggggga",
           "tgagtatccctgggatgacttaaaaaaaagggggggtgctctcccgatttttgaatatgtaggatcattcgccagggtccga",
           "gctgagaattggatgaaaaaaaagggggggtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggaga",
           "tcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaataaaaaaaagggggggcttatag",
           "gtcaatcatgttcttgtgaatggatttaaaaaaaaggggggggaccgcttggcgcacccaaattcagtgtgggcgagcgcaa",
           "cggttttggcccttgttagaggcccccgtaaaaaaaagggggggcaattatgagagagctaatctatcgcgtgcgtgttcat",
           "aacttgagttaaaaaaaagggggggctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgta",
           "ttggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcataaaaaaaagggggggaccgaaagggaag",
           "ctggtgagcaacgacagattcttacgtgcattagctcgcttccggggatctaatagcacgaagcttaaaaaaaaggggggga" ]

combined_dna = ''.join(dna_seq)


def FrequencyMap(Text, k):
 freq = {}
 n = len(Text)
 for i in range(n - k + 1):
  Pattern = Text[i:i + k]
  freq[Pattern] = 0
 for i in range(n - k + 1):
  Pattern = Text[i:i + k]
  freq[Pattern] += 1
 return freq


def FrequentWords(Text, k):
 words = []
 freq = FrequencyMap(Text, k)
 m = max(freq.values())
 for key, value in freq.items():
  if value == m:
   words.append(key)
 return words

most_freq_15mer = FrequentWords(combined_dna, 15)
print(most_freq_15mer)