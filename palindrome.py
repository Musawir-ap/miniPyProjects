while True:
    text = input('enter..... : ').lower().replace(' ','')
    n = len(text)//2
    for i in range(n):
        if text[i] != text[-1-i]:
            print(f'{text} is not palindrome')
            p = False
            break
        p = True
    if p:
        print(f'{text} is a palindrome')
