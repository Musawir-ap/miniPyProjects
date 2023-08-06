def read_int(prompt, min, max):
    while True:
        try:
            n = int(input(prompt))
            if min <= n <= max:
                return n
                # break
            else:
                print('Error: the value is not within permitted range (min..max)')
            # assert n < min and n > max
            
        except(ValueError):
            print('Error: wrong input')
            
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
