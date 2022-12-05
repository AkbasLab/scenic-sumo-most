import os
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

import scenic
from scenic.simulators.sumo.simulator import SumoSimulator

def main():
    config = {
        
        "gui" : False,
        # "gui" : True,
        
        #Collisions
        "--collision.action" : "warn",
        "--collision.check-junctions": "", 
        "--collision.stoptime": 50,

        # Logging
        "--error-log" : "%s/error-log.txt" % (FILE_DIR),

        # Smooth lane changing
        "--lanechange.duration": 2,

        # Traci Connection
        # "--num-clients" : 1,

        # GUI Options
        "--delay" : 100,
        "--start" : "--quit-on-end",

        # RNG
        "--seed" : 333
      
    }

        
    scenes = ["1S1.scenic", "2S13.scenic"]
    
    for scene in scenes:
        scene_fn = "%s/scenes/%s" % (FILE_DIR, scene)
        map_fn = "%s/maps/CurvyRoad.net.xml" % (FILE_DIR)

        print("Iitial test of %s" % scene)
        scenario = SumoSimulator(map_fn, scene_fn, config)

        # Create more simulaitons
        for i in range(1,3+1):
            print(":: Test %d ::" % i)
            x = scenario.createSimulation()

        print("\n")
    return

if __name__ == "__main__":
    main()