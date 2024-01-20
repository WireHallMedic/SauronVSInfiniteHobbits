from simulation import *
from game_record import *
import statistics


if __name__ == "__main__":
   end_turns = []
   kills = []
   for _ in range(1000000):
      sim = Simulation()
      sim.run()
      end_turns.append(sim.game_record.ending_turn)
      kills.append(sim.game_record.dead_hobbits)
   print("+++ Results +++")
   print("Duration:")
   print("  Average: {:.2f}".format(statistics.mean(end_turns)))
   print("  Median:  {}".format(int(statistics.median(end_turns))))
   print("  Min:     {}".format(min(end_turns)))
   print("  Max:     {}".format(max(end_turns)))
   print("Dead Hobbits:")
   print("  Average: {:.2f}".format(statistics.mean(kills)))
   print("  Median:  {}".format(int(statistics.median(kills))))
   print("  Min:     {}".format(min(kills)))
   print("  Max:     {}".format(max(kills)))