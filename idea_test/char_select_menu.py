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
    "a": "p",
    "b": "a",
    "c": "h",
    "d": "c",
    "e": "s",
    "f": "m",
    "g": "b",
    "h": "c",
    "i": "i"
  
  }  
  selection = input("||  Who am I? ")
  try:
    picked_char = char_sel[selection.lower()]
  except:
    print("||  Reevaluating life choices.")
    selection = input("||  Who am I? ")
    try:
      picked_char = char_sel[selection.lower()]
    except:
      print("||  What am self?")
      selection = input("||  Who am I? ")
      try:
         picked_char = char_sel[selection.lower()]
      except:
         print("||  Having an existential crisis.")
         quit()    
  
  return picked_char
  