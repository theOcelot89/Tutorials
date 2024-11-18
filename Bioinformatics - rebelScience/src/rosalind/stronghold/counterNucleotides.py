def countNucFrequency(seq):
    frequencyDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in seq:
        frequencyDict[nucleotide] += 1
    return frequencyDict

DNAstring = "AAAGCGGACGGCTGAAAATCAAGACGATCTTTCTCTAGCTATCAGCGTCGGTATACACGATTCGGTCTAGCTCTAGTCTTTCCATAAAGCAGGAAAGCACGGGCACGAGATGTCGAGAGGTGTGACGGTCCAGTAACCGTGTCAGATGGGGTCTAGAACTAACCCGTGGAACGTCCGGTGCATGATACAGACTACCGCCTGGGAAAAAAGCACTTGTTCAGAGGGATGCATTCTTATGCGACTTTTGGACTTGACCTAGATTGATTCCGCGCCACTTCTCAAGAGTGGGAACGCCGGTCCTTGGAGCCGCCGGAGTAGTGCCGAGCAGTTAATTTGTTGCCCGGTAGAATTATGGATGAAACAGTAAAACAGTAGAAGGTATATTTGGCCGTACAACGAGCTCCAGGGAATCCGGATGCTGCCTGACTAACTACGGGCAATTATGAGACGTTACGGAAGTTCTCGCTATGCCAAAAGTGATACATGATTCCTTACACTCCTGGTAGCAAATGGAGATAGAAGTCAGCGTTAAGCGAACAATATCTCAGACAGTGTGAGCTCAAGAACGAGTCTATTTCCATTGGGCTCGTCAGTAGAAGGGGTGGACGAAGAGTTCTACGGGCGAACTGCGAGGGTGAGGCGTGTTAACTCGAGCATTGCCCAGCCCCCCTAATGTCGATCGATTCTCTAGGAGTACACAACCTGGCATGCGACTAGGCCTAAATAAATGGAGAGCCAGACTTATTCGGAATACTCAAGTACCCTCCAGGCGTTCTTTGCGATCGAGGGGACTGGCACCGTTTCCGTGGTGAAAGTTTTTCACACTATACGGCTCTTCTGA"
result = countNucFrequency(DNAstring)
result = ' '.join([str(val) for key, val in result.items()])
print(result)