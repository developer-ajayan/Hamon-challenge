# Hamon-challenge

## Purpose:
The purpose of the function is to find the number of times each character is present in s and return the result as a dictionary. The operation involves looping through s and adding each character that is not already present in the dictionary r. If the character is already present, its value is increased.

## Suggestion:
The code is already in O(n) time complexity. If we change the code like below we can acheive   the same performance with more readability also using more meaningful variable names is important for clarity.

As functionality improvement we can raise/return(as our need) error if the word is not a string additionally remove space in between character in the word to avoid counting of spaces.

 ** note: my code suggestion is added in ElementCounter.py **
## Unit test cases
 1. string
 2. string with repeated characters
 3. string with spaces
 4. string with case sensitive
 5. empty/None
 4. Non string

** note : Unit testcases are added in TestElementCounter.py **
