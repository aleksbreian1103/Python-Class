f = open('v:/type_text.txt','a')
f.close()

while True:
    f = open('v:/type_text.txt','r')
    print(f.read())
    f.close()
    f = open('v:/type_text.txt','a')
    intext = raw_input("Enter text: ")
    if intext == "":
        break
    f.write(intext)
    f.close()

f.close()
