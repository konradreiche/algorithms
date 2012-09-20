import math

'''
Question

        Implement an algorithm to determine if a string has all unique characters. What
        if you cannot use additional data structures?

Solution 1

        Compare every character of the string with every other character of the
        string.

        Time Complexity O(n^2)
        Space Complexity O(1)

Solution 2

        If it is allowed to modify the input string a sorting algorithm could be
        applied and then check whether neighboring characters are identical.


        Time Complexity O(n log n)
        Space Complexity O(1)

Solution 3

        Dependent on the string encoding there is a different size of maximum
        possible characeters. If there are more characters in the string than can
        be encodied the result is false.

        A boolean array allocated with the maximum size of possible characeters is
        used as a hash map to find out whether a character was already used.

        Time Complexity O(n)
        Space Complexity O(1)
'''
def hasUniqueCharacters(string, bits):

        maximum = 2 ** bits
        if len(string) > maximum:
                return False

        isUsed = maximum * [False]
        for i in range(len(string)):
                position = ord(string[i])
                if isUsed[position]:
                        return False
                
                isUsed[position] = True
                

        return True

print hasUniqueCharacters('Hello Berlin!', 8)
print hasUniqueCharacters('Konrad', 8)

'''
Solution 4

        The required space of solution 3 can be reduced by using a bit vector
        instead of boolean array. The ordinal number of the character is mapped
        to a power of two which can then be used to perform checks on the bit
        vector.

        Time Complexity O(n)
        Space Complexity O(1)
'''
def hasUniqueCharacters2(string, bits):

        maximum = 2 ** bits
        space = int(math.log(maximum, 2)) - 5
        bitVectors = [0] * space
        for i in range(len(string)):
                value = ord(string[i])
                selector = int(math.log(value - 1, 2)) - 5
                bitVector = bitVectors[selector]
                
                if (bitVector & (1 << value) > 0):
                        return False

                bitVectors[selector] |= (1 << value)

        return True

                
print hasUniqueCharacters2('Hello Berlin!', 8)
print hasUniqueCharacters2('Konrad', 8)
