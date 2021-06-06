
print("\n")
print("You come to a fork in the path.")
print("\n")
direction = input("Do you take the 'left' path or the 'right' path?: ")

if direction == "left":
  print("\n")
  print("You went " + direction + " and stumbled upon a bandit's hideout.")
elif direction == "right":
  print("\n")
  print("You went " + direction + " and discovered a cave filled with living skelitons.")
else:
  print("\n")
  print("You went off the path and got lost.")