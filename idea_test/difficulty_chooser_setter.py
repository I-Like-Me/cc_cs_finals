def select_dif():  
  print("""||                                                                                                
||                                                                                                   
||                                                                                                   
||  Please select your difficulty level:                                                                    
||                                                                                                   
||                                                                                                   
||                                                                                                   
||  A) - Easy                                                                     
||                                                                                                   
||  B) - Medium                                                                           
||                                                                                                   
||  C) - Hard                                                                                      
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
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   
||                                                                                                   """)
  
  dif_sel = {
    "a": "easy",
    "b": "medium",
    "c": "hard",
  }  
  selection = input("||  How hard is life? ")
  try:
    picked_dif = dif_sel[selection.lower()]
  except:
    print("||  commit.")
    selection = input("||  How hard is life? ")
    try:
      picked_dif = dif_sel[selection.lower()]
    except:
      print("||  COMMIT!")
      selection = input("||  How hard is life? ")
      try:
         picked_dif = dif_sel[selection.lower()]
      except:
         print("||  ...fuck it...")
         quit()    
  
  return picked_dif
  