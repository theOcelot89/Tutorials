# DNA toolkit file
import collections
from utils import *
from structures import *

Counter = collections.Counter

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nucleotide in tmpseq:
        if nucleotide not in Nucleotides:
            return False
    return colored(tmpseq)

def countNucFrequency(seq):
    frequencyDict = {"A": 0, "C": 0, "T": 0, "G": 0}
    for nucleotide in seq:
        frequencyDict[nucleotide] += 1
    return frequencyDict

def countNucFrequenceWithCollections(seq):
    return dict(collections.Counter(seq))

def transcription(seq):
    """ Takes a DNA sequence and replace Thymine with Uracil."""
    RNA = seq.replace('T', 'U')
    return RNA

# returns reverse complementary DNA string
def reverse_compliment(seq):
    """Produces a reversed complementary DNA string 5' to 3'."""

    # DNA_reversed_complimentary = ''.join([DNA_Reversecomplement[nuc] for nuc in seq])[::-1]
    # return colored(DNA_reversed_complimentary)

    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]

def gc_content(seq):        

    gc_content = round((seq.count("C") + seq.count("G")) / len(seq) * 100)
    return gc_content

def gc_content_per_section(seq, k = 20):
    res = []
    for i in range(0, len(seq)
                    + 1 - k, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res   

def translate_seq(seq, init_pos=0):
    amino_acid_seq = [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2,3)]
    return amino_acid_seq

def codon_usage(seq, aminoAcid):
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoAcid:
            tmpList.append(seq[i:i+3])
    
    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)

    return freqDict , totalWight

def gen_reading_frames(seq):
    frames = {}
    # for original strand first (3 ORFs)
    for start_pos in range(3):
        frames[colored('  '.join(seq[i:i+3] for i in range(start_pos, len(seq),3)))] = translate_seq(seq, start_pos)

    # for reversed complementary after (3 ORFs)
    reversed = reverse_compliment(seq)
    for start_pos in range(3):
        frames[colored('  '.join(reversed[i:i+3] for i in range(start_pos, len(reversed),3)))] = translate_seq(reversed, start_pos)


    return frames

def scan_reading_frames(amino_acid_seq):
    current_protein = []
    proteins = []

    for amino in amino_acid_seq:
        if amino == "_":
            if current_protein :
                for amino in current_protein:
                    proteins.append(amino)
                current_protein = []
        else:
            if amino == "M":
                current_protein.append('')
            for i in range(len(current_protein)):
                current_protein[i] += amino
    return proteins

def complete_scan(seq, startPos=0, endPos=0, ordered=False):
    total_proteins = []

    # check for specific position in DNA if specified
    if endPos > startPos:
        rfs = gen_reading_frames(seq[startPos : endPos])
    else:
        rfs = gen_reading_frames(seq)

    # find all proteins in all the refs
    for i, item in enumerate(rfs.items()):
        codons = item[0]
        aminos = item[1]
        print(i+1, codons, "\n", aminos)
        proteins = scan_reading_frames(aminos)
        print("Found proteins:", proteins, "\n")
        [total_proteins.append(protein) for protein in proteins]
    
    # sort if specified
    if ordered:
        total_proteins = sorted(total_proteins, key=len, reverse=True)


    return total_proteins









