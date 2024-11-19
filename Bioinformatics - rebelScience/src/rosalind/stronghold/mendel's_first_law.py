genotypes = {
    "dominant" : ("+", "+"),
    "heterozygous": ("+", "-"),
    "recessive": ("-", "-")
}

populations = {
    "dominant" : 28,
    "heterozygous": 25,
    "recessive": 17 
}

def mendels_law(hom_dominant,heterozygous,hom_recessive):

    population = hom_dominant + heterozygous + hom_recessive    

    results = []

    # first create branch for each genotype
    for key1, value1 in populations.items():

        p1 = (value1) / (population)
        populations[key1] -= 1    

        # for each genotype iterate on all genotypes
        for key2, value2 in populations.items():

            dom_counter = 0
            total_combinations = 0
            
            # check all possible genotype combination & and track dominant phenotypes (they must contain at least one +)
            for gene1 in genotypes[key1]:
                for gene2 in genotypes[key2]:
                    total_combinations +=1  
                    print(gene1, gene2) 
                    if "+" in gene1 or "+" in gene2:
                        print("found above:")
                        dom_counter += 1

            # print("dom counter:", dom_counter)
            # print("total combinations:", total_combinations)
            # print(f"population {key1} is {populations[key1]}")
            # print(f"population {key2} is {populations[key2]}")
            # print(f'population as for now is {population-1}')

            # formula is (dominant phenotypes/all combinations) population of second population/ total population
            p2 =  (((dom_counter/total_combinations) * populations[key2])) / (population - 1)
            results.append((f"{key1} x {key2}:",  p1*p2, ))

        populations[key1] += 1

    return results 

results= mendels_law(populations["dominant"], populations["heterozygous"], populations["recessive"])

counter = 0
sum = 0
for i in results:
    print(i[1])
    sum += i[1]
print(round(sum,5))



