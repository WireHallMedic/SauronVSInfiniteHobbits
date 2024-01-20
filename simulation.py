from rng import *
from sauron import *
from game_record import *

class Simulation:

   def __init__(self):
      self.sauron = Sauron()
      self.game_record = GameRecord()
   
   def run(self):
      turn_number = 0
      while not sauron.is_dead():
         turn_number += 1
         if sauron_fight_roll() >= hobbit_fight_roll():
            self.sauron_attack()
         else:
            self.hobbit_attack()
      self.game_record.register_ending_turn(turn_number)
   
   def sauron_attack(self):
      self.game_record.register_dead_hobbits(sauron_wound_roll())
   
   def hobbit_attack(self):
      for _ in range(hobbit_wound_roll()):
         self.sauron.apply_wound()
      