def f(s):
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r

'''
Purpose:
    The purpose of the function is to find the number of times each character is present in s and return the result as a dictionary. The operation involves looping through s and adding each character that is not already present in the dictionary r. If the character is already present, its value is increased.

Suggestion:
    1. The code is already in O(n) time complexity. If we change the code like below we can acheive   the same performance with more readability also using more meaningful variable names is important for clarity.


    2. As functionality improvement we can raise/return(as our need) error if the word is not a string additionally remove space in between character in the word to avoid counting of spaces.
    A set of unit tests for this function.

Unit test cases
 1. string
 2. string with repeated characters
 3. string with spaces
 4. string with case sensitive
 5. empty/None
 4. Non string


'''

def elementCounter(word):
    result = {}
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    word = word.replace(" ", "")  # Remove spaces
    for char in word:
        result[char] = result.get(char, 0) + 1
    return result

print(elementCounter("AaBBccC"))

 