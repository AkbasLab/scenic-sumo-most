from scenic.simulators.sumo.model import *
from scenic.core.distributions import *
import random

model scenic.simulators.sumo.model

'''Using CurvyRoad.sumocfg'''

kph2mps = 1/3.6

the_route = ["492300616#0", "159453012"]

lanes = [0,1]
ego_lane = random.choice(lanes)
lanes.remove(ego_lane)
npc1_lane = random.choice(lanes)

ego_dist = 100

ego = Car at 0 @ 0, 
    with lane ego_lane,
    with distance ego_dist,
    with track True,
    with route the_route,
    with name "ego",
    with color [255,0,0,255],
    with speed Uniform(1,30) * kph2mps

npc1 = Car at 0 @ 2,
    with name "npc1",
    with lane npc1_lane,
    with color [255,255,0,255],
    with distance Uniform(-100,100) + ego_dist,
    with route the_route,
    with speed Uniform(0,30) * kph2mps,
    with changeLane ego_lane

npc2 = Car at 0 @ 4,
    with name "npc2",
    with lane ego_lane,
    with color [255,255,0,255],
    with distance Uniform(-100,-10) + ego_dist,
    with route the_route,
    with speed Uniform(0, 30) * kph2mps

