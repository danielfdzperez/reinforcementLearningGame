from common import *
from tile import *
import factories as fc
'''
    Maps and their configurations
'''
map1 = ([
        [ W, W, W, W, W, W, W, W, W, W,W,W,W,W,W ],
        [ W, S, O, P, P, P, P, P, P, P,P,P,P,S,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, P, P, P, P, P, P, P, P,P,P,P,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, W, P, W, P, P, P, S, P,P,P,W,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, P, P, P, P, P, P, P, P,P,P,P,P,W ],
        [ W, P, W, S, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, P, P, P, P, P, P, P, P,P,P,P,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, W, P, R, P, W, W, P, W,R,P,W,P,W ],
        [ W, S, P, P, P, P, P, P, P, P,P,P,P,S,W ],
        [ W, W, W, W, W, W, W, W, W, W,W,W,W,W,W ]
        ],{ W:fc.wall, P:fc.path, S:fc.path, R:fc.enemyRespawn, O:fc.path})

map2 = ([
        [ W, W, W, W, W, W, W, W, W, W,W,W,W,W,W ],
        [ W, S, O, P, P, P, P, P, P, P,P,P,P,S,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, P, P, P, P, P, P, P, P,P,P,P,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, W, P, W, P, P, P, S, P,P,P,W,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, P, P, P, P, P, P, P, P,P,P,P,P,W ],
        [ W, P, W, S, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, P, P, P, P, P, P, P, P,P,P,P,P,W ],
        [ W, P, W, P, W, P, W, W, P, W,W,P,W,P,W ],
        [ W, P, W, P, R, P, W, W, P, W,R,P,W,P,W ],
        [ W, S, P, P, P, P, P, P, P, P,P,P,P,S,W ],
        [ W, W, W, W, W, W, W, W, W, W,W,W,W,W,W ]
        ],{ W:fc.water, P:fc.dockPath, S:fc.dockPath, R:fc.doorEnemyRespawn, O:fc.dockPath})

maps = [map2,map1]
