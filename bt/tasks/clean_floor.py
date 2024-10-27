
import bt_library as btl
import random

class CleanFloor(btl.Task):
    """
    Implementation of the Clean Floor task: cleans floor (until random failure: set at 10% of the time)
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Cleaning floor')
        
        # Simulate a low chance of failing (nothing left to clean)
        if random.random() < 0.1:  # 10% chance of failing
            self.print_message('Nothing left to clean')
            return self.report_failed(blackboard)
        
        # Otherwise, continue to clean floor
        self.print_message('Continuing to clean floor')
        return self.report_running(blackboard)