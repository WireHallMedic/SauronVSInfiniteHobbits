from rng import *

class Sauron:
   
   def __init__(self):
      self.wounds = 5
      self.might = 3
   
   def is_dead(self):
      return self.wounds <= 0
   
   def one_ring_save(self):
      """ Returns true if saved, false if not"""
      if one_ring_save():
         return True
      # on a failed roll, spend might to add one
      if self.might > 0:
         self.might -= 1
         return True
      return False
   
   def apply_wound(self):
      # take a wound if it's not the last one
      if self.wounds > 1:
         self.wounds -= 1
      elif not self.one_ring_save():
         self.wounds -= 1