import random

# Create random_list below:
random_list = []

for i in range(20):
  random_list.append(random.randint(1,21))
  

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)