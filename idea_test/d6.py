import random

def roll_d6():
  # Create random_list below:
  random_list = []

  for i in range(6):
    random_list.append(random.randint(1,7)) 
  
  # Create randomer_number below:
  randomer_number = random.choice(random_list)
  return randomer_number
  # Print randomer_number below:
print(roll_d6())