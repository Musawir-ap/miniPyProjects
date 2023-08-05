while True:
    date = input('enter your birthdate...')
    if date.isdigit() and len(date) == 8:
        break
    print('enter valid date...')

def doflife(digits):
    if len(digits) == 1:
        return digits
    digits = [int(x) for x in digits]
    digits = str(sum(digits))
    return doflife(digits)
    
print(doflife(date))
