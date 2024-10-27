import bt_library as btl

class DoNothing(btl.Task):
    """
    Implementation of the Do Nothing task.
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Does nothing and automatically succeeds
        self.print_message('Doing nothing')
        return self.report_succeeded(blackboard)