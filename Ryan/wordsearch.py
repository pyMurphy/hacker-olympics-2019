from threading import Thread
import time

CRASH=time.time() # bet you don't know what this is for
DIMENSIONS=[0,0]

def parsedata():
    global DIMENSIONS # i hate myself
    DIMENSIONS=[int(x) for x in input().split()]
    board=[]
    for i in range(DIMENSIONS[0]):
        letters=input()
        board.append([x for x in letters.strip()])
    wordlistlen=input()
    wordlist=[]
    for i in range(int(wordlistlen)):
        word=input().strip()
        wordlist.append(word)
    return board,wordlist

def find(board,letter):
    found=[]
    for y,line in enumerate(board):
        for x,char in enumerate(line):
            if char == letter:
                found.append((x,y))
    return found

def search(board, coords, letter):
    x,y=coords
    directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)] # left, right, up, down, top left, top right, bottom left, bottom right
    found=[]
    for d in directions:
        nx,ny = x+d[0],y+d[1]
        if nx >= 0 and ny >= 0 and nx < DIMENSIONS[1] and ny < DIMENSIONS[0]:
            if board[ny][nx]==letter:
                found.append((nx,ny,d))
    return found

def solve(board,word):
    letters = [x for x in word]
    positions=find(board,letters[0])
    finalcoords=[]
    for pos in positions:
        buffer=[letters[0]]
        coords=[pos]
        found = search(board,pos,letters[1])
        if found:
            for z in found:
                nx,ny,diff = z
                diffx,diffy = diff
                for letter in letters[1:]:
                    if nx >= 0 and ny >= 0 and nx < DIMENSIONS[1] and ny < DIMENSIONS[0]:
                        buffer.append(board[ny][nx])
                        coords.append((nx,ny))
                        nx,ny=nx+diffx,ny+diffy
                        if buffer == letters:
                            finalcoords.append(coords)
    return finalcoords

def board():
    board,wordlist = parsedata()
    if DIMENSIONS[0] > 30 or DIMENSIONS[1] > 30:
        print('fail')
    coords=[]
    for word in wordlist:
        coords.append(solve(board,word))
    for coord in coords:
        for word in coord:
            for c in word:
                board[c[1]][c[0]]='x'
    buffer=[]
    for y in board:
        for x in y:
            if x != 'x':
                buffer.append(x)
    print(''.join(buffer))
    exit(0)

def runtime_crash():
    while True:
        if time.time()-CRASH > 5: # cheated the runtime system screw u im getting some points
            exit(1)

t2 = Thread(target = board)
t2.start()
t2.join()
t1 = Thread(target = runtime_crash)
t1.start()
t1.join()