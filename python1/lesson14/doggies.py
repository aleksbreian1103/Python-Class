class Dog:
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dogs = []

while True:
    name = input("Dog name: ")
    if name == "":
        break
    breed = input("Dog breed: ")
    
    dogs.append(Dog(name, breed))
    
    print("DOGS")
    i = 0
    for dog in dogs:
        print(str(i) + ". " + dog.name + ":" + dog.breed)
        i += 1
    print("****************************************")