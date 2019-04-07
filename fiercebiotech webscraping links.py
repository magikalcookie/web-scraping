from bs4 import BeautifulSoup
import requests
import time
#create website input
a = raw_input('Enter website: ')
#website for input: https://www.fiercebiotech.com/biotech?page=0%2C     #4025 (added 4 pg; 6021 last), 06APR19
#website for input: https://www.fiercebiotech.com/research?page=0%2C     #553 or higher, 30MAR19
#website for input: https://www.fiercebiotech.com/cro?page=0%2C         #324 or higher, 30MAR19
#website for input: https://www.fiercebiotech.com/medtech?page=0%2C     #1530 or higher, 30MAR19

#create empty list
links = []

#create code to parse
for i in range(2026, 1825, -1):
    aa = a+str(i)
    html = requests.get(aa)
    soup = BeautifulSoup(html.text, 'html.parser')
    for link in soup.find_all('a'):
        try:
            b = link.get('href')
            b = b.encode('utf8')
            if b.startswith('http'):
                continue
            if b.startswith('#'):
                continue
            if 'page=0%2C' in b:
                continue
            if b in links:
                pass
            else:
                links.append(b)
        except:
            continue
    time.sleep(10)
links.sort()
with open('fblinks.txt', 'w') as f:
    for item in links:
        print >> f, item
f.close()
#close('fblinks.txt')