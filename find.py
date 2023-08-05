while True:
    str1 = input('enter a string...: ').lower()
    str2 = input('enter word to search...: ').lower()
    if str1 != '' and str1 != '':
        break
    print('enter valid...')

def pos(str1, str2):
    for ch in str2:
        index = str1.find(ch)
        if index == -1:
            flag = False
            break
        flag = True
    return 'Yes' if flag else 'No'

print(pos(str1, str2))
