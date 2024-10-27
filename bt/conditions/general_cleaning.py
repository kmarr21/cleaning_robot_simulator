import bt_library as btl
from ..globals import GENERAL_CLEANING

class GeneralCleaning(btl.Condition):
    """
    Implementation of the condition "general cleaning requested".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking if general cleaning is requested')

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(GENERAL_CLEANING, False) \
            else self.report_failed(blackboard)