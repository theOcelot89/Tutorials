# Read Data
def readfile(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f.readlines()] # each line is trimmed from spaces and stored into a list
    
def gc_content(seq):   
    gc_content = round((seq.count("C") + seq.count("G")) / len(seq) * 100, 6)
    return gc_content

def FASTAdict_from_FASTAFile(FASTA):
    FASTADict = {}
    for line in FASTA:
        if '>' in line: # checks if line is a label or not
            FASTALabel = line
            FASTADict[FASTALabel] = ''
        else:
            FASTADict[FASTALabel] += line
    return FASTADict

def highest_GC_Content(dict):
    highest_label = None
    highest_content = 0

    for key,value in dict.items():
        GC_Content = gc_content(value)
        if GC_Content > highest_content:
            highest_label = key
            highest_content = GC_Content

    return highest_label, highest_content


# Read FASTA File
FASTA = readfile("src/rosalind/stronghold/testData/fasta.txt")

# Create dictionary for {laber:DNA} format
FASTADict = FASTAdict_from_FASTAFile(FASTA)

# Find the entry with the highest GC Content
results = highest_GC_Content(FASTADict)

print(results[0].replace('>',''))
print(results[1])
