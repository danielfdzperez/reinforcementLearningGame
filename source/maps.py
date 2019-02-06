from common import *
from tile import *
import factories as fc
from random import shuffle
'''
    Maps and their configurations
'''
map1 = ([
        [ W, W, W, W, W, W, W, W, W, W ,W, W, W, W, W ],
        [ W, S, O, P, P, P, P, P, P, P ,P, P, P, S, W ],
        [ W, P, W, P, W, P, W, W, P, W ,W, P, W, P, W ],
        [ W, P, P, P, P, P, P, P, P, P ,P, P, P, P, W ],
        [ W, P, W, P, W, P, W, W, P, W ,W, P, W, P, W ],
        [ W, P, W, P, W, P, P, P, S, P ,P, P, W, P, W ],
        [ W, P, W, P, W, P, W, W, P, W ,W, P, W, P, W ],
        [ W, P, P, P, P, P, P, P, P, P ,P, P, P, P, W ],
        [ W, P, W, S, W, P, W, W, P, W ,W, P, W, P, W ],
        [ W, P, W, P, W, P, W, W, P, W ,W, P, W, P, W ],
        [ W, P, P, P, P, P, P, P, P, P ,P, P, P, P, W ],
        [ W, P, W, P, W, P, W, W, P, W ,W, P, W, P, W ],
        [ W, P, W, P, R, P, W, W, P, W ,R, P, W, P, W ],
        [ W, S, P, P, P, P, P, P, P, P ,P, P, P, S, W ],
        [ W, W, W, W, W, W, W, W, W, W ,W, W, W, W, W ]
        ],{ W:fc.greenWall, P:fc.grassPath, S:fc.grassPath, R:fc.archEnemyRespawn, O:fc.grassPath})

map2 = ([
        [ W, W, W, W, W, W, W, W, W, W, W, W, W, W, W ],
        [ W, S, P, P, P, P, P, O, P, P, P, P, P, S, W ],
        [ W, P, W, W, W, P, W, W, W, W, W, W, W, P, W ],
        [ W, P, P, P, P, P, P, P, P, P, P, P, P, P, W ],
        [ W, P, W, P, W, W, W, W, P, W, W, W, W, P, W ],
        [ W, P, S, P, P, P, P, P, P, P, P, P, W, P, W ],
        [ W, W, W, P, W, P, W, W, P, W, W, P, W, P, W ],
        [ W, W, W, P, W, P, W, W, P, W, W, P, W, P, W ],
        [ W, W, W, P, W, P, W, W, P, W, W, P, W, P, W ],
        [ W, W, W, P, W, P, W, W, P, W, W, P, W, P, W ],
        [ W, P, P, P, P, P, P, P, P, W, W, P, W, P, W ],
        [ W, P, W, P, W, P, W, W, P, W, W, P, W, P, W ],
        [ W, P, R, P, W, P, W, W, P, W, W, P, R, P, W ],
        [ W, S, P, P, P, P, P, P, P, P, P, P, P, S, W ],
        [ W, W, W, W, W, W, W, W, W, W, W, W, W, W, W ]
        ],{ W:fc.water, P:fc.dockPath, S:fc.dockPath, R:fc.doorEnemyRespawn, O:fc.dockPath})

map3 = ([
        [ W, W, W, W, W, W, W, W, W, W, W, W, W, W, W ],
        [ W, W, S, P, P, P, P, P, P, P, P, P, O, P, W ],
        [ W, W, P, W, W, W, W, W, W, W, P, P, W, P, W ],
        [ W, W, P, P, P, P, P, P, P, P, P, P, S, P, W ],
        [ W, W, P, P, W, W, W, W, P, W, P, P, W, P, W ],
        [ W, W, P, P, P, P, S, P, P, P, P, P, P, P, W ],
        [ W, W, P, P, W, P, W, W, P, W, P, P, W, P, W ],
        [ W, W, P, P, P, P, W, W, P, P, P, P, P, P, W ],
        [ W, W, P, P, W, P, P, P, P, W, P, P, W, P, W ],
        [ W, W, P, P, P, P, W, W, P, P, P, P, P, P, W ],
        [ W, W, P, P, W, P, W, W, P, W, P, P, W, P, W ],
        [ W, W, P, P, P, P, W, W, P, S, P, P, W, P, W ],
        [ W, R, P, P, W, P, W, W, P, W, P, P, R, P, W ],
        [ W, W, S, P, P, P, P, P, P, P, P, P, P, S, W ],
        [ W, W, W, W, W, W, W, W, W, W, W, W, W, W, W ]
        ],{ W:fc.water, P:fc.dockPath, S:fc.dockPath, R:fc.doorEnemyRespawn, O:fc.dockPath})

map4 = ([
        [ W, W, W, W, W, W, W, W, W, W ,W, W, W, W, W ],
        [ W, S, P, P, P, P, P, O, P, P ,P, P, P, S, W ],
        [ W, P, W, P, W, P, W, P, W, P ,W, P, W, P, W ],
        [ W, P, P, P, P, P, P, P, W, P ,W, P, W, P, W ],
        [ W, P, W, P, W, P, W, P, W, P ,W, P, P, P, W ],
        [ W, P, W, P, W, P, P, P, W, S ,P, P, W, W, W ],
        [ W, P, W, P, W, P, W, P, W, W ,W, P, W, W, W ],
        [ W, P, P, P, P, P, S, P, W, W ,W, P, P, P, W ],
        [ W, P, W, W, W, W, W, W, W, W ,W, P, W, P, W ],
        [ W, P, W, W, W, W, W, W, W, W ,W, P, W, P, W ],
        [ W, P, P, P, P, P, P, P, W, P ,P, P, W, P, W ],
        [ W, P, W, P, W, P, W, P, W, P ,W, P, W, P, W ],
        [ W, P, W, P, R, P, W, P, W, P ,W, P, R, P, W ],
        [ W, S, P, P, P, P, P, P, P, P ,P, P, P, S, W ],
        [ W, W, W, W, W, W, W, W, W, W ,W, W, W, W, W ]
        ],{ W:fc.greenWall, P:fc.grassPath, S:fc.grassPath, R:fc.archEnemyRespawn, O:fc.grassPath})


maps = [map1,map2,map3,map4]
