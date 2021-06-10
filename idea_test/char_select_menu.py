def select_char():  
  print("""||                                                                                                
||                                                                                                   
||                                                                                                   
||  Please select your character:                                                                    
||                                                                                                   
||                                                                                                   
||                                                                                                   
||  A) - 90's Pizza Delivery Guy                                                                     
||                                                                                                   
||  B) - Android Assassin                                                                            
||                                                                                                   
||  C) - Hacker                                                                                      
||                                                                                                   
||  D) - CEO                                                                                         
||                                                                                                   
||  E) - Swat Officer                                                                                
||                                                                                                   
||  F) - Cyborg Mechanic                                                                             
||                                                                                                   
||  G) - Barista Hipster                                                                             
||                                                                                                   
||  H) - Cab Driver                                                                                  
||                                                                                                   
||  I) - Intern                                                                                      
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   """)
  
  char_sel = {
    "a": "pizza",
    "b": "assassin",
    "c": "hacker",
    "d": "ceo",
    "e": "swat",
    "f": "mechanic",
    "g": "barista",
    "h": "cab",
    "i": "intern"
  
  }  
  selection = input("||  Who would you like to be? ")
  try:
    picked_char = char_sel[selection.lower()]
  except:
    print("||  Reevaluating life choices.")

  selection = input("||  Who would you like to be? ")
  try:
    picked_char = char_sel[selection.lower()]
  except:
    print("||  What am self?")
  
  selection = input("||  Who would you like to be? ")
  try:
    picked_char = char_sel[selection.lower()]
  except:
    print("|| Having an existential crisis.")
    quit()    
  
  return picked_char
  
#character_selection = select_char()

#print("You chose " + character_selection)