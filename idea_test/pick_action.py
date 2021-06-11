import d6

def take_action(p_b_num, p_m_num, p_c_num, n_b_num, n_m_num, n_c_num,):
  actions = {
    "body": [p_b_num, n_b_num],
    "mind": [p_m_num, n_m_num],
    "charm": [p_c_num, n_c_num]
  }
  
  player_action = input("type 'body', 'mind', or 'charm: ")
  
  if actions[player_action][0] >= actions[player_action][1]:
    resolution = "player wins"
  else:
    resolution = "npc wins"
  return resolution



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  # if p_dif == "easy" and p_w_count < 3 and p_l_count < 4:
    # print("continue")
    # p_w_count += 1
  # elif p_dif == "medium" and p_w_count < 6 and p_l_count < 2:
    # print("continue")
    # p_w_count += 1
  # elif p_dif == "hard" and p_w_count < 9 and p_l_count < 1:
    # print("continue")
    # p_w_count += 1
  # elif p_dif == "easy" and p_w_count == 3:
    # print("you win")
  # elif p_dif == "medium" and p_w_count == 6:
    # print("you win")
  # elif p_dif == "hard" and p_w_count == 9:
    # print("you win")
  # elif p_dif == "easy" and p_l_count == 3:
    # print("you lose")
  # elif p_dif == "medium" and p_l_count == 2:
    # print("you lose")
  # elif p_dif == "hard" and p_l_count == 1:
    # print("you lose")
  # else:
    # print("error")
  # return p_w_count
