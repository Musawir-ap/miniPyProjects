strng = input('enter to encrypt...: ')
shift = '0'
# while shift.isdigit() and 1<= int(shift) <= 25:
while True:
    shift = input('enter shift value 1-25: ')
    if shift.isdigit() and 1<= int(shift) <= 25:
        break
    else:
        print('enter valid shift value!')


def cypher(strng, shift):
    cypher = ''
    shift = int(shift)
    for c in strng:
        if not c.isalpha():
            cypher += c
            continue
        code = ord(c) + shift
        if c.islower():
            if code > ord('z'):
                code = code - ord('z')
                code = ord('a') + code -1
        if c.isupper():
            if code > ord('Z'):
                code = code - ord('Z')
                code = ord('A') + code -1
        if code:
            cypher += chr(code)
    return cypher

print(cypher(strng, shift))
