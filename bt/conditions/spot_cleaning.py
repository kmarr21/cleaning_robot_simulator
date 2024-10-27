import bt_library as btl
from ..globals import SPOT_CLEANING

class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "spot cleaning requested".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking if spot cleaning is requested')

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(SPOT_CLEANING, False) \
            else self.report_failed(blackboard)