#PYTHONIC LOWERCASE

lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
s = input()
s = [i for i in s]

newString = []
for i in s:
    if i in caps:
        newString.append( lower[caps.index(i)] )
    else:
        newString.append(i)

print(''.join(newString))
