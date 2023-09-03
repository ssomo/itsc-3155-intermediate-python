#Takes in 2 dict data structures and creates a new dict
#that combines the 2 dicts by summing values for the common keys
def get_combined_dict(my_dict_1, my_dict_2):
    dct = {} #empty dict data structure

    for k in my_dict_1:
            #Checks my_dict_2 has any common keys with my_dict_2
            if k in my_dict_2:
                #Sums the values for the common keys to dct
                dct[k] = my_dict_1[k] + my_dict_2[k]
    #Returns dct
    return dct

#Sample Test
if __name__ == '__main__':
    my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
    my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
    combined_dict = get_combined_dict(my_dict_1, my_dict_2)
    print(combined_dict)