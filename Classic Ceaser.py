#Classic Ceaser
from random import randint
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

### ENCRYPT ###
def encrypt(string, k):
    newString = []

    #index caps
    caps = [i for i in range(len(string)) if ord(string[i])>65 and ord(string[i])<90]
    spaces = [i for i in range(len(string)) if string[i]==' ']

    string = string.lower()
    string = ''.join(string.split(' '))
    for i in range(len(string)):
        letter = alphabet.index(string[i])
        newString.append( alphabet[(letter+k)%26] )

    for i in spaces:
        newString.insert(i, ' ')
        
    for i in caps:
        newString[i] = newString[i].upper()
        
    return ''.join(newString)

### ENCRYPTER & DECRYPTER ###   
string = str(input())
k = int(input())
print(encrypt(string,k))
