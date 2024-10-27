#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt as bt
import bt_library as btl

# Instantiation of tree according to assignment criteria
tree_root = bt.Priority([
    # First priority: check battery and charge if needed
    bt.Sequence([
        bt.BatteryLessThan30(),
        bt.Timer(10, bt.FindHome()),
        bt.GoHome(),
        bt.Charge()
    ]),

    # Second priority: cleaning activities (spot, general, dusty; each as needed)
    bt.Selection([
        # Fist, we check if spot cleaning is needed; if so, we clean it
        bt.Sequence([
            bt.SpotCleaning(),
            bt.Timer(20, bt.CleanSpot()),
            bt.DoneSpot()
        ]),
        # Next, we check for other types of cleaning
        bt.Sequence([
            # First, if general cleaning is needed we do this
            bt.GeneralCleaning(),
            # Then, if a dusty spot is detected, we clean the spot
            bt.Priority([
                bt.Sequence([
                    bt.DustySpot(),
                    bt.Timer(35, bt.CleanSpot()),
                    bt.AlwaysFail()
                ]),
                # Then we do general floor cleaning until failure
                bt.UntilFails(bt.CleanFloor())
            ]),
            # . . . and then report done with general cleaning
            bt.DoneGeneral()
        ])
    ]),
    
    # Third priority: do nothing
    bt.DoNothing()
])

# Store the root node in a behavior tree instance
robot_behavior = btl.BehaviorTree(tree_root)