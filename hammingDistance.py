"""
    Have the function hammingDistance(strList) take the array of strings
    stored in strList, which will only contain two strings of equal length
    andm USING ITERATION return the hamming distance between them...

    Sample Test Cases:
        Input: "10011", "10100"
        Output: 3

        Input: "helloworld", "worldhello"
        Output: 8

"""
#iterative
def hammingDistance1(strList):
    distance = 0
    first , second = strList
    for i in range(len(first)):
        if first[i] != second[i]:
            distance += 1

    return distance
#head recursion
def hammingDistance2(strList):
    first, second = strList
    if first == '':
        return 0
    else:
        if first[0] == second [0]:
            return hammingDistance2([first[1:],second[1:]]) #take everything except first character and reconstruct strList
        else:
            return hammingDistance2([first[1:],second[1:]]) + 1 #same as previous, but if they are not equal, increases return count by 1

#using zip() and map()
def hammingDistance3(strList):
    
    def isDifferent(pair):
        return pair[0] != pair[1]
    
    first, second = strList
    matches = list(map(isDifferent, zip(first, second)))
    print(matches)

    return matches.count(True)

#using lambda
def hammingDistance4(strList):
    first, second = strList
    matches = list(map(lambda x: x[0] != x[1],zip(first, second)))
    print(matches)
    
    return matches.count(True)

#using filter()
def hammingDistance5(strList):
    first, second = strList
    matches = list(filter(lambda x: x[0] != x[1],zip(first, second)))
    print(matches)
    
    return len(matches)

#using internal for loop
def hammingDistance6(strList):
    first, second = strList
    matches = [True for i in range(len(first)) if first[i] != second[i]]
    print(matches)

    return len(matches)

                   
if __name__ == '__main__':
    slist1 = [ "10011", "10100" ]
    slist2 = [ "helloworld" , "worldhello" ]
    
    print("List 1: " , slist1)
    print("List 2: ", slist2)
    print('\n')

    print("Function Definition 1:")
    print(hammingDistance1(slist1))
    print(hammingDistance1(slist2))
    print('\n')

    print("Function Definition 2:")
    print(hammingDistance2(slist1))
    print(hammingDistance2(slist2))
    print('\n')

    print("Function Definition 3:")
    print(hammingDistance3(slist1))
    print(hammingDistance3(slist2))
    print('\n')

    print("Function Definition 4:")
    print(hammingDistance4(slist1))
    print(hammingDistance4(slist2))
    print('\n')

    print("Function Definition 5:")
    print(hammingDistance5(slist1))
    print(hammingDistance5(slist2))
    print('\n')

    print("Function Definition 6:")
    print(hammingDistance6(slist1))
    print(hammingDistance6(slist2))
    print('\n')
