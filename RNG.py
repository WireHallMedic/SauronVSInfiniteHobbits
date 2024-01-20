import random

def _roll_1d6():
   return random.randint(1, 6)

def _fight_roll(dice):
   max = 0
   cur = 0
   for roll in range(dice):
      cur = _roll_1d6()
      if cur > max:
         max = cur
   return max

def _num_of_successes(rolls, target):
   successes = 0
   for roll in range(rolls):
      if _roll_1d6() >= target:
         successes += 1

def sauron_fight_roll():
   return _fight_roll(4)

def hobbit_fight_roll():
   return _fight_roll(8)

def sauron_wound_roll():
   return _num_of_successes(8, 3)

def hobbit_wound_roll():
   wounds = _num_of_successes(16, 6)
   wounds = _num_of_successes(wounds, 6)
   return wounds