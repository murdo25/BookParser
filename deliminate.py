import sys
import re

f = open(sys.argv[1], 'r')

lst = ''
sentenceList = []
for line in f:
    #print(line)    

    if line == '\n':
        #renive new lines and deliminate
        #print("FOUND A NEW LINE!!!! :D ") 
        lst.replace('\n','')
        sentenceList.append(re.finall(lst))
        lst = ''
        
    else:
        line.replace('\n','')
        lst += line
		
print(sentenceList)

#vec.append(f.readline())
#print(f.readline())
#f.read()


