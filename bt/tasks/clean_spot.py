import bt_library as btl

class CleanSpot(btl.Task):
    """
    Implementation of the Clean Spot task: will continue cleaning spot until external decorator halts it (timer)
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print message to indicate cleaning spot, and keep running;
        #   timer decorators will always determine how long this task lasts (not handled in task)
        self.print_message('Cleaning spot')
        return self.report_running(blackboard)