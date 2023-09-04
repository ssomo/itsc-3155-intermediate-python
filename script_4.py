sum = 0

for i in range(5):
    idx = i + 1 
    num = (input('Enter int #{}: '.format(idx)))
    while not num.isdigit():
        print('Invalid input. Please enter an int.')
        num = input('Enter int #{}: '.format(idx))
    num = int(num)
    sum += num

print('Your sum is', sum)
