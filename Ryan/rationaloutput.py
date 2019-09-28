with open(__file__) as f:
    data = f.read()
chars=[]
for i in data:
    if not i.isspace():
        chars.append(i)
print(''.join(chars)*17)