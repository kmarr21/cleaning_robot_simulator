import bt_library as btl
from ..globals import SPOT_CLEANING

class DoneSpot(btl.Task):
    """
    Implementation of the Done Spot task.
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Marking spot cleaning as done')
        blackboard.set_in_environment(SPOT_CLEANING, False) # Sets blackboard value of SPOT_CLEANING to False
        return self.report_succeeded(blackboard) # Succeeds and exits