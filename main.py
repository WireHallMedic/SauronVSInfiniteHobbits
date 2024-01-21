from simulation import *
from game_record import *
import statistics


if __name__ == "__main__":
   end_turns = []
   kills = []
   for i in range(100000):
      sim = Simulation()
      sim.run()
      end_turns.append(sim.game_record.ending_turn)
      kills.append(sim.game_record.dead_hobbits)
      if i % 1000 == 0:
         print("{}k".format(i // 1000))
   print("+++ Results +++")
   print("Duration (Turns):")
   print("  Average: {:.2f}".format(statistics.mean(end_turns)))
   print("  Median:  {}".format(int(statistics.median(end_turns))))
   print("  Min:     {}".format(min(end_turns)))
   print("  Max:     {}".format(max(end_turns)))
   print("Casualities (Dead Hobbits):")
   print("  Average: {:.2f}".format(statistics.mean(kills)))
   print("  Median:  {}".format(int(statistics.median(kills))))
   print("  Min:     {}".format(min(kills)))
   print("  Max:     {}".format(max(kills)))