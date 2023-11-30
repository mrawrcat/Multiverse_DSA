# big-O-2

'''contains-duplicate problem
Summarize:
We have an array that contains at least one element and at most 105 elements.
(these elements are integers)
We want to return true if there are any duplicates and false 
if there are no duplicates. 

Pseudocode planning:
First declare the function with a parameter that accepts an array.
Check if the array has only one element. If it does return false.
(One element = no duplicates so every element is distinct)
Create an empty hash map (dictionary) that stores the integer we iterate through in the array
Every iteration check if this integer is stored in the hash map
If there is a corresponding value then output true.
If there is not add the number in the hash map.
when we get to the end return false 
'''

def containsDuplicate(array):
    array.sort() # sorting the array/list allows us to find duplicates faster
    if len(array) == 1:
        return False
    else:
        hashmap_dictionary = {}
        for element in array:
            if(element in hashmap_dictionary):
                return True
            else:
                hashmap_dictionary[element] = array.index(element)
                
        return False
    
    
car = [1,3,5,2,3,4]

print(car)
  
print(containsDuplicate(car))
         

  
    


