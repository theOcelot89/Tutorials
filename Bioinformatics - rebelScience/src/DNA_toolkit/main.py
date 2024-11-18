from DNAToolkit import *
from utils import *
import random


# create random DNA string
randomDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(100)])
randomDNAStr = NM_000207_3  

# print(validateSeq(randomDNAStr))
# print(countNucFrequency(randomDNAStr))
# print("with collections module", countNucFrequenceWithCollections(randomDNAStr))

# Transcription Production
print("\n")
print(bold + "DNA Transcription" + end )
print("DNA:", validateSeq(randomDNAStr))
print("RNA:", colored(transcription(randomDNAStr)))
print("DNA elements", countNucFrequenceWithCollections(randomDNAStr))
print("RNA elements", countNucFrequenceWithCollections(transcription(randomDNAStr)))
print("\n")

# DNA reverse complimentary production
print(bold + "DNA Reversed complementary strand" + end)
print(f"DNA: 5' {validateSeq(randomDNAStr)} 3'")
print(f"        {''.join(['|' for i in range(len(randomDNAStr))])}")
print(f"COM: 3' {colored(reverse_compliment(randomDNAStr)[::-1])} 5")
print(f"RCO: 5' {colored(reverse_compliment(randomDNAStr))} 3'" )
print("\n")

# DNA strand GC content in %
print(bold + "GC Content" + end)
print("DNA:", validateSeq(randomDNAStr))
print(f"GC content: {gc_content(randomDNAStr)}%")
print("\n")

# DNA strand GC Content per subsection
frame = 5
print(bold + "GC Content per Section" + end)
print("DNA:", validateSeq(randomDNAStr))
print(f"GC content per {frame} nucleotides: {gc_content_per_section(randomDNAStr, frame)}")
print("\n")

# Amino acids based on DNA sequence
print(bold + "Amino acids based on DNA sequence" + end)
print("DNA:", validateSeq(randomDNAStr))
print("DNA in codons:", colored(' '.join(randomDNAStr[i:i+3] for i in range(0, len(randomDNAStr),3))))
print("Amino Acids:", translate_seq(randomDNAStr))
print("DNA strand length:", len(randomDNAStr))
print("Number of last bases not translated:" , len(randomDNAStr)%3)
print("\n")

# Amino acids percentage
amino_acid_to_search = "_" 
print(bold + "Specific amino acid content" + end)
print("DNA:", validateSeq(randomDNAStr))
print("Amino in interest:", amino_acid_to_search)
results = codon_usage(randomDNAStr, amino_acid_to_search)
print("Total aminos found:", results[1] )
print("frequency of different codons:", results[0])
print("\n")

# ORFs
print(bold + "ORFs for a DNA strand & its complementary " + end)
print("DNA:", validateSeq(randomDNAStr))
print(f"RCO: {colored(reverse_compliment(randomDNAStr))}" )
print('\n')
for i, items in enumerate(gen_reading_frames(randomDNAStr).items()):
    print(i+1, items[0], "\n", items[1], "\n")
print('\n')


# Scan ORF for protein
print(bold + "Scanning ORF for proteins.. " + end)
print("DNA:", validateSeq(randomDNAStr))
items = gen_reading_frames(randomDNAStr).items()
DNAOrf = list(items)[0][0]
orf = list(items)[0][1]
print("DNA codons:", DNAOrf)
print('Amino Acids:', orf)
print("Found proteins:", scan_reading_frames(orf))
print('\n')

# Scan all ORFs of a sequence for protein
print(bold + "Scanning all possible ORFs for proteins.. " + end)
print("DNA:", validateSeq(randomDNAStr), '\n')
total_proteins = complete_scan(randomDNAStr, 0,0, ordered=True)
print("Total proteins found in 6 ORFS:", len(total_proteins), total_proteins)
for protein in total_proteins:
    print(f'{protein}')
print('\n')


