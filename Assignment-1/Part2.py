def isStringPermutation(s1: str, s2:str)-> bool:
    letters = {}
    for letter in s1:
        if letter in letters.keys():
            letters[letter] = letters[letter]+1
        else:
            letters[letter] = 1
    for letter in s2:
        if letter in letters.keys():
            if letters[letter] >= 1:
                letters[letter] = letters[letter]-1
            else:
                return False
        else:
            return False
    for value in letters.values():
        if value != 0:
            return False
    return True

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    equalSumNums = {}
    returnedArray = []
    for num in inputArray:
        equalSumNums[num] = targetSum-num
    for key in equalSumNums.keys():
        if equalSumNums[key] in equalSumNums.keys():
            returnedArray.append([key,equalSumNums[key]])
    length = int(len(returnedArray)/2.0)
    for i in range(0,length):
        returnedArray.pop()
    return returnedArray
    
'''
#testing
if __name__ == "__main__":
    print(isStringPermutation("asdf","fsax"))
    print(pairsThatEqualSum([5,0],5))
'''
