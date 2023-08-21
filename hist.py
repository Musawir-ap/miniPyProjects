from os import strerror, path

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'r')
    count_dict = {}
    for l in src.readlines():
        for c in l:
            _c = ord(c.lower())
            if _c in range(97, 123):
                if(chr(_c)) in count_dict.keys():
                    count_dict[chr(_c)] += 1
                else:
                    count_dict[chr(_c)] = 1
    s_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    hist = open(f'{path.splitext(srcname)[0]}.hist', 'w')
    for k, v in s_dict.items():
        hist.write(f'{k} -> {v}\n')
        print(f'{k} -> {v}')
    hist.close()  
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	
