#Project Milestone 4
#(i) Create and read file handle
x = 'C:/Users/Acarag/OneDrive/Documents/web scraping data/fiercebiotech_biotech'
import os
os.chdir(x)
print os.getcwd()

#(ii) Create list object of file handle
with open('fblinks.txt', 'r') as f:
    content = f.readlines()
content.sort()

#(iii) Deleting "newline" ('\n') list items after sorting. Note: Not fool-proof
tick = 0
for item in content:
    if item.startswith('\n'):
        tick += 1
    else:
        pass
print tick
del content[0:tick+1]
content = list(map(lambda x:x.strip(),content))

#(1) Scrape & Build Dictionary
a = 'https://www.fiercebiotech.com'
x = int(raw_input('Enter range (beg): ')) #Example: 0
y = int(raw_input('Enter range (end): ')) #Example: 5
#Note: x=0 & y=5 is [0,1,2,3,4]; next numbers should be x=5 & y=10 to check [5,6,7,8,9].
#Note: content[y] does not work if value for len(content) is inputed; last value is len(content)-1.
#Beautiful Soup instruction: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests
import time
data = {}
body = []
count = 0
exceptions = {}
for i in range(x, y):
    try:
        aa = a+content[i]
        html = requests.get(aa)
        soup = BeautifulSoup(html.text, 'html.parser')
        #print soup.title 
        data[str(i)+'-(1)Title'] = soup.title #Title
        for author in soup.find('footer'): #Author
            author = author.find('a')
            if author == -1:
                pass
            else:
                #print author
                data[str(i)+'-(2)Author'] = author
        for date in soup.find('time'): #DateTime
            #print date
            data[str(i)+'-(3)DateTime'] = date
        for text in soup.find_all('p'): #Article-body
            if text.get('class'):
                pass
            else:
                #print text
                body.append(text)
                data[str(i)+'-(4)Body'] = body
        #time.sleep(10)
    except:
        count+=1
        exceptions[str(i)+'-Exception'] = time.asctime(time.localtime(time.time()))
        continue

#(2a) Write exceptions to file
with open('exceptions.txt', 'w') as k:
    print >> k, 'Total:', count, '\n', exceptions
k.close()

#(2b) Write dictionary to pickle
