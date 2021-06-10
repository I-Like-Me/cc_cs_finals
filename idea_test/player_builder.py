class Player:
  def __init__(self, p_name, p_job, p_body, p_mind, p_charm, difficulty):
    self.p_name = p_name
    self.p_job = p_job
    self.p_body = p_body
    self.p_mind = p_mind
    self.p_charm = p_charm
    self.difficulty = difficulty
    self.win_count = 0
    self.loss_count = 0