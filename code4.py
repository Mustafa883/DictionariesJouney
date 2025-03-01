print("Part4: ")
def rearrange(dictionary):
    invert = {
        
    }
    for key, value in dictionary.items():
        if value in invert:
            invert[value].append(key)
        else:
            invert[value] = [key]
    return invert
dictionary = {
    "Alice": 10, 
    "Bob": 20, 
    "Charlie": 10,
    "David": 30
    }
invert = rearrange(dictionary)
print(invert)
print("Part4 ended.")