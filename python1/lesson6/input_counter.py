import dictionary

newset = set()
newdict = {}
setlen = 0
    
while True:
    line = input("Line input: ")
    if len(line) == 0:
        break
    
    for punc in ",?;.":
        line = line.replace(punc, "")
    words = line.strip().split(" ")
    
    for word in words:
        newset.add(word)
        if setlen < len(newset):
            newdict[word] = len(newset)
            setlen = len(newset)
        
    for key, value in newdict.items():
        print(key, value)
    
