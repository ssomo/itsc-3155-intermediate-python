#Takes in a string from the user and returns a dictionary that keeps
#count of each letter
def get_string_dict(string):
    #Breaks up the string into a list of characters
    lst = list(string)
    dct = {} #Empty dictionary
    for i in lst:
        if i not in dct:
            dct[i.lower()] = lst.count(i)
        #Checks if the value of i is a space
        if i.isspace():
            #Removes the key from the dictionary
            del dct[i]
    #Returns the dictionary
    return dct
    
if __name__ == '__main__':
    string = str(input('Enter a string: '))
    print(get_string_dict(string))