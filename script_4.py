#To hold the sum
sum = 0

#Loops 5 times
for i in range(5):
    idx = i + 1 #index number
    #Prompts the user to enter an int
    num = (input('Enter int #{}: '.format(idx)))
    #Checks if the value inputted is not an int
    while not num.isdigit():
        #Error Message
        print('Invalid input. Please enter an int.')
        #Prompts the user to enter the int again
        num = input('Enter int #{}: '.format(idx))
    #Formats the input into an int
    num = int(num)
    #Sums the numbers
    sum += num

#Prints out the sum
print('Your sum is', sum)
