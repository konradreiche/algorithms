'''
Question

        Given two strings, write a method to decide whether one is the
        permutation of the other.

Solution 1

        Iterate for each character of one string the complete other string
        and memorize found character pairs in a boolean array with the
        string length. Also check whether the string have different
        lengths.

        Time Complexity O(n^2)
        Space Complexity O(n)
'''
def isPermutation(string1, string2):

        if len(string1) != len(string2):
                return False

        size = len(string1)
        checkList = size * [False]
        for i in range(size):
                for j in range(size):
                        if ((string1[i] == string2[j]) and (not
                                        checkList[j])):
                                checkList[j] = True
                                break

        return all(checkList)

print isPermutation("Konrad", "darnoK")
print isPermutation("Konrad", "dannoK")
print isPermutation("Konrad", "Konrad   ")

'''
Solution 2

        In a permutation only the order might differ, hence another
        solution is to sort both strings and compare them.

        Time Complexity O(n log n)
        Space Complexity O(n)
'''
def isPermutation2(string1, string2):

        if len(string1) != len(string2):
                return False

        list1 = list(string1)
        list2 = list(string2)
        list1.sort()
        list2.sort()

        return list1 == list2

print isPermutation2("Konrad", "darnoK")
print isPermutation2("Konrad", "dannoK")
print isPermutation2("Konrad", "Konrad   ")

'''
Solution 3

        Another definition of a permutation, respectively anagram, is two
        words with the same character count. The definition can be checked
        by count the characters of one string and count the characters
        down when iterating the second string. Here it depends on the
        character encoding how big the count array is going to be.

        Time Complexity O(n)
        Space Complexity O(1)
'''
def isPermutation3(string1, string2, bits):
        
        if len(string1) != len(string2):
                return False

        maximum = 2 ** bits
        count = maximum * [0]
        for i in range(len(string1)):
                
                index = ord(string1[i])
                count[index] = count[index] + 1

        for i in range(len(string2)):
                
                index = ord(string2[i])
                count[index] = count[index] - 1
                if (count[index] < 0):
                        return False
                

        return True

        
print isPermutation3("Konrad", "darnoK", 8)
print isPermutation3("Konrad", "dannoK", 8)
print isPermutation3("Konrad", "Konrad   ", 8)
