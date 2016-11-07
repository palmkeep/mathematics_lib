
#
#   maths.py
#
#   
#





#
#   powerset
#
#   Returns a list of all possible subsets of the set 
#
def powerset(orig_set):
    powerset = [[]]
    for i in range(1, 1 + len(orig_set)):
        powerset = unordered_choose(orig_set, i, powerset)
    return powerset
        


#
#   choose
#
#
#
def choose(listElements, cardinality, Ordered):
    if Ordered:
        return ordered_choose(listElements, cardinality)
    elif not Ordered:
        return unordered_choose(listElements, cardinality)



#
#   ordered_choose
#
#   Returns a list containing all the possible ways to choose
#   (cardinality) elements from (listElements) while order is taken
#   into account
#
def ordered_choose(listElements, cardinality, listChosen=None, chosen=None):
    if listChosen is None:
        listChosen = []
    if chosen is None:
        chosen = []
    for i in range(len(listElements)):
        tempListElements = listElements[:]
        chosen.append(tempListElements[i])
        del tempListElements[i]

        if cardinality == 1:
            listChosen.append(chosen[:])
        else:
            listChosen = ordered_choose(tempListElements, cardinality - 1, 
                                        listChosen, chosen)
        chosen.pop()
    return listChosen



#
#   unordered_choose
#
#   Returns a list containing all possible ways to choose 
#   (cardinality) elements from (listElements) without
#   concern for the order in which they are choosen
#
def unordered_choose(listElements, cardinality, listChosen=None, chosen=None):
    if listChosen is None:
        listChosen = []
    if chosen is None:
        chosen = []

    for i in range(1 + len(listElements) - cardinality):
        chosen.append(listElements[i])

        if cardinality == 1:
            listChosen.append(chosen[:])
        else:
            listChosen = unordered_choose(  listElements[i+1:], cardinality - 1,
                                            listChosen, chosen)
        chosen.pop()

    return listChosen



#   combine
# 
#   Returns a list of combinations from the elements in ListElements   
#
#   Ordered = True  : Returns an ordered list
#   Ordered = False : Returns an unordered list
#   Cardinality = N : Sets the size of a combination to N 
#
def combine(listElements, cardinality, ordered=True, listCombinations=None, 
            combination=None, firstElement=0):
    if listCombinations is None:
        listCombinations = []
    if combination is None:
        combination = []

    for i in range(firstElement, len(listElements)):
        combination.append(listElements[i])
        if cardinality == 1:
            listCombinations.append(combination[:])
        elif ordered:
            listCombinations = combine(listElements, cardinality - 1,
                                        ordered, listCombinations, 
                                        combination)
        else:
            listCombinations = combine(listElements, cardinality - 1, 
                                        ordered, listCombinations, 
                                        combination, i)
        combination.pop()
    return listCombinations



#
#
#
#
#
#def combine_sets(listSets, cardinality):





#
#   factorize
#
#   Returns a list of all the prime factors of n
#   If n < 0 and negatives=True :   -1 will be set as the first element 
#                                   of the output  
#
#   Returns: A list containing all of the prime factors of n 
#
def factorize(n, negatives=False):
    listFactors = []
    if n == 0:
        return [0]
    elif n < 0:
        if negative:
            listFactors.append(-1)
        n = abs(n)

    
    while(n % 2 == 0):
        listFactors.append(2)
        n = n // 2

    i = 3
    while(n != 1):
        while(n % i == 0):
            listFactors.append(i)
            n = n // i
        i += 2
    
    return listFactors



#
#   factorial
#
#   Returns the factorial of n
#
def factorial(a):
    fact = 1
    for i in range(1, Integer + 1):
        fact = fact * i
    return fact



#   !!! NOT FINISHED !!!
#   gcd
#
#   Returns: The greatest common divisor of a and b
#
def gcd(a, b):
    aFactors = factorize(a)
    bFactors = factorize(b)

    return aFactors, bFactors



#
#   primesbelow
#
#   Sieve of Eratosthenes
#   
#
def primesbelow(n):
    numbers = []
    for i in range(n + 1):
        numbers.append(i)
    
    index = 2
    while(index < n):
        if numbers[index] != 0:
            if index * 2 <= n:
                j = 2
                while(index * j <= n):
                    numbers[index * j] = 0
                    j += 1
        index += 1

    primes = []

    for k in range(2, len(numbers)):
        if numbers[k] != 0:
            primes.append(numbers[k])

    return primes



def crypt():
    print('FINISH THIS')
