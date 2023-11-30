
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
To do this we can first make both strings into lists. Then we can iterate through every character in ransomNote and check if the
character is in magazine. If it is in magazine, remove that first character we find in magazine. If we complete the loop and checked
all of the characters, we can safely say that magazine has the required characters to spell out the ransomNote.

This solution is O(n) because we iterate through ransomNote once
'''


def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    for char in ransomNote:
        if char in magazine:
            magazine.remove(char)
        else:
            return False
    return True


note = 'Abraca dabra'

magazine = 'cadabraabra lsv' #no uppercase
magazine2 = 'cadabraabrAlsv' #no space
magazine3 = 'cadabr aabrAlsv' #space and uppercase

print(canConstruct(note, magazine))
print(canConstruct(note, magazine2))
print(canConstruct(note, magazine3))
