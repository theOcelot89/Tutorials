class genome_Toolkit():

    def __init__(self):
        print("genome toolkit created..")

    def count_kmers(self, sequence, kmer):
        kmers_count= 0

        for position in range(len(sequence) - (len(kmer) - 1) ):
            print(sequence[position:position + len(kmer)])
            if sequence[position:position + len(kmer)] == kmer:
                kmers_count += 1
        return kmers_count