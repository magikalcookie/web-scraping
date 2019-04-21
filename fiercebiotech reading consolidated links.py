#Project Milestone 3
#(1) Create and read file handle
x = 'C:/Users/Acarag/OneDrive/Documents/web scraping data/fiercebiotech_biotech'
import os
os.chdir(x)
print os.getcwd()

#(2) Create list object of file handle
with open('fblinks.txt', 'r') as f:
    content = f.readlines()
content.sort()

#(3) Found last '\n' @ [60295]; deleting white space
del content[0:60296]
content = list(map(lambda x:x.strip(),content))

#(4) Create dictionary of key words
#Create empty dictionary
final_dict={}
#Find index values by '-' locations:
count = 0
count_list = []
##If doing it one at a time, use: 
    ##y = raw_input('Enter start index position: ')
    ##a = content[int(y)]
##If doing it all at once, use: 
    ##for a in content:
for a in content:
    for i in a:
        dash = i.find('-')
        if dash == -1:
            pass
            count+=1
        else:
            count_list.append(count)
    #print count_list
    
    #Append first term (minus '/')
    first = a[1:count_list[0]+0]
    #print first
    if first not in final_dict:
        final_dict[first] = 1
    else:
        final_dict[first] += 1
    
    #Loop for words in between first and last
    for i in range(len(count_list)):
        mid = a[count_list[i-1]+i:count_list[i]+i]
        #print mid
        if mid not in final_dict:
            final_dict[mid] = 1
        else:
            final_dict[mid] += 1
    #Append last term
    d = len(count_list)
    last = a[count_list[d-1]+d:len(a)]
    #print last
    if last not in final_dict:
        final_dict[last] = 1
    else:
        final_dict[last] += 1
    
    print final_dict