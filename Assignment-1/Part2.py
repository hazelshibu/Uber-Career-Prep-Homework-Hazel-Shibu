import unittest
def isStringPermutation(s1:str, s2:str) -> bool:
    # dictionary: keys-> letters, values->num of occurrences
    map = {}
    # first string
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

class TestLinkedList(unittest.TestCase):
    def testperms(self):
        self.assertEqual(isStringPermutation("asdf","fsax"),False)
        self.assertEqual(isStringPermutation("x","x"),True)
        self.assertEqual(isStringPermutation("h i","i h"),True)
        self.assertEqual(isStringPermutation("happy","yaphp"),True)
        self.assertEqual(isStringPermutation("",""),True)
        self.assertEqual(isStringPermutation(" "," "),True)
        self.assertEqual(isStringPermutation("hi","ih"),True)
    
    def testequalsum(self):
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5],5),[[2, 3], [1, 4]])
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5],1),[])
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5],7),[[3, 4], [2, 5]])
        self.assertEqual(pairsThatEqualSum([1, 8, 3, 4, 5],9),[[1, 8], [4, 5]])
        self.assertEqual(pairsThatEqualSum([8,8,8,8],16),[[8, 8], [8, 8], [8, 8]])
        self.assertEqual(pairsThatEqualSum([3,4],7),[[3, 4]])
        self.assertEqual(pairsThatEqualSum([],5),[])
        self.assertEqual(pairsThatEqualSum([1],5),[])

if __name__ == '__main__':
    unittest.main()
