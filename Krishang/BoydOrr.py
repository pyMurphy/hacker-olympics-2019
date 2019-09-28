import random
import requests 
from bs4 import BeautifulSoup 

URL = 'https://www.enchantedlearning.com/wordlist/adjectives.shtml'
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser') 

adjectives = (soup.find(id="main-content").get_text(" "))

listofwords = adjectives.split(" ")

while '' in listofwords:
    listofwords.remove('')

newAdjectives = listofwords[18::]

for words in newAdjectives:
    if len(words) == 1:
        newAdjectives.remove(words)

for a in range(0,int(input("How many facts would you like today?"))):
    Sen1 = ("The Boyd Orr is")
    num2 = random.randrange(0,len(newAdjectives))
    print(Sen1+ ' '+ newAdjectives[num2])