import bt_library as btl
from ..globals import DUSTY_SPOT_SENSOR

class DustySpot(btl.Condition):
    """
    Implementation of the condition "dusty spot detected".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking if dusty spot is detected')

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False) \
            else self.report_failed(blackboard)