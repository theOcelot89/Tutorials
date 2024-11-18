from bio_seq import bio_seq
from utils import *

strand = bio_seq()    
strand.generate_random_sequence(40, "RNA")

print(strand.get_seq_info())
print(strand.get_seq_type())
print(strand.get_countNucFrequency())
print(f"DNA : {colored(strand.seq)}")
print(f"RNA 🧬: {colored(strand.transcription())}")
print(f"RCM: {colored(strand.reverse_compliment())}")
print(f"{strand.gc_content()}%")
print(strand.gc_content_per_section())
print(strand.translate_seq())
print(strand.codon_usage('L'))
# print(strand.gen_reading_frames())

for i, items in enumerate(strand.gen_reading_frames().items()):
    print(i+1, items[0], "\n", items[1], "\n")
print('\n')

print(strand.scan_reading_frames(strand.translate_seq()))


print(bold + "Scanning all possible ORFs for proteins.. " + end)
total_proteins = strand.complete_scan()
print("Total proteins found in 6 ORFS:", len(total_proteins), total_proteins)
for protein in total_proteins:
    print(f'{protein}')
print('\n')

writeTextFile("test.txt",strand.seq,)

for seq, rf in strand.gen_reading_frames().items():
    writeTextFile("test.txt", str(rf),'a')

FASTAFile = read_FASTA('fasta_samples.txt')
print(FASTAFile)
