#Leet Code Problems - September 13th, 2023
#Sheridan Lucero

"""
#1. Two Sum--------------------------------------

def twoSum(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                print(i, j)
                return
            
testNums = [3,3]
tar = 6

twoSum(testNums, tar)

#2. Palindrome-----------------------------------

def isPalindrome(x: str):
    if x[::1] == x[::-1]: # x[::-1] - to step through a string variable backwards
        print("True")
        return True
    else:
        print("False")
        return False

testX = input("Enter number: ")

isPalindrome(testX)

#3. Roman to Int---------------------------------
def romanToInt(s: str):
    s_int = 0
    
    #remove specific roman numeral combos
    if("IV" in s):
        s_int += 4
        s= s.replace("IV", "00")
            
    if("IX" in s):
        s_int += 9
        s = s.replace("IX", "00")

    if("XL" in s):
        s_int += 40
        s = s.replace("XL", "00")

    if("XC" in s):
        s_int += 90
        s = s.replace("XC", "00")

    if("CD" in s):
        s_int += 400
        s = s.replace("CD", "00")
    
    if("CM" in s):
        s_int += 900
        s = s.replace("CM", "00")

    #add the rest of the roman numerals
    for x in range(len(s)):
        if (s[x] == 'I'):
            s_int += 1
        elif(s[x] == 'V'):
            s_int += 5
        elif(s[x] == 'X'):
            s_int += 10
        elif(s[x] == 'L'):
            s_int += 50
        elif(s[x] == 'C'):
            s_int += 100
        elif(s[x] == 'D'):
            s_int += 500
        elif(s[x] == 'M'):
            s_int += 1000

    return s_int

testS = "MCMXCIV"
romanToInt(testS)
"""

#October 12th, 2023

#4 Longest Common Prefix--------------------------
def longestCommonPrefix(words: list[str]):

    first = words[0]
    second = words[1]
    prefix = ""

    

    #initial check to see if the words have a prefix in common
    for i in range(len(first)):
        if first[i] == second[i]:
            prefix + first[i]
        else:
            print(prefix)
            break;

test = ["flower","flow","flight"]
longestCommonPrefix(test)


    
