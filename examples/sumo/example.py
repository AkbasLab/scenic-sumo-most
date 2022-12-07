import os
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

import warnings
warnings.filterwarnings("ignore", category=UserWarning) 

import scenic
import json
from scenic.simulators.sumo.simulator import SumoSimulator


def describe(car) -> str:
        features = ["name", "route", "distance", "lane",
            "speed","speedMode","color","changeSpeed","tau",
            "parkPos","laneMode","laneChanges","routeID"]
        
        d = {}
        for key, val in car.__dict__.items():
            if key in features:
                d[key] = val

        pretty = json.dumps(d, sort_keys=True, indent=2)
        print(pretty)
        return pretty

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

    
    scene_fn = "%s/scenes/2S13.scenic" % (FILE_DIR)
    map_fn = "%s/maps/CurvyRoad.net.xml" % (FILE_DIR)
    simulator = SumoSimulator(map_fn, scene_fn, config)

    for i in range(5):
        simulator.createSimulation()



    # scenario = scenic.scenarioFromFile(scene_fn)

    
    # scene, n_iter = scenario.generate()
    # vehicles = [scenicObj for scenicObj in scene.objects \
    #     if str(type(scenicObj)) \
    #         == "<class 'scenic.simulators.sumo.model.Car'>"]
        
    # for veh in vehicles:
    #     # print(veh.name)
    #     describe(veh)                
    

    return

if __name__ == "__main__":
    main()