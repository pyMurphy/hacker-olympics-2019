#HOW MUCH GUTS

#GUTSANDGUTS

def guts(string):
    letters  = {}
    letters['g'] = [i for i in range(len(string)) if string[i] == 'g']
    letters['u'] = [i for i in range(len(string)) if string[i] == 'u']
    letters['t'] = [i for i in range(len(string)) if string[i] == 't']
    letters['s'] = [i for i in range(len(string)) if string[i] == 's']

    combo = 0
    for i in letters['g']:
        for j in letters['u']:
            if j>i:
                for k in letters['t']:
                    if k>j:
                        for l in letters['s']:
                            if l>k:
                                combo += 1


    print(combo%1000000007)

string = input().lower()
string.split()

if len(string) <= 1000000000
    guts(string)
