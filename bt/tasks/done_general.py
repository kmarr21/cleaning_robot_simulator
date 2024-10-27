import bt_library as btl
from ..globals import GENERAL_CLEANING

class DoneGeneral(btl.Task):
    """
    Implementation of the Done General task.
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Marking general cleaning as done')
        blackboard.set_in_environment(GENERAL_CLEANING, False) # Sets blackboard value of GENERAL_CLEANING to False
        return self.report_succeeded(blackboard) # Succeeds and exits