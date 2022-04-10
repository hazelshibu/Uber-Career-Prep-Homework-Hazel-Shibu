def isStringPermutation(s1:str, s2:str) -> bool:
    map = {}
    for letter in s1:
        if letter in map.keys():
            map[letter] = map[letter] + 1
        else:
            map[letter] = 1
    # second string
    for letter in s2:
        if letter in map.keys():
            map[letter] = map[letter] - 1
        else:
            return False
    for key in map.keys():
        if map[key] != 0:
            return False
    return True

def pairsThatEqualSum(inputArray: list, targetSum: int)->list:
    dictionary = {}
    listOfPairs = []
    for num in inputArray:
        if num not in dictionary.values(): 
            dictionary[num] = targetSum-num
        else:
            listOfPairs.append([targetSum-num,num])
    return listOfPairs
 
#testing
if __name__ == "__main__":
    print(isStringPermutation("asdf","fsax"))
    print(isStringPermutation("x","x"))
    print(isStringPermutation("",""))
    print(isStringPermutation(" "," "))
    print(isStringPermutation("h i","i h"))
    print(isStringPermutation("hi","i h"))
    print(isStringPermutation("happy","yaphp"))
    print(pairsThatEqualSum([1, 2, 3, 4, 5],5))
    print(pairsThatEqualSum([1, 2, 3, 4, 5],1))
    print(pairsThatEqualSum([1, 2, 3, 4, 5],7))
    print(pairsThatEqualSum([1, 8, 3, 4, 5],9))
    print(pairsThatEqualSum([8,8,8,8],16))
    print(pairsThatEqualSum([1],5))
    print(pairsThatEqualSum([3,4],7))
    print(pairsThatEqualSum([],5))
