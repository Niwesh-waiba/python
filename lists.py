import random
test_seed =  int(input("create a seed number:"))
random.seed(test_seed)
nameAsCSV = input("Give me everybody's names separated by a comma: ")
names = nameAsCSV.split(", ")
print(names)
x = len(names)
print(names[random.randint(0,x-1)] + " is going to pay the bill.")
# alt code 
# print(random.choice(names) + "is going to pay the bill")