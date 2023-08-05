while True:
    text1 = input('enter first word....: ').lower().replace(' ','')
    text2 = input('enter second word....: ').lower().replace(' ','')
    if text1 != '' and text2 != '':
        break
    print('enter valid words...')
    
lst = list(text2)
anagram = True
for c in text1:
    if c not in  lst:
        anagram = False
        break
    index = lst.index(c)
    del lst[index]
    
if anagram and len(lst) == 0:
    print(f'{text1} and {text2} are anagrams...!')
else:
    print('not anagrams...!')