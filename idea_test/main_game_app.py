class Player:
  def __init__(self, name, job, body, mind, charm):
    #"Current character info."
    self.current_name = current_name
    self.current_job = current_job
    self.current_body = current_body
    self.current_mind = current_mind
    self.current_charm = current_charm
    self.current_dead = False
    self.current_npc = False
    self.confrontation_count = 0
    
    #"First character info."
    self.name_1 = None
    self.job_1 = None
    self.body_1 = None
    self.mind_1 = None
    self.charm_1 = None
    self.dead_1 = None
    self.npc_1 = None
    self.confrontation_count_1 = None
    
    #"Second character info."
    self.name_2 = None
    self.job_2 = None
    self.body_2 = None
    self.mind_2 = None
    self.charm_2 = None
    self.dead_2 = None
    self.npc_2 = None
    self.confrontation_count_2 = None
    
    #"Third character info."
    self.name_3 = None
    self.job_3 = None
    self.body_3 = None
    self.mind_3 = None
    self.charm_3 = None
    self.dead_3 = None
    self.npc_3 = None
    self.confrontation_count_3 = None
  
  def current_opponent_listen(self):
    pass
  
  def action_choice(self):
    pass
  
  def next_opponent(self):
    pass
  
  def encounter_listen(self):
    pass
  
  def success(self):
    pass
  
  def failure(self):
    pass

class NPC:
  def __init__(self, name, job, body, mind, charm):
    #"Current NPC info."
    self.name = name
    self.job = job
    self.body = body
    self.mind = mind
    self.charm = charm
    self.dead = False
    self.npc = True
    self.creation_count = 0 

class EncounterTracker:
  def __init__(self, current_player, current_npc, current_situation):
    self.current_player = current_player
    self.current_npc = current_npc
    self.current_situation = current_situation
    self.player_role = Node
    self.npc_role = Node
    self.winner = None
    self.loser = None
  
  def encounter_phase(self):
    pass


def scene_director():
  pass