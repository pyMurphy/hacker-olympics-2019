#ESCAPING AREA 51

nAndM = input().split(' ')
n = int(nAndM[0])
m = int(nAndM[1])
w = input().split(' ')
w = [int(i) for i in w]
#w = [int(input()) for i in range(m)] #alien wieght

average = round(sum(w)/n) #aim for each person to carry the average per person

for i in range(n): #for each person
    carry = 0
    for i in range(2): #carrying 2 aliens
        if carry >= average:
            print(0, end = ' ')
        else:
            try:
                weight = w.pop()
            except:
                weight = 0
            carry += weight
            print(weight, end = ' ')
    print('')

