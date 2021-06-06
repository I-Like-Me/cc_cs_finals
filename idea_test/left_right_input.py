class TriChoice:
  def __init__(self, choice, you_choose, result):
    self.choice = choice
    self.you_choose = you_choose
    self.result = result
    self.situation = "{you_choose_txt}{action_txt}{result_txt}"
  
  def adventure(self):
    action = input("What would you like to do?: ")
  
    if action == self.choice[0]:
      print("\n")
      print(self.situation.format(you_choose_txt = self.you_choose, action_txt = action, result_txt = self.result[0]))
    elif action == self.choice[1]:
      print("\n")
      print(self.situation.format(you_choose_txt = self.you_choose, action_txt = action, result_txt = self.result[1]))
    elif action == self.choice[2]:
      print("\n")
      print(self.situation.format(you_choose_txt = self.you_choose, action_txt = action, result_txt = self.result[2]))   
    else:
      print("\n")
      print("You went off the path and got lost.")
      
class SignPost(TriChoice):
  def __init__(self, choice, you_choose, result):
    super().__init__(choice, you_choose, result)
    print("\n")
    print("You have come to a cross road. Would you like to go {choice_0}, {choice_1}, or {choice_3}? ".format(choice_0 = choice[0], choice_1 = choice[1], choice_3 = choice[2]))

sign_post_1 = SignPost(["right", "left", "forward"], "You walk ", [" and fall in a pit.", " and find the town.", " and bandits attack."])

sign_post_1.adventure()

    

# print("\n")
# print("You come to a fork in the path.")
# print("\n")
# direction = input("Do you take the 'left' path or the 'right' path?: ")

# if direction == "left":
  # print("\n")
  # print("You went " + direction + " and stumbled upon a bandit's hideout.")
# elif direction == "right":
  # print("\n")
  # print("You went " + direction + " and discovered a cave filled with living skelitons.")
# else:
  # print("\n")
  # print("You went off the path and got lost.")