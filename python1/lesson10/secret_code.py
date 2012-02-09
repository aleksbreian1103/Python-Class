linein = input("Enter input: ")
linein = linein[::-1]
linearr = []

linelen = len(linein)
for index in range(linelen):
    linearr.append(chr(ord(linein[index])+1))
    
print(''.join(linearr))

