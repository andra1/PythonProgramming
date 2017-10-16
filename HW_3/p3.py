import sys
new =  list(map(lambda x: 'fizzbuzz' if x % 15  == 0 else ('buzz' if x % 5 == 0 else ('fizz' if x % 3 == 0 else x)), [x for x in range(1,(int(sys.argv[1]) + 1))]))
print("\n".join('%s' %x for x in new))
