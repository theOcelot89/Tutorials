def rabbits(generations, offsprings):

    adults = 0
    kids = 1

    for generation in range(generations-1):

        # new_kids = adults * offsprings
        # new_adults = adults + kids
        
        # population = new_adults + new_kids
        # # print(population)
        # adults = new_adults
        # kids = new_kids

        #pythonic way
        kids, adults = adults * offsprings, adults + kids
        population = kids  + adults
    
    return population

def rabbits_2(generations, offsprings):

    parent, child = 1, 1
    for generation in range(generations-1):
        
        child, parent = parent, parent + (child* offsprings)
        # print(child)
    return child

print(rabbits(5,3 ))
print(rabbits_2(5,3))

                