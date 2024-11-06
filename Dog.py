from csv import reader

class Dog:
    def __init__(self, count, name, breed):
        self.count = count
        self.name = name
        self.breed = breed
        
    def __str__(self):
        return f"{self.name}     {self.breed}"

dogs = []
with open ('dog_list.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter= ',')
    next(csv_reader)
    for count, name, breed in csv_reader:
        dogs.append(Dog(count, name, breed))

num=1
for item in dogs:
    print(num,item)
    num += 1