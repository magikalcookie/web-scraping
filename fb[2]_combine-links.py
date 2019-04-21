#Project Milestone 2
#(1) Set working directory
##Location: C:/Users/Acarag/OneDrive/Documents/web scraping data/fiercebiotech_biotech
##a = raw_input('Enter working directory (change \ to /): ')
a = 'C:/Users/Acarag/OneDrive/Documents/web scraping data/fiercebiotech_biotech' #Whichever file location
import os
os.chdir(a)
print os.getcwd()

#(2) Create one entire object of listed data
#See os functions: print dir(os)
b = os.listdir(os.getcwd())
links = []
for i in b:
    try:
        fhand = open(i)
        for line in fhand:
            if line in links:
                pass
            else:
                links.append(line)
    except:
        continue
links.sort()
with open('fblinks.txt', 'w') as f:
    for item in links:
        print >> f, item
f.close()
