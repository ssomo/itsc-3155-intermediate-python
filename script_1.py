#function that takes in a list an returns 
# a list of unique elements of the inputted list
def get_unique_list(my_list):
    lst = [] #empty list
    #Loops through the elements in my_list
    for i in my_list:
        if i not in lst:
            lst.append(i) #appends unique elements to lst
    #returns the list
    return lst

#Sample Test
if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 1, 4]
    unique_list = get_unique_list(my_list)
    print(unique_list)