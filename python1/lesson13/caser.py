import sys

def capitalize(instr):
    return instr.capitalize()
    
def title(instr):
    return instr.title()
    
def upper(instr):
    return instr.upper()
    
def lower(instr):
    return instr.lower()
    
def exit(instr):
    print("Goodbye for now!")
    sys.exit()

funcdict = {
    "capitalize": capitalize,
    "title": title,
    "upper": upper,
    "lower": lower,
    "exit": exit
}
options = funcdict.keys()

while True:
    func = input('Enter a function name {0}: '.format(', '.join(options)))
    instr = input('Enter a string: ')
    option = funcdict.get(func, None)
    if option:
        print(option(instr))
    else:
        print('Please select a valid option!')  