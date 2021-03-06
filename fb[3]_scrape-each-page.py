####Note: Check out selenium module for python to figure out how to scrape javascript websites
###https://selenium-python.readthedocs.io/
#Project Milestone 4
#Import packages needed
import os #for step (i)
from bs4 import BeautifulSoup #for step (1)
import requests #for step (1)
import time #for step (1)
try: #for step (2b)
    import cPickle as pickle #for step (2b)
except ImportError:  # python 3.x
    import pickle 
import csv
import json

#(i) Create and read file handle
x = 'C:/Users/Acarag/Desktop/webscraping' #change '\' to '/'
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
del content[0:tick+1] #The #+1 includes the '/\n' line too
content = list(map(lambda x:x.strip(),content))

#(iv) Create excel/csv file to store data
csvout = open('fiercebiotech_mycode.csv', 'a')
writer = csv.writer(csvout)

#(1) Scrape & Build Dictionary
a = 'https://www.fiercebiotech.com'
x = int(raw_input('Enter range (beg): ')) #Example: 0
y = int(raw_input('Enter range (end): ')) #Example: 5
#Note: x=0 & y=5 is [0,1,2,3,4]; next numbers should be x=5 & y=10 to check [5,6,7,8,9].
#Note: content[y] does not work if value for len(content) is inputed; last value is len(content)-1.
#Beautiful Soup instruction: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
data = {}
count = 0
exceptions = {}
for i in range(x, y):
    try:
        body = []
        bodystring = ''
        aa = a+content[i]
        data[str(i)+'-(0)Reference'] = aa
        html = requests.get(aa)
        soup = BeautifulSoup(html.text, 'html.parser')
        #print soup.title
        soup.title = soup.title.encode('utf-8')
        soup.title = soup.title[7:-8] 
        data[str(i)+'-(1)Title'] = soup.title #Title
        for author in soup.find('footer'): #Author
            author = author.find('a')
            if author == -1:
                pass
            else:
                #print author
                author1 = author.encode('utf-8')
                author2 = author1[:-4]
                author3 = author2.find('>')
                author4 = author2[author3+1:]
                data[str(i)+'-(2)Author'] = author4
        for date in soup.find('time'): #DateTime
            #print date
            data[str(i)+'-(3)DateTime'] = date.encode('utf-8')
        for text in soup.find_all('p'): #Article-body
            if text.get('class'):
                pass
            else:
                #print text
                text = text.encode('utf-8')
                text = text[3:-4]
                bodystring += text+' '
                body.append(text)
                data[str(i)+'-(4)Body'] = body
        writer.writerow([i, aa, soup.title, author4, date.encode('utf-8'), bodystring])
        time.sleep(10)
    except Exception as e:
        count+=1
        exceptions[str(i)+'-Error'] = e
        exceptions[str(i)+'-Reference'] = aa
        exceptions[str(i)+'-Exception'] = time.asctime(time.localtime(time.time()))
        continue

#(2a) Write exceptions to file
with open('exceptions_'+str(x)+'-'+str(y)+'.txt', 'w') as k:
    print >> k, 'Total:', count, '\n', exceptions
k.close()

csvout.close()
#(2b) Write dictionary to pickle
#try:
#    with open('data_'+str(x)+'-'+str(y)+'.p', 'wb') as fp:
#        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
#    fp.close()
#except:
#    with open('data_'+str(x)+'-'+str(y)+'.txt', 'w') as t:
#        print >> t, data
#    t.close()

#(2c) Write dictionary to text file only
with open('data_'+str(x)+'-'+str(y)+'.txt', 'w') as t:
    print >> t, data
t.close()

#(3) Pickle load as 'data' variable
##with open('data.p', 'rb') as fp:
    ##data = pickle.load(fp)
