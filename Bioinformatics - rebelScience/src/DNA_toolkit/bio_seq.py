from bio_structs import *
from utils import *
import random
from collections import Counter

class bio_seq:
    """A sequence class for DNA, RNA & Proteins"""

    def __init__(self, seq="ATGC", seq_type="DNA", label="No Label") -> None:
        """Sequence initialization & validation"""

        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f'Provided data does not seem to be a correct {self.seq_type} sequence -> {self.seq}'

    def __validate(self):

        # tmpseq = self.seq.upper()
        # for nucleotide in tmpseq:
        #     if nucleotide not in Nucleotides:
        #         print("Not valid DNA strand")
        #         return False
        tmpseq = set(NUCLEOTIDE_BASE[self.seq_type]).issuperset(self.seq)
            
        return tmpseq
    
    def get_seq_type(self):
        return self.seq_type

    def get_seq_info(self):
        """Renders seq information"""
        return f"[Label]: {self.label}\n[Sequence]: {colored(self.seq)}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"

    def generate_random_sequence(self, length=10, seq_type="DNA", label="Random generated strand"):
        # print("gen fun", seq_type)
        # print("gen fun", self.seq_type)
        seq = "".join(random.choice(NUCLEOTIDE_BASE[seq_type]) for x in range(length))
        self.__init__(seq, seq_type, label)
    
    def get_countNucFrequency(self):
        # frequencyDict = {"A": 0, "C": 0, "T": 0, "G": 0}
        # for nucleotide in self.seq:
        #     frequencyDict[nucleotide] += 1
        # return frequencyDict

        # pythonic way
        return dict(Counter(self.seq))

    def transcription(self):
        """ Takes a DNA sequence and replace Thymine with Uracil."""
        if self.seq_type == "DNA":
            RNA = self.seq.replace('T', 'U')
            return RNA
        elif self.seq_type == "RNA":
            return print("Transcription error: Not a DNA sequence")

    
    def reverse_compliment(self):
        """Produces a reversed complementary DNA string 5' to 3'."""

        # DNA_reversed_complimentary = ''.join([DNA_Reversecomplement[nuc] for nuc in seq])[::-1]
        # return colored(DNA_reversed_complimentary)

        #pythonic way
        if self.seq_type == "DNA":
            mapping = str.maketrans("ATCG", "TAGC")
            return self.seq.translate(mapping)[::-1]
        elif self.seq_type == "RNA":
            mapping = str.maketrans("AUCG", "UAGC")
            return self.seq.translate(mapping)[::-1]    

    
    def gc_content(self):        

        gc_content = round((self.seq.count("C") + self.seq.count("G")) / len(self.seq) * 100)
        return gc_content
    
    def gc_content_per_section(self, k = 10):


        res = []
        for i in range(0, len(self.seq) + 1 - k, k):

            subseq = self.seq[i:i+k]
            res.append(round((subseq.count("C") + subseq.count("G")) / len(subseq) * 100))

        return res   
    
    def translate_seq(self, init_pos=0):

        if self.seq_type == "DNA":
            amino_acid_seq = [DNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2,3)]
            return amino_acid_seq
        elif self.seq_type == "RNA":
            amino_acid_seq = [RNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2,3)]
            return amino_acid_seq

    def codon_usage(self, aminoAcid):

        tmpList = []
        if self.seq_type == "DNA":
            for i in range(0, len(self.seq) - 2, 3):
                if DNA_Codons[self.seq[i:i+3]] == aminoAcid:
                    tmpList.append(self.seq[i:i+3])

        if self.seq_type == "RNA":
            for i in range(0, len(self.seq) - 2, 3):
                if RNA_Codons[self.seq[i:i+3]] == aminoAcid:
                    tmpList.append(self.seq[i:i+3])
                
        freqDict = dict(Counter(tmpList))
        totalWight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWight, 2)

        return freqDict , totalWight
    
    def gen_reading_frames(self):
        frames = {}
        # for original strand first (3 ORFs)
        for start_pos in range(3):
            frames[colored('  '.join(self.seq[i:i+3] for i in range(start_pos, len(self.seq),3)))] = self.translate_seq( start_pos)


        tmp_seq = bio_seq(self.reverse_compliment(), self.seq_type)
        # for reversed complementary after (3 ORFs)

        for start_pos in range(3):
            frames[colored('  '.join(tmp_seq.seq[i:i+3] for i in range(start_pos, len(tmp_seq.seq),3)))] = tmp_seq.translate_seq(start_pos)


        return frames

    def scan_reading_frames(self, amino_acid_seq):
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

    def complete_scan(self, startPos=0, endPos=0, ordered=False):
        total_proteins = []

        # check for specific position in DNA if specified
        if endPos > startPos:
            tmp_seq = bio_seq(self.seq[startPos : endPos], self.seq_type)
            rfs = tmp_seq.gen_reading_frames()
        else:
            tmp_seq = bio_seq(self.seq, self.seq_type)
            rfs = tmp_seq.gen_reading_frames()

        # find all proteins in all the refs
        for i, item in enumerate(rfs.items()):
            codons = item[0]
            aminos = item[1]
            print(i+1, codons, "\n", aminos)
            proteins = self.scan_reading_frames(aminos)
            print("Found proteins:", proteins, "\n")
            [total_proteins.append(protein) for protein in proteins]
        
        # sort if specified
        if ordered:
            total_proteins = sorted(total_proteins, key=len, reverse=True)


        return total_proteins


