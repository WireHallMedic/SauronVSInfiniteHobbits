class GameRecord:
   
   def __init__(self):
      self.dead_hobbits = 0
      self.ending_turn = 0
   
   def register_dead_hobbits(self, deaths):
      self.dead_hobbits += deaths
   
   def register_ending_turn(self, turn_num):
      self.ending_turn = turn_num