
#
#   maths.py
#
#   
#





#
#   powerset
#
#   Returns a list of all possible subsets of the original set
#   Includes the empty set and the original set itself
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
#   Returns a list containing possible ways to choose elements from ListElements
#   Order is not taken into account
#   
#   cardinality = N : N elements are chosen
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
#   Elements may be chosen several times
#
#   ordered = True  : Returns an ordered list
#   ordered = False : Returns an unordered list
#   cardinality = N : Sets the size of a combination to N 
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
    aFactors = a
    bFactors = b
    if isinstance(aFactors, int) or isinstance(aFactors, float):
        aFactors = factorize(a)
    if isinstance(b, int) or isinstance(b, float):
        bFactors = factorize(b)

    try:
        a_factor = a_factors[0]
        b_factor = b_factors[0]
    except:
        return []
    if a_factor == b_factor:
        return [ a_factor ] + gcd(a_factors[1:], b_factors[1:])
    elif a_factor < b_factor:
        return gcd(a_factors[1:], b_factors)
    elif a_factor > b_factor:
        return gcd(a_factors, b_factors[1:])



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



#
#   quadratic_eq
#
#
#
def quadratic_eq(a, b, c, y):
    y = y / a
    c = c / a
    b = b / a
    a = 1

    if y - c + ((b/2)**2) < 0:
        raise IOError("Function does not handle imaginary roots yet")
    return -(b/2)+((y-c+((b/2)**2))**(1/2)), -(b/2)-((y-c+((b/2)**2))**(1/2))



def crypt():
    print('FINISH THIS')



<<<<<<< HEAD
# Not finished
=======

>>>>>>> 8f4696ee4244209df6ded74e23617177d6cfb5cd
def fancy_print(major_list):
    col_lengths = []
    rows = len(major_list)
    columns = len(major_list[0])

    for col in range(columns):
        col_length = 0
        for row in range(rows):
            major_list[row][col] = str(major_list[row][col])
            col_length = max(col_length, len(major_list[row][col]))
        col_lengths.append(col_length)

    for row in range(rows):
        line = ""
        for col in range(columns):
            col_elem = major_list[row][col]
            col_elem_len = len(col_elem)

            i = 0
            while col_lengths[col] > col_elem_len + i:
                line += " "
                i += 1
            line += col_elem + " "
        print(line)
