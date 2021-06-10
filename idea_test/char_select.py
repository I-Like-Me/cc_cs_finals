def select_char():  
  selection = None
  print("""  
  Please select your character.
  
  A) - 90's Pizza Delivery Guy
  
  B) - Android Assasin

  C) - Hacker  
  
  D) - CEO 
  
  E) - Swat Officer
  
  F) - Cyborg Mechanic 
  
  G) - Genetically Altered Scientist
  
  H) - Cab Driver
  
  I) - Intern 
  
  J) - Barista Hipster 
  
  """)
  
  selection = input("Who would you like to be? ")
  return selection
  
character_selection = select_char()

print("You chose " + character_selection)