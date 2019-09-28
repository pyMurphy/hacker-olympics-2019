#Classic Ceaser
from random import randint
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

### ENCRYPT ###
def encrypt(string, k):
    newString = []

    #index caps
    caps = [string.index(i) for i in string if ord(i)>65 and ord(i)<90]

    string = string.lower()
    for i in range(len(string)):
        letter = alphabet.index(string[i])
        newString.append( alphabet[(letter+k)%26] )

    for i in caps:
        newString[i] = newString[i].upper()
        
    return ''.join(newString)

### ENCRYPTER & DECRYPTER ###   
string = str(input())
k = int(input())
print(encrypt(string,k))
