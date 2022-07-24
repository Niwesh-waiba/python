import random
 
test_seed =int(input("create a seed number"))
random.seed(test_seed)

Random_integer = random.randint(0,1)
print(Random_integer)

if Random_integer==1:
    print('"heads"')
else:
    print('"tails')