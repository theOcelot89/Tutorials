# for bold text
bold = '\033[1m'
end = '\033[0m'

def colored(seq):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[95m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""
    if not seq:
        return "Not seq found.."
    else:
        for nuc in seq:
            if nuc in bcolors:
                tmpStr += bcolors[nuc] + nuc
            else:
                tmpStr += bcolors['reset'] + nuc

        return tmpStr + '\033[0;0m'


    bcolors = {
        'A': '\033[91m',    # Alanine (A) - Red
        'C': '\033[92m',    # Cysteine (C) - Green
        'D': '\033[93m',    # Aspartic Acid (D) - Yellow
        'E': '\033[94m',    # Glutamic Acid (E) - Blue
        'F': '\033[95m',    # Phenylalanine (F) - Magenta
        'G': '\033[96m',    # Glycine (G) - Cyan
        'H': '\033[97m',    # Histidine (H) - White
        'I': '\033[90m',    # Isoleucine (I) - Bright Black
        'K': '\033[91m',    # Lysine (K) - Red (lighter)
        'L': '\033[92m',    # Leucine (L) - Green (lighter)
        'M': '\033[93m',    # Methionine (M) - Yellow (lighter)
        'N': '\033[94m',    # Asparagine (N) - Blue (lighter)
        'P': '\033[95m',    # Proline (P) - Magenta (lighter)
        'Q': '\033[96m',    # Glutamine (Q) - Cyan (lighter)
        'R': '\033[97m',    # Arginine (R) - White (lighter)
        'S': '\033[90m',    # Serine (S) - Bright Black (lighter)
        'T': '\033[91m',    # Threonine (T) - Red (again to differentiate)
        'V': '\033[92m',    # Valine (V) - Green (again to differentiate)
        'W': '\033[93m',    # Tryptophan (W) - Yellow (differentiated)
        'Y': '\033[94m',    # Tyrosine (Y) - Blue (differentiated)
        '_': '\033[95m',    # Stop Codon (*) - Magenta
        'reset': '\033[0;0m' # Reset color
    }

    tmpStr = ""

    for aa in seq:
        if aa in bcolors:
            tmpStr += bcolors[aa] + aa
        else:
            tmpStr += bcolors['reset'] + aa

    return tmpStr + bcolors['reset']

def colored_protein(seq):
    bcolors = {
        'A': '\033[91m',    # Alanine (A) - Red
        'C': '\033[92m',    # Cysteine (C) - Green
        'D': '\033[93m',    # Aspartic Acid (D) - Yellow
        'E': '\033[94m',    # Glutamic Acid (E) - Blue
        'F': '\033[95m',    # Phenylalanine (F) - Magenta
        'G': '\033[96m',    # Glycine (G) - Cyan
        'H': '\033[97m',    # Histidine (H) - White
        'I': '\033[90m',    # Isoleucine (I) - Bright Black
        'K': '\033[91m',    # Lysine (K) - Red (lighter)
        'L': '\033[92m',    # Leucine (L) - Green (lighter)
        'M': '\033[93m',    # Methionine (M) - Yellow (lighter)
        'N': '\033[94m',    # Asparagine (N) - Blue (lighter)
        'P': '\033[95m',    # Proline (P) - Magenta (lighter)
        'Q': '\033[96m',    # Glutamine (Q) - Cyan (lighter)
        'R': '\033[97m',    # Arginine (R) - White (lighter)
        'S': '\033[90m',    # Serine (S) - Bright Black (lighter)
        'T': '\033[91m',    # Threonine (T) - Red (again to differentiate)
        'V': '\033[92m',    # Valine (V) - Green (again to differentiate)
        'W': '\033[93m',    # Tryptophan (W) - Yellow (differentiated)
        'Y': '\033[94m',    # Tyrosine (Y) - Blue (differentiated)
        '*': '\033[95m',    # Stop Codon (*) - Magenta
        'reset': '\033[0;0m' # Reset color
    }

    colored_seq = []

    for aa in seq:

        if aa in bcolors:
            amino = (bcolors[aa] + aa + bcolors['reset'])
            colored_seq.append(str(amino))
        else:
            colored_seq.append(aa)  # Append without coloring if not in the dictionary

    return colored_seq

def readTextFile(filepath):
    with open(filepath, "r") as f:
        return "".join([l.strip() for l in f.readlines()])
    
def writeTextFile(filepath, seq, mode='w'):
    with open(filepath, mode) as f:
        f.write(seq + "\n")

def read_FASTA(filepath):
    with open(filepath, 'r') as f:
        FASTAFile = [l.strip() for l in f.readlines()]

    FASTADict = {}
    FASTALabel = ''

    for line in FASTAFile:
        if '>' in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ''
        else:
            FASTADict[FASTALabel] += line
    
    return FASTADict

def hammington_distance(seq1, seq2):
    h_distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            h_distance += 1
    return h_distance

s1 = 'ABCDEFG'
s2 = 'LSDKFJF'

print(hammington_distance(s1,s2))

def h_d_set(seq1,seq2):
    nuc_seq_1 = set([(x,y) for x,y in enumerate(seq1)])
    nuc_seq_2 = set([(x,y) for x,y in enumerate(seq2)])
    # print(nuc_seq_1)
    # print(nuc_seq_2)

    return len(nuc_seq_1.difference(nuc_seq_2))

print(h_d_set(s1,s2))

def h_d_zip(seq1,seq2):
    zippedSeq = zip(seq1,seq2)

    h_distance = [(nuc1, nuc2) for nuc1, nuc2 in zippedSeq if nuc1 != nuc2]
    return h_distance

print(h_d_zip(s1,s2))