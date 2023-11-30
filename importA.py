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
    
    