
#ransom note

'''
LeetCode problem 383 RansomNote
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Summarize:

We have two strings ransomNote and magazine. We need to figure out if the string in magazine contains the required letters 
to spell out ransomNote. If we can spell out the string in ransomNote using the string in magazine return true.
Else return false.

Psuedocode planning:

To see if magazine has enough characters to spell out the string in ransomNote we need to be able to compare the characters
in both strings.
To do this we can first make both strings into lists.


'''

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
    '''
    '''
    
ransomNote = ['a','b','c']
magazine = ['b','a','c','d','a','b','c','a','b']

for char in ransomNote:
    if char in magazine:
        magazine.remove(char)
        print(magazine)
            