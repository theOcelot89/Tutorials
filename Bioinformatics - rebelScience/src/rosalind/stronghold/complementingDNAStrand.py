DNA_Reversecomplement = {"A" : "T", "T" : "A", "G" : "C", "C": "G"}

def reverse_compliment(seq):
    """Produces a reversed complementary DNA string 5' to 3'."""
    DNA_reversed_complimentary = ''.join([DNA_Reversecomplement[nuc] for nuc in seq])[::-1]
    return (DNA_reversed_complimentary)

print(reverse_compliment("GTTTTTTCATACGATCACCCTCTGAGAATAGGAGCACTCGTTCCATCGGCCCACAGATCCCTGTTCCAAAGTCTTCAGCGCTCATAGTTGACTATCAAGGGATCGAGTCTCGAGGGACGTATTGACGGGCGTCCGAGTCAGGGACTGATAAGCATTCGCTTTTCCATTGTACATTACATAAAGCGTCCTATTTTTAGTCTTCAGAAGGGCCCTCAAGAGTTCCCCCAATCTTACGGCATCTAAATAGAGAAAATCAAGCCAATATGTGCCCTAACAACGTTGGGCTGTCGGCAGTGACTTACCGAGTCGCTGTCCGCCTTTGCCATGATTCATAACTCTCGACGTCATATACAATTAGTCCTTTACCTCTAAAGTGGCTCACTATCCTTTCCACAGCGAGTGTACCCGTCCCGCAGTGAATGCTTAGGGCCCTTTGGGGCTATGGCGCGACACCCACACGGCTGAAACGTGCTCTTCAAATTGCGTCATTGCACTAAACAGAAATGGTTGATTCGCTAGAGGGGTCAGTCTGACTCAAGATTAGTACGTATTAAAAATAATATCACTTGTCTGAGCCGGGCTCAGGGTAGTTCACAATTTGGCCAACGGCAACCGCCCAATACCTATTGAGTCTGGTGGTTTGGGCCCACGTACTAAATACCAGGGCAATAACCGAGATTTTTTTAACATCGATGGTGCTACCGTTTTCTCGAGTTTATAGCCATACGTCTTAGGCTGATATCGTGCCTCGTACTTGAACAAAACTTGCTGCACTACTGGAAAACAACTCTGGTGGGCATGTATCTTACTCCTCCGGCCGCAGGTAACAGATTTGTGGATCGAGTTCGAAAGGCGCATCATGGGGTCTTACTCTAGTCAGATAAATCGCTGTCGTGAGCTTACAAGCGCCCGGAGACAGGCAGCGATACTCACCCGCGAACCCCAGCGACAGAATT"))
