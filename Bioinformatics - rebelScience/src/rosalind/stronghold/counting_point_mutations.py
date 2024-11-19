def hamming_distance(s1,s2):

    distance = 0 
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            distance += 1
    return distance

s1= "CATCTGTGCCGCGATCGTGGGTTGCCGTCCTACGCCCCGAGGATCCCCACTCGTTGCCGCGGTGACTTCAAAGATACCGTGAGAGCCTCTGGCGTTCTCGACGCGATCACCTACCTGATAAAGTTGCAAGATAATTGGTGACCACTTCTTGGAGCAAGCTCACTATATGAATCAGCGTGAGCAGAATTACTGGTACCATGAACTGCGCCAACCTCTAAGTATTACACCTAGCTTGCGGCCAACGCCTATTCAGCTTGAAGATGCACACATGCACAGCATCCCGCACGGAATGTCGCGCGAGTCCAACGAGATATGACTAATTGCTGTACTCGTGGGCCTTGTTCCCCTGTGTAGAATAGGCCGGCTCTTGACTTTACGCCGAAAAACCCGTAAATACGCCCTTTTGGCGAGCACGTGTCTGTCTCCAGACCCGCCTGATGGTGACGTGTAGATACTCCCCCACAAAAAGATACCGTGCGTTACGGATATTAGGGACGTTATCGTGAATGGAGGTCGTACTCGATTGCAATGAACATTAAGCACATACACCAGGTTCTCACGACAATACGCGCTGGGGCTCCCATTGTCACTACTCCCTGTGAAAGCCGTCGAGTTAATTTTAAATCTATACCCAATTAACGTCTGCAGTTGGTATCTATAGACGGCCCAGCGGTCTTTCTGCGGTCAGTGCCTGACATGTTGTAGTGGTAAAGCTTAGTTAAGGCTTATGAGCAGATGTGGGTTTCTGGTATGGGTGGTATTCGCAAGTTCTATTCGTGCGGCACTATCTCCAATCCCTTATGGTTCAAGTTCTGTCTCGCTGGGTGATGGCCTGTGAATACGCCATCGACTTGCATTAGCGCCGGAGGCGTTTTGGTATCGCGTCCTAGGACTACACCTCAGGGACATCTCCA"
s2= "CGGCCCTCTCGCGCTAGGGAGGTCTGAGCCAACACCCCGCTACCAGCCAGTGGTGGCGACCGGTTCCCCTATCATACCGAGGCCGTCTCCGAGCTGCACCACGCTAAAACTCCCGGCCTGTACCGGGAGGGCTATGGGGTGGCGCTCGTAGGAGCCAGCTATGTGGAATGATATGGTGAAGTAGGTTAGATGGAACTTTAGCATAACATAACCCATACGGATTATTCTTTGATTGCAGCCAATGATTCTTATCGATCTTGATGCACACTTCAGCAGCGTTCCAGTTGGGATAGATCGCTAGTAAATCGACATATGTAAGGATGGCTAAGTTCTGGTACATTTTCCACCCAAACGGATACAGAATTACGTCAATTCAGCCGGCCGAACGCTTAAATATGGCTACGAGCGGGGCATGGTCGTGATTCCAGAACCCGCGGAATAGGACGCTGAAATAATACCCGCGAGACATAAACCATCCGTGGCAGAAATTATCCCGGTTGTCAGTATGGGGAAAAGTGAGCGTACGTATCGAAGCGCTAAGATTAACTATTCCGACTCACTCCAACACGCGCTGCCCCGCCCACTATAGAGATTCCATCGCAAAACTTGTTAAGCACTGAGCAAAGTCTAGCCATTTCAGGATGACGATTGTTTCGTACAGACTGCCGTTTGGGCTTACTGCCGCTCCCGCCCGAGGTTCGCTTGGAGTTAGACTCAATTTCGTGATAAAAAACTATGTCTAGTGCGAATTTAGATGTATATTCCAACTTCCAGACGGGAGTCTCTATCGCTGAACCCTTCTGACGTAAGTCCCGATGTATGCGATCTTGCCCTGGATATACAGCGTCGGCTTGCAACCAGGTAGGAGTCGCTTAGGTTACCAGTTCTAGGATCATTATAGTCGGGGTTATCTA"

print(hamming_distance(s1,s2))